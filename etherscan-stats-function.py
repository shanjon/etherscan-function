import json
import datetime

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

from newrelic import agent
from etherscan import Etherscan
today = datetime.date.today().strftime('%Y-%m-%d')

# In a python Lambda, the runtime loads the handler code as a module; so code in the top level
# of the module occurs once, during cold start.
print("Lambda Handler starting up")
eth = Etherscan("Y3WUGXJMF8F755634XHTWAVIDA23IRHZWB") # key in quotation marks

# call made to get ETH stats
total_eth_supply = eth.get_total_eth_supply()
eth_last_price = eth.get_eth_last_price()
ethbtc = json.dumps(eth_last_price['ethbtc'])
ethusd = json.dumps(eth_last_price['ethusd'])
#eth_nodes_size = eth.get_eth_nodes_size(today, today, geth, default, asc)
# data{"ethbtc": "0.07396", "ethbtc_timestamp": "1649211343", "ethusd": "3346.24", "ethusd_timestamp": "1649211347"}

# stripped
ethbtc_strip = ethbtc.replace('"','')
ethusd_strip = ethusd.replace('"','')

def lambda_handler(event, context):
    # At this point, we're handling an invocation. Cold start is over; this code runs for each invocation.
    
    # ETHSupply
    agent.record_custom_event("ETHStats", {
        "Supply": total_eth_supply,
        "ETHBTC": ethbtc_strip,
        "ETHUSD": ethusd_strip,
      #  "nodesSize": eth_nodes_size,
        "Currency": "Ethereum"
        
    })

    
    # This attribute gets added to the normal AwsLambdaInvocation event
    # agent.add_custom_parameter('customAttribute', 'customAttributeValue')

    # As normal, anything you write to stdout ends up in CloudWatch
    print("Hello, world")

    return "Success!"
