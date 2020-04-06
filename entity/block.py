
class Block:
    def __init__(self, index : "int" = None,
                        time_stamp : "long long" = None,
                        data : "string" = None,
                        pre_hash : "string" = None,
                        block_hash : "string" = None):
        self.__index = index
        self.__time_stamp = time_stamp
        self.__data = data
        self.__pre_hash = pre_hash
        self.__block_hash = block_hash
    
    @property
    def index(self):
        return self.__index
    
    @property
    def time_stamp(self):
        return self.__time_stamp
    
    @property
    def data(self):
        return self.__data
    
    @property
    def pre_hash(self):
        return self.__pre_hash
    
    @property
    def block_hash(self):
        return self.__block_hash
    
    @index.setter
    def index(self, index):
        if self.__index is None:
            self.__index = index
    
    @time_stamp.setter
    def time_stamp(self, time_stamp):
        if self.__time_stamp is None:
            self.__time_stamp = time_stamp

    @data.setter
    def data(self, data):
        if self.__data is None:
            self.__data = data
    
    @pre_hash.setter
    def pre_hash(self, pre_hash):
        if self.__pre_hash is None:
            self.__pre_hash = pre_hash
    
    @block_hash.setter
    def block_hash(self, block_hash):
        if self.__block_hash is None:
            self.__block_hash = block_hash