import numpy as np
import matplotlib.pyplot as plt

# Se asume un valor de 10 para las constantes
c = 10

def entropias(a):
    return c * (3*10**(-2)) * (a**(1/3) + (2/3)*(80-a)**(1/3) )   

def proporcion(a):
    return a/80

valores = np.linspace(0, 80, 100)

eje_y = entropias(valores)
eje_x = proporcion(valores)

# Se crea la figura
fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel(r'$U_A / 80$',fontsize=10)
ax.set_ylabel('$S$',fontsize=10)       
plt.plot(eje_x, eje_y, c='purple')
plt.savefig('termodinamica.png', dpi=300, bbox_inches='tight')
plt.show()