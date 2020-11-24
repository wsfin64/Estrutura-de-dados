class Computador:

    def __init__(self, ip, hostname, prioridade=False):
        self.__ip = ip
        self.__hostname = hostname
        self.__prioridade = prioridade

    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, novo_ip):
        self.__ip = novo_ip

    @property
    def hostname(self):
        return self.__hostname

    @hostname.setter
    def hostname(self, novo_hostname):
        self.__hostname = novo_hostname

    @property
    def prioridade(self):
        return self.__prioridade

    def ativar_prioridade(self):
        self.__prioridade = True

    def desativar_prioridade(self):
        self.__prioridade = False

    def __str__(self):
        return f'IP: {self.ip} HOSTNAME: {self.hostname} PRIORIDADE: {self.prioridade}'
