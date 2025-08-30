import os
import win32gui
import win32process
import win32ui
import win32con
from PIL import Image, ImageGrab

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

    # Copy the window image to the bitmap
    saveDC.BitBlt((0, 0), (width, height), mfcDC, (0, 0), win32con.SRCCOPY)

    # Release the device context and bitmap
    saveDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hdc)
    win32gui.DeleteObject(saveBitMap.GetHandle())

    # Convert bitmap to PIL.Image
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    img = Image.frombuffer(
        'RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1
    )

    # Save the image to file
    img_path = os.path.join(os.path.dirname(__file__), 'window.bmp')
    img.save(img_path)

    # Search for green pixel from bottom to top
    width, height = img.size
    print(f"Image size: ({width}, {height})")
    green_pixel = (37, 110, 255)
    for y in range(height-1, -1, -1):
        pixel = img.getpixel((column_index, y))
        if pixel == green_pixel:
            print(f"Found green pixel at ({column_index}, {y}).")
            return y
    return None

# Example usage:
search_green_pixel('希沃云班',11968,323)
