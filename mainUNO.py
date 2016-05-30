import os
from datetime import datetime
ahora = datetime.now()
#file = '06 Abril.txt'
#destino = 'PONchador'+str(ahora.month)+str(ahora.day)+str(ahora.hour)+str(ahora.minute)+'.txt'

# Este es el archivo final, se abre y cierra en cada funcion
destino = 'PONCH.txt'

def ponchaUNO(filename):
    d = open(destino, 'a')
    with open('./'+str(filename), 'r') as f:
        for line in f.readlines():

            if line[0].isdigit():
                linea = line.split()
                empleado = linea[0]
                print(empleado)

                fecha = linea[1].replace('/','')
                print(fecha)

                # Obtenemos el valor de la hora y lo convertimos a entero para poder evaluarlo
                hora = int(linea[2].replace(':',''))
                print('hora: ',hora)

                # con este if se normaliza la hora, si la hora es  entre las 1525 y 1540 se asumo las 1535
                if hora >= 1525 and hora <= 1540:
                    hora = str(1535)
					
				# este normaliza la hora de las 6am
                elif hora >= 540 and hora <= 605:
                    hora = str(600)

                # Aqui agregamos un 0 a la hora en caso de que sea de 4 digitos (ejemplo 5:40 a 0540)
                if len(str(hora)) == 3:
                    hora = '0'+str(hora)
                hora = str(hora)

                salida = (empleado+fecha+hora+'100\n')
                
                print(salida)
                d.write(salida)

    d.close()
    os.rename(filename, 'proccesed/'+filename)


def ponchaDOS(filename):
    d = open(destino, 'a')

    with open(filename, 'r') as f:

        for line in f.readlines():
            print(line)
            input()
            if line.startswith('Acrylic\t00'):
                datos = line.split('\t')
                noempleado = datos[1]

                fecha = datos[6].split()
                fecha1 = fecha[0].split('/')

                # Formateando el dia
                if len(fecha1[0]) != 2:
                    dia = '0'+fecha1[0]
                else:
                    dia = fecha1[0]

                # Formateando el mes
                if len(fecha1[1]) != 2:
                    mes = '0'+fecha1[1]
                else:
                    mes = fecha1[1]
                
                # Formateando la hora
                fecha2 = fecha[1].split(':')
                if len(fecha2[0]) != 2:
                    hora = '0'+ fecha2[0]
                else:
                    hora = fecha2[0]

                #Formateando los minutos
                if len(fecha2[1]) != 2:
                    mins = '0'+fecha2[1]
                else:
                    mins = fecha2[1]

                hora = hora + mins

                # La normalizamos a las 06:00 y las 15:35 
                print(hora)
                print(int(hora))
                if int(hora) >= 545 and int(hora) <= 605:
                    hora = "0600"
                if int(hora) >= 1525 and int(hora) <= 1540:
                    hora = '1535'



                print(noempleado+ dia+ mes+ hora + '100')
                input()
                d.write(noempleado+ dia+ mes+ hora + '100\n')
   
    d.close()
    os.rename(filename, 'proccesed/'+filename)

if __name__ == '__main__':

    # Hace un listado de los archivos .txt en el directorio actual
    files = [f for f in os.listdir('.') if f.endswith('txt')]

    # Este for es para procesar cada archivo
    for filename in files:
        
        # Aqui se lee la primer linea de el archivo y se determina a que ponchador corresponde y lo envia a su respectiva funcion
        with open(filename,'r') as archivo:
            linea1 = archivo.readline()
            if linea1.startswith('Ac'):
                print ('ponchador 1: ' + filename)
                archivo.close()
                ponchaUNO(filename)

            elif linea1.startswith('Dep'):
                print ('ponchador 2: ' + filename)
                archivo.close()
                ponchaDOS(filename)

