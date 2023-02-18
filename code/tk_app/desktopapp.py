import tkinter



setting = tkinter.Tk()
setting.title('Desktop App')
setting.geometry('800x600')
setting.resizable(False, False)

canvas = tkinter.Canvas(setting, width=800, height=600, bg="skyblue", highlightthickness=0)
canvas.pack()

settingimg = tkinter.PhotoImage(file = 'image/bonsai.png')
canvas.create_image(400, 300, image=settingimg, tags='image')

results='盆栽'
canvas.create_text(400, 70, text=results, font=('ヒラギノ明朝 ProN', 100), fill='#ffffff', tags='text')


setting.mainloop()