import re
import os
from PIL import Image, ImageDraw, ImageFont

def capture_text_from_end(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    pattern = r'(test execution summary.*?)(?=(test execution summary|$))'
    matches = re.findall(pattern, text, re.DOTALL)
    
    if matches:
        # 获取最后一个匹配项的内容
        last_match = matches[-1][0]  # 修改这里以获取正确的匹配组
        return last_match
    else:
        return "未找到指定内容"

def text_to_image(text, output_path, font_path='C:\\Windows\\Fonts\\Consola.ttf', font_size=12):
    # 根据文本长度和字体大小估算所需的图像尺寸
    lines = text.split('\n')
    max_line_length = max(len(line) for line in lines)
    image_width = max_line_length * font_size
    image_height = len(lines) * font_size * 1  # 为行间距留出空间
    
    image = Image.new('RGB', (int(image_width), int(image_height)), color = (0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    
    y_text = 0
    for line in lines:
        draw.text((0, y_text), line, font=font, fill=(255, 255, 255))
        y_text += font_size * 1  # 更新下一行的y坐标
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)

file_path = os.path.join('results', 'April_11', 'OAK-170_esu_drv.txt')
captured_text = capture_text_from_end(file_path)

# 构造输出图片的路径
base_name = os.path.basename(file_path)
output_dir = os.path.join(os.getcwd(), 'pics')
output_file_name = os.path.splitext(base_name)[0] + '.png'
output_path = os.path.join(output_dir, output_file_name)

text_to_image(captured_text, output_path)

print(f'图片已保存至: {output_path}')