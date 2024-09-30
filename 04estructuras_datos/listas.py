# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Listas

lista = ["Uno", "Dos", "Tres", "Cuatro"]
lista2 = list(("Uno", "Dos", "Tres", "Cuatro"))
print(f"{lista} tipo:{type(lista)}")
print(f"{lista2} tipo:{type(lista2)}")


lista.append("Cinco")
print(lista)

lista.pop()
print(lista)

lista.insert(3,"Cinco")
print(lista)

lista.pop(2)
print(lista)

lista.sort()
print(lista)

lista.reverse()
print(lista)

lista.insert(2, "Tres")
print(lista)

