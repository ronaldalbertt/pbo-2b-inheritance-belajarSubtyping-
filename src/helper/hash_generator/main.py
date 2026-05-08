from hash_manager import HashManager

from md5_hash import MD5Hash
from sha1_hash import SHA1Hash
from sha256_hash import SHA256Hash
from sha512_hash import SHA512Hash


class CLI:

    def __init__(self):
        self.manager = HashManager()

    def clear(self):
        print("\n" * 50)

    def banner(self):
        print("=" * 60)
        print("        STRING HASH GENERATOR - OOP & SUBTYPING")
        print("=" * 60)

    def menu(self):
        print("\n[ AVAILABLE ALGORITHMS ]")
        print("1. MD5")
        print("2. SHA1")
        print("3. SHA256")
        print("4. SHA512")
        print("0. Exit")

    def choose_algorithm(self, choice):

        algorithms = {
            "1": MD5Hash(),
            "2": SHA1Hash(),
            "3": SHA256Hash(),
            "4": SHA512Hash()
        }

        return algorithms.get(choice)

    def show_result(self, algorithm, text, result):

        print("\n" + "=" * 60)
        print("HASH RESULT")
        print("=" * 60)

        print(f"Algorithm : {algorithm.__class__.__name__}")
        print(f"Input Text: {text}")
        print(f"Hash Length : {len(result)}")
        print("-" * 60)
        print(result)
        print("=" * 60)

    def run(self):

        while True:

            self.clear()
            self.banner()
            self.menu()

            choice = input("\nChoose algorithm : ")

            if choice == "0":
                print("\nProgram selesai...")
                break

            algorithm = self.choose_algorithm(choice)

            if algorithm is None:
                print("\n[ ERROR ] Invalid choice")
                input("\nPress Enter to continue...")
                continue

            self.manager.set_algorithm(algorithm)

            text = input("\nInput text : ")

            result = self.manager.generate_hash(text)

            self.show_result(algorithm, text, result)

            input("\nPress Enter to continue...")


if __name__ == "__main__":
    app = CLI()
    app.run()