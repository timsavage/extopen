import os
import subprocess
import sys


if sys.platform.startswith('darwin'):
    def _execute(path):
        subprocess.call(('open', path))

elif os.name == 'nt':
    def _execute(path):
        os.startfile(path)

elif os.name == 'posix':
    def _execute(path):
        subprocess.call(('xdg-open', path))

else:
    _execute = None


def is_supported():
    """
    The current OS is a supported by open with
    """
    return _execute is not None


def file(path):
    """
    Open a file in with the defualt application.

    :param path: Path of the file to open.

    """
    if _execute is None: 
        raise OSError("Open with is not supported on this OS")

    if os.path.isfile(path):
        _execute(path)
    else:
        raise IOError("File `{}` not found".format(path))


def directory(path):
    """
    Open a directory with the file browser.

    :param path: Path of the directory to open.

    """
    if _execute is None: 
        raise OSError("Open with is not supported on this OS")

    if os.path.isdir(path):
        _execute(path)
    else:
        raise IOError("Directory `{}` not found".format(path))

