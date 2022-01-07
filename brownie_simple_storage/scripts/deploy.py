from brownie import accounts, config,SimpleStorage 

def deploy_simple():
    #adding account from .env -> config -> config.accounts
    #account=accounts.add(config["wallets"]["from_key"])
    account=accounts[0]
    simple_storage=SimpleStorage.deploy(  {'from': account} )   #deploying contract
    
    stored_value=simple_storage.retrieve() #transaction
    
    print(stored_value)

    #store transaction
    transaction=simple_storage.store(15, {'from': account})
    
    #how many blocks to wait for the transaction to be mined or get nonce +1
    transaction.wait(1)
    
    stored_value=simple_storage.retrieve() #transaction
    
    print(stored_value)

def main():
    deploy_simple()