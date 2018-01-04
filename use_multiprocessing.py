from multiprocessing import Process
import os


def run_proc(name):
    print('Run child process {0} ({1})'.format(name,os.getpid()))

if __name__ == '__main__':
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    print('running')
    p.join()
    print('child done')
    
