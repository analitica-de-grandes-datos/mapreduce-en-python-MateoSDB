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
       credit=line [0:-1].split(',')
       
       
       sys.stdout.write("{}\t{}\n".format(credit[3],credit[4]))
