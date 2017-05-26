inputs =[1,1,0,1]
decimal = sum([pow(2,i) for i in range(len(inputs)) if inputs[len(inputs)-i-1] == 1])
print(decimal)