#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/ python3
import sys 
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
    for line in sys.stdin:
       data=line.split(',')[0]
       num=int(line.split(",")[1])
       
       sys.stdout.write("{},{},{}\n".format(num,data,num))
