class Computador:

    def __init__(self, ip):
        self.__ip = ip

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, novo_ip):
        self.__ip = novo_ip

    def __str__(self):
        return f'IP: {self.ip}'
