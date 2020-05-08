from entity.hash_generate import HashGenerate
from entity.index_generator import IndexGenerator
from entity.policy import Policy
from entity.block import Block

class Miner:
    def __init__(self, policy : Policy, index_generator : IndexGenerator, hash_generator : HashGenerate):
        self.__policy = policy
        self.__index_generator = index_generator
        self.__hash_generator = hash_generator

    def mine(self, block : Block):
        while True:
            index = self.__index_generator.next()
            block_object = str(index) + str(block.time_stamp) + str(block.data) + str(block.pre_hash)
            block_hash = self.__hash_generator.generate(block_object)
            if self.__policy.check(block_hash):
                block.index = index
                block.block_hash = block_hash
                return block
