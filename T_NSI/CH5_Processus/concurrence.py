import threading

COMPTEUR = 0

verrou = threading.Lock()

def increment():
    verrou.acquire()
    global COMPTEUR
    for val in range(100000):
        COMPTEUR = COMPTEUR + 1
    verrou.release()
mes_threads = []

for n in range(4):
    th = threading.Thread(target=increment, args=[])
    th.start()
    mes_threads.append(th)
    
for thread in mes_threads:
    thread.join()

print(" valeur finale : ", COMPTEUR)
