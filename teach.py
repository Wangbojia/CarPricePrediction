import threading,time

def run(num):
    # function code: here we print sth
    print('subthread (%s) beginning'%(threading.current_thread().name))
    # sleep for 2s
    time.sleep(2)

    print('num is:',num)

    time.sleep(2)

    print('subthread (%s) ends'%(threading.current_thread().name))

# program entry:
'''
two ways to use a .py file
1. used as script
2. imported as module
'''


def r(n):
    global num
    for i in range(1000000):
        # modify data
        with lock:
            num = num + n
            num = num - n
if __name__=='__main__':
    # # case 1

    # print('main thread beginning',threading.current_thread().name)
    # # target: which func to call
    # t = threading.Thread(target=run,name = 'runThread',args=(1,))
    # # run t
    # t.start()
    # # wait for t ends, if removed print main will happen because t sleeps for 2s
    # t.join()
    # print('main thread ends',threading.current_thread().name)

    # case 2 threads modify data at same time. consistency?
    num = 0
    lock = threading.Lock()
    t1 = threading.Thread(target=r,args=(6,))
    t2 = threading.Thread(target=r,args=(9,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('num=',num)
