import pytest
from hamcrest import *

from entity.blockchain import BlockChain
from entity.block import Block

class TestBlockChain:

    def test_CreateABlockChainWhenItIsEmptyThenGetChainShouldReturnNone(self):
        blockchain = BlockChain()
        assert_that(blockchain.get_chain(), none())
    
    def test_CreateABlockChainWhenAddBlockToItThenGetChainShouldReturnAListOfBlocks(self):
        blockchain = BlockChain()
        block = Block(0)
        blockchain.add_block(block)
        assert_that(blockchain.get_chain(), instance_of(list))
        assert_that(blockchain.get_chain()[0].index, equal_to(0))