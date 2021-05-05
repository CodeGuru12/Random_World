import os
import errno
from pathlib import Path
import platform
import tkinter

def getOS():
    ''' Return operating system, windows, linux, darwin '''
    return platform.system().lower()

def convert_to_iso(cart_x,cart_y):
    '''
    Returns isometric coordinates from cartesian coordinates
    '''
    return (cart_x - cart_y), (cart_x + cart_y)/2


def getScreenResolution():
    """
    Workaround to get the size of the current screen in a multi-screen setup.

    Returns:
        geometry (str): The standard tkinter geometry string.
            [width]x[height]+[left]+[top]
    """
    root = tkinter.Tk()
    root.update_idletasks()
    root.attributes('-fullscreen', True)
    root.state('iconic')
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    return (screen_width,screen_height)

class Enum(tuple): 
    '''Allows enumerations to be defined as 
       options = Enum(['COLOR','NOCOLOR'])
       Acccessing enum: options.COLOR returns 0, options.NOCOLOR returns 1
     '''
    __getattr__ = tuple.index


class struct:
    ''' Class mimmicks c-style struct so variables can be grouped
        in the same data structure. There is sometimes a need to group similarly
        used variables together, but we don't need a full blown class with methods.
    '''
    def __init__(self, **kargs):
        self.__dict__.update(**kargs)

    def __setattr__(self, attribute, value):
        ''' Prevent attributes from being added after struct is created 
            This is not necessary, but without this method you are allowed
            to add attributes to an already created struct which is not 
            something we want.
        '''
        if (not attribute in self.__dict__):
            custom_msg = 'Attribute does not exist'
            raise AttributeError(errno.ENOENT, custom_msg,attribute)
        else:
            self.__dict__[attribute] = value


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
    file_path = Path(run_directory + '/' + file_directory)
    if (not os.path.isfile(file_path) ):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),file_path)

    return str(file_path)

def cartesian2iso(x,y):
    return (x - y), (x + y)/2



if (__name__ == '__main__'):

    path = get_file_path('/Assets/Sprites/Walk_sprite_sheet.png')

    print(path)