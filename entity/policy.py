from abc import abstractmethod

class Policy:

    @abstractmethod
    def check(self, hash : str):
        pass


