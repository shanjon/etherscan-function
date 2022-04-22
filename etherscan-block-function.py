import json
import datetime
import time

now = int( time.time() )
print( now )


def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

from newrelic import agent
from etherscan import Etherscan

# In a python Lambda, the runtime loads the handler code as a module; so code in the top level
# of the module occurs once, during cold start.
print("Lambda Handler starting up")
eth = Etherscan("XXXXXXXXXXXXXXX") # key in quotation marks

# call made to access to blocks
block_number = eth.get_block_number_by_timestamp(now, "before")
block_reward = eth.get_block_reward_by_block_number(block_number)
blockNumber = json.dumps(block_reward['blockNumber'])
blockMiner = json.dumps(block_reward['blockMiner'])
blockReward = json.dumps(block_reward['blockReward'])
uncles = json.dumps(block_reward['uncles'])
uncleInclusionReward = json.dumps(block_reward['uncleInclusionReward'])

# stripped
blockNumber_strip = blockNumber.replace('"','')
blockMiner_strip = blockMiner.replace('"','')
blockReward_strip = blockReward.replace('"','')
uncles_strip = uncles.replace('"','')
uncleInclusionReward_strip = uncleInclusionReward.replace('"','')
#block_reward = eth.get_block_reward_by_block_number()

def lambda_handler(event, context):
    # At this point, we're handling an invocation. Cold start is over; this code runs for each invocation.

    # BlockNumber
    agent.record_custom_event("Block", {
        "BlockNumber": blockNumber_strip,
        "BlockMiner": blockMiner_strip,
        "BlockReward": blockReward_strip,
        "Uncles": uncles_strip,
        "UncleInclusionReward": uncleInclusionReward_strip,
        "Currency": "Ethereum"
    })
    

    # As normal, anything you write to stdout ends up in CloudWatch
    print("Hello, world")

    return "Success!"
