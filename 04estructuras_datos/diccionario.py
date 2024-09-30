# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Diccionarios (clave: valor)

diccionario = {
    1: "Uno",
    2: "Dos",
    3: "Tres"
}
diccionario2 = dict([
    (1, "Uno"),
    (2, "Dos"),
    (3, "Tres")
])
diccionario3 = dict(
    Uno=1,
    Dos=2,
    Tres=3
)
print(f"{diccionario} tipo:{type(diccionario)}")
print(f"{diccionario2} tipo:{type(diccionario2)}")
print(f"{diccionario3} tipo:{type(diccionario3)}")

print(diccionario[1])
print(diccionario3["Dos"])

diccionario[1] = "Cuatro"
diccionario[5] = "Cinco"
diccionario["número"] = "Patata"
print(diccionario)

print(diccionario.keys())
print(diccionario.values())

diccionario.pop(5, "No encontrado")
print(diccionario)

diccionario.popitem()
print(diccionario)