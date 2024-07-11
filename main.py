from contr import Controller
from model import Model
from view import View
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # create a model
        model = Model()

        # create a view
        view = View()

        # create a controller
        controller = Controller(model, view)

        # set the controller to view and model
        view.set_controller(controller)
        model.set_controller(controller)



if __name__ == '__main__':
    app = App()
    app.mainloop()
