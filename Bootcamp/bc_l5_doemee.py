
# we gaan hier een loop voor maken
for i in range(10):
    nummer = i + 1
    resultaat = nummer * 7

    print(f"{nummer} x 7 = {resultaat}")

    print(resultaat)
# We maken een programma die herhaaldelijk (met een input()) ‘?’ zegt 
# totdat het resultaat daarvan gelijk is aan ‘quit’.
# Daarna printen we het aantal iteraties (Het aantal keren dat de vraag is gesteld).
running = True

while(running):
    confirm = input("Stop the program? (YES/NO): ")
    
    if confirm == "YES":
        running = False
