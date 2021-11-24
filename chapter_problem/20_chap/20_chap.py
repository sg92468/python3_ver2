# # 20.1.2 PILとPillow
# from PIL import Image
# img = Image.open('test.JPG')
# print(img.format)
# print(img.size)
# print(img.mode)

# # img.show()
# crop = (55, 70, 85, 100)
# img2 = img.crop(crop)

# img2.save('cropped.gif', 'GIF')
# img3 = Image.open('cropped.gif')
# print(img3.format)
# print(img3.size)

# # 20.1.3 ImageMagick
# from wand.image import Image
# from wand.display import display
# img = Image(filename='test.JPG')
# print(img.size)
# print(img.format)
# display(img)

# # 20.4 GUI
# import tkinter
# from PIL import Image, ImageTk
# main = tkinter.Tk()
# img = Image.open('test.JPG')
# tking = ImageTk.PhotoImage(img)
# tkinter.Label(main, image=tking).pack()
# main.mainloop()

# q20.1,2,3
import matplotlib.pyplot as plt

x = (0, 3, 6, 9, 14)
y = (0, 5, 2, 8, 10)
fig, plots = plt.subplots(nrows=1, ncols=3)

plots[0].scatter(x, y)
plots[1].plot(x, y)
plots[2].plot(x, y, 'o-')

plt.show()