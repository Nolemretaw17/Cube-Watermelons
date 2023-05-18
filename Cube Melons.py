test_input = "10 10 11 5"
x = test_input.split(" ")

Length = int(x[0])
Width = int(x[1])
Height = int(x[2])
Side = int(x[3])
CubeMelon = int(x[3])**3
Answer = (Length // Side) * (Width // Side) * (Height // Side)

if Length < Side or Width < Side or Height < Side:
    print("0")
else:
    print(Answer)