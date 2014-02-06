"""elb-dance.

Usage:
  elb-dance register <elb-name> [--instance-id=<id>] [--role=<role>]
  elb-dance deregister <elb-name> [--instance-id=<id>] [--role=<role>]
  elb-dance (-h | --help)
  elb-dance --version

Options:
  -h --help           Show this screen.
  --version           Show version.
  --instance-id=<id>  The instance id to use

"""
from docopt import docopt
from elb_dance.main import register_and_in_service, deregister
from version import VERSION


def cli_entry():
    arguments = docopt(__doc__, version='elb-dance {}'.format(VERSION))

    if arguments['--version']:
        print("elb-dance version {}".format(VERSION))
        return

    instance_id = arguments.get('--instance-id')
    elb_name = arguments['<elb-name>']
    role = arguments.get('--role')

    try:
        if arguments['register']:
            register_and_in_service(elb_name, role, instance_id)
        elif arguments['deregister']:
            deregister(elb_name, role, instance_id)
    except Exception as ex:
        print ex
