liste = []
tek_liste = []
liste_sayi = int(input('Kaç Sayı Girilecek: '))

for sor in range(liste_sayi):
    girilen_sayi = int(input('Sayıyı Gir: '))
    liste.append(girilen_sayi)

for sayi in liste:
    if(sayi%2==1):
        tek_liste.append(sayi)

tek_liste.sort()
print(tek_liste[len(tek_liste)-1])