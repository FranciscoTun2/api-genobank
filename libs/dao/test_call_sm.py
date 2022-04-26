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

account = w3.eth.account.privateKeyToAccount(root_key)
w3.eth.default_account = account.address


json_interface = load_json('json_test.json')
contract = w3.eth.contract(
    address=contract_address,
    abi=json_interface['abi']
)

response = contract.functions.uintToAddredd(15000000).call()
print(response)

# response = contract.functions.WhoIAm().call()
# print("Who i am?",response)
# print("accouts\n",w3.eth.accounts)

response = contract.functions.getValue().call()
print("getValue",response)


tx = contract.functions.setValue(696900).buildTransaction({
    'nonce': w3.eth.getTransactionCount(account.address)
})
signed = w3.eth.account.signTransaction(tx, private_key=root_key)
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
print(tx_hash.hex())
w3.eth.waitForTransactionReceipt(tx_hash)

response = contract.functions.getValue().call()
print("getValue",response)


# contract.function('mint').call()


# with open('json_test.json') as json_file:
#     data = json.load(json_file)
#     print(data)

# 'gasPrice': self.w3.toWei('470', 'gwei'),
#             	'from': account.address,
#             	'nonce': self.w3.eth.getTransactionCount(account.address)