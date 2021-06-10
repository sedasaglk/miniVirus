import random

for i in range(5):
    acilacakDosya = open("sil"+str(i)+".txt","w")
    for a in range(50):
        acilacakDosya.write(str(random.randint(123245648,54545153444)))
