import os

def save(image, outdir, name, extension, fps=30, images=[]):
    dirs = os.listdir()
    actual_dir = os.getcwd()
    dir_exists = False

    for i in range(len(dirs)):
        if dirs[i] == outdir:
            dir_exists = True

    if not dir_exists:
        os.mkdir(outdir)
    
    save_dir = f'{actual_dir}/{outdir}/{name}.{extension}'
    try:
        if extension == 'gif':
            images[0].save(
                save_dir,
                save_all=True,
                append_images=images[0:],
                optimize=False,
                duration=fps,
                loop=0
            )
        else:
            image.save(save_dir)
        return True
    except:
        return False