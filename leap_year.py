def leap_year():
    text=input("ingrese el año: ")
    year=int(text)
    resto=year%4
    cent=year%100
    cuat=year%400
    if resto==0:
        if cent==0:
            if cuat==0:
                print(f"El año {year} es bisiesto")
            else:
                print(f"el año {year} no es bisiesto")
            else: 
                print(f"El año {year} es bisiesto")
            else:
                 print(f"el año {year} no es bisiesto")
leap_year()

