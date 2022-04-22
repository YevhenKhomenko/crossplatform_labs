import tkinter as tk
from GuiView import View
from GuiController import Controller
from Model import Users


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Lab2')

        # create a model
        model = Users()

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()

