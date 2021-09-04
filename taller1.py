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

def p1(p, v, t):
    return (p * v) / (0.37 * (t + 460))