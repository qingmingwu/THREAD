import threading


def thread_job():
    print("This is an added Thread, number is %s" % threading.current_thread())


def main():
    added_thread = threading.Thread(target=thread_job)
    # # 查看进程中还有几个线程在运行
    # print(threading.active_count())
    # # 返回一个包含正在运行的线程的list
    # print(threading.enumerate())
    # # 当前执行的线程
    # print(threading.current_thread())

    added_thread.start()


if __name__ == "__main__":
    main()
