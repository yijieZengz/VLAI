# # from PIL import Image, ImageOps

# # # Load the image
# # image_path = '/Users/cengyijie/Desktop/截屏2024-07-02 17.59.51.png'  # Replace with your image path
# # image = Image.open(image_path)

# # # Define the border size
# # border_size = 2  # Adjust the border size if needed

# # # Add a black border around the image
# # bordered_image = ImageOps.expand(image, border=border_size, fill='black')

# # # Save the new image
# # bordered_image.save('/Users/cengyijie/Downloads/work2/1.jpg')
# from PIL import Image, ImageOps

# def add_black_border(input_image_path, output_image_path):
#     # 打开图像
#     image = Image.open(input_image_path)

#     # 定义边框宽度（2像素）
#     border_width = 2

#     # 添加黑色边框
#     bordered_image = ImageOps.expand(image, border=border_width, fill='black')

#     # 保存带边框的图像
#     bordered_image.save(output_image_path)

# # 示例调用
# input_image_path = '/Users/cengyijie/Downloads/final_concatenated_image.jpg'  # 输入图像路径
# output_image_path = '/Users/cengyijie/Downloads/final_concatenated_image.jpg'  # 输出图像路径
# add_black_border(input_image_path, output_image_path)
from PIL import Image, ImageOps

def expand_image_borders(image_path, output_path):
    # 打开输入图片
    image = Image.open(image_path)
    
    # 获取原始图片尺寸
    original_width, original_height = image.size
    
    # 新图片尺寸，比原始图片每边大4像素
    new_width = original_width + 4
    new_height = original_height + 4
    
    # 创建一个新的黑色背景的图片
    new_image = Image.new('RGB', (new_width, new_height), (0, 0, 0))
    
    # 将原始图片粘贴到新图片的中心
    new_image.paste(image, (2, 2))
    
    # 保存处理后的图片
    new_image.save(output_path)

# 使用示例：
expand_image_borders('/Users/cengyijie/Downloads/final_concatenated_image.jpg', '/Users/cengyijie/Downloads/final_concatenated_image.jpg')
