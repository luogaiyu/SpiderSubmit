from PIL import Image
import os

# 将 webp 格式的图片转换成png格式

# 设置源目录和目标目录
src_dir = r'D:\Desktop\workRelated\chatgpt\image\html\html3\Midjourney Showcase_files'
dst_dir = src_dir + '\\result'
try:
    os.mkdir(dst_dir)
except:
    pass
# 遍历源目录下所有文件
for filename in os.listdir(src_dir):
    # 检查文件是否为webp格式
    if filename.endswith('.webp'):
        # 打开图片并保存为png格式
        with Image.open(os.path.join(src_dir, filename)) as im:
            png_filename = os.path.splitext(filename)[0] + '.png'
            im.save(os.path.join(dst_dir, png_filename), 'png')