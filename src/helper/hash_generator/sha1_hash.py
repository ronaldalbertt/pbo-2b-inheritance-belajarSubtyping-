import hashlib
from hash_algorithm import HashAlgorithm
class SHA1Hash(HashAlgorithm):
    def hash(self, text: str) -> str:
        result = hashlib.sha1(text.encode())

        return result.hexdigest()