matrix = [[10,20],
          [30,40],
          [50,60]]
matrix_transpose = [[0,0,0],
                    [0,0,0]]

for row in range(len(matrix)):
    for columns in range(len(matrix[0])):

     matrix_transpose [columns][row]=matrix [row][columns]
print("transpesed Martix is :")
for item in matrix_transpose:
   print(item)
