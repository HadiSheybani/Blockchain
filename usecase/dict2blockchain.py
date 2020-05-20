
from entity.blockchain import BlockChain
from entity.block import Block
from usecase.dict2block import Dict2Block

class Dict2BlockChain:
    def __init__(self):
        self.__dict2block = Dict2Block()

    def convert(self, blockchain_dict : dict):
        blockchain = BlockChain()
        for key in blockchain_dict:
            try:
                block = self.__dict2block.convert(blockchain_dict[key])
                blockchain.add_block(block)
            except ValueError:
                raise ValueError(key + " value is incorrect")
        return blockchain