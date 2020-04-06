
from .block import Block

class BlockChain:

    def __init__(self, chain : list = None):
        self.__chain = list()
        if chain is not None:
            self.__chain = chain.copy()
        

    def get_chain(self):
        if self.__chain.__len__() == 0:
            return None
        return self.__chain.copy()
    
    def add_block(self, block : Block):
        self.__chain.append(block)