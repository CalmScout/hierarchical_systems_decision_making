import numpy as np

# проверяет интервальную матрицу парных сравнений на согласованость по определению
# Входящими параметрами есть матрицы L U значений верхних и нажних границ интервалов.
#

def isConsistentIPCM(L,U):
    flag = True
    if len(L) != len(U):
        errorCode = 0
        print("Error")

    n = len(L)

    matr1 = np.zeros((n,n))
    matr2 = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            l = 0
            for k in range(n):
                matr1[l] = L[i][k]*L[k][j]
                matr2[l] = U[i][k]*U[k][j]
                l += 1
            print(matr1)
            print(matr2)

            if np.max(matr1) > np.min(matr2):

                flag = False

    return flag

#
# Проверяет интервальные матрицы парных сравнений на слабую, порядковую согласованость
# Входящими параметрами есть матрицы L U значений верхних и нажних границ интервалов.
# Используется для проверки предпочтение по ЦЕНТРУ МАСС

def isWeakConsistICPM1(L,U):
    flag = True
    if len(L)!=len(U): print("Error: Different size of matrix L U")
    N = len(L)

    A=np.ones((N,N))

    #находим центр масс, по матрицам L U как среднее арифметическое и сравниваем
    for i in range (len(L)):
        for j in range (len(L)):
            A[i][j]=(L[i][j]+U[i][j])/2

    if N>2:
        for i in range(N):
            for j in range(i,N):
                for k in range(i,N):
                    if (A[i][j] > 1) and (A[j][k] > 1) and (A[i][k] < 1):
                        flag = False
                        break
                    if (A[i][j] == 1) and (A[j][k] > 1) and (A[i][k] <= 1):
                        flag = False
                        break
                    if (A[i][j] > 1) and (A[j][k] == 1) and (A[i][k] <= 1):
                        flag = False
                        break

    return flag

#
# Проверяет интервальные матрицы парных сравнений на слабую, порядковую согласованость
# Входящими параметрами есть матрицы L U значений верхних и нажних границ интервалов.
# Используется для проверки ПОРЯДКОВОЕ ПРЕДПОЧТЕНИЕ
#Запишем число 1 как интервальное со значениями [1;1]
#
def isWeakConsistICPM2(L,U):
    flag = True
    if len(L)!=len(U): print("Error: Different size of matrix L U")
    N = len(L)

    if N>2:
        for i in range(N):
            for j in range(i,N):
                for k in range(i,N):
                    if (L[i][j] > 1 and U[i][j]>1) and (L[j][k] > 1 and U[j][k] >1) and (L[i][k] < 1 and U[i][k] <1):
                        flag = False
                        break
                    if (L[i][j] == 1 and U[i][j]==1) and (L[j][k] > 1 and U[j][k] >1) and (L[i][k] <= 1 and U[i][k] <=1):
                        flag = False
                        break
                    if (L[i][j] > 1 and U[i][j]>1) and (L[j][k] == 1 and U[j][k] == 1) and (L[i][k] <= 1 and U[i][k] <=1):
                        flag = False
                        break

    return flag

