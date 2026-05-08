import hashlib
from hash_algorithm import HashAlgorithm
class SHA256Hash(HashAlgorithm):
    def hash(self, text: str) -> str:
        result = hashlib.sha256(text.encode())
        return result.hexdigest()