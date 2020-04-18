
from entity.block import Block

class Block2Dict:

    def convert(self, block : Block):
        block_dict = dict()
        self.__add(block_dict, "index", block.index)
        self.__add(block_dict, "time_stamp", block.time_stamp)
        self.__add(block_dict, "data", block.data)
        self.__add(block_dict, "pre_hash", block.pre_hash)
        self.__add(block_dict, "block_hash", block.block_hash)
        return block_dict
    
    def __add(self, block_dict : dict, name : str, value):
        if value is not None:
            block_dict[name] = str(value)