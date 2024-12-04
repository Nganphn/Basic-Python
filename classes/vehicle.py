class Vehicle:

    # overrise the constructor
    def __init__(self, make = "", model = "", engine_cc = 0, power_kw = 0):
        self.make = make
        self.model = model
        self.engine_cc = engine_cc
        self.power_kw = power_kw

    # override conversion to string
    def __str__(self):
        return self.make + " " + self.model + ", " + str(self.engine_cc) + "cc, " + str(self.power_kw) + "kw"
    
    def hoursepower(self):
        return self.power_kw * 1.341

    make = ""
    model = ""
    engine_cc = 0
    power_kw = 0