import pytest
from hamcrest import *

from entity.sha256_hash import SHA256Hash

class TestSHA256Hash:

    def test_GivenAStringObjectWhenCallGenerateThenItShouldReturnProperHash(self):
        hash_object = SHA256Hash()
        output = hash_object.generate("Hello")
        assert_that(output, equal_to("185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"))