import argparse
import boto3

ec2 = boto3.resource('ec2', region_name='us-west-2')

def configure_arguments(resource_parser):
    parser = resource_parser.add_parser('ec2', help='Manage EC2 instances')

    subparser = parser.add_subparsers(description='EC2 Commands', dest='ec2')

    create_parser = subparser.add_parser('create', help='Create a new EC2 instance')

    create_parser.add_argument('name', help='The name of the EC2 instance.')
    create_parser.add_argument('--ami', default='ami-0e34e7b9ca0ace12d', help='The ID of the AMI.')
    create_parser.add_argument('--type', default='t2.micro', help='The instance type.')
    create_parser.add_argument('--max', default=1, help='The maximum number of instances to launch.')
    create_parser.add_argument('--min', default=1, help='The minimum number of instances to launch.')
    create_parser.add_argument('--tags', default=[], nargs='+', help='The tags to apply to the resources during launch')

    start_parser = subparser.add_parser('start', help='Start a previously stopped instance')
    start_parser.add_argument('--ids', nargs='+', help='The IDs of the instances.')
    start_parser.add_argument('--name', help='The name of the instance.')

    stop_parser = subparser.add_parser('stop', help='Stop a previously started instance')
    stop_parser.add_argument('--ids', nargs='+', help='The IDs of the instances.')
    stop_parser.add_argument('--name', help='The name of the instance.')

    terminate_parser = subparser.add_parser('terminate', help='Destroy an existing EC2 instance')
    terminate_parser.add_argument('--ids', nargs='+', help='The IDs of the instances.')
    terminate_parser.add_argument('--name', help='The name of the instance.')

    list_parser = subparser.add_parser('list', help='List EC2 instances')
    list_parser.add_argument('--limit', type=int , help='The maximum number of results to return.')

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
    tags = dict(tags.split('=') for tags in args.tags)
    tags['Name'] = args.name
    
    create_params = {
        'ImageId': args.ami,
        'InstanceType': args.type,
        'MaxCount': args.max,
        'MinCount': args.min,
        'TagSpecifications': [
            {
                'ResourceType': 'instance',
                'Tags': [{'Key': key, 'Value': val} for (key, val) in tags.items()]
            }
        ]
    }

    instances = ec2.create_instances(**create_params)

    for i in instances:
        i.wait_until_exists()

    _list_details(instances)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.ServiceResource.instances
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/collections.html
def list_instances(args):
    print('Listing EC2 instances...')

    if args.limit:
        instances = list(ec2.instances.limit(args.limit))
    else:
        instances = list(ec2.instances.all())
    
    _list_details(instances)

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.start
def start_instances(args):
    print('Starting EC2 instances...')

    filters = []

    if args.ids:
        filters.append({
            'Name': 'instance-id',
            'Values': args.ids
        })

    if args.name:
        filters.append({
            'Name': 'tag:Name',
            'Values': [args.name]
        })

    instances = ec2.instances.filter(Filters=filters)

    _list_details(instances)

    for i in instances:
        i.stop()

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.stop
def stop_instances(args):
    print('Stopping EC2 instances...')

    filters = []

    if args.ids:
        filters.append({
            'Name': 'instance-id',
            'Values': args.ids
        })

    if args.name:
        filters.append({
            'Name': 'tag:Name',
            'Values': [args.name]
        })

    instances = ec2.instances.filter(Filters=filters)

    _list_details(instances)

    for i in instances:
        i.stop()

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Instance.terminate
def terminate_instances(args):
    print('Terminating EC2 instances...')

    filters = []

    if args.ids:
        filters.append({
            'Name': 'instance-id',
            'Values': args.ids
        })

    if args.name:
        filters.append({
            'Name': 'tag:Name',
            'Values': [args.name]
        })

    instances = ec2.instances.filter(Filters=filters)

    _list_details(instances)

    for i in instances:
        i.terminate()

def _list_details(instances):
    print(''.join((
        'Id'.ljust(25),
        'Type'.ljust(25),
        'Status'.ljust(25),
        'Tags'
    )))

    for i in instances:
        print(''.join((
            str(i.instance_id).ljust(25),
            str(i.instance_type).ljust(25),
            str(i.state['Name']).ljust(25),
            ', '.join([f'{t["Key"]}={t["Value"]}' for t in i.tags])
        )))