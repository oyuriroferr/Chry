import psutil
import time
import threading

def kill_task_manager():
    while True:
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.info['name'].lower() == "taskmgr.exe":
                psutil.Process(process.info['pid']).terminate()
        time.sleep(1)  # Verifica a cada segundo
# Cria e inicia as threads

thread1 = threading.Thread(target=kill_task_manager)

thread1.start()

# Aguarda as threads terminarem (o que não vai acontecer, pois elas estão em loops infinitos)

thread1.join()
