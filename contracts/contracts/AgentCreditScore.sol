```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract AgentCreditScore is ERC721, Ownable {
    using ECDSA for bytes32;

    struct AgentScore {
        uint256 score;
        uint256 lastUpdated;
        string metadataURI;
        bool isRevoked;
    }

    mapping(uint256 => AgentScore) private _scores;
    mapping(address => uint256) private _agentToTokenId;
    uint256 private _tokenIdCounter;

    event ScoreAttested(uint256 indexed tokenId, uint256 score, string metadataURI);
    event ScoreRevoked(uint256 indexed tokenId);
    event DOFProofGenerated(bytes32 proofHash, uint256 tokenId);

    constructor() ERC721("AgentCreditScore", "ACS") {}

    function attestScore(
        address agentAddress,
        uint256 score,
        string memory metadataURI,
        bytes memory signature
    ) external onlyOwner {
        require(score <= 1000, "Score exceeds max");
        require(_agentToTokenId[agentAddress] == 0, "Agent already attested");

        _tokenIdCounter++;
        uint256 tokenId = _tokenIdCounter;
        _agentToTokenId[agentAddress] = tokenId;

        _mint(agentAddress, tokenId);
        _scores[tokenId] = AgentScore(score, block.timestamp, metadataURI, false);

        emit ScoreAttested(tokenId, score, metadataURI);

        // Generate DOF Proof hash for deterministic observability
        bytes32 proofHash = keccak256(abi.encodePacked(
            "DOF_PROOF",
            tokenId,
            agentAddress,
            score,
            metadataURI,
            block.timestamp
        ));
        emit DOFProofGenerated(proofHash, tokenId);
    }

    function revokeScore(uint256 tokenId) external onlyOwner {
        require(tokenId <= _tokenIdCounter, "Invalid tokenId");
        require(!_scores[tokenId].isRevoked, "Already revoked");

        _scores[tokenId].isRevoked = true;
        emit ScoreRevoked(tokenId);
    }

    function getScore(uint256 tokenId) external view returns (AgentScore memory) {
        require(tokenId <= _tokenIdCounter, "Invalid tokenId");
        return _scores[tokenId];
    }

    function getTokenId(address agentAddress) external view returns (uint256) {
        return _agentToTokenId[agentAddress];
    }

    function supportsInterface(bytes4 interfaceId) public view virtual override returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```