import pytest
from hamcrest import *
from unittest.mock import Mock

from usecase.miner import Miner
from entity.block import Block
from entity.policy import Policy
from entity.hash_generate import HashGenerate
from entity.index_generator import IndexGenerator

class TestMiner:

    def test_GivenABlockWhenCallMineThenItShouldReturnCompleteBlockWithHashAndIndex(self):
        block = Mock(return_value = Block)
        block.time_stamp = 1000
        block.data = "Hello World"
        block.pre_hash = "pre_hash"

        policy = Mock(return_value = Policy)
        policy.check.return_value = True

        hash_generator = Mock(return_value = HashGenerate)
        hash_generator.generate.return_value = "bfc67cb022d482b0860acd864d021979a827fab44e0b4cd1030dbb058b7d9e7c"

        index_generator = Mock(return_value = IndexGenerator)
        index_generator.next.return_value = 0

        miner = Miner(policy, index_generator, hash_generator)
        block = miner.mine(block)

        hash_generator.generate.assert_called_once_with(str(0) + str(1000) + "Hello World" + "pre_hash")
        index_generator.next.assert_called_once()
        policy.check.assert_called_once()

        assert_that(block.index, equal_to(0))
        assert_that(block.block_hash, equal_to("bfc67cb022d482b0860acd864d021979a827fab44e0b4cd1030dbb058b7d9e7c"))