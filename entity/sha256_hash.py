from .hash_generate import HashGenerate
import hashlib

class SHA256Hash(HashGenerate):
    def __init__(self):
        self.__hash_object = hashlib.sha256()

    def generate(self, object : str):
        self.__hash_object.update(str(object).encode('utf-8'))
        return self.__hash_object.hexdigest()