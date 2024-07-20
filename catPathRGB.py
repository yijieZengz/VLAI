from PIL import Image

# 两个列表中的图片路径
list2 = ['/Users/cengyijie/Downloads/episodePath/1.jpg',
         '/Users/cengyijie/Downloads/episodePath/2.jpg',
        #  '/Users/cengyijie/Downloads/episodePath/3.jpg',
         '/Users/cengyijie/Downloads/episodePath/4.jpg',
         '/Users/cengyijie/Downloads/episodePath/5.jpg',
         '/Users/cengyijie/Downloads/episodePath/6.jpg']
list2.reverse()

list1 = ['/Users/cengyijie/Downloads/episodeRGB/1.jpg',
         '/Users/cengyijie/Downloads/episodeRGB/2.jpg',
        #  '/Users/cengyijie/Downloads/episodeRGB/3.jpg',
         '/Users/cengyijie/Downloads/episodeRGB/4.jpg',
         '/Users/cengyijie/Downloads/episodeRGB/5.jpg',
         '/Users/cengyijie/Downloads/episodeRGB/6.jpg']

# 定义黑色填充区域的宽度
black_space_width = 15

# 存放上下拼接后的图片
vertical_images = []

for path1, path2 in zip(list1, list2):
    image1 = Image.open(path1)
    image2 = Image.open(path2)

    # 确保图像的宽度一致
    width = min(image1.width, image2.width)
    image1 = image1.resize((width, image1.height), Image.LANCZOS)
    image2 = image2.resize((width, image2.height), Image.LANCZOS)

    # 创建新的图像用于上下拼接
    new_height = image1.height + image2.height
    new_image = Image.new('RGB', (width, new_height))

    # 拼接图像
    new_image.paste(image1, (0, 0))
    new_image.paste(image2, (0, image1.height))

    vertical_images.append(new_image)

# 计算水平拼接后的总宽度和高度
total_width = sum(image.width for image in vertical_images) + \
    black_space_width * (len(vertical_images) - 1)
total_height = max(image.height for image in vertical_images)

# 创建新的图像用于水平拼接
final_image = Image.new('RGB', (total_width, total_height), (0, 0, 0))

# 水平拼接图片并添加黑色空隙
x_offset = 0
for image in vertical_images:
    final_image.paste(image, (x_offset, 0))
    x_offset += image.width + black_space_width

# 保存最终的拼接图片
final_image.save("/Users/cengyijie/Downloads/final_concatenated_image_change.jpg")
