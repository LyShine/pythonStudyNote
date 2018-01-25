# from multiprocessing import Pool
# # 得到进程池
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     # 我不懂这里为什么得到的是这个进程的pid
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     # 创建四个进程等待被调用
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#         # 调用五次，因为只有四个进程，最后一个进来的要等待其他任务执行完才能被执行
#         # 注意这里是非阻塞的
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()