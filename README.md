# Generate-Sample-Image

<p align="center">
    <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/green1.png" alt="green1.png" title="green1.png"  width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/green2.png" alt="green2.png" title="green2.png"  width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/green3.png" alt="green3.png" title="green3.png"  width="200">
</p>

色づいた背景の中央付近に"色+数字"が白文字で表示された画像を生成するためのソースコードです。
例えば，緑色の背景の中央付近に"緑1"と表示した画像green1.png、"緑2"と表示した画像green2.png、"緑3"と表示した画像green3.png、などを生成します。

- [![python-shield]][python-url]で書かれています。
- 各色について"色+数字"を99枚まで(num = 99)は綺麗に表示できます。
## 🧑‍💻使用方法
### 実行方法
以下のように実行すると、緑色(green)、赤色(red)、青色(blue)、紫色(purple)、茶色(brown)、灰色(gray)、桃色(pink)、黒色(black)、水色(light blue)について、色づいた背景の中央付近に"色+数字"が白文字で表示された画像を生成する。
```Console
L3on@MacBook:Generate-Sample-Image$ python generate_sample_image.py 
./sample_image/green1.png を生成しました
...
./sample_image/green3.png を生成しました
./sample_image/red1.png を生成しました
...
./sample_image/red3.png を生成しました
./sample_image/blue1.png を生成しました
...
./sample_image/blue3.png を生成しました
./sample_image/purple1.png を生成しました
...
./sample_image/purple3.png を生成しました
./sample_image/brown1.png を生成しました
...
./sample_image/brown3.png を生成しました
./sample_image/gray1.png を生成しました
...
./sample_image/gray3.png を生成しました
./sample_image/pink1.png を生成しました
...
./sample_image/pink3.png を生成しました
./sample_image/black1.png を生成しました
...
./sample_image/black3.png を生成しました
./sample_image/light blue1.png を生成しました
...
./sample_image/light blue3.png を生成しました
```
### 実行結果
[sample_imageディレクトリ内][sample_image_dir-url]のような画像を生成できます。
<details>
<summary>num = 3 とした場合に生成した画像全て</summary>

<p align="center">
    <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/green1.png" alt="green1.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/green2.png" alt="green2.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/green3.png" alt="green3.png" width="200">
</p>
<p align="center">
    <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/red1.png" alt="red1.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/red2.png" alt="red2.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/red3.png" alt="red3.png" width="200">
</p>
<p align="center">
    <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/blue1.png" alt="blue1.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/blue2.png" alt="blue2.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/blue3.png" alt="blue3.png" width="200">
</p>
<p align="center">
    <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/purple1.png" alt="purple1.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/purple2.png" alt="purple2.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/purple3.png" alt="purple3.png" width="200">
</p>
<p align="center">
    <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/brown1.png" alt="brown1.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/brown2.png" alt="brown2.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/brown3.png" alt="brown3.png" width="200">
</p>
<p align="center">
    <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/gray1.png" alt="gray1.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/gray2.png" alt="gray2.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/gray3.png" alt="gray3.png" width="200">
</p>
<p align="center">
    <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/pink1.png" alt="pink1.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/pink2.png" alt="pink2.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/pink3.png" alt="pink3.png" width="200">
</p>
<p align="center">
    <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/black1.png" alt="black1.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/black2.png" alt="black2.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/black3.png" alt="black3.png" width="200">
</p>
<p align="center">
    <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/light blue1.png" alt="light blue1.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/light blue.png" alt="light blue2.png" width="200"> <img src="https://github.com/L3onSW/Generate-Sample-Image/blob/main/sample_image/light blue3.png" alt="light blue3.png" width="200">
</p>
</details>

## 💻 環境
- Python 3.8.3
  - numpy=1.18.5
  - matplotlib=3.2.2
  - pillow=7.2.0

## 📚 参考文献
1. [HTMLカラーコード: WEB色見本 原色大辞典. (参照：2024-03-26).][rgb-url]

<!-- 使用したリンク -->
[python-shield]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[python-url]: https://www.python.org
[sample_image_dir-url]: https://github.com/L3onSW/Generate-Sample-Image/blob/master/sample_image/
[rgb-url]: https://www.colordic.org/
