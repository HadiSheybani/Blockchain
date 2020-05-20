import pytest
from hamcrest import *

from usecase.dict2blockchain import Dict2BlockChain

class TestDict2BlockChain:

    def setup_method(self):
        self.__blockchain_dict = dict()
        self.__blockchain_dict['block0'] = {'index' : '0', 
                                            'time_stamp' : '1000', 
                                            'data' : 'first block', 
                                            'pre_hash' : 'nothing', 
                                            'block_hash' : 'first block hash'}
        self.__blockchain_dict['block1'] = {'index' : '1', 
                                            'time_stamp' : '2000', 
                                            'data' : 'second block', 
                                            'pre_hash' : 'first block hash', 
                                            'block_hash' : 'second block hash'}
        self.__dict2blockchain = Dict2BlockChain()

    def test_GivenBlockChainWithWrongBlockWhenCallConvertThenItShouldRaiseValueError(self):
        del self.__blockchain_dict['block0']['index']
        try:
            self.__dict2blockchain.convert(self.__blockchain_dict)
            assert False
        except ValueError as error:
            assert_that(str(error), equal_to('block0 value is incorrect'))

    def test_GivenBlockChainWithRightBlockWhenCallConvertThenItShouldReturnBlockChain(self):
        try:
            blockchain = self.__dict2blockchain.convert(self.__blockchain_dict)
            chain = blockchain.get_chain()
            assert_that(chain[0].index, equal_to(0))
            assert_that(chain[0].time_stamp, equal_to(1000))
            assert_that(chain[0].data, equal_to('first block'))
            assert_that(chain[0].pre_hash, equal_to('nothing'))
            assert_that(chain[0].block_hash, equal_to('first block hash'))
            assert_that(chain[1].index, equal_to(1))
            assert_that(chain[1].time_stamp, equal_to(2000))
            assert_that(chain[1].data, equal_to('second block'))
            assert_that(chain[1].pre_hash, equal_to('first block hash'))
            assert_that(chain[1].block_hash, equal_to('second block hash'))
        except ValueError:
            assert False

