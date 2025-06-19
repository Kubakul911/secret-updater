def lock_pc():
    import ctypes
    ctypes.windll.user32.LockWorkStation()

lock_pc()
