import os
import errno


class struct:
    def __init__(self, **kargs):
        self.__dict__.update(**kargs)
        

def get_file_path(file_directory, fileName):
    '''
    get_file_path 
    Description: Get absolute file path from current working directory, it will 
                 raise a FileNotFoundError exception if the file doesn't exist

    Inputs: file_directory- Folder from current directory
            fileName - name of file to get path of
    
    Outputs: Absolute path to file

    run_directory - Is the current run path, while file_directory is the file path
    below the current root directory.
    '''
    run_directory = os.path.dirname(os.getcwd())
    file_path = os.path.join(run_directory, file_directory,fileName)

    if (not os.path.isfile(file_path)):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),file_path)

    return file_path

