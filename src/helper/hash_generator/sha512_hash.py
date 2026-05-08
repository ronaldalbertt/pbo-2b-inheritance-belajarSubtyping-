import hashlib
from hash_algorithm import HashAlgorithm
class SHA512Hash(HashAlgorithm):
    def hash(self, text: str) -> str:
        result = hashlib.sha512(text.encode())
        return result.hexdigest()