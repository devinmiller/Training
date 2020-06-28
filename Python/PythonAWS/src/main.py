from argparse import ArgumentParser 

import ec2

command_map = {
    'ec2': ec2.parse_arguments
}

if __name__ == '__main__':
    parser = ArgumentParser(description='A CLI for AWS')

    resource_parser = parser.add_subparsers(description='Manage specific AWS resources', dest='command')

    # Will eventually need to load sub parsers dynamically
    ec2.configure_arguments(resource_parser)

    args = parser.parse_args() 

    # Find the command to execute from the command map
    command_to_exec = command_map[args.command]
    command_to_exec(args)

    