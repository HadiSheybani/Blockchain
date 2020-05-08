from .index_generator import IndexGenerator

class IntegerIndexGenerator(IndexGenerator):
    
    def __init__(self):
        self.__counter = 0
    
    def next(self):
        self.__counter = self.__counter + 1
        return self.__counter - 1
    
    def reset(self):
        self.__counter = 0