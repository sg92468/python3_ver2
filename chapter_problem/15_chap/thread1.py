import threading

def do_this(what):
    whoami(what)

def whoami(what):
    print(f"Thread {threading.current_thread()} says: {what}")

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this, args=(f"{n}"))
        p.start()

