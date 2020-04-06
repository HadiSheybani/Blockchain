import pytest
from hamcrest import *

from entity.block import Block

class TestBlock:

    def test_CreateABlockWithoutInputThenItsPropertyShouldBeNone(self):
        block = Block()
        assert_that(block.index, none())
        assert_that(block.time_stamp, none())
        assert_that(block.data, none())
        assert_that(block.pre_hash, none())
        assert_that(block.block_hash, none())
    
    def test_CreateABlockWhenSetAPropertyThenItCouldNotBeSetAgain(self):
        block = Block(0, 0, "hello", "123", "456")
        block.index = 1
        block.time_stamp = 1
        block.data = "bye"
        block.pre_hash = "789"
        block.block_hash = "100"
        assert_that(block.index, equal_to(0))
        assert_that(block.time_stamp, equal_to(0))
        assert_that(block.data, equal_to("hello"))
        assert_that(block.pre_hash, equal_to("123"))
        assert_that(block.block_hash, equal_to("456"))
