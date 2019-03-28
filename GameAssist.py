# -*- coding:utf-8 -*-
import win32gui
import time

import pyautogui as pyg

import importlib, sys

importlib.reload(sys)


class GameAssist:

    def __init__(self, wdname):
        """初始化"""

        # 取得窗口句柄
        self.hwnd = win32gui.FindWindow(0, wdname)
        if not self.hwnd:
            print("窗口找不到，请确认窗口句柄名称：【%s】" % wdname)
            exit()
        # 窗口显示最前面
        # win32gui.SetWindowPos(self.hwnd , win32con.HWND_TOP, 600,300,600,600,win32con.SWP_SHOWWINDOW)
        win32gui.SetForegroundWindow(self.hwnd)
        size = win32gui.GetWindowRect(self.hwnd)
        print("窗口位置：", size)

        # gps = win32api.GetCursorPos()
        # print self.hwnd
        # time.sleep(15)
        # topx, topy = size[0], size[1]
        # time.sleep(2)
        # 1、用grab函数截图，参数为左上角和右下角左标
        # ImageGrab.grab((topx + 399, topy + 890, topx + 399 + 182, topy + 890 + 33)).save('E:\pycharm\ceshi.jpg')
        # win32api.SetCursorPos(gps)
        # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        # win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)

    # 程序入口、控制中心
    def start(self):
        global i
        i = 1
        while True:
            time.sleep(2)

            # im = pyg.screenshot(region=(990, 197, 268, 66))
            # im.save("zdtest.png")
            pz3 = pyg.locateOnScreen('pz3.png', confidence=0.80, grayscale=True)
            bt = pyg.locateOnScreen('bt7.png', confidence=0.80, grayscale=True)
            m5 = pyg.locateOnScreen('m5.png', confidence=0.80, grayscale=True)
            zd = pyg.locateOnScreen('E:\pycharm\\zd.png', confidence=0.90)
            size = win32gui.GetWindowRect(self.hwnd)
            topx, topy = size[0], size[1]
            if pz3 != None or bt != None or m5 != None:
                if pz3 != None:
                    pos = pz3
                    tank = "pz35t"
                elif bt != None:
                    pos = bt
                    tank = "bt7"
                else:
                    pos = m5
                    tank = "m5"
                s_x, s_y = pyg.center(pos)
                pyg.click(s_x, s_y)
                time.sleep(0.5)
                pyg.click(topx + 910, topy + 150)
                print(tank, "开始战斗，第", i, "次出战")
                i = i + 1
                while True:
                    time.sleep(1)
                    zbzd = pyg.locateOnScreen('zbzd.png', confidence=0.70, grayscale=True)
                    if zbzd != None:
                        pyg.keyDown('e')
                        print('按下e')
                        break
                # if zd != None:
                #     s_x, s_y = pyg.center(zd)
                #     pyg.click(s_x, s_y)
                #     print("点击", pyg.center(zd), "，开始战斗")
                #     while True:
                #         time.sleep(1)
                #         zbzd = pyg.locateOnScreen('zbzd.png', confidence=0.70, grayscale=True)
                #         if zbzd != None:
                #             pyg.keyDown('e')
                #             print('按下e')
                #             break

                while True:
                    jh = pyg.locateOnScreen('jihui.png', confidence=0.60, grayscale=True)
                    zj = pyg.locateOnScreen('zanji.png', confidence=0.80, grayscale=True)
                    if jh != None:
                        pyg.keyUp('e')
                        print('松开e')
                        time.sleep(0.5)
                        pyg.press('esc')
                        time.sleep(0.5)
                        pyg.click(topx + 960, topy + 480)
                        time.sleep(0.5)
                        pyg.click(topx + 1080, topy + 630)
                        print("点击", "，回城")
                        break
                    if zj != None:
                        pyg.keyUp('e')
                        print('松开e')
                        time.sleep(1)
                        pyg.click(topx + 50, topy + 80)
                        print("点击", "，回城")
                        break


if __name__ == "__main__":
    wdname = u'WoT Blitz ‎- WoT Blitz'
    # wdname = u'BlueStacks App Player'
    # wdname = u'夜神模拟器'

    demo = GameAssist(wdname)
    demo.start()
