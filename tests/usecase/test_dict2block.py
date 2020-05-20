import pytest
from hamcrest import *

from usecase.dict2block import Dict2Block

class TestDict2Block:
    def setup_method(self):
        self.__dict2block = Dict2Block()
        self.__block_dict = dict()
        self.__block_dict['index'] = 1
        self.__block_dict['time_stamp'] = 1000
        self.__block_dict['data'] = 'helloworld'
        self.__block_dict['pre_hash'] = 'thisisprehash'
        self.__block_dict['block_hash'] = 'thisisblockhash'

    def __check_valueerror(self, e : str):
        try:
            self.__dict2block.convert(self.__block_dict)
            assert False
        except ValueError as error:
            assert_that(str(error), equal_to(e))

    def test_GivenADictWithoudIndexKeyWhenCallConvertThenItShouldRasieValueError(self):
        del self.__block_dict['index']
        self.__check_valueerror('No Index Value')
        
    def test_GivenADictWithoudTimeStampWhenCallConvertThenItShouldRaiseValueError(self):
        del self.__block_dict['time_stamp']
        self.__check_valueerror('No Time Stamp Value')
    
    def test_GivenADictWithoudDataWhenCallConvertThenItShouldRaiseValueError(self):
        del self.__block_dict['data']
        self.__check_valueerror('No Data Value')

    def test_GivenADictWithoudPreHashWhenCallConvertThenItShouldRaiseValueError(self):
        del self.__block_dict['pre_hash']
        self.__check_valueerror('No PreHash Value')
    
    def test_GivenADictWithoudBlockHashWhenCallConvertThenItShouldRaiseValueError(self):
        del self.__block_dict['block_hash']
        self.__check_valueerror('No BlockHash Value')
    
    def test_GivenARightDictWhenCallConvertThenItShouldReturnBlock(self):
        block = self.__dict2block.convert(self.__block_dict)
        assert_that(block.index, equal_to(1))
        assert_that(block.time_stamp, equal_to(1000))
        assert_that(block.data, equal_to('helloworld'))
        assert_that(block.pre_hash, equal_to('thisisprehash'))
        assert_that(block.block_hash, equal_to('thisisblockhash'))