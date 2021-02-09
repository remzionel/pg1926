yazdir = ''
for sayi in range(0, 101):
    if(int(sayi)%3==0 and int(sayi)%5==0):
        yazdir += 'FizzBuzz'
    elif(int(sayi)%3==0):
        yazdir += 'Fizz'
    elif(int(sayi)%5==0):
        yazdir += 'Buzz'
    else:
        yazdir += str(sayi)
    yazdir += '\n'
    sayi += 1
print(yazdir)