# with open('./1.txt','a') as f:
# 	# print(f.readline()) 读取文本文件
# 	f.write('append text')

# stringIO 的读写

# from io import StringIO
# f=StringIO('./fact.py');
# # f.write('你好')
# print(f.readlines())


# BytesIO的读写

# from io import BytesIO
# f=BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())

# 进程
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    # p.join()
    print('Child process end.')