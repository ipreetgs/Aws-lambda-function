import boto3
from datetime import datetime
from termcolor import colored

def lambda_handler(event, context):
    CreateBudget()

def CreateBudget():
    try:
        client = boto3.client('budgets')
        rsponse = client.create_budget(
            AccountId='269001393029',
            Budget={
                'BudgetName': 'demobudget',
                'BudgetType': 'COST',
                'BudgetLimit': {
                    'Amount': '100',
                    'Unit': 'USD'
                },
                'CostFilters': {
                    ' TagKeyValue': ['name$gurpreet'],
                    ' Service': ['ec2', 'EC2-Instances (Elastic Compute Cloud - Compute)',
                                 'EC2-Other, EC2-ELB (Elastic Load Balancing)', 'S3 (Simple Storage Service)']
                },
                'TimeUnit': 'MONTHLY',
                'TimePeriod': {
                    'Start': datetime(2022, 11, 11),
                    'End': datetime(2023, 1, 1)
                },

            }

        ),
        sucs = colored('Success', 'green', attrs=['reverse', 'blink'])
        return sucs
    except Exception as eror:
        motivation = colored('try again with some logic!! F****n Idiot', 'red', attrs=['reverse', 'blink'])
        return eror,motivation
