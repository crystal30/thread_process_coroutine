import os
#fork只能用于linux/unix中
# pid = os.fork()
# print("bobby")
# if pid == 0:
#   print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
# else:
#   print('我是父进程：{}.'.format(pid))


import multiprocessing
import time
def get_html(n):
    time.sleep(n)
    print("sub_progress {} success".format(n))
    return n

if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # print(progress.pid)
    # progress.start()
    # print(progress.pid)
    # progress.join()
    # print("main progress end")

    #使用进程池 功能同concurrent.futures.ProcessPoolExecutor
    #multiprocessing是更底层的实现
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result1 = pool.apply_async(get_html, args=(3,))
    # result2 = pool.apply_async(get_html, args=(2,))
    #
    # #等待所有任务完成（前提是关掉pool，不让新的任务进来）
    # pool.close()
    # pool.join()
    #
    # print(result1.get())
    # print(result2.get())

    #imap 类似于线程池 concurrent.futures.ThreadPoolExecutor.map 方法
    # for result in pool.imap(get_html, [1,5,3]):
    #     print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [1,5,3]):
        print("{} sleep success".format(result))




