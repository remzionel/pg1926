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
    School("Atatürk", "İlk Okul", "Resmi Müfredat, Okul Gezileri", 1980, 24, 36, 485),
    School("Akdeniz", "Orta Okul", "Resmi Müfredat, Okul Gezileri", 1960, 20, 21, 360),
    School("Cumhuriyet", "Lise", "Resmi Müfredat, Sosyal Etkinlikler, Sportif Etkinlikler", 1945, 29, 42, 750),
    School("Anadolu", "Üniversite","Resmi & Seçmeli Müfredat, Sosyal Etkinlikler, Konferanslar", 1958, 275, 321, 19250)
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
