from random import randint
rondes = 3
score = 20
while True:
    te_raden = randint(1,5)
    gok = int(input('Kies een getal van 1 t/m 5: '))
    rondes -= 1
    if (te_raden == gok):
        print("Je hebt het getal goed geraden!")
        score += 1
    else:
        print("Je hebt het getal niet goed geraden!")
        score -= 1
    if rondes == -0:
        print(f"Score: {score}")
        print("Game over!")
        exit()