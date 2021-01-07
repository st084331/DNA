import random
X = ""
Y = ''
n = random.randint(3,1000)
m = random.randint(3,1000)
for i in range(n):
    r1 = random.randint(0, 100)
    if r1 <= 25:
        X += 'A'
    elif 25 < r1 <= 50:
        X += 'C'
    elif 50 < r1 <= 75:
        X += 'T'
    else:
        X += 'G'
for i in range(m):
    r2 = random.randint(0, 100)
    if r2 <= 25:
        Y += 'A'
    elif 25 < r2 <= 50:
        Y += 'C'
    elif 50 < r2 <= 75:
        Y += 'T'
    else:
        Y += 'G'
print('Вот наши последовательности')
print(X)
print(Y)
matrix = []
# Получаем коэфициенты
d = -(max(n,m))
A = d**2
for i in range(len(X) + 1):
    matrix.append([])
    for j in range(len(Y) + 1):
        matrix[i].append([])
# Базис матицы
for i in range(len(matrix)):
    matrix[i][0] = 0
    matrix[i][1] = d * i
for j in range(len(matrix[0])):
    matrix[0][j] = 0
    matrix[1][j] = d * j
# Строим матрицу
for i in range(len(X)):
    for j in range(len(Y)):
        if X[i] == Y[j]:
            a = A
        else:
            a = -A
        matrix[i+1][j+1] = max(matrix[i][j] + a, matrix[i+1][j] + d, matrix[i][j+1] + d)
New_X = ""
New_Y = ""
i = len(X) - 1
j = len(Y) - 1

while (i >= 0 and j >= 0):
    S = matrix[i+1][j+1]
    SDiag = matrix[i][j]
    SUp = matrix[i+1][j]
    SLeft = matrix[i][j+1]
    if X[i] == Y[j]:
        a = A
    else:
        a = -A
    if (S == SDiag + a):
            New_X = X[i] + New_X
            New_Y = Y[j] + New_Y
            i -= 1
            j -= 1
    elif (S == SLeft + d):
        New_X = X[i] + New_X
        New_Y = "-" + New_Y
        i -= 1
    elif (S == SUp + d):
        New_X = "-" + New_X
        New_Y = Y[j] + New_Y
        j -= 1

while i >= 0:
    New_X = X[i] + New_X
    New_Y = "-" + New_Y
    i -= 1
while j >= 0:
    New_X = "-" + New_X
    New_Y = Y[j] + New_Y
    j -= 1
print('Проводим выравнивание')
print(New_X)
print(New_Y)
result_str = ''
for i in range(len(New_X)):
    if New_X[i] == '-':
        result_str += New_Y[i]
    elif New_Y[i] == '-':
        result_str += New_X[i]
    elif New_X[i] == New_Y[i]:
        result_str += New_X[i]
    else:
        print('Ошибочка', i)
print('Объединяем')
print(result_str)