# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Condicionales

print(f"Indica su edad.")
edad = int(input())

if (edad >= 18):
    print(f"Eres mayor de edad.")
elif (edad > 12):
    print(f"Eres adolescente.")
else:
    print(f"Eres un niño.")

match edad:
    case 0:
        print(f"¡A nacer!👶")
    case 18:
        print(f"¡A la cárcel!👨‍⚖️")
    case 65:
        print(f"¡Jubilación!👵👴")
    case 100:
        print(f"💀")
    case _:
        print(f"Que edad menos especial...🤣")