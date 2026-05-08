import os
from hash_manager import HashManager
from md5_hash import MD5Hash
from sha1_hash import SHA1Hash
from sha256_hash import SHA256Hash
from sha512_hash import SHA512Hash

# Kelas utilitas untuk pewarnaan teks di terminal (ANSI Escape Codes)
class Color:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    RESET = '\033[0m'
    MAGENTA = '\033[95m'

class CLI:
    def __init__(self):
        self.manager = HashManager()
        # Pemetaan menu ke KELAS (bukan objek/instance) untuk efisiensi memori
        self.algorithm_map = {
            "1": MD5Hash,
            "2": SHA1Hash,
            "3": SHA256Hash,
            "4": SHA512Hash
        }

    def clear(self):
        """Membersihkan layar terminal secara native sesuai OS."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def banner(self):
        print(f"{Color.CYAN}{Color.BOLD}")
        print("╔══════════════════════════════════════════════════════════╗")
        print("║                                                          ║")
        print("║                ⚡ CRYPTO HASH GENERATOR ⚡               ║")
        print("║                (OOP & Subtyping Concept)                 ║")
        print("║                                                          ║")
        print("╚══════════════════════════════════════════════════════════╝")
        print(f"{Color.RESET}")

    def menu(self):
        print(f"{Color.YELLOW}[ AVAILABLE ALGORITHMS ]{Color.RESET}")
        print(f"  {Color.GREEN}1.{Color.RESET} MD5      {Color.RED}(Legacy/Insecure){Color.RESET}")
        print(f"  {Color.GREEN}2.{Color.RESET} SHA1     {Color.RED}(Legacy/Insecure){Color.RESET}")
        print(f"  {Color.GREEN}3.{Color.RESET} SHA256   {Color.GREEN}(Recommended){Color.RESET}")
        print(f"  {Color.GREEN}4.{Color.RESET} SHA512   {Color.GREEN}(High Security){Color.RESET}")
        print(f"  {Color.MAGENTA}0.{Color.RESET} Exit\n")

    def show_result(self, algorithm_name, text, result):
        print(f"\n{Color.CYAN}┌{'─' * 58}┐{Color.RESET}")
        print(f"{Color.CYAN}│{Color.RESET} {Color.BOLD}HASH RESULT{Color.RESET}".ljust(69) + f"{Color.CYAN}│{Color.RESET}")
        print(f"{Color.CYAN}├{'─' * 58}┤{Color.RESET}")
        
        print(f"{Color.CYAN}│{Color.RESET} {Color.YELLOW}Algorithm   :{Color.RESET} {algorithm_name}".ljust(69) + f"{Color.CYAN}│{Color.RESET}")
        print(f"{Color.CYAN}│{Color.RESET} {Color.YELLOW}Input Text  :{Color.RESET} {text[:40]}{'...' if len(text) > 40 else ''}".ljust(69) + f"{Color.CYAN}│{Color.RESET}")
        print(f"{Color.CYAN}│{Color.RESET} {Color.YELLOW}Hash Length :{Color.RESET} {len(result)} chars".ljust(69) + f"{Color.CYAN}│{Color.RESET}")
        
        print(f"{Color.CYAN}├{'─' * 58}┤{Color.RESET}")
        
        # Format output hash agar mudah dibaca jika terlalu panjang
        print(f"{Color.GREEN}{result}{Color.RESET}")
        print(f"{Color.CYAN}└{'─' * 58}┘{Color.RESET}\n")

    def run(self):
        while True:
            self.clear()
            self.banner()
            self.menu()

            choice = input(f"{Color.BOLD}Select Algorithm (0-4): {Color.RESET}").strip()

            if choice == "0":
                print(f"\n{Color.CYAN}System shutting down. Goodbye!{Color.RESET}")
                break

            algorithm_class = self.algorithm_map.get(choice)

            if algorithm_class is None:
                print(f"\n{Color.RED}[ ERROR ] Invalid choice. Please select 0-4.{Color.RESET}")
                input(f"{Color.MAGENTA}Press Enter to continue...{Color.RESET}")
                continue

            # Instansiasi objek hanya saat diperlukan
            algorithm_instance = algorithm_class()
            self.manager.set_algorithm(algorithm_instance)

            text = input(f"{Color.BOLD}Input text to hash: {Color.RESET}")
            
            if not text:
                print(f"\n{Color.RED}[ ERROR ] Input text cannot be empty.{Color.RESET}")
                input(f"{Color.MAGENTA}Press Enter to continue...{Color.RESET}")
                continue

            result = self.manager.generate_hash(text)
            
            # Menggunakan nama kelas sebagai representasi algoritma
            algo_name = algorithm_instance.__class__.__name__.replace('Hash', '')
            self.show_result(algo_name, text, result)

            input(f"{Color.MAGENTA}Press Enter to return to menu...{Color.RESET}")


if __name__ == "__main__":
    app = CLI()
    try:
        app.run()
    except KeyboardInterrupt:
        print(f"\n{Color.RED}Program interrupted by user. Exiting...{Color.RESET}")