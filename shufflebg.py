from PIL import Image
import numpy, random
from save import save

def generate_bg(input_image):
    array_image = numpy.array(input_image)

    random.shuffle(array_image)
    for i in range(len(array_image)):
        random.shuffle(array_image[i])
        for j in range(len(array_image[i])):
            random.shuffle(array_image[i][j])

    bg = Image.fromarray(array_image)

    return bg
    
def generate_img(name_image, number_image, extension):
    image = Image.open(f'./input/{name_image}')
    bg_pxl = image.getpixel((0, 0))

    bg = generate_bg(image)

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.getpixel((x, y)) == bg_pxl:
                image.putpixel((x, y), bg.getpixel((x, y)))
        
    return save(image, 'metadata', f'image_{number_image}', extension)

def generate_gif(name_image, extension='png', fps=30):
    images = []
    for i in range(fps):
        generate_img(name_image, f'{i:0>3}', extension)
        images.append(Image.open(f'./metadata/image_{i:0>3}.{extension}'))
        
    save(images, 'output', 'shuffle', 'gif', images=images)

def main():
    name_image = 'test1.png'
    generate_gif(name_image)

main()