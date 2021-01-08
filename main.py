import random

def RAND():
    r = random.randint(0, 100)
    if r <= 25:
        return 'A'
    elif 25 < r <= 50:
        return 'C'
    elif 50 < r <= 75:
        return 'T'
    else:
        return 'G'

n = 100
m = 100
X = ''
Y = ''
for i in range(n):
    X += RAND()
for i in range(m):
    Y += RAND()
# Тест с малым изменением
"""
Y = X
A = []
for i in Y:
    A.append(i)
for i in range(5):
    A[random.randint(0,m - 1)] = RAND()
Y = ''.join(A)
"""
# Конец
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
#Тест для длинной последовательности
"""
if len(New_X) - len(X) <= 5:
    print('Верное выравнивание')
"""