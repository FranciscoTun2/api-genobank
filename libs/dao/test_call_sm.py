from web3 import Web3, HTTPProvider
import json

# open json file and load it
# create function to open json file and load it

root_key = 'c51fe1c412b6ec7f5d30261ac55eeac1991153c6a68919806ef69964ba88e3ee'
contract_address = '0x8DEAB2Ab3162F44FFF37d5F550f4a9a4Eaaa027D'

w3 = Web3(HTTPProvider('https://api.avax-test.network/ext/bc/C/rpc'))

def load_json(path):
    with open(path) as inFile:
        return json.load(inFile)

json_interface = load_json('json_test.json')
contract = w3.eth.contract(
    address=contract_address,
    abi=json_interface['abi']
)

response = contract.functions.uintToAddredd(15000000).call()
print(response)

response = contract.functions.WhoIAm().call(
  {'from': '0x1FCe7a83BbE1Cd899AF95A1Dda5299CA06438bA8'}
)
print(response)
print(w3.eth.accounts)

response = contract.functions.setValue(1500)
print(response)

response = contract.functions.getValue().call()
print(response)


# contract.function('mint').call()


# with open('json_test.json') as json_file:
#     data = json.load(json_file)
#     print(data)

# 'gasPrice': self.w3.toWei('470', 'gwei'),
#             	'from': account.address,
#             	'nonce': self.w3.eth.getTransactionCount(account.address)