import multiprocessing
from pyomyo import Myo, emg_mode
import csv
import time

file_path = 'fingers_open.csv' #use your own absolute path \\gesture-name.csv
file = open(file_path, 'w', newline='')
writer = csv.writer(file)

#Myo Setup
q = multiprocessing.Queue()

def worker(q):
    m = Myo(mode=emg_mode.RAW)
    m.connect()
    
    def add_to_queue(emg, movement):
        q.put(emg)

    m.add_emg_handler(add_to_queue)

    m.vibrate(1)

    while True:
        m.run()


if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, args=(q,))
    p.start()
    emg_list = []
    print("Main Process Started")
    start_time = time.time()
    while True:
        while not(q.empty()):
            emg = list(q.get())
            emg_list.append(emg)

        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= 20:
            break
            
    p.terminate()
    print("Saving and closing")
    writer.writerows(emg_list)
    file.close()
    quit()
