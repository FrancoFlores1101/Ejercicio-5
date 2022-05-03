class PlanAhorro:
    __codigo:0
    __modelo=''
    __version=''
    __valor=float
    __cantidadcuotas=int
    __cantidadlicitar=0
    def __init__(self,cod,modelo,version,valor,cantidadcuotas=30,cantidadlicitar=15):
        self.__codigo=cod
        self.__modelo=modelo
        self.__version=version
        self.__valor=float(valor)
        self.__cantidadcuotas=int(cantidadcuotas)
        self.__cantidadlicitar=int(cantidadlicitar)
    def calcularCuota(self):
        c = float((self.__valor/self.__cantidadcuotas)+ self.__valor*0.10)
        return c
    def actualizar(self,n):
        self.__valor=n
    def getcodgio(self):
        return self.__codigo
    def getmodelo(self):
        return self.__modelo
    def getversion(self):
        return self.__version
    def getlicitar(self):
        return self.__cantidadlicitar
    def modificarlicitar(self,l):
         self.__cantidadlicitar = l
