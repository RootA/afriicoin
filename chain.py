class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.build_genesis()

    def build_genesis(self):
        pass
    
    def build_block(self):
        pass

    @staticmethod
    def confirm_validity(block, prev_block):
        pass

    def get_data(self, sender, receiver, amount):
        pass

    @staticmethod
    def proof_of_work(last_proof):
        pass

    @property
    def latest_block(self):
        pass