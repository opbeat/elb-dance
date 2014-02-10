import time
import boto.ec2.elb
import boto.utils


def instance_metadata():
    metadata = boto.utils.get_instance_metadata(timeout=2, num_retries=2)
    if not metadata:
        raise RuntimeError("Could not get instance metadata, "
                           "is this even an EC2 instance?")
    return metadata


def current_instance():
    return instance_metadata()['instance-id']


def elb_connection(role):
    if role:
        try:
            creds = instance_metadata()['iam']['security-credentials'][role]
            return boto.ec2.elb.ELBConnection(
                creds['AccessKeyId'],
                creds['SecretAccessKey'],
                security_token=creds['Token']
            )
        except KeyError:
            raise KeyError("Role '{}' not found for instance.".format(role))

    # We assume environment variables are set
    return boto.ec2.elb.ELBConnection()


def deregister(elb_name, role=None, instance_id=None):
    instance_id = instance_id or current_instance()
    elb_connection(role).deregister_instances(elb_name, instance_id)
    print("Deregistered '{}'".format(instance_id))


def register_and_in_service(elb_name, role=None, instance_id=None):
    conn = elb_connection(role)
    instance_id = instance_id or current_instance()
    conn.register_instances(elb_name, instance_id)

    print("Registered '{}'".format(instance_id))

    healthy = False
    while not healthy:
        time.sleep(0.5)
        instance_state = conn.describe_instance_health(elb_name, instance_id)[0]
        healthy = instance_state.state == 'InService'

    print("In service '{}'".format(instance_id))
