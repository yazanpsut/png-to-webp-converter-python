import time
from pathlib import Path
from PIL import Image
import os


def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


if __name__ == '__main__':
    print("\033[95m##########          Welcome          ##########\033[0m")
    print("\033[94m##########   Png to Webp Converter   ##########\033[0m")
    print("\033[91m##########   Auther: Yazan Alhorani  ##########\033[0m")
    print('Enter directory of pngs to be converted to webp')
    dir_of_pngs = input()
    while not os.path.exists(dir_of_pngs):
        print('Please enter a valid full path:')
        dir_of_pngs = input()
    print('Enter compression rate (0-100):')
    compression = input()
    try:
        compression = int(compression)
    except ValueError:
        pass
    while type(compression) != int or compression < 0 or compression > 100:
        print('Please inter an integer from 0 to 100')
        compression = input()
        try:
            compression = int(compression)
        except ValueError:
            pass
    print('Enter size controller in kb (if image in path less than this size'
          ' it will keep the compression at 100, and 0 to ignore this option):')
    size_ctrl = input()
    try:
        size_ctrl = int(size_ctrl)
    except ValueError:
        pass
    while type(size_ctrl) != int or size_ctrl < 0:
        print('Please enter integer size 0 or above for the size controller:')
        size_ctrl = input()
        try:
            size_ctrl = int(size_ctrl)
        except ValueError:
            pass

    paths = Path(dir_of_pngs).glob("**/*.png")

    l = len([name for name in os.listdir(dir_of_pngs) if
             os.path.isfile(os.path.join(dir_of_pngs, name)) and name.endswith('.png')])
    print('Number of PNGs: ' + l)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=50)

    i = 0
    for source in paths:
        destination = source.with_suffix(".webp")
        size = os.stat(source.__str__()).st_size
        image = Image.open(source)  # Open image
        if size_ctrl == 0 or size > size_ctrl * 1024:
            image.save(destination, format="webp", optimize=True, quality=compression)  # Convert image to webp
        else:
            image.save(destination, format="webp", optimize=True, quality=100)  # Convert image to webp

        printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=50)
        i += 1
