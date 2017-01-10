"""
#######
Extopen
#######

Provides a cross platform set of tools for opening files externally with the default registered application for
the current operating system.

The currently supported operating systems are Windows NT (eg NT, XP onwards), OSX, Linux.

Please report any bugs/submit patches to: https://github.com/timsavage/extopen/

Usage:

    >>> import extopen
    >>> extopen.is_supported()
    True
    >>> extopen.file("/path/to/my/file")
    >>> extopen.directory("/home/")
    
"""
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
    :raises OSError: If extfile is not supported on this OS.
    :raises IOError: If file is not found (or is a directory)

    """
    if _execute is None: 
        raise OSError("Open with is not supported on this OS")

    if os.path.isfile(path):
        _execute(path)
    else:
        raise IOError("File `{}` not found or is a directory.".format(path))


def directory(path):
    """
    Open a directory with the file browser.

    :param path: Path of the directory to open.
    :raises OSError: If extfile is not supported on this OS.
    :raises IOError: If directory is not found (or is a file)

    """
    if _execute is None: 
        raise OSError("Open with is not supported on this OS")

    if os.path.isdir(path):
        _execute(path)
    else:
        raise IOError("Directory `{}` not found of is a file.".format(path))

