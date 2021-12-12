import threading

COMPTEUR = 0

def increment():
    global COMPTEUR
    for val in range(100000):
        COMPTEUR = COMPTEUR + 1
        
mes_threads = []

for n in range(4):
    th = threading.Thread(target=increment, args=[])
    th.start()
    mes_threads.append(th)
    
for thread in mes_threads:
    thread.join()

print(" valeur finale : ", COMPTEUR)
