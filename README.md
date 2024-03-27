# Generate-Sample-Image
色づいた背景の中央付近に"色+数字"が白文字で表示された画像を生成するためのソースコードです。例えば，緑色の背景の中央付近に"緑1"と表示した画像green1.pngを生成します。
<img src="https://github.com/L3onSW/Generate-Sample-Image/blob/master/sample_image/green1.png" alt="green1.png" title="green1.png">
- [![python-shield]][python-url]で書かれています。
- 各色について"色+数字"を99枚まで(num = 99)は綺麗に表示できます。
## 🧑‍💻使用方法
### 実行方法
以下のように実行すると、緑色(green)、赤色(red)、青色(blue)、紫色(purple)、茶色(brown)、灰色(gray)、桃色(pink)、黒色(black)、水色(light blue)について、色づいた背景の中央付近に"色+数字"が白文字で表示された画像を生成する。
```Console
L3on@MacBook:Generate-Sample-Image$ python generate_sample_image.py 
./sample_image/green1.png を生成しました
...
./sample_image/green10.png を生成しました
./sample_image/red1.png を生成しました
...
./sample_image/red10.png を生成しました
./sample_image/blue1.png を生成しました
...
./sample_image/blue10.png を生成しました
./sample_image/purple1.png を生成しました
...
./sample_image/purple10.png を生成しました
./sample_image/brown1.png を生成しました
...
./sample_image/brown10.png を生成しました
./sample_image/gray1.png を生成しました
...
./sample_image/gray10.png を生成しました
./sample_image/pink1.png を生成しました
...
./sample_image/pink10.png を生成しました
./sample_image/black1.png を生成しました
...
./sample_image/black10.png を生成しました
./sample_image/light blue1.png を生成しました
...
./sample_image/light blue10.png を生成しました
```
### 実行結果
[sample_imageディレクトリ内][sample_image_dir-url]のような画像を生成できます。

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
