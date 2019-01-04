class Equipo(object):

    def __init__(self, n, c, ca, num):
        self.nombres=n
        self.ciudad=c
        self.campeonatos=ca
        self.numJugadores=num

    def setNombres(self, n):
        self.nombres=n

    def getNombres(self):
        return self.nombres

    def setCiudad(self,c):
        self.ciudad=c

    def getCiudad(self):
        return self.ciudad

    def setCampeonatos(self, c):
        self.campeonatos=c

    def getCampeonatos(self):
        return  self.campeonatos

    def setNumJugadores(self, n):
        self.numJugadores=n

    def gerNimJugadores(self):
        return self.numJugadores

    def __str__(self):
        return "%s %s %s %s"%(self.nombres,self.ciudad,self.campeonatos,self.numJugadores)



class Operaciones(object):

    def __init__(self, listado):
        self.lista = listado

    def ordenarnombre(self):

        return sorted(self.lista, key=lambda equipo: equipo.nombres)

    def ordenarCamperonatos(self):

        return sorted(self.lista, key=lambda equipo: equipo.campeonatos)
