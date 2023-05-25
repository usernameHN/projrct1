hours = 0
minutes = 0
seconds = 0
while 1 == 1:
    hours = int(input("enter a hours :"))
    minutes = int(input("enter a min :"))
    seconds = int(input(" enter a seconds :"))
    hours = hours * 3600
    minutes = minutes * 60
    print(hours, minutes, seconds)
    if hours == "exit" or minutes == "exit" or seconds == "exit":
        break
