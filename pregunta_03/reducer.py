#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
#! /usr/bin python3

import sys

#
# Esta funcion reduce los elementos que tienen la misma clave
#
#! /usr/bin/ python3
if __name__ == '__main__':

  for line in sys.stdin:
        numero, llave, valor = line.split(",")
        valor=int(valor)

        sys.stdout.write(llave + "," + str(valor) + "\n")
