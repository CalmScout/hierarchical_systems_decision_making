import numpy as np
from scipy.optimize import linprog

def gpm(L,U):
    n= int(len(L))
    #Формируем диагональную матрицу
    I=np.zeros((len(L),len(L)))
    for i in range(n):
        I[i,i]=1
    f=np.zeros(6*n)
    for i in range((2*n),(6*n)):
        f[i]=1

    A1eq=np.zeros((n,6*n))
    b1eq=np.zeros((n,1))
    A2eq = np.zeros((n, 6 * n))
    b2eq = np.zeros((n,1))

    for i in range(n):
        for j in range(n):
            A1eq[i,j] = -(n-1)*I[i,j]
            A1eq[i,(j+n)] = (L[i][j]-I[i][j])
            A1eq[i,(j+2*n)] = -I[i,j]
            A1eq[i,(j+3*n)] = -I[i,j]

            A2eq[i,j] = (U[i][j]-I[i][j])
            A2eq[i, (j + n)] = -(n - 1) * I[i, j]
            A2eq[i, (j + 4 * n)] = -I[i, j]
            A2eq[i, (j + 5 * n)] = -I[i, j]

    Aeq=np.zeros((2*n,6*n))
    beq=np.zeros(2*n)

    for j in range(6*n):
        for i in range(n):
            Aeq[i,j]=A1eq[i,j]
            Aeq[i+n, j] = A2eq[i, j]

    A1=np.zeros((n,6*n))
    b1=np.ones(n)
    for i in range(n):
        b1[i]=-b1[i]
    A2 = np.zeros((n, 6 * n))
    b2 = np.ones(n)

    E=np.ones((n,n))

    for i in range(n):
        for j in range(n):
            A1[i,j]=-I[i,j]
            A1[i,j+n]=-(E[i,j]-I[i,j])

            A2[i, j] = E[i,j]-I[i, j]
            A2[i, j + n] = I[i, j]

    A3=np.zeros((n,6*n))
    b3=np.zeros(n)

    for i in range(n):
        for j in range(n):
            A3[i,j]=I[i,j]
            A3[i,j+n]=-I[i,j]

    A=np.zeros((3*n,6*n))
    b=np.zeros((3*n, 1))
    for j in range(6*n):
        for i in range(n):
            A[i,j]=A1[i,j]
            A[i+n,j]=A2[i,j]
            A[i+2*n,j]=A3[i,j]

    for i in range(n):
        b[i]=b1[i]
        b[i+n]=b2[i]
        b[i+2*n]=b3[i]

    lb=np.zeros((6*n,1))
    ub=[]

    #[x,fval]=linprog(f,A,b,Aeq,beq,lb,ub)
    res = linprog(f, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, bounds=(0,None),options={"disp": True})

    X = res.x
    # блок вывода

    print("f",f)
    print('A=',A)
    print('b=',b);
    print('Aeq=',Aeq)
    print('beq=', beq)

    #J=fval
    #for i in range(1,n):
       # wL = x[i]
    # i in range (n+1,2*n):
       # wU= x[i]

    wL = np.zeros(n)
    wU = np.zeros(n)
    for i in range(n):
        wL[i] = X[i]
        wU[i] = X[i + n]

    print("X = ")
    print(res.x)
    print("J* = ")
    print(res.fun)
    print("wL = ", end=" ")
    print(wL)
    print("wU = ", end=" ")
    print(wU)

    return {"J*": res.fun, "wL": wL, "wU": wU}
