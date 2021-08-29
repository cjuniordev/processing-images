from PIL import Image
import numpy
import random
import os

def save(image, name, outdir):
    dirs = os.listdir()
    actual_dir = os.getcwd()

    dir_exists = False
    for i in range(len(dirs)):
        if dirs[i] == outdir:
            dir_exists = True

    if not dir_exists:
        os.mkdir(outdir)
    
    try:
        image.save(f'{actual_dir}/{outdir}/{name}.png')
        return True
    except:
        return False


def generate_bg(input_image):
    array_image = numpy.array(input_image)

    random.shuffle(array_image)
    for i in range(len(array_image)):
        random.shuffle(array_image[i])
        for j in range(len(array_image[i])):
            random.shuffle(array_image[i][j])

    bg = Image.fromarray(array_image)

    return save(bg, 'bg', 'metadata')
    
def generate_img(name_image):
    input_image = Image.open(f'./input/{name_image}')
    bg_pxl = input_image.getpixel((0, 0))

    if not generate_bg(input_image):
        print('Error!')
    
    bg_image = Image.open('./metadata/bg.png')
    for x in range(input_image.size[0]):
        for y in range(input_image.size[1]):
            if input_image.getpixel((x, y)) == bg_pxl:
                input_image.putpixel((x, y), bg_image.getpixel((x, y)))
        
    image_save = save(input_image, 'processed_image', 'output')
    if image_save: print('Sucess!')
    else: print('Error!')

def main():
    name_image = input('Type a image name in a `input` folder and her extension: ')
    generate_img(name_image)    

main()