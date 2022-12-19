from pathlib import Path
from PIL import Image
import os

if __name__ == '__main__':
    print('Enter directory of pngs to be converted to webp')
    dir_of_pngs = input()
    while not os.path.exists(dir_of_pngs):
        print('Please enter a valid full path:')
        dir_of_pngs = input()
    print('Enter compression rate (0-100):')
    compression = input()
    while type(compression) != int or compression < 0 or compression > 100:
        print('Please inter an integer from 0 to 100')
        compression = input()
    print('Enter size controller in kb (if image in path less than this size'
          ' it will keep the compression at 100, and 0 to ignore this option):')
    size_ctrl = input()
    while type(size_ctrl) != int or size_ctrl < 0:
        print('Please enter integer size 0 or above for the size controller:')
        size_ctrl = input()

    paths = Path(dir_of_pngs).glob("**/*.png")

    for source in paths:
        destination = source.with_suffix(".webp")
        size = os.stat(source.__str__()).st_size
        image = Image.open(source)  # Open image
        if size_ctrl == 0 or size > size_ctrl * 1024:
            image.save(destination, format="webp", optimize=True, quality=compression)  # Convert image to webp
        else:
            image.save(destination, format="webp", optimize=True, quality=100)  # Convert image to webp
