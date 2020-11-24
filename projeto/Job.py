class Job:

    def __init__(self, computador, recurso):
        self.__computador = computador
        self.__recurso = recurso

    @property
    def computador(self):
        return self.__computador

    @property
    def recurso(self):
        return self.__recurso

    def __str__(self):
        return f'|{self.computador} -> recurso: {self.recurso}|'
