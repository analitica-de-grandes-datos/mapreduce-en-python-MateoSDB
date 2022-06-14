#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    curkey = None
    suma = 0
    conteo1 = 0

    for line in sys.stdin:

        key, value, conteo = line.split("\t") 
        value = float(value)
        conteo = float(conteo) 
        if key == curkey:

            suma += value
            conteo1 += conteo
        else:

            if curkey is not None:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, float(suma/conteo1)))  

            curkey = key
            suma = value 
            conteo1 = conteo 
            promedio= float(float(value)/float(conteo1)) 
            
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, float(suma/conteo1)))