import tkinter as tk


class View(tk.Frame):
    def __init__(self, parent):

        super().__init__(parent)

        self.label = tk.Label(self, text='User:')
        self.label.grid(row=1, column=0)

        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(self, textvariable=self.input_var, width=30)
        self.input_entry.grid(row=1, column=1, sticky=tk.NSEW)

        self.add_button = tk.Button(self, text='Add', command=self.add_button_clicked)
        self.add_button.grid(row=1, column=2, padx=10)
        self.del_button = tk.Button(self, text='Del', command=self.del_button_clicked)
        self.del_button.grid(row=2, column=2, padx=10)
        self.show_button = tk.Button(self, text='Show', command=self.show_button_clicked)
        self.show_button.grid(row=3, column=2, padx=10)

        self.output_label = tk.Label(self, text='Users:', foreground='red')
        self.output_label.grid(row=4, column=1, sticky=tk.W)

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def add_button_clicked(self):
        if self.controller:
            self.controller.add(self.input_var.get())

    def del_button_clicked(self):
        if self.controller:
            self.controller.delete()

    def show_button_clicked(self):
        if self.controller:
            self.controller.show()

    def show(self, user_list):
        self.output_label['text'] = user_list
        self.output_label['foreground'] = 'green'
        self.output_label.after(9000, self.hide_user_list)

        self.input_entry['foreground'] = 'black'
        self.input_var.set('')

    def hide_user_list(self):
        self.output_label['text'] = ''






