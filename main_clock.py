import math
from datetime import datetime
import time
import tkinter
import threading
from params import *


def get_time():
    """現在時刻から針を描画する"""
    while True:
        now = datetime.now()

        # 角度計算
        angle_h = float(BASE_AGL - 30 * now.hour - 0.5 * now.minute)
        angle_m = int(BASE_AGL - 6 * now.minute)
        angle_s = int(BASE_AGL - 6 * now.second)

        # 針の終端位置
        pos_hx = round(math.cos(math.radians(angle_h))*NEEDLE_H)
        pos_hy = round(math.sin(math.radians(angle_h))*NEEDLE_H)
        pos_mx = round(math.cos(math.radians(angle_m))*NEEDLE_M)
        pos_my = round(math.sin(math.radians(angle_m))*NEEDLE_M)
        pos_sx = round(math.cos(math.radians(angle_s))*NEEDLE_S)
        pos_sy = round(math.sin(math.radians(angle_s))*NEEDLE_S)

        # 針の描写
        canvas.create_line(CENTER, CENTER[0]+pos_hx, CENTER[1]-pos_hy, width=8, tags=W_TAG, fill='white')
        canvas.create_line(CENTER, CENTER[0]+pos_mx, CENTER[1]-pos_my, width=5, tags=W_TAG, fill='white')
        canvas.create_line(CENTER, CENTER[0]+pos_sx, CENTER[1]-pos_sy, width=2, tags=W_TAG, fill='white')

        time.sleep(0.2)

        # キャンバス初期化
        canvas.delete("needle")


if __name__ == '__main__':

    # キャンバス作成
    canvas = tkinter.Canvas(master=None, width=WIDTH, height=HEIGHT, bg='#1c1c1c')

    # 円表示
    canvas.create_oval(10, 10, 390, 390, outline='white', fill='#1c1c1c', width=4)

    # 目盛り表示
    for mark in range(0, 360, 30):
        mark_i_x = round(math.cos(math.radians(mark))*(RADIUS-MARK))
        mark_i_y = round(math.sin(math.radians(mark))*(RADIUS-MARK))
        mark_o_x = round(math.cos(math.radians(mark))*RADIUS)
        mark_o_y = round(math.sin(math.radians(mark))*RADIUS)
        canvas.create_line((CENTER[0]+mark_i_x, CENTER[1]+mark_i_y), (CENTER[0]+mark_o_x, CENTER[1]+mark_o_y), width=3, fill='white')

    # キャンバス表示
    canvas.pack()

    # スレッド作成
    thread = threading.Thread(target=get_time, daemon=True)

    # スレッド開始
    thread.start()

    # イベントループ
    canvas.mainloop()