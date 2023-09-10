class Menu:
    def __init__(self, menu):
        self.menu = menu
        self.position = 0

    def to_the_right(self):
        self.position = (self.position + 1) % len(self.menu)

    def to_the_left(self):
        self.position = (self.position - 1) % len(self.menu)

    def display(self):
        modified_menu = []

        for index, item in enumerate(self.menu):
            if index == self.position:
                modified_menu.append([item])
            else:
                modified_menu.append(item)

        return str(modified_menu)
