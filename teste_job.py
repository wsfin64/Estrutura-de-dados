from Computador import Computador
from FilaEncadeada import FilaEncadeada, FilaException
from Recurso import Recurso
from Job import Job

pc = Computador('192.168.0.10')
pc2 = Computador('192.168.0.12')
pc3 = Computador('192.168.0.22')

arquivo = Recurso(800, 'video.mp4')
arquivo2 = Recurso(2, 'foto.jpg')
arquivo3 = Recurso(2048, 'linux.rar')

job = Job(pc, arquivo)
job2 = Job(pc2, arquivo2)
job3 = Job(pc3, arquivo3)

fila = FilaEncadeada()
fila.enfileirar(job)
fila.enfileirar(job2)
fila.enfileirar((job3))

print(fila)

print(fila.mostrar_cabeca())

fila.desenfileirar()
print(fila)
print(fila.mostrar_cabeca())