count = 0
nummer = 625
while True:
    nummer -= 25
    count += 1
    print(nummer, count, "keer")
    if nummer <= 0:
        exit()