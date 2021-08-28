from logger import logger

from win32api import GetSystemMetrics
import pyautogui
import win32gui
import ast

class utils:

    class config:
        def __init__(self, mode, window_width, window_height, fps, delay):
            self.mode = mode
            self.window_width = window_width
            self.window_height = window_height
            self.fps = fps
            self.delay = delay

    conf = None

    def read_config():
        try:
            file = open("Configs.txt", "r")
            contents = file.read()
            dictionary = ast.literal_eval(contents)
            file.close()
        except Exception as obj_erro:
            print(" Exception: " + str(obj_erro))
            logger.write_log(" Exception: " + str(obj_erro))
            return
        utils.conf = utils.config(dictionary["mode"], dictionary["window_width"], dictionary["window_height"], dictionary["fps"], dictionary["delay"]) 
        return

    def capture_window(window_title=None, mode=None):
        
        if mode == 1:
            x, y, x1, y1 = 0, 0, GetSystemMetrics(0), GetSystemMetrics(1)
            im = pyautogui.screenshot(region=(x, y, x1, y1))
            return im

        if mode == 2:
            if window_title:
                hwnd = win32gui.FindWindow(None, window_title)
                if hwnd:
                    win32gui.SetForegroundWindow(hwnd)
                    x, y, x1, y1 = win32gui.GetClientRect(hwnd)
                    x, y = win32gui.ClientToScreen(hwnd, (x, y))
                    x1, y1 = win32gui.ClientToScreen(hwnd, (x1 - x, y1 - y))
                    im = pyautogui.screenshot(region=(x, y, x1, y1))
                    return im
                else:
                    print('Window not found!')
                    logger.write_log("Problema ao buscar janela")
            else:
                im = pyautogui.screenshot()
                return im


