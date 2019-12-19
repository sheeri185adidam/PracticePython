import os
import glob

if __name__ == '__main__':
    print(os.curdir)
    print(os.getcwd())
    print(glob.glob('*.py'))

    print([os.path.realpath(f) for f in glob.glob('*.py')])