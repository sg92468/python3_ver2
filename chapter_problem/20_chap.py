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

