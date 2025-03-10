import win32gui
import win32api
import win32con
from win32con import HORZRES, VERTRES
import random
import ctypes
import colorsys
hdc = win32gui.GetDC(0)
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sw, sh] = [ctypes.windll.gdi32.GetDeviceCaps(hdc,HORZRES), ctypes.windll.gdi32.GetDeviceCaps(hdc,VERTRES)]

color = 0
while True:


    rgb_color = colorsys.hsv_to_rgb(color, 1.0, 1.0)

    brush = win32gui.CreateSolidBrush(
        win32api.RGB(
            int(rgb_color[0]) * 255, int(rgb_color[1]) * 255, int(rgb_color[2]) * 255
        )
    )
    win32gui.SelectObject(hdc, brush)
    win32gui.BitBlt(
        hdc,
        random.randint(-10, 10),
        random.randint(-10, 10),
        sw,
        sh,
        hdc,
        0,
        0,
        win32con.SRCCOPY,
    )
    win32gui.BitBlt(
        hdc,
        random.randint(-10, 10),
        random.randint(-10, 10),
        sw,
        sh,
        hdc,
        0,
        0,
        win32con.PATINVERT,
    )
    color += 0.05
