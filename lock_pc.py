# lock_pc.py
import ctypes

def lock_pc():
    # Для Windows
    ctypes.windll.user32.LockWorkStation()
    
    # Для Linux (раскомментировать если нужно)
    # import os
    # os.system('xdg-screensaver lock')
    
    return True
