from abc import abstractmethod

class IndexGenerator:

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def reset(self):
        pass