import numpy as np

def gradiente_descendiente_variada(x_k, epsilon = (10**(-12))):
    contador = 1
    steps = [x_k]
    delta = 1
    k = 1
    alpha = 0.5
    while delta > epsilon:
        if contador == 2:
            x_k1 = x_k - 1/k*(np.array([2*x_k[0]+np.sin(np.pi*x_k[1]), np.pi*x_k[0]*np.cos(np.pi*x_k[1])+2*x_k[1]])) + alpha*(x_k - steps[-1])
            delta = np.linalg.norm(x_k1 - x_k)
            k += 1
            steps.append(x_k)
        else:
            x_k1 = x_k - 1/k*(np.array([2*x_k[0]+np.sin(np.pi*x_k[1]), np.pi*x_k[0]*np.cos(np.pi*x_k[1])+2*x_k[1]]))
            delta = np.linalg.norm(x_k1 - x_k)
            k += 1
            contador += 1
            steps.append(x_k1)
    return k, x_k, steps

x_0 = np.array([1/2, -3/4])
pasos, x_k1, fxparcial = gradiente_descendiente_variada(x_0)
print("El número de pasos es: ", pasos)
print("El valor de x_k1 es: ", x_k1)
print("La gradiente es: ", np.array(fxparcial))