import os
import sys
import win32gui
import win32api

from win32con import WM_INPUTLANGCHANGEREQUEST
from pynput.keyboard import Key, Listener, KeyCode
from PyQt5.QtWidgets import QMessageBox, QApplication

# 中文输入法id: 0x0804
# English IME id: 0x0409
# https://msdn.microsoft.com/en-us/library/cc233982.aspx

lock = True # 锁定状态
lt_from_t = False # 因为按t而解锁键盘

english_ime_id = 0x0409
your_ime_id = 0x0804 # Change to your ime id

minecraft_titles = [
    "Minecraft",
    "Lunar",
    "BadLion",
    "LiquidBounce",
    "Feather",
    "我的世界"
] # 关于Minecraft的标题名称(将你的游戏标题添加进来,只需要写一部分就可以了,带有版本号的不要写版本号)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def msgerror(title: str, message: str):
    """显示一条错误消息"""
    app = QApplication(sys.argv)
    QMessageBox.critical(None, title, message)

def msginfo(title: str, message: str):
    """显示一条提示消息"""
    app = QApplication(sys.argv)
    QMessageBox.information(None, title, message)


def on_press(key: Key):
    global lock, lt_from_t
    hwnd = win32gui.GetForegroundWindow() # 获取句柄
    win_title: str = win32gui.GetWindowText(hwnd)
    if key == Key.f12:
        change_ime(your_ime_id) # 恢复状态
        sys.exit()
    is_mc = False
    for w in minecraft_titles:
        if w.lower() in win_title.lower():
            is_mc = True
    if is_mc:
        if not lt_from_t:
            change_ime(english_ime_id)
    else:
        change_ime(your_ime_id)
        return
    if (key == KeyCode.from_char("t") or key == KeyCode.from_char("/")) and lock == True:
        change_ime(your_ime_id)
        lock = False
        lt_from_t = True
    elif key == KeyCode.from_char("e") and lock == True and lt_from_t == False:
        change_ime(your_ime_id)
        lock = False
    elif key == KeyCode.from_char("e") and lock == False and lt_from_t == False:
        change_ime(english_ime_id)
        lock = True
    elif key == Key.esc or key == Key.enter:
        change_ime(english_ime_id)
        lock = True
        lt_from_t = False

def change_ime(ime_id):
    """切换语言"""
    hwnd = win32gui.GetForegroundWindow() # 获取句柄
    # win_title: str = win32gui.GetWindowText(hwnd)
    # is_mc = False
    # for w in minecraft_titles:
    #     if w.lower() in win_title.lower():
    #         is_mc = True
    # if not is_mc:
    #     return
    # im_list = win32api.GetKeyboardLayoutList() # 所有的输入法
    result = win32api.SendMessage(hwnd, WM_INPUTLANGCHANGEREQUEST, 0, ime_id)
    if result != 0:
        # 未安装对应输入法
        msgerror("Error", f"没有安装对应输入法, 输入法id: {ime_id}\nid对应的语言可见https://msdn.microsoft.com/en-us/library/cc233982.aspx")

def main():
    msginfo("使用提示", """Minecraft键盘锁使用方法\n当在游戏中输入文字时会解除输入法的锁定,而玩游戏时会自动回锁\n按下f12退出""")
    change_ime(english_ime_id)
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == '__main__':
    main()
