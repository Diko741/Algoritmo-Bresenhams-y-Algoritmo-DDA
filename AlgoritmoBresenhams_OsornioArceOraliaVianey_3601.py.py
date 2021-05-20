import matplotlib.pyplot as plt
def Bresenham(x1, y1, x2, y2, color):
    x = x1
    y = y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = (2 * dy) - dx
    for i in range(x1 , x2):
        plt.title("***ALGORITMO BRESENHAMS***")
        plt.plot(round(x), round(y), color)
        x=x+1
        if p<0:
            p = p + (2 * dy)
        else:
            p = p + (2 * dy ) - (2 * dx)
            y=y+1
        print(x)
        print(y)
        print("\033[4;35m"+"p="+'\033[0;m', p)
    plt.show()

    print("\033[1;33m"+"LOS VALORES OPTENIDOS SON"+'\033[0;m') 
    print("\033[4;35m"+"dx="+'\033[0;m',dx)
    print("\033[4;35m"+"dy="+'\033[0;m',dy)
    print("\033[4;35m"+"p="+'\033[0;m',p)
   
def main():
    
    print("\033[1;33m"+"INGRESE LAS COORDENADAS"+'\033[0;m') 
    x1=int(input("\033[4;35m"+"X1="+'\033[0;m'))
    y1 = int(input("\033[4;35m"+"Y1="+'\033[0;m'))
    x2 = int(input("\033[;36m"+"X2="+'\033[0;m'))
    y2 = int(input("\033[;36m"+"Y2="+'\033[0;m'))
    color = "m."
    Bresenham(x1, y1, x2, y2, color)

if __name__ == '__main__':
    main()