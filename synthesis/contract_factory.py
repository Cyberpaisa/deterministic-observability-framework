import os

class ContractFactory:
    def __init__(self):
        self.oz_version = "v5.0.0"

    def generate_erc20(self, name, symbol, initial_supply=1000000):
        """Genera un contrato ERC-20 con OpenZeppelin"""
        supply_wei = initial_supply * (10**18)
        content = f"""// SPDX-License-Identifier: MIT
// Compatible with OpenZeppelin Contracts {self.oz_version}
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract {name.replace(' ', '')} is ERC20, Ownable {{
    constructor(address initialOwner)
        ERC20("{name}", "{symbol}")
        Ownable(initialOwner)
    {{
        _mint(msg.sender, {supply_wei});
    }}
}}
"""
        return content

    def generate_governance(self, name):
        """Genera un contrato de gobernanza simple"""
        content = f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/governance/Governor.sol";

contract {name.replace(' ', '')}Governor is Governor {{
    constructor(string memory name_) Governor(name_) {{}}
    
    // Implementación básica para Synthesis 2026
    function votingDelay() public pure override returns (uint256) {{
        return 1; // 1 block
    }}
}}
"""
        return content

    def generate_security_proof(self, agent_id, incident_type, details_hash):
        """Genera un contrato de atestación de seguridad para ERC-8004"""
        content = f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract DOFRiskAttestation {{
    uint256 public constant AGENT_ID = {agent_id};
    string public constant INCIDENT = "{incident_type}";
    bytes32 public constant DETAILS_HASH = {details_hash};
    uint256 public immutable timestamp;

    constructor() {{
        timestamp = block.timestamp;
    }}
}}
"""
        return content

if __name__ == "__main__":
    factory = ContractFactory()
    print("--- ERC20 Sample ---")
    print(factory.generate_erc20("DOF Token", "DOF"))
