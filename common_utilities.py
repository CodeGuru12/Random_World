import os
import errno
from pathlib import Path

class struct:
    def __init__(self, **kargs):
        self.__dict__.update(**kargs)


def get_file_path(file_directory):
    '''
    get_file_path 
    Description: Get absolute file path from current working directory, it will 
                 raise a FileNotFoundError exception if the file doesn't exist

    Inputs: file_directory- filepath from running directory

    
    Outputs: Absolute path to file

    run_directory - Is the current run path, while file_directory is the file path
    below the current root directory.
    '''
    run_directory = os.path.dirname(__file__)
    file_path = Path(run_directory + file_directory)

    if (not os.path.isfile(file_path) ):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),file_path)

    return str(file_path)



if (__name__ == '__main__'):
    path = get_file_path('/Assets/Sprites/Walk_sprite_sheet.png')

    print(path)