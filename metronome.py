#lang Python
import time
import winsound

bpm = int(input('Enter your BPM: '))
claptime = int(input('Enter how long you want to practice in seconds: '))

def main(bpm, claptime, bpb = 4):
    sleep = 60.0 / bpm
    counter = 0
    timestart = time.perf_counter()
    while True:
        counter += 1
        if counter % bpb:
            winsound.PlaySound('clap.wav',winsound.SND_ASYNC)
            print('Clap')
        else:
            winsound.PlaySound('clap.wav',winsound.SND_ASYNC)
            print('Clap')
        if time.perf_counter() - timestart >= claptime:
            print('DONE!')
            break
        time.sleep(sleep)
 
 
 
main(bpm,claptime)