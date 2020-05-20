import threading
import time
import subprocess

active_threads = []
output_file = open("output.txt", "w+")


def worker(thread_number, total_tasks, total_threads, ip_list):
    i = 0
    task_number = -1
    while task_number < total_tasks:

        if task_number != -1:

            ip = str(ip_list[task_number]).replace("\n", "")

            bash_command = "curl -s --max-time 7.0 --socks5 " + ip + " https://www.google.com"

            #print(bash_command +"\n")

            bash_response = str(subprocess.Popen(bash_command, shell=True, stdout=subprocess.PIPE).stdout.read())

            if (str(bash_response) != "b''"):
                output_file.write(ip + "\n")

        task_number = i * total_threads + thread_number

        i = i + 1


def start_thread(thread_number, total_tasks, total_threads, ip_list):
    print("thread launched " + str(thread_number)+"\n")
    active_threads.append(threading.Thread(target=worker, args=(thread_number, total_tasks, total_threads, ip_list)))
    active_threads[thread_number].start()
