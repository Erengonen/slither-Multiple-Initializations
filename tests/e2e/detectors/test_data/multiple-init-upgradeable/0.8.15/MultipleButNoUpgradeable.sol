//SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.15;

import "./Initializable.sol";
import "./ERC20Pausable.sol";
import "./ERC20BurnableUpgradeable.sol";
contract MultipleButNoUpgradeable is ERC20Pausable, ERC20BurnableUpgradeable{

    function initialize() external initializer{
        __ERC20Pausable_init();
        __ERC20Burnable_init();
    }
}