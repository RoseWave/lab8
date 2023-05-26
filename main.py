from PIL import Image, ImageDraw, ImageFont


def proc1():
    a = Image.open('1.jpg')
    a.show()
    b = a.crop((150, 350, 450, 650))
    b.show()
    b.save('1.2.jpg')


def proc2():
    a = {'23 февраля': '23.jpg', 'Новый год': 'нг.jpg', '8 марта': '8.jpg'}
    print("У нас есть открытки к таким праздникам: 23 февраля, Новый год, 8 марта")
    b = input("Открытка к какому празднику вас интерисует? ")

    if b in a:
        x = Image.open(a[b])
        x.show()
    else:
        print("У нас нет подходящей картинки :(")


def proc3():
    x = Image.open('8.jpg')
    a = input("Напишите, кого вы хотите поздравить с днем рождения в именительном падеже: ")

    font = ImageFont.truetype("calibri.ttf", 35)
    drawer = ImageDraw.Draw(x)
    drawer.text((15, 15), a + ", поздравляю с 8 Марта!", font=font, fill='black')

    x.show()
    x.save('с 8 марта.png')


proc3()
