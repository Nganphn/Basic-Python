def cel_2_fah(tem1):
    fah = round((tem1 * 2 + 30), 1)
    
    print(fah)

cel_2_fah(float(input("Provide the temperature in Celsius: ")))

def fah_2_cel(tem2):
    cel = round(((tem2 - 30) / 2), 1)
    
    print(cel)

fah_2_cel(float(input("Provide the temperature in Fahrenheit: ")))