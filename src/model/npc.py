from src.helper.pilihan import Pilihan

class Npc:
    def __init__(self):
        self.pilihan = "" # default = kosong
    
    def pilih_acak(self):
        obj_pilihan = Pilihan()
        self.pilihan = obj_pilihan.get_computer_choice()