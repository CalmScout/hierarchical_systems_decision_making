#создает строку парных сравнений со случайными числами от 1 до 9
str=GIPCM.genRandLinePC(n)

[A, warn]=GIPCM.createWeakConsistantPCM(str) # генерирует слабо согласованую матрицу парных сравнений

print('A:',A)

if cCPCM.isConsist(A)== True: 
    print ('A is consist')
elif cCPCM.isWeakConsist(A)== True:
    print ('A is Weak consist')

[L,U]=GIPCM.createConsistantIPCM(A) #генерирует из чткой интервальную матрицу парных сравнений,

#данный метод часто при формировании интервальной матрицы парных сравнений формирует полностью согласованную матрицу. 


if FLW.isConsistentIPCM(L,U) == True: #проверка на то что интервальная матрица является согласованой
    print('L U is Consist ok');
elif cCIPCM.isWeakConsistICPM1(L, U)==True: #проверка на то что интервальная матрица является слабо согласованой предпочтение по центру масс
    print("L,U is weak Consist")
    if cCIPCM.isWeakConsistICPM2(L,U)==True: print("L,U 2 is weak Consist") #проверка на то что интервальная матрица является слабо согласованой порядковое предпотение
