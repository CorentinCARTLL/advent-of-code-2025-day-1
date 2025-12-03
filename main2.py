with open('input.txt', 'r',encoding='utf-8') as fichier:
    instructions = fichier.read().split()

position = 50
code =0


for i in range(len(instructions)):
    sens = instructions[i][0]
    valeur =int(instructions[i][1:])
    print("Instruction : ",instructions[i])

    print(valeur)
    if sens =="L":
        position += valeur
    if sens == "R":
        position -= valeur
    print("Position après instruction",position)
    print("Code: ",code)

print(code)
