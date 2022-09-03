import matplotlib.pyplot as plt
import numpy as np

def main():
    
    plt.style.use(['science','no-latex'])
    
    A = 1
    
    entropias = lambda ua : A * 3e-2 * (ua**(1/3) + (2/3)*(80-ua)**(1/3) )    
    relacion_ua = lambda ua : ua/80
    
    muestra = np.linspace(0, 80, 100)
    
    lista_x = relacion_ua(muestra)
    lista_y = entropias(muestra)
       
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlabel(r'$U_A / (U_A + U_B) $',fontsize=10)
    ax.set_ylabel('$Entropía \,\,total$',fontsize=10)
    plt.plot(lista_x, lista_y)
    
    plt.savefig('tarea2.png', dpi=300, bbox_inches='tight')
    plt.show()
 
if __name__ == "__main__":
    main()
    