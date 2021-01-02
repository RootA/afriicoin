from app import Block

class Blockchain(object):
    """
    @chain - stores all the blocks
    @current_data - stores all the info about the block
    @build_genesis - creates the first block
    """
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.build_genesis()

    def build_genesis(self):
        self.build_block(proof_number=0, prev_hash=0)
    
    def build_block(self, proof_number, prev_hash):
        block = Block(
            index=len(self.chain),
            proof_number=proof_number,
            prev_hash=prev_hash,
            data=self.current_data
        )

        self.current_data = []
        self.chain.append(block)
        return block

    @staticmethod
    def confirm_validity(block, prev_block):
        if prev_block.index + 1 != block.index:
            return False
        elif prev_block.compute_hash() != block.prev_hash:
            return False
        elif block.timestamp & lt; = prev_block.timestamp:
            return False
        
        return True

    def get_data(self, sender, receiver, amount):
        pass

    @staticmethod
    def proof_of_work(last_proof):
        pass

    @property
    def latest_block(self):
        pass