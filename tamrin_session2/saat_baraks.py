while 1 == 1:
    seconds = int(input("enter a taime of seconds: "))
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    print(f"{hours : }:{minutes :}:{seconds :}")

    if seconds == "exit":
        break
