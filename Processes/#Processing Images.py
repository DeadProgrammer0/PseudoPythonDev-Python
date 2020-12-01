import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = [f'{i}.jpg' for i in range(1,6)]


size = (1200, 1200)


def process_image(img_name):
# for img_name in img_names:
    img = Image.open(f'Download/{img_name}')

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'Processed/{img_name}')
    print(f'{img_name} was processed...')


if __name__ == "__main__":
    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)


    end = time.perf_counter()

    print(f'Finished in {end-start} seconds')   