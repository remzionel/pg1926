class School:
    def __init__(self, name, stype, lessons, year, classRooms, teachers, total):
        self.name       = name
        self.stype      = stype
        self.lessons    = lessons
        self.year       = year
        self.classRooms = classRooms
        self.teachers   = teachers
        self.total      = total
 

Schools = [
    School("Atatürk", "İlkokul", "Resmi Müfredat", 1980, 24, 36, 485),
    School("Akdeniz", "OrtaOkul", "Resmi Müfredat", 1960, 20, 21, 360),
    School("Cumhuriyet", "Lise", "Resmi-Seçmeli Müfredat", 1945, 29, 42, 750),
    School("Anadolu", "Üniversite","Resmi-Seçmeli Müfredat, Serbest Etkinlikler, Sosyal Etkinlikler, Konferanslar", 1958, 200, 100, 1000)
]

for school in Schools:
    print(
        'Okul Adı: ' + school.name,
        'Okul Türü: ' + school.stype,
        'Dersler: ' + school.lessons,
        'Açılış Yılı: ' + str(school.year),
        'Sınıf/derslik Sayısı: ' + str(school.classRooms),
        'Öğretmen Sayısı: ' + str(school.teachers),
        'Toplam Mevcut: ' + str(school.total)
    )