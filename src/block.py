# Step 1: Import necessary libraries
import hashlib
import json
import time

# Step 2: Define a Block class to represent a block in the blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash value of the block using SHA-256 algorithm
        """
        hash_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Mine the block by finding a hash value that satisfies the given difficulty level
        """
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

# Step 3: Define a Blockchain class to represent the blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        """
        Create the genesis block of the blockchain
        """
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Get the latest block in the blockchain
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Add a new block to the blockchain
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Check if the blockchain is valid by verifying the hash value of each block
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Step 4: Test the decentralized learning framework using blockchain
if __name__ == "__main__":
    # Create a blockchain
    blockchain = Blockchain()

    # Add blocks to the blockchain
    blockchain.add_block(Block(1, time.time(), "Data 1", ""))
    blockchain.add_block(Block(2, time.time(), "Data 2", ""))
    blockchain.add_block(Block(3, time.time(), "Data 3", ""))

    # Check if the blockchain is valid
    print("Is blockchain valid? ", blockchain.is_chain_valid())
