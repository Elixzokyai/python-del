class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
    def print_task(self):
        print(f"Task title: {self.title} : {self.description}")
task1 = Task("Buy Groceries", "Milk,flour and sugar")
task1.print_task()
