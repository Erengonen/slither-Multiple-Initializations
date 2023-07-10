//SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.15;

import "./Initializable.sol";
contract ERC20Upgradeable is Initializable {
    string private _name;
    string private _symbol;
    
    function __ERC20_init(string memory name_, string memory symbol_) internal onlyInitializing {
        __ERC20_init_unchained(name_, symbol_);
    }

    function __ERC20_init_unchained(string memory name_, string memory symbol_) internal onlyInitializing {
        _name = name_;
        _symbol = symbol_;
    }
}