from hash_algorithm import HashAlgorithm
class HashManager:

    def __init__(self):
        self.algorithm = None

    def set_algorithm(self, algo: HashAlgorithm):
        self.algorithm = algo

    def generate_hash(self, text: str) -> str:

        if self.algorithm is None:
            return "Algorithm not set"

        return self.algorithm.hash(text)