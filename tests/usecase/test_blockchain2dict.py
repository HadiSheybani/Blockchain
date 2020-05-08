import pytest
from hamcrest import *
from unittest.mock import Mock

from entity.block import Block
from entity.blockchain import BlockChain
from usecase.block2dict import Block2Dict
from usecase.blockchain2dict import BlockChain2Dict

class TestBlockChain2Dict:

    def test_GivenABlockChainWhenCallConvertThenItShouldReturnProperDict(self):
        block1 = self.__mock_block(1, 1000, "hello", "pre_hash1", "block_hash1")
        block2 = self.__mock_block(2, 2000, "world", "pre_hash2", "block_hash2")
        block2dict = Block2Dict()
        blockchain = Mock(return_value = BlockChain)

        blockchain.get_chain.return_value = [block1, block2]

        blockchain2dict = BlockChain2Dict(block2dict)
        bc_dict = blockchain2dict.convert(blockchain)

        assert_that(bc_dict['block0'], equal_to({"index": "1", "time_stamp": "1000", 
                                                "data": "hello", "pre_hash": "pre_hash1",
                                                "block_hash": "block_hash1"}))
        assert_that(bc_dict['block1'], equal_to({"index": "2", "time_stamp": "2000", 
                                                "data": "world", "pre_hash": "pre_hash2",
                                                "block_hash": "block_hash2"}))

    def __mock_block(self, index, time_stamp, data, pre_hash, block_hash):
        block = Mock(return_value = Block)
        block.index = index
        block.time_stamp = time_stamp
        block.data = data
        block.pre_hash = pre_hash
        block.block_hash = block_hash
        return block
