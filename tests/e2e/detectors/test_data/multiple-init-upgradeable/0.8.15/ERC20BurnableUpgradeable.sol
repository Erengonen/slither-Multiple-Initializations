//SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.15;

import "./Initializable.sol";
/**
 * @dev Extension of {ERC20} that allows token holders to destroy both their own
 * tokens and those that they have an allowance for, in a way that can be
 * recognized off-chain (via event analysis).
 */
contract ERC20BurnableUpgradeable is Initializable {
    function __ERC20Burnable_init() internal onlyInitializing {
        __ERC20Burnable_init_unchained();
    }

    function __ERC20Burnable_init_unchained() internal onlyInitializing {
    }

}