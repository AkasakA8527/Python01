import os
from PIL import Image

input_folder = '10'
cropped_folder = 'cropped'
pdf_filename = 'output.pdf'

if not os.path.exists(cropped_folder):
  os.makedirs(cropped_folder)

input_files = sorted([
  f for f in os.listdir(input_folder)
  if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')
])

left_crop = 50    # 左からのクロップピクセル数
top_crop = 1204   # 上からのクロップピクセル数
right_crop = 389  # 右からのクロップピクセル数
bottom_crop = 122 # 下からのクロップピクセル数

for filename in input_files:
  filepath = os.path.join(input_folder, filename)
  image = Image.open(filepath)
  width, height = image.size
  # クロップ領域の計算
  left = left_crop
  top = top_crop
  right = width - right_crop
  bottom = height - bottom_crop
  # クロップ実行
  cropped_image = image.crop((left, top, right, bottom))
  cropped_image.save(os.path.join(cropped_folder, filename))

cropped_files = sorted([
  f for f in os.listdir(cropped_folder)
  if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')
])

image_list = []
for filename in cropped_files:
  filepath = os.path.join(cropped_folder, filename)
  image = Image.open(filepath)
  # PDF保存のためにRGBモードに変換。RGBモードのことは要勉強。
  if image.mode != 'RGB':
      image = image.convert('RGB')
  image_list.append(image)

if image_list:
  pdf_path = os.path.join(cropped_folder, pdf_filename)
  image_list[0].save(pdf_path, save_all=True, append_images=image_list[1:])

