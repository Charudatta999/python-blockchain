from brownie import accounts, config, SimpleStorage, network

def read_contract():
    print(SimpleStorage[-1])
    print(SimpleStorage[-1].retrieve())
    
def main():
    read_contract()