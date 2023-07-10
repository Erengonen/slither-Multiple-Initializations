//SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.15;
import "./Initializable.sol";
import "./ERC20Upgradeable.sol";
import "./ERC20BurnableUpgradeable.sol";
contract MultipleInitUpgradeable is ERC20Upgradeable, ERC20BurnableUpgradeable{

    function initialize() external initializer{
        __ERC20_init("Some Token", "CX");
        __ERC20Burnable_init();
    }
}