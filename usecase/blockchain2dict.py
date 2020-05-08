from entity.block import Block
from entity.blockchain import BlockChain
from .block2dict import Block2Dict

class BlockChain2Dict:
    def __init__(self, block2dict : Block2Dict):
        self.__block2dict = block2dict
    
    def convert(self, blockchain : BlockChain):
        chain = blockchain.get_chain()
        chain_dict = dict()
        counter = 0
        for block in chain:
            block_dict = self.__block2dict.convert(block)
            chain_dict["block" + str(counter)] = block_dict
            counter = counter + 1
        return chain_dict