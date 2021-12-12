import threading

verrou1 = threading.Lock()
verrou2 = threading.Lock()

def fonction1():
    verrou1.acquire()
    print("section critique 1.1")
    verrou2.acquire()
    print("section critique 1.2")
    verrou2.release()
    verrou1.release()

def fonction2():
    verrou2.acquire()
    print("section critique 2.1")
    verrou1.acquire()
    print("section critique 2.2")
    verrou1.release()
    verrou2.release()

th1 = threading.Thread(target=fonction1, args=[])
th2 = threading.Thread(target=fonction2, args=[])

th1.start()
th2.start()