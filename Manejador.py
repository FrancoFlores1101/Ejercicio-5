import csv
from clase import PlanAhorro


class manejplan:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def leer(self):
        archivo=open('planes.csv')
        reader=csv.reader(archivo,delimiter=';')
        for row in reader:
            p=PlanAhorro(row[0],row[1],row[2],row[3],row[4],row[5])
            self.__lista.append(p)
    def Actualizar(self):
        print('#### ACTUALIZACION DE IMPORTES ####')
        for PlanAhorro in self.__lista:
            print('-------------------------------')
            print(PlanAhorro.getcodgio(),PlanAhorro.getmodelo(),PlanAhorro.getversion())
            print('Ingrese nuevo valor')
            n=float(input())
            PlanAhorro.actualizar(n)
        print('--------------')
    def Mostrar(self,k):
        print('#### AUTOMOVILES CON CUOTA MENOR  A ',k,'####')
        for PlanAhorro in self.__lista:
            if PlanAhorro.calcularCuota() < k:
                print('---------')
                print(PlanAhorro.getcodgio(),PlanAhorro.getmodelo(),PlanAhorro.getversion())
        print('--------------')
    def MostrarMonto(self):
        print('##### MONTO A LICITAR CADA VEHICULO ####')
        for PlanAhorro in self.__lista:
             print(PlanAhorro.getcodgio(),PlanAhorro.getmodelo(),PlanAhorro.getversion())
             print(PlanAhorro.calcularCuota()*PlanAhorro.getlicitar())
    def modificar(self):
        print('ingrese nueva cantidad de cuotas para licitar')
        k=int(input())
        for PlanAhorro in self.__lista:
            PlanAhorro.modificarlicitar(k)
