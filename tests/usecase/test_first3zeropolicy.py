import pytest
from hamcrest import *

from usecase.first3zeropolicy import First3ZeroPolicy

class TestFirst3ZeroPolicy:
    def setup_method(self):
        self.__policy = First3ZeroPolicy()
    
    def test_GivenRightHashWhenCallCheckThenItShouldReturnTrue(self):
        hash = "000thisisrighthash"
        assert_that(self.__policy.check(hash), equal_to(True))
    
    def test_GivenWrongHashWhenCallCheckThenItShouldReturnFalse(self):
        hash = "thisiswronghash"
        assert_that(self.__policy.check(hash), equal_to(False))