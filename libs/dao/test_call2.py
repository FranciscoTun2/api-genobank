from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware
import json

def load_json(path):
    with open(path) as inFile:
        return json.load(inFile)
_json_interface = load_json('json_test2.json')
_abi=_json_interface['abi']


contract_address = '0x7a3afBB180f29DFA9f3d8BA71A499D828B097636'

w3 = Web3(HTTPProvider('https://api.avax-test.network/ext/bc/C/rpc'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
root_key = 'c51fe1c412b6ec7f5d30261ac55eeac1991153c6a68919806ef69964ba88e3ee'
account = w3.eth.account.privateKeyToAccount(root_key)
w3.eth.default_account = account.address


greeter = w3.eth.contract(
    address=contract_address,
    abi=_abi
)
saludo = greeter.functions.greet().call()
print(saludo)


# Call a payable function
tx_hash = greeter.functions.setGreeting("adios").buildTransaction({
    'nonce': w3.eth.getTransactionCount(account.address)
    })
signed = w3.eth.account.signTransaction(tx_hash, private_key=root_key)
tx_hash = w3.eth.sendRawTransaction(signed.rawTransaction)
# wait for transaction to be mined
w3.eth.waitForTransactionReceipt(tx_hash)

print(tx_hash.hex())



saludo = greeter.functions.greet().call()
print(saludo)


# 0x7a3afBB180f29DFA9f3d8BA71A499D828B097636