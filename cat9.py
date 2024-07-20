from PIL import Image

# Example usage
image_paths = [
    "/Users/cengyijie/Downloads/image72963_toilet.png", 
    '/Users/cengyijie/Downloads/image72965_toilet.png', 
    '/Users/cengyijie/Downloads/image13980_toilet.png', 
    '/Users/cengyijie/Downloads/image13976_toilet.png',
    '/Users/cengyijie/Downloads/image75013_bed.png', 
    '/Users/cengyijie/Downloads/image75011_bed.png',
    '/Users/cengyijie/Downloads/image399_bed.png', 
    '/Users/cengyijie/Downloads/image395_bed.png', 
    '/Users/cengyijie/Downloads/Xnip2024-07-08_16-47-18.jpg'
]
image_paths=["/Users/cengyijie/Downloads/map2/image231_bed.png",
             "/Users/cengyijie/Downloads/map2/image233_bed.png",
             "/Users/cengyijie/Downloads/map2/image0_toilet.png",
             "/Users/cengyijie/Downloads/map2/image2_toilet.png",
             "/Users/cengyijie/Downloads/map2/image1326_tv.png",
             "/Users/cengyijie/Downloads/map2/image1328_tv.png",
             "/Users/cengyijie/Downloads/map2/image1590_potted plant.png",
             "/Users/cengyijie/Downloads/map2/image1598_potted plant.png",
             "/Users/cengyijie/Downloads/Xnip2024-07-08_16-27-10.jpg"
             
             ]

# image_paths=["/Users/cengyijie/Desktop/截屏2024-07-02 17.59.12.png",
#              "/Users/cengyijie/Downloads/work2/1a.jpg",
#              "/Users/cengyijie/Desktop/截屏2024-07-02 17.59.39.png",
#              "/Users/cengyijie/Downloads/work2/1b.jpg"]
# 打开所有图片
images = [Image.open(img_path) for img_path in image_paths]

# 按需组合图片
comb_images = []
for i in range(0, 8, 2):
    width = max(images[i].width, images[i+1].width)
    height = images[i].height + images[i+1].height
    combined_image = Image.new('RGB', (width, height))
    combined_image.paste(images[i], (0, 0))
    combined_image.paste(images[i+1], (0, images[i].height))
    comb_images.append(combined_image)

# 横向拼接 A, B, C, D 图像，并添加0.5 cm间隔
gap = 15  # 0.5 cm = 5 pixels
total_width = sum(img.width for img in comb_images) + 3 * gap
max_height = max(img.height for img in comb_images)

combined_4 = Image.new('RGB', (total_width, max_height))

x_offset = 0
for img in comb_images:
    combined_4.paste(img, (x_offset, 0))
    x_offset += img.width + gap

# 处理第九张图片
image9 = images[8]
new_height = max_height
new_width = int(image9.width * (new_height / image9.height))
image9_resized = image9.resize((new_width, new_height))

# 创建最终图片，并添加间隔
final_width = combined_4.width + gap + image9_resized.width
final_image = Image.new('RGB', (final_width, max_height))

final_image.paste(combined_4, (0, 0))
final_image.paste(image9_resized, (combined_4.width + gap, 0))

# 保存最终图片
final_image.save('/Users/cengyijie/Downloads/final_image01.jpg')








