import socks_checker

input_file = open("ips.txt", "r")
ips = input_lines = input_file.readlines()

total_threads = 1000
total_tasks = len(ips)

print("total_tasks : " + str(total_tasks)+"\n")

i = 0
while i < total_threads:

    socks_checker.start_thread(i, total_tasks, total_threads, ips)

    i = i+1
