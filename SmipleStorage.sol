//SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract SmipleStorage{

    uint256  favouriteNumber;

    function store(uint256 _favNumber) public{
        favouriteNumber = _favNumber;
    }

    function reterive () public view returns(uint256){
        return favouriteNumber;
    }
    struct People{
        uint256 favouriteNumber;
        string name;
    }

    People public person = People({favouriteNumber:1,name:"Charudatta"});
    //array
    People[] public people;
    //create map
    mapping(string=> uint256) public nameTOFavNum;
    //name will be stored in memory
    function addPerson(string memory _name,uint256 _favNumber) public {
        people.push(People({favouriteNumber: _favNumber,name:_name}));
        //creating a map
        nameTOFavNum[_name] = _favNumber;

    }

}