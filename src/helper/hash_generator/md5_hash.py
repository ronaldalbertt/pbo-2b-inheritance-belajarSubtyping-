import hashlib
from hash_algorithm import HashAlgorithm
class MD5Hash(HashAlgorithm):
    def hash(self, text: str) -> str:
        result = hashlib.md5(text.encode())

        return result.hexdigest()