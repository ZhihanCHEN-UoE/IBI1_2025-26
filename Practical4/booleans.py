X = True
Y = False
lis = []
text = ["X and Y","X or Y","not (X and Y)","not (X or Y)"]
command = [X and Y,X or Y,not(X and Y),not (X or Y)]
for i in range(len(text)):
    W = command[i]
    lis.append([text[i],command[i]])
print(lis)
# the result of this programme is [['X and Y', False], ['X or Y', True], ['not (X and Y)', True], ['not (X or Y)', False]]

