with open('input.txt', 'r',encoding='utf-8') as fichier:
    instructions = fichier.read().split()

position = 50
code = 0
for i in range(len(instructions)):
    sens = instructions[i][0]
    valeur =int(instructions[i][1:])
    if sens =="L":
        print("Gauche")
        position += valeur
    if sens == "R":
        print("Droite")
        position -= valeur
    if position > 99:
        position %= 100
    if position < 0:
        position %=100
    if position == 0:
        code +=1
        print(code)
    print(position)

print(code)
