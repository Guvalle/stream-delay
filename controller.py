from utils import utils

from PIL import Image, ImageTk
from logger import logger

import tkinter
import win32gui

class controller(object):
    
    def create_window():
        root = tkinter.Tk()
        root.title("Stream Focus by Guto V0.1BETA - For complete version and updates email gustavoavalle@hotmail.com")
        canvas = tkinter.Label(root)
        canvas.pack()

        #Inicializacao do array de imagens
        try:
            img = ImageTk.PhotoImage(Image.open("sflogo.jpg"))
        except Exception as obj_erro:
            print(" Exception: " + str(obj_erro))
            logger.write_log(" Exception: " + str(obj_erro))
            return
        sleep = int(1000 / utils.conf.fps) - 1 
        img_array = [img] * int((utils.conf.delay * utils.conf.fps)/5)
    
        def loopCapture():
            #descobre qual a janela ativa, pega o nome dela e tira uma screenshot
            img = utils.capture_window(win32gui.GetWindowText(win32gui.GetForegroundWindow()), utils.conf.mode)

            #redimensiona a imagem para o tamanho da janela
            img = img.resize((utils.conf.window_width, utils.conf.window_height), Image.ANTIALIAS)
            #adiciona a screenshot ao array de imagens
            img_array.append(ImageTk.PhotoImage(img))
            #remove a imagem mais antiga
            del img_array[0]
        
            #atualiza a exibicao da janela
            canvas.config(image=img_array[0])
            root.update_idletasks()
            root.after(sleep, loopCapture)

        loopCapture()
        root.mainloop()


