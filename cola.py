from collections import deque 

cola = deque (["ana", "carlos"])

cola.append("Jorge")
cola.append("Luis")

print("Cola actual:", cola)

atendido = cola.popleft()
print("Se atendio a: " + atendido)

print("Cola restante", cola)