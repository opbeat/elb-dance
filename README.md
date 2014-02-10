elb-dance
=========

elb-dance is used to deregister and register instances with ELB.
It can register and block until the instance is back "In Service".


## Install

elb-dance can be installed from pypi:

    pip install elb-dance


Remember `sudo` if you're not installing into a virtualenv owned by you.

## Usage

    elb-dance.

    Usage:
      elb-dance register <elb-name> [--instance-id=<id>] [--role=<role>]
      elb-dance deregister <elb-name> [--instance-id=<id>] [--role=<role>]
      elb-dance (-h | --help)
      elb-dance --version

    Options:
      -h --help           Show this screen.
      --version           Show version.
      --instance-id=<id>  The instance id to use
      --role=<role>       IAM role use to get temporary access keys.

## Examples

The following examples assume that IAM instance roles are set up to allow you to access the load balancer.


De-register an instance from the ELB named `my-elb`, assuming the instance has role `myrole`. Run the following *on the instance*:

    elb-dance deregister my-elb1

Register an instance and return when it's returned to service.

    elb-dance register my-elb1

If you need to set credentials manually, it can be done through the environement
variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

Other authentication options are detailed here: https://code.google.com/p/boto/wiki/BotoConfig

## Thanks

* [docopt](https://github.com/docopt/docopt) by Vladimir Keleshev et al. which we've embedded into elb-dance
* [boto](https://github.com/boto/boto)

## License

MIT
