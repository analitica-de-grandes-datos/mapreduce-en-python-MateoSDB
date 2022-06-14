#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
if __name__ == '__main__':
    
 list=[]  
 for line in sys.stdin:
    key1, date, value = line.split("\t") 
    valor=int(value) 
    list.append([key1, date, valor]) 

 list = sorted(list, key=lambda x: (x[2]))  
 list= list[0:6] 
 for line in list: 
    sys.stdout.write("{}   {}   {}\n".format(line[0], line[1], line[2]))