# Desarrollo de aplicaciones multiplataforma 2024/25
# Álvaro Cilleruelo Sinovas

# Fizz - Buzz

def fizz_buzz (fizz, buzz):
    num_fizz = 0
    num_buzz = 0
    for i in range(100):
        if ((i % 3) == 0):
            if (i % 5 == 0):
                print(f"{fizz}-{buzz}")
                num_fizz += 1
                num_buzz += 1
            else:
                print(f"{fizz}")
                num_fizz += 1
        elif (i % 5 == 0):
            print(f"{buzz}")
            num_buzz += 1
    print(f"Fizz se ha impreso {num_fizz} veces y Buzz {num_buzz} veces.")     