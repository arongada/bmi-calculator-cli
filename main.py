suly = float(input("Suly: "))
magassag = float(input("Magassag: "))
bmi = suly / (magassag/100)**2
if bmi <= 16:
    print("súlyos soványság")
elif bmi <= 16.99:
    print("mérsékelt soványság")
elif bmi <= 18.49:
    print("	enyhe soványság")
elif bmi <= 24.99:
    print("normális testsúly")
elif bmi <= 29.99:
    print("túlsúlyos")
elif bmi <= 34.99:
    print("I. fokú elhízás")
elif bmi <= 39.99:
    print("II. fokú elhízás")
elif bmi >= 40:
    print("III. fokú (súlyos) elhízás")
