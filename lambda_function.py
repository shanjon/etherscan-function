import json

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

# call made to access to ETH gas prices
gas_oracle = eth.get_gas_oracle()

# access keys SafeGasPrice, ProposeGasPrice, and FastGasPrice
safe_gas = gas_oracle["SafeGasPrice"]
propose_gas = gas_oracle["ProposeGasPrice"]
fast_gas = gas_oracle["FastGasPrice"]


def lambda_handler(event, context):
    # At this point, we're handling an invocation. Cold start is over; this code runs for each invocation.

    # SafeGasPrice
    agent.record_custom_event("GasPrice", {
        "Price": safe_gas,
        "gasType": "SafeGas",
        "Currency": "Ethereum"
    })

    # FastGasPrice
    agent.record_custom_event("GasPrice", {
        "Price": fast_gas,
        "gasType": "FastGas",
        "Currency": "Ethereum"
    })

    # ProposeGasPrice
    agent.record_custom_event("GasPrice", {
        "Price": propose_gas,
        "gasType": "ProposeGas",
        "Currency": "Ethereum"
    })
    
    
    # This attribute gets added to the normal AwsLambdaInvocation event
    # agent.add_custom_parameter('customAttribute', 'customAttributeValue')

    # As normal, anything you write to stdout ends up in CloudWatch
    print("Hello, world")

    return "Success!"
