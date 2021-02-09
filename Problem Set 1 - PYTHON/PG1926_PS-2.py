import re
def epostaKontrol(eposta): 
    eposta_sablon = r"^([A-Za-z0-9_\-]+)@([a-zA-Z0-9]+)(([.]{1})([a-zA-Z]{2,3})|([.]{1})([a-zA-Z]{2,3})([.]{1})([a-zA-Z]{2}))$"
    kontrol = re.search(eposta_sablon, eposta)
    return kontrol

girilenAdres = input('E-Posta Adresi Giriniz: ')

if(epostaKontrol(girilenAdres)):
    print('E-Posta Adresi Kriterlere Uygundur.')
else:
    print('E-Posta Adresi Kriterlere Uygun Değildir.')