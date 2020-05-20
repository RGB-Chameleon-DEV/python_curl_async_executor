import threading
import subprocess


class async_bash_execute:

    def __init__(self, ip_list, total_threads=int):
        self.ips = ip_list
        self.total_tasks = len(self.ips)
        self.total_threads = total_threads
        self.output_file = open("output.txt", "w+")
        self.active_threads = []
        self.solved_tasks = 0
        print(str(self.total_tasks) + " tasks ")

    def start_threads(self):

        i = 0
        while i < self.total_threads:
            self.active_threads.append(threading.Thread(target=self.thread, args=(i)))
            self.active_threads[i].start()

            i = i + 1

        print("all threads online")

    def thread(self, thread_number):

        print("thread " + str(thread_number) + " online \n")
        i = 0
        task_number = -1
        while task_number < self.total_tasks:

            if task_number != -1:

                ip = str(self.ips[task_number]).replace("\n", "")

                bash_command = "curl -s --max-time 7.0 --socks5 " + ip + " https://www.google.com"

                bash_response = str(subprocess.Popen(bash_command, shell=True, stdout=subprocess.PIPE).stdout.read())

                if str(bash_response) != "b''":
                    self.output_file.write(ip + "\n")

            task_number = i * self.total_threads + thread_number
            i = i + 1
            self.solved_tasks = self.solved_tasks + 1
            print("progress = " + str(self.solved_tasks) + "/" + str(self.total_tasks))

        print("thread " + str(thread_number) + " offline")
