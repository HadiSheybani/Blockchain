import pytest
from hamcrest import *

from entity.integer_index_generator import IntegerIndexGenerator

class TestIntegerGenerator:

    def test_WhenCallGenerateThenItShouldReturnLastNumberPlusOne(self):
        index_gen = IntegerIndexGenerator()
        
        for counter in range(0, 1000):
            assert_that(index_gen.next(), equal_to(counter))