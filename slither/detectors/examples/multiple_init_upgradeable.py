from typing import List, Tuple

from slither.core.declarations.contract import Contract
from slither.core.declarations.function_contract import FunctionContract
from slither.detectors.abstract_detector import (
    AbstractDetector,
    DetectorClassification,
    DETECTOR_INFO,
)
from slither.utils.output import Output


class MultipleInitUpgradeable(AbstractDetector):
    """
    Openzeppelin Multiple Upgradable Initializer Calls Detector
    """

    ARGUMENT = "multiple-init-upgradeable"
    HELP = "Multiple upgradeable initializer calls detector."
    IMPACT = DetectorClassification.HIGH
    CONFIDENCE = DetectorClassification.HIGH

    WIKI = "https://docs.openzeppelin.com/contracts/4.x/upgradeable#multiple-inheritance"

    WIKI_TITLE = "Multiple Initializer Calls"
    WIKI_DESCRIPTION = "Initializer functions are not linearized by the compiler like constructors. Because of this, each __{ContractName}_init function embeds the linearized calls to all parent initializers. As a consequence, calling two of these init functions can potentially initialize the same contract twice."

    WIKI_EXPLOIT_SCENARIO = """
```solidity
    import "@openzeppelin/contracts-upgradeable/token/ERC20/SafeERC20Upgradeable.sol";
    import "@openzeppelin/contracts-upgradeable/token/ERC20/ERC20PausableUpgradeable.sol";
    import "@openzeppelin/contracts-upgradeable/token/ERC20/ERC20BurnableUpgradeable.sol";
    import "@openzeppelin/contracts-upgradeable/access/OwnableUpgradeable.sol";

    contract SomeToken is
        ERC20Upgradeable,
        ERC20PausableUpgradeable,
        ERC20BurnableUpgradeable
    //    OwnableUpgradeable
    {
        function initialize() public initializer {
            __ERC20_init("Some Token", "CX");
            __ERC20Pausable_init();
        }
    }
```
"""
    WIKI_RECOMMENDATION = "Ensure not more than one upgradeable _init() called. "

    # Check the Initialize function inside find how many function calls ends with _init()
    @staticmethod
    def detect_init_func(func: FunctionContract) -> bool:
        """Detect if the function is calling multiple _init functions"""
        if not func.name == "initialize":
            return False
        
        calls = [c.name for c in func.internal_calls]
        if len([call for call in calls if call.endswith("_init")]) <= 1:
            return False

        return True
    
    # Check contract name ends with Upgradeable
    def count_upgradable_inheritances(self, contract):
        count = 0
        for inherited_contract in contract.inheritance:
            if inherited_contract.name.endswith("Upgradeable"):
                count += 1
        return count
        
    def detect_multiple_init(self, contract: Contract) -> List[FunctionContract]:
        ret = []
        for f in contract.functions_declared:
            # If initialize() calls more than one _init() and has more than one Upgradeable inheritance
            if self.detect_init_func(f) and self.count_upgradable_inheritances(contract) > 1:
                ret.append(f)
        return ret

    def _detect(self) -> List[Output]:
        """Detect the functions with multiple _init calls"""
        results = []
        for c in self.contracts:
                functions = self.detect_multiple_init(c)
                for func in functions:

                    info: DETECTOR_INFO = [func, " calls multiple _init functions\n"]

                    res = self.generate_result(info)

                    results.append(res)

        return results

