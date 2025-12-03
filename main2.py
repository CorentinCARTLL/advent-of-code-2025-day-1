with open('input.txt', 'r',encoding='utf-8') as fichier:
    instructions = fichier.read().split()

position = 50
code =0


for i in range(len(instructions)):
    sens = instructions[i][0]
    valeur =int(instructions[i][1:])
    print("--------------Instruction : ",instructions[i])
    print("Position initiale : ", position)
    print("Code avant: ",code)
    if sens =="L":
        distance_zero = position
        if position ==0:
            distance_zero =100
        if valeur >= distance_zero:
            code +=1
            reste= valeur-distance_zero
            code += reste//100
        position =(position-valeur)%100
    if sens == "R":
        distance_zero = 100-position
        if valeur >= distance_zero:
            code +=1
            reste = valeur- distance_zero
            code += reste//100
        position =(position+valeur)%100
    print("Position après instruction",position)
    print("Code après : ",code)

print(code)
