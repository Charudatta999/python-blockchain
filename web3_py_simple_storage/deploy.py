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
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))
chain_id =1337
my_address ="0xEB20Bbd4F066404Fb68b732D88269B43d5F2f94B"
private_key ="0x310dfd88cd38333e926b8e04b7b490c858476e3749a9a38ceb497c8fbe655342"

#create the contract in python
SimpleStorage = w3.eth.contract(abi=abi,bytecode=bytecode)
print(SimpleStorage)

#get the latest transaction

nonce = w3.eth.getTransactionCount(my_address)
print(nonce)

