# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Sets (inmutables, desordenados y únicos)

set1 = set(["Uno", "Dos", "Tres", "Cuatro"])
print(f"{set1} tipo:{type(set1)}")

set1.add("Uno") # Elementos únicos
print(set1)

set1.add("Cinco")
print(set1)

set1.remove("Cinco")
print(set1)

set1.pop() #aleatorio
print(set1)

set1.clear()
print(set1)




