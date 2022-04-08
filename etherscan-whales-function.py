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

# In a python Lambda, the runtime loads the handler code as a module; so code in the top level
# of the module occurs once, during cold start.
print("Lambda Handler starting up")
eth = Etherscan("Y3WUGXJMF8F755634XHTWAVIDA23IRHZWB") # key in quotation marks


# calls made to get whales' ETH balance
snoop_balance = eth.get_eth_balance("0xce90a7949bb78892f159f428d0dc23a8e3584d75")
# curry_balance = eth.get_eth_balance("0x3bEcf83939f34311b6bEe143197872d877501B11")
# madonna_balance = eth.get_eth_balance("0x6ef962ea7e64e771d3a81bce4f95328d76d7672b")
paris_balance = eth.get_eth_balance("0xb6aa5a1aa37a4195725cdf1576dc741d359b56bd")
serena_balance = eth.get_eth_balance("0x0864224f3cc570ab909ebf619f7583ef4a50b826")
lohan_balance = eth.get_eth_balance("0x3781d92e5449b5b689fee308ded44882085b6312")
cuban_balance = eth.get_eth_balance("0xa679c6154b8d4619af9f83f0bf9a13a680e01ecf")

def lambda_handler(event, context):
    # At this point, we're handling an invocation. Cold start is over; this code runs for each invocation.
    
    # SnoopDoggBalance
    agent.record_custom_event("accountBalance", {
        "Balance": snoop_balance,
        "Whale": "SnoopDogg",
        "Currency": "Ethereum"
    })
    
    # StephenCurryBalance
   # agent.record_custom_event("accountBalance", {
   #     "Balance": curry_balance,
#        "Whale": "StephenCurry",
 #       "Currency": "Ethereum"
  #  })
 
    # MadonnaBalance
   # agent.record_custom_event("accountBalance", {
    #    "Balance": madonna_balance,
     #   "Whale": "Madonna",
      #  "Currency": "Ethereum"
    #})
    
    # ParisHiltonBalance
    agent.record_custom_event("accountBalance", {
        "Balance": paris_balance,
        "Whale": "ParisHilton",
        "Currency": "Ethereum"
    })

    # SerenaWilliamsBalance
    agent.record_custom_event("accountBalance", {
        "Balance": serena_balance,
        "Whale": "SerenaWilliams",
        "Currency": "Ethereum"
    })

    # LindsayLohanBalance
    agent.record_custom_event("accountBalance", {
        "Balance": lohan_balance,
        "Whale": "LindsayLohan",
        "Currency": "Ethereum"
    })

    # MarkCubanBalance
    agent.record_custom_event("accountBalance", {
        "Balance": cuban_balance,
        "Whale": "MarkCuban",
        "Currency": "Ethereum"
    })
    
    # This attribute gets added to the normal AwsLambdaInvocation event
    # agent.add_custom_parameter('customAttribute', 'customAttributeValue')

    # As normal, anything you write to stdout ends up in CloudWatch
    print("Hello, world")

    return "Success!"
