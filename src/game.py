from src.helper.juri import Juri
from src.model.npc import Npc
from src.model.player import Player

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
            
            player = Player()
            player.input_pilihan()

            if player.pilihan == "exit":
                print("Terima kasih sudah bermain!")
                break

            if player.pilihan not in ["batu", "gunting", "kertas"]:
                print("Input tidak valid, coba lagi.\n")
                continue

            computer = Npc()
            computer.pilih_acak()
            print(f"Komputer memilih: {computer.pilihan}")

            obj_juri = Juri()
            obj_juri.determine_winner(player, computer)

