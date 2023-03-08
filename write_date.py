from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%Y/%m/%d, %H:%M:%S")
file = open("ultima_execucao.txt", "w")
a = file.write(date_time)
file.close()
print(date_time)