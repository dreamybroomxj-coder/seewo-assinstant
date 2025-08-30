import win32gui
import win32process
import win32ui
import win32con
from PIL import Image,ImageGrab

def search_green_pixel(window_title, pid, column_index):
    # Find the window by title
    hwnd = win32gui.FindWindow(None, window_title)
    if not hwnd:
        print(f'Window "{window_title}" not found.')
        return None
    # Check if the window's process ID matches the given PID
    if win32process.GetWindowThreadProcessId(hwnd)[1] != pid:
        print(f'PID {pid} not match.')
        return None
    
    # Get the device context and window size
    hdc = win32gui.GetWindowDC(hwnd)
    window_rect = win32gui.GetWindowRect(hwnd)
    width = window_rect[2] - window_rect[0]
    height = window_rect[3] - window_rect[1]

    # Create a bitmap object and select it into a DC
    mfcDC = win32ui.CreateDCFromHandle(hdc)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)

    rect = win32gui.GetWindowRect(hwnd)
    img = ImageGrab.grab(rect)
    width, height = img.size
    print(f"Image size: ({width}, {height})")  # 添加调试信息
    green_pixel = (37, 110, 255)
    for y in range(height-1, -1, -1):  # From bottom to top
        #if column_index < width and y < height:  # 添加断言检查坐标是否超出图片范围
        pixel = img.getpixel((column_index, y))
        if pixel == green_pixel:
            print(f"Found green pixel at ({column_index}, {y}).")
            return y
    return None# Example usage:
search_green_pixel('希沃云班',11968,323)