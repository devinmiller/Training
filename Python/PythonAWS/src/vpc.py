import argparse
import boto3

ec2 = boto3.resource('ec2', region_name='us-west-2')

def configure_arguments(resource_parser):
    parser = resource_parser.add_parser('vpc', help='Manage VPC instances')

    subparser = parser.add_subparsers(description='VPC Commands', dest='vpc')

    list_parser = subparser.add_parser('list', help='List VPC instances')
    list_parser.add_argument('--limit', type=int , help='The maximum number of results to return.')

def parse_arguments(args):
    command_map = {
        'list': list_instances,
    }

    func = command_map[args.vpc]
    func(args)

def list_instances(args):
    print('Listing VPC instances...')

    _list_details(ec2.vpcs.all())

def _list_details(instances):
    print(''.join((
        'Id'.ljust(25),
        'State'.ljust(25),
        'Default'.ljust(25),
        'Tags'
    )))

    for i in instances:
        tags = i.tags if i.tags else []
        print(''.join((
            str(i.vpc_id).ljust(25),
            str(i.state).ljust(25),
            str(i.is_default).ljust(25),
            ', '.join([f'{t["Key"]}={t["Value"]}' for t in tags])
        )))