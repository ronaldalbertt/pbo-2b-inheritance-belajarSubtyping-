from pilihan import Pilihan
from juri import Juri

class Game:

    def display_logo(self):
        print(" █████╗ ███████╗███████╗ █████╗ ███╗   ██╗")
        print("██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║")
        print("███████║█████╗  █████╗  ███████║██╔██╗ ██║")
        print("██╔══██║██╔══╝  ██╔══╝  ██╔══██║██║╚██╗██║")
        print("██║  ██║██║     ██║     ██║  ██║██║ ╚████║")
        print("╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝")
    
    def display_menu(self):
        print("=== Game Batu Gunting Kertas ===")
        print("Silahkan ketik,")
        print("batu, gunting, kertas : untuk bermain")
        print("help : untuk cara bermain")
        print("exit : untuk keluar\n")

    def play_game(self):

        self.display_logo()
        self.display_menu()
        
        while True:
            player = input("Pilihan kamu: ").lower()

            if player == "exit":
                print("Terima kasih sudah bermain!")
                break

            if player not in ["batu", "gunting", "kertas"]:
                print("Input tidak valid, coba lagi.\n")
                continue

            obj_pilihan = Pilihan()
            computer = obj_pilihan.get_computer_choice()
            print(f"Komputer memilih: {computer}")

            obj_juri = Juri()
            obj_juri.determine_winner(player, computer)


if __name__ == "__main__":
    game = Game()   # membuat object game
    game.play_game()