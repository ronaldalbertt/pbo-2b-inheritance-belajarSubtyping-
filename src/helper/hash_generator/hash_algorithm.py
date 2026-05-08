from abc import ABC, abstractmethod
class HashAlgorithm(ABC):
    @abstractmethod
    def hash(self, text: str) -> str:
        pass