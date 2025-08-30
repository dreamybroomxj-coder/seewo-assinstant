import win32gui

def get_window_rect(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    return (rect[0], rect[1], rect[2], rect[3])

def get_window_corners(window_name, pid):
    hwnd = win32gui.FindWindowEx(0, 0, None, window_name)
    #if hwnd == 0:
    #    return None
    #if win32gui.GetWindowThreadProcessId(hwnd)[1] != pid:
    #    return None
    rect = get_window_rect(hwnd)
    corners = [(rect[0], rect[1]), (rect[2], rect[1]), (rect[2], rect[3]), (rect[0], rect[3])]
    return corners

print(get_window_corners("希沃云班",11968))
