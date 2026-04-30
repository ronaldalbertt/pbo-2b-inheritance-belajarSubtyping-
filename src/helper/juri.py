
class Juri:
    def determine_winner(self, player, computer):
        if player == computer.pilihan:
            print("Hasil: Seri!\n")
        elif (player == "batu" and computer.pilihan == "gunting") or \
            (player == "gunting" and computer.pilihan == "kertas") or \
            (player == "kertas" and computer.pilihan == "batu"):
            print("Hasil: Menang!\n")
        else:
            print("Hasil: Kalah!\n")

