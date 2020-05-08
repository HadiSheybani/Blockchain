import pytest
from hamcrest import *
from unittest.mock import Mock

from entity.block import Block
from usecase.block2dict import Block2Dict

class TestBlock2Dict:

    def test_GivenABlockWhenCallConvertThenItShouldReturnProperDict(self):
        block = Mock(return_value = Block)
        block.index = 1
        block.time_stamp = 1000
        block.data = "hello"
        block.pre_hash = "pre_hash"
        block.block_hash = "block_hash"
        
        block2dict = Block2Dict()
        block_dict = block2dict.convert(block)
        assert_that(block_dict["index"], equal_to("1"))
        assert_that(block_dict["time_stamp"], equal_to("1000"))
        assert_that(block_dict["data"], equal_to("hello"))
        assert_that(block_dict["pre_hash"], equal_to("pre_hash"))
        assert_that(block_dict["block_hash"], equal_to("block_hash"))
