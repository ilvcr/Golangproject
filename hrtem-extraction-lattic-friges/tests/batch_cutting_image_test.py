from PIL import Image
import os

# 定义待批量裁剪的图像地址
IMAGE_INPUT_PATH = '../app/static/data/raw_images'
# 定义裁剪后的图像存放地址
IMAGE_OUTPUT_PATH = '../app/static/data/crop_images'
# 定义左，上，右和下像素坐标
BOX_LEFT, BOX_UP, BOX_RIGHT, BOX_DOWN = 186, 186, 1350, 1330

for each_image in os.listdir(IMAGE_INPUT_PATH):
    # 每个图像全路径
    image_input_fullname = IMAGE_INPUT_PATH + '/' + each_image
    # PIL库打开每一张图
    img = Image.open(image_input_fullname)

    # 从此图像返回一个矩形区域。 盒子是一个4元组定义左，上，右和下像素坐标。
    box = (BOX_LEFT, BOX_UP, BOX_RIGHT, BOX_DOWN)
    # 进行ROI裁剪
    roi_area = img.crop(box)
    # 裁剪后每个图像全路径
    image_output_fullname = IMAGE_OUTPUT_PATH + '/' + each_image
    # 保存处理后的图像
    roi_area.save(image_output_fullname)
    print('{0} crop Done.'.format(each_image))
