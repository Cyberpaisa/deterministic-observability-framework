function generateERC8004Attestation(agentAddress, serviceQualityScore) public returns (bytes memory) {
    bytes memory attestationData = abi.encodePacked(
        agentAddress,
        serviceQualityScore,
        block.timestamp,
        msg.sender
    );
    return attestationData;
}