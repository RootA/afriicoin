import hashlib
import time

class Block(object):
    """
    @index check to see which position the block is in the blockchain
    @data represents in an object all the info about the block (id, amount, sender, receiver etc)
    @timestamp represents the time at which the block was created
    """
    def __init__(self, index, proof_number, prev_hash, data, timestamp=None):
        self.index = index
        self.proof_number = proof_number
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        
    @property
    def compute_hash(self):
        string_block = f'{self.index}{self.proof_number}{self.prev_hash}{self.data}{self.timestamp}'
        return hashlib.sha256(string_block.encode()).hexdigest()
