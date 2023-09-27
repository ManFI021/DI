def suma (a,b):
    return a+b
def resta (a,b):
    return max(a,b)-min(a,b)
def multiplicacion(a,b):    
    return a*b
def division(divisor,dividendo):
    if divisor== 0 or dividendo==0:
        return 'División valor 0'
    else:
        return divisor/dividendo