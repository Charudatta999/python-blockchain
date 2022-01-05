from solcx import compile_standard, install_solc
import json
from web3 import Web3 

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
private_key ="0x78e074130ac8f79edbeff554dc378ecebad7120faabfebeac73b339824032888"

#create the contract in python
SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)
print(SimpleStorage)

#get the latest transaction

nonce = w3.eth.getTransactionCount(my_address)
print(nonce)

# 1. Build a Transaction
# 2. Sign a Transaction
# 3. Send a Transaction

transaction = SimpleStorage.constructor().buildTransaction( {
    "gasPrice": w3.eth.gas_price, 
    "chainId": chain_id, 
    "from": my_address, 
    "nonce": nonce, 
})

# transaction = SimpleStorage.constructor().buildTransaction(
#     {"chainId":chain_id,"from":my_address,"nonce":nonce}
#     )
print(transaction)
