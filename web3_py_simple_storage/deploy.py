from solcx import compile_standard, install_solc
import json
from web3 import Web3 
from dotenv import load_dotenv
import os
load_dotenv()


with open("SmipleStorage.sol", "r") as file:
    simple_storage_file = file.read()
    
# compiled solidity

install_solc("0.6.0")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SmipleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}

            }
        }
    },
    solc_version="0.6.0"
)

with open("compiled_code.json","w") as file:
    json.dump(compiled_sol,file)
#getting bytecode
bytecode = compiled_sol["contracts"]["SmipleStorage.sol"]["SmipleStorage"]["evm"]["bytecode"]["object"]

#getting ABI

abi=compiled_sol["contracts"]["SmipleStorage.sol"]["SmipleStorage"]["abi"]

# requiremnts for conecting to chain
w3 = Web3(Web3.HTTPProvider("http://172.23.240.1:7545"))
chain_id =1337
my_address ="0x699e53bBd3B7e870432940CF856F8F54AB814E11"
private_key = os.getenv("PRIVATE_KEY")

#create the contract in python
SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)


#get the latest transaction

nonce = w3.eth.getTransactionCount(my_address)
print(nonce)

# 1. Build a Transaction


transaction = SimpleStorage.constructor().buildTransaction( {
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id, 
    "from": my_address, 
    "nonce": nonce, 
})




# 2. Sign a Transaction
signed_txn = w3.eth.account.sign_transaction(transaction,private_key)


# 3. Send a Transaction to deploy
tx_hash=w3.eth.sendRawTransaction(signed_txn.rawTransaction)

tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# Working with the contract 
# needs to address of deployed contract
# need to get the contract abi

# get the contract address

simpe_storage = w3.eth.contract(address=tx_receipt.contractAddress,abi=abi)

# there are two ways to interact with the contract
# 1. call() :-> It will not make a state change but it will return the value
# 2. transact() :-> It will make a state change 
#    And it will return the value and also change the state e.g. set value of x


# calling retrieve() using call
value = simpe_storage.functions.retrieve().call()
print(value)

# using  transact() and initialising value of favourite number

# 1. create a transaction
store_transaction = simpe_storage.functions.store(10).buildTransaction({
    "chainId":chain_id,
    "gasPrice":w3.eth.gas_price,
    "nonce":nonce+1,# a nonce can be used only once for a transaction
})

# 2. sign the transaction
sign_store_txn = w3.eth.account.sign_transaction(store_transaction,private_key)

# 3.Get the transaction hash
store_txn_hash = w3.eth.sendRawTransaction(sign_store_txn.rawTransaction)

# 4.getting txn receipt after getting mined
store_txn_receipt = w3.eth.waitForTransactionReceipt(store_txn_hash)

# 5. get the value changed by store function
value = simpe_storage.functions.retrieve().call()
print(value)


# get the contract instance

