import argparse
import boto3

rds = boto3.client('rds', region_name='us-west-2')

def configure_arguments(resource_parser):
    parser = resource_parser.add_parser('rds', help='Manage RDS instances')

    subparser = parser.add_subparsers(description='RDS Commands', dest='rds')