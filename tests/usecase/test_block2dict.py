import pytest
from hamcrest import *
from unittest.mock import Mock

from entity.block import Block
from usecase.block2dict import Block2Dict

class TestBlock2Dict:

    def test_GivenABlockWhenCallConvertThenItShouldReturnProperDict(self):
        block = Mock(return_value = Block)
        block.index.return_value = 1
        block.time_stamp.return_value = 1000
        block.data.return_value = "hello"
        block.pre_hash.return_value = "pre_hash"
        block.block_hash.return_value = "block_hash"
        
        block2dict = Block2Dict()
        block_dict = block2dict.convert(block)
        assert_that(block_dict["index"], "1")
        assert_that(block_dict["time_stamp"], "1000")
        assert_that(block_dict["data"], "hello")
        assert_that(block_dict["pre_hash"], "pre_hash")
        assert_that(block_dict["block_hash"], "block_hash")
