#!/usr/bin/python
# _*_ coding:utf-8 _*_
"""
  @author: likaiyan
  @date: 2021/1/17 12:18 下午
  @desc: img2ascii
"""

from PIL import Image
import argparse


class Img2Ascii:

    def __init__(self):
        width, height, source_file_path, target_file_path = self.parse_args()
        self.img_width = width
        self.img_height = height
        self.source = source_file_path
        self.target = target_file_path

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('source_file_path')
        parser.add_argument('target_file_path')
        parser.add_argument('--width', type=int, default=50)
        parser.add_argument('--height', type=int, default=50)
        args = parser.parse_args()
        return args.width, args.height, args.source_file_path, args.target_file_path

    def to_char(self, r, g, b, alpha=256):
        if alpha == 0:
            return ' '
        gary = (2126 * r + 7152 * g + 722 * b) / 10000
        ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        x = int(gary / (alpha + 1.0) * len(ascii_char))
        return ascii_char[x]

    def save_target_file(self, content):
        with open(self.target, 'w') as f:
            f.write(content)

    def run(self):
        img = Image.open(self.source)
        img = img.resize((self.img_width, self.img_height), Image.NEAREST)
        txt = ''
        for i in range(img.height):
            for j in range(img.width):
                content = img.getpixel((j, i))
                if isinstance(content, int):
                    content = (content, content, content)
                txt += self.to_char(*content)
            txt += '\n'
        print(txt)
        self.save_target_file(txt)

if __name__ == '__main__':
    Img2Ascii().run()