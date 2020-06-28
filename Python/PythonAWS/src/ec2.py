from argparse import ArgumentParser

import boto3

def configure_arguments(resource_parser):
    parser = resource_parser.add_parser('ec2', help='Manage EC2 instances')

    subparser = parser.add_subparsers(description='EC2 Commands', dest='ec2')

    create_parser = subparser.add_parser('create', help='Create a new EC2 instance')
    create_parser.add_argument('name', help='The name of the EC2 instance.')
    create_parser.add_argument('--ami', required=False, default='ami-0e34e7b9ca0ace12d', help='The ID of the AMI.')
    create_parser.add_argument('--type', required=False, default='t2.micro', help='The instance type.')
    create_parser.add_argument('--max', required=False, default=1, help='The maximum number of instances to launch.')
    create_parser.add_argument('--min', required=False, default=1, help='The minimum number of instances to launch.')
    create_parser.add_argument('--tags', required=False, nargs='+', help='The tags to apply to the resources during launch')

    start_parser = subparser.add_parser('start', help='Start a previously stopped instance')
    start_parser.add_argument('ids', nargs='+', help='The IDs of the instances.')

    stop_parser = subparser.add_parser('stop', help='Stop a previously started instance')
    stop_parser.add_argument('ids', nargs='+', help='The IDs of the instances.')

    terminate_parser = subparser.add_parser('terminate', help='Destroy an existing EC2 instance')
    terminate_parser.add_argument('ids', nargs='+', help='The IDs of the instances.')

    list_parser = subparser.add_parser('list', help='List EC2 instances')
    list_parser.add_argument('--max', required=False, type=int , default='10', help='The maximum number of results to return.')

def parse_arguments(args):
    command_map = {
        'create': create_instance,
        'list': list_instances,
        'stop': stop_instances,
        'start': start_instances,
        'terminate': terminate_instances
    }

    func = command_map[args.ec2]
    func(args)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.create_instances
def create_instance(args):
    print('Creating EC2 instance...')

    ec2 = boto3.client('ec2', region_name='us-west-2')

    create_params = {
        'ImageId': args.ami,
        'InstanceType': args.type,
        'MaxCount': args.max,
        'MinCount': args.min,
    }

    tags = dict(tags.split('=') for tags in args.tags)
    tags['Name'] = args.name

    create_params['TagSpecifications'] = [{ 'ResourceType': 'instance', 'Tags': [{'Key': key, 'Value': val} for (key, val) in tags.items()]}]

    ec2.run_instances(**create_params)


# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances
def list_instances(args):
    print('Listing EC2 instances...')

    ec2 = boto3.client('ec2', region_name='us-west-2')

    list_params = {
        'MaxResults': args.max
    }

    response = ec2.describe_instances(**list_params)

    instances = response['Reservations'][0]['Instances']

    for i in instances:
        print(', '.join((
            i['InstanceId'],
            i['InstanceType'],
            i['State']['Name']
        )))

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.start_instances
def start_instances(args):
    print('Starting EC2 instances...')

    ec2 = boto3.client('ec2', region_name='us-west-2')

    ec2.start_instances(InstanceIds=args.ids)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.stop_instances
def stop_instances(args):
    print('Stopping EC2 instances...')

    ec2 = boto3.client('ec2', region_name='us-west-2')

    ec2.stop_instances(InstanceIds=args.ids)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.terminate_instances
def terminate_instances(args):
    print('Terminating EC2 instances...')

    ec2 = boto3.client('ec2', region_name='us-west-2')

    ec2.terminate_instances(InstanceIds=args.ids)