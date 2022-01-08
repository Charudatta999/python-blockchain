from brownie import SimpleStorage,accounts

#   Testing is separated into three categories 

#   1.) Arrange - create objects and variables of the classes which are going to be tested
#   2.) Act - call methods on the objects created in the arrange step
#   3.) Assert - check the results of the act step


#   Arrange
def test_deploy():
    account=accounts[0]
    simple_storage = SimpleStorage.deploy(  {'from': account} )   #deploying contract
    
     #   Act
    starting_value=simple_storage.retrieve() #transaction
    
    simple_storage.store(15, {'from': account}) #transaction
    
    ending_value=simple_storage.retrieve() #transaction
    
    #   Assert
    assert starting_value == 0
    assert ending_value == 15
      
    