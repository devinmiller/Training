import argparse
import boto3
from service_base import Client

class RDS(Client):
    def __init__(self, root_parser):
        resource_parser = root_parser.add_parser('rds', help='Manage RDS instances')
        command_parser = resource_parser.add_subparsers(description='RDS Commands', dest='func')

        self._build_list_command(command_parser)
        self._build_create_command(command_parser)

        super().__init__('rds') 

    def can_parse(self, command):
        return 'rds' == command.lower()

    def _build_create_command(self, parser):
        cmd_create = parser.add_parser('create', help='Create RDS instance')
        cmd_create.add_argument('engine', help='The name of the database engine to be used')
        cmd_create.add_argument('--dbname', help='The name of the database created with the instance')

    def _build_list_command(self, parser):
        cmd_list = parser.add_parser('list', help='List RDS instances')

    def list(self, args):
        print(self.client.describe_db_instances())