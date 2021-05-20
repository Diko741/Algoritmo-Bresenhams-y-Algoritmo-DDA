
import matplotlib.pyplot as plt
def DDA(x1, y1, x2, y2, color):
    #Calcular el valor de dx y dy
    dx = abs(x2 - x1) 
    dy = abs(y2 - y1)
    steps = 0
    # Evaluación de la pendiente 
    if dx > dy :
        steps = (dx)
    else:
        steps = (dy)
    # Debe haber uno igual a 1 y uno menor a 1
    xInc = float(dx / steps)
    yInc = float(dy / steps)
    # Redondee para asegurarse de que el incremento de x e y 
    # sea menor o igual a 1, de modo que la línea recta generada sea lo más uniforme posible
    xInc = round(xInc,1)
    yInc = round(yInc,1)
    for i in range(0, int(steps + 1)):
        plt.title("***ALGORITMO DDA***")
		 # Dibijar los pixeles
        plt.plot(round(x1), round(y1), color)
        x1 += xInc
        y1 += yInc
        print(x1)
        print(y1)
    plt.show()
    #Imprime los valores para cada variable 
    print("\033[1;33m"+"LOS VALORES OPTENIDOS SON"+'\033[0;m') 
    print("\033[4;35m"+"dx="+'\033[0;m',dx)
    print("\033[4;35m"+"dy="+'\033[0;m',dy)
    print("\033[4;35m"+"steps="+'\033[0;m',steps)
    print("\033[4;35m"+"XInc="+'\033[0;m',xInc)
    print("\033[4;35m"+"YInc="+'\033[0;m',yInc)

def main():
    #solicitar los valores que son asignados a las variables de inicalización 
    print("\033[1;33m"+"INGRESE LAS COORDENADAS"+'\033[0;m') 
    x1=int(input("\033[4;35m"+"X1="+'\033[0;m'))
    y1 = int(input("\033[4;35m"+"Y1="+'\033[0;m'))
    x2 = int(input("\033[;36m"+"X2="+'\033[0;m'))
    y2 = int(input("\033[;36m"+"Y2="+'\033[0;m'))
    color = "m*"
    #Establesel los valores de los parametros para la la funcion DDA
    DDA(x1, y1, x2, y2, color)

#funcion de arranque 
if __name__ == '__main__':
    main()
