from sympy import *


def newton_raphson(fn, dfn, point, dx=0.000001, dy=-1, maxiter=10):
    """
    Función, Derivada, Punto inicial, 
    Precisión(por defec = 0.000001), Iteraciones(por defec = 10)
    """
    x = Symbol('x')
    for i in range(maxiter):
        fx = fn.subs(x, point)
        dfx = dfn.subs(x, point)

        # NR Formula: x - f(x) / f'(x)
        xnew = round((point - fx / dfx), 4)

        if dy == -1:
            if abs(xnew - point) < dx:
                break
        elif abs(xnew - point) < dx and abs(fn.subs(x, xnew)-fx) < dy:
            break

        print('Iteracion Nro.:', i) # Para ver si la operación esta tardando demasiado

        point = xnew

    return xnew


def main():
    x = Symbol('x')

    # Ingreso de datos
    # -----------------------------------------------------------------

    # Ingresar la función a aproximar.
    fn = (1/4 * (x**2)) - 7 - (3 * sin(x))
    # Punto inicial de aproximacion
    point = 4

    # Precisión
    dx = 10**(-2)

    # -----------------------------------------------------------------
    
    dfn = fn.diff(x)  # Derivada de la función.
    result = round(newton_raphson(fn, dfn, point, dx), 4) # se redondea a 4 decimales

    print(f'Root: {result}')

    while 1:
        input('Inserte cualquier tecla para cerrar >> ')
        break


if __name__ == '__main__':
    main()
