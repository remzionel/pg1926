liste_i = input('Lütfen aralarında 0 (sıfır) da bulunan en az 3 tane sayıyı aralarında boşluk bırakarak yazınız. ');
liste = list(map(int, liste_i.split()))
liste_yeni = []

liste_yeni = [sayi for sayi in liste if sayi == 0]
liste_yeni += [sayi for sayi in liste if sayi != 0]

print(liste)
print(liste_yeni)