#!/opt/anaconda3/bin/python
# ======================================================================
# 色づいた背景の中央付近に"色+数字"が白文字で表示された画像を生成する
# 例えば，緑色の背景の中央付近に"緑1"と表示した画像green1.pngを生成する
#
# Created on 2024/03/26, author: L3onSW
# ======================================================================
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro',
                               'Yu Gothic',
                               'Meirio',
                               'Takao',
                               'IPAexGothic',
                               'IPAPGothic',
                               'Noto Sans CJK JP']

# 全色共通で各色ごとに生成する画像の枚数
num = 10
# RGBのタプルを順に格納したリスト(ただし白色の文字を挿入して見やすい色を選択)
rgb_list = []
# RGBのタプルを順に格納したリストに対応した色の名前(ただし1文字の漢字で統一)
color_kanji_list = []
# RGBのタプルを順に格納したリストに対応した色の名前(ただし英語)
color_english_list = []

# 緑色(green)
rgb_green = (0, 92, 66)
rgb_list.append(rgb_green)
color_kanji_list.append("緑")
color_english_list.append("green")
# 赤色(red)
rgb_red = (220, 20, 60)
rgb_list.append(rgb_red)
color_kanji_list.append("赤")
color_english_list.append("red")
# 青色(blue)
rgb_blue = (0, 63, 142)
rgb_list.append(rgb_blue)
color_kanji_list.append("青")
color_english_list.append("blue")
# 紫色(purple)
rgb_purple = (75, 0, 130)
rgb_list.append(rgb_purple)
color_kanji_list.append("紫")
color_english_list.append("purple")
# 茶色(brown)
rgb_brown = (98, 45, 24)
rgb_list.append(rgb_brown)
color_kanji_list.append("茶")
color_english_list.append("brown")
# 灰色(gray)
rgb_gray = (98, 96, 99)
rgb_list.append(rgb_gray)
color_kanji_list.append("灰")
color_english_list.append("gray")
# 桃色(pink)
rgb_pink = (216, 52, 115)
rgb_list.append(rgb_pink)
color_kanji_list.append("桃")
color_english_list.append("pink")
# 黒色(black)
rgb_black = (0, 0, 0)
rgb_list.append(rgb_black)
color_kanji_list.append("黒")
color_english_list.append("black")
# 水色(light blue)
rgb_light_blue = (0, 117, 194)
rgb_list.append(rgb_light_blue)
color_kanji_list.append("水")
color_english_list.append("light blue")

# 画像をまとめて置くディレクトリ(ただし最後に"/"をつけない)
img_dir = "./sample_image"

# 画像サイズを指定するタプル: 幅81, 高さ61
img_size = (81, 61)
# 画像サイズに合わせてハードコーディングした軸の表示方法を格納したリスト
xticks_list = [0, 10, 20, 30, 40, 50, 60, 70, 80]
xtickslabels_list = ["0", "10", "20", "30", "40", "50", "60", "70", "80"]
yticks_list = [0, 10, 20, 30, 40, 50, 60]
ytickslabels_list = ["0", "10", "20", "30", "40", "50", "60"]

# 各色について順に格納したリストを利用して画像を生成していく
for i in range(len(color_english_list)):
    # 画像ファイルのパスを定義
    img_name_header = color_english_list[i]
    img_name_body = [str(j+1) for j in range(num)]
    img_name_footer = ".png"
    # 画像の生成
    for j in range(num):
        im = Image.new("RGB",  img_size, rgb_list[i])
        im_list = np.asarray(im)
        fig, ax = plt.subplots()
        plt.imshow(im_list)
        # 軸の設定
        ax.set_xticks(xticks_list)
        ax.set_xticklabels(xtickslabels_list, fontsize=20)
        ax.set_yticks(yticks_list)
        ax.set_yticklabels(ytickslabels_list, fontsize=20)
        # 漢字で色の名前を表示
        plt.text(15, 40, color_kanji_list[i]+str(j+1),
                 fontsize=100, fontweight="bold", color="white")
        # 画像を保存するディレクトリが無い場合には作成する
        os.makedirs(img_dir, exist_ok=True)
        # 画像のパスを定義する
        img_name = img_dir + "/"
        img_name += img_name_header + img_name_body[j] + img_name_footer
        # 画像を保存
        plt.savefig(img_name, format="png", dpi=100)
        print(img_name + " を生成しました")
        # 図を閉じる
        plt.close(fig)
