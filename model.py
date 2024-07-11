from contr import Controller
import random

class Model:
    def __init__(self):
        self.ilosc_prob = None
        self.ilosc_skrzyzowan = None
        self.controller = None

    def losuj_trasy(self):  # losuje trasy, czyli ciagi kolejnych kierunkow jazdy
        trasy = []
        for i in range(self.ilosc_prob):
            trasa = []
            for j in range(self.ilosc_skrzyzowan):
                # losujemy kierunek: 0 stopni- prosto,90 stopni - do gory, 180 -w lewo, 270 - w prawo
                liczba = random.randint(0, 3) * 90
                trasa.append(liczba)
            trasy.append(trasa)
        return trasy


    def oczekiwana_odleglosc(self,trasy):
        lista = []
        for trasa in trasy:
            x, y = 0.0, 0.0
            biezacy_kierunek = 0
            for kierunek in trasa:
                biezacy_kierunek = (biezacy_kierunek +  kierunek)%360
                if biezacy_kierunek == 0:
                    x += 1
                elif biezacy_kierunek == 90:
                    y += 1
                elif biezacy_kierunek == 180:
                    x -= 1
                else:
                    y -= 1
            lista.append((x**2 + y**2)**(0.5))
        return sum(lista)/len(lista)

    def set_controller(self, controller):
        self.controller = controller