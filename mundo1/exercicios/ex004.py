algo = input("Digite algo: ")



print(f"o tipo primitivo desse valor é {type(algo)}/n")
print(f"só tem espaços? {algo.isspace()}")
print(f"é um número? {algo.isnumeric()}")
print(f"é alfabético? {algo.isalpha()}")
print(f"é alfanumerico? {algo.isalnum()}")
print(f"Está em maiúsculas? {algo.isupper()}")
print(f"Está em minúsculas? {algo.islower()}")
print(f"Está capitalizada? {algo.istitle()}")