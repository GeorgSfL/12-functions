def count_steps():
    distance = float(input("Bitte geben Sie die zurückgelegte Entfernung in cm ein: "))
    steplength = float(input("Bitte geben Sie Ihre Schrittlänge in cm ein: "))
    return distance/steplength

steps = count_steps()
print(steps)