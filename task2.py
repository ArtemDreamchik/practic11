from PIL import Image
import os

for file in os.listdir("images/task2images"):
    if file.lower().endswith(".jpg") or file.lower().endswith(".png"):

        img = Image.open("images/task2images/doge.jpg")
        img.show()

        print('Формат: ', img.format)
        print('Размер: ', img.size)
        print('Цветовая модель: ', img.mode)

