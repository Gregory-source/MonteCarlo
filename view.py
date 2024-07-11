from  contr import Controller
import simulation
import tkinter as tk

class View(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Monte Carlo Simulation")
        self.geometry("500x500")
        self.controller= None
        self.create_widgets()

    def create_widgets(self):
        l1 = tk.Label(self, text="Ilosc skrzyzowan")
        l1.grid(row=0, column=0, pady=2)
        self.ilosc_skrzyzowan_entry = tk.Entry(self, width=30)
        self.ilosc_skrzyzowan_entry.grid(row=0, column=1, pady=3)

        l2 = tk.Label(self, text="Ilosc prob")
        l2.grid(row=1, column=0, pady=2)
        self.ilosc_prob_entry = tk.Entry(self, width=30)
        self.ilosc_prob_entry.grid(row=1, column=1, pady=3)

        # simulation button
        self.simulation_button = tk.Button(self, text='Symulacja', command=self.simulate)
        self.simulation_button.grid(row=3, column=1, pady = 5)

    def set_controller(self, controller):
        self.controller = controller

    def simulate(self):
        if self.controller:
            self.controller.model.ilosc_skrzyzowan = int(self.ilosc_skrzyzowan_entry.get())
            self.controller.model.ilosc_prob = int(self.ilosc_prob_entry.get())
            trasy = self.controller.model.losuj_trasy()
            oczekiwana = self.controller.model.oczekiwana_odleglosc(trasy)
            print("Oczekiwana odleglosc to: {}".format(oczekiwana))
            s = simulation.Simulation(trasy)
            s.rysuj_zasieg(oczekiwana)
            return oczekiwana
