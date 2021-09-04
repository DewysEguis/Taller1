#Primers Commit

#Ejercicio 1
def y1():
    y = ( ( 5 + 2 - 5)**2 * 5 + 8 / 2 - 30) / 2 * 5 - 3
    return y

def y2():
    z = 5
    n = 3
    m = z - n
    y = (((z + 2 - n)**2 * m + 8 / 2 - 30) / 2 * 5 - 3 )**5 + 15 * 3 - 9 / 3
    return y

def y3():
    z = 5
    n = ((8+2-4)**2 * 5 + 8 + 7 / 2 - 30* 5 ) / 2 * 5 - 3;
    m = z**2 * 3 + n;
    y = ((((z+2-n)**2 * m+8/2 - 30) / 2 * 5 - 3)**5 + 15 * 3 - 9 / 3)**2 - 5 / 4
    return y

# Ejercicios 2

def p1a(p, v, t):
    return (p * v) / (0.37 * (t + 460))

def p2b(ed):
    return (200 - ed) / 10

def p2c(in1, in2, in3):
    total = in1 + in2 + in3
    ptaje1 = in1 * 100 / total
    ptaje2 = in2 * 100 / total
    ptaje3 = in3 * 100 / total
    return ptaje1, ptaje2, ptaje3

def p2c(sal):
    return sal + (sal * 0.015)

def p2d(sueldo):
    ley = sueldo * 0.01
    seguro_social = sueldo * 0.04
    seguro_forsozo = sueldo * 0.005
    caja = sueldo * 0.05
    sueldo_final = sueldo - ley - seguro_social - seguro_forsozo - caja
    return ley, seguro_social, seguro_forsozo, caja, sueldo_final

def p2e(n_pa, tam, col):
    return (n_pa * 20000) + (tam * 15000) + (col * 25000)

def p2f(ti):
    return 100000 + (120000 * (ti - 1))

def p2g(ti_h):
    des = (ti_h * 20000) * 0.05
    pago = ti_h * 20000 - des
    return pago, des