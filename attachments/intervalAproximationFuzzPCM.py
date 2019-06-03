import numpy as np

# Формирование нечеткой матрицы парных сравнений из заданой четкой матрицы
# Входящими параметрами являются четкая матрица парных сравненй PCM и тип цункции принадлежности нечеткого числа MF (membership function)
# на выходе получаем нечеткую матрицу парных сравненй

def createFuzzyPCM(PCM,MF):
    if len(PCM)<2:
        print ('Error PCM should have at least 2 elements')
    elif len(PCM)!=len(PCM[1]):
        print ("PCM is not a square matrix")
    else:
        FPCM=np.empty((len(PCM),len(PCM)),dtype=object)
        for i in range(len(PCM)):
            for j in range(len(PCM)):
                FPCM[i,j]=MF(PCM[i,j])
    return(FPCM)

# Функция формирует интервальную оценку уровня альфа
# входящими параметрами данной функции являются Нечеткое число треугольного типа, и значение уровня альфа,
# которое находится в диапазоне [0,1]
#
def getIntervalValue(a,alpha):
    if alpha <0 or alpha >1:
        print('Error! Alpha is not in range [0,1]')
    else:
        L=a[1]-(1-alpha)*(a[1]-a[0])
        U=a[1]+(1-alpha)*(a[2]-a[1])
    return[L,U]

#Функция создает множество k интервальных мариц парных сравнений
#разбивая интервал которому принадлежит аьфа [0,1] на k равных значений
#и формирует интервальную матрицу парных сравнений для каждого значения альфа
#входяшими параметрами есть нечеткая матрица парных сравнений и число к, количество интервалов
#
def setIntervalPCM(A,K):
    print('----------------------------------------')
    groupIPCM = np.empty((K), dtype=object)
    for k in range (K) :
        IPCM=np.empty((len(A),len(A)),dtype=object)
        for i in range(len(A)):
            for j in range(len(A)):
                IPCM[i,j]=getIntervalValue(A[i,j],(k)/K)
        groupIPCM[k]=IPCM
    return (groupIPCM)



