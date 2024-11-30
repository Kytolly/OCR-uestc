from pdf2image import convert_from_path

# 将 PDF 文件转换为图像
images = convert_from_path('cache/test.pdf')

# 保存图像
for i, image in enumerate(images):
    image.save(f'page_{i+1}.png', 'PNG')
