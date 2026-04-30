class Player:
    def __init__(self):
        self.pilihan = "" # default kosong

    def input_pilihan(self):
        self.pilihan = input("Pilihan kamu: ").lower()