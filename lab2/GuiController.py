class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add(self, name):
        self.model.add_user(name)
        self.view.show(str(self.model.get_users()))

    def delete(self):
        self.model.delete_last_user()
        self.view.show(str(self.model.get_users()))

    def show(self):
        self.view.show(str(self.model.get_users()))
