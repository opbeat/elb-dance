elb-dance
=========

elb-dance is used to deregister and register instances with ELB.
It can register and block until the instance is back "In Service".


## Install

As long as elb-dance is not on pypi. You need to do:

    pip install https://github.com/opbeat/elb-dance.git


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
      --role=<role>       IAM role use to get temporary access keys

## Examples

De-register an instance from the ELB named `my-elb`, assuming the instance has role `myrole`. Run the following *on the instance*:

    elb-dance deregister my-elb --role=myrole

Register an instance and return when it's returned to service.

    elb-dance register my-elb --role=myrole
