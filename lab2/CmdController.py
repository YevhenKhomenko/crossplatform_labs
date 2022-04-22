from CmdView import View
from Model import Users


class Controller:

    def __init__(self):
        self.model = Users()
        self.view = View()

    def run(self):
        self.view.show_message("Enter operation type ('+' - add, '-' - del, 'l' - list, 'q' - quit): ")
        while True:
            cmd = self.view.get_input()

            if cmd == '+':
                self.view.show_message('Enter persons name: ')
                name = self.view.get_input()
                self.model.add_user(name)

            if cmd == '-':
                self.model.delete_last_user()

            if cmd == 'l':
                self.view.show_message(self.model.get_users())

            if cmd == 'q':
                break



