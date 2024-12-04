class Cat:
    def __init__(self, name = "", color = ""):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name + ", " + "Color: " + self.color
    
    def meow(self):
        return "Meoooooow!"

    name = ""
    color = ""