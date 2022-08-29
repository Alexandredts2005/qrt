import threading
 
def hello(n):
    for i in range(5):
        print("je suis le thread", n, "et ma valeur est", i)
    print("--- Fin du thread ", n)

for n in range(5):
    th = threading.Thread(target=hello, args=[n])
    th.start()
