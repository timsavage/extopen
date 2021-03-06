from setuptools import setup, find_packages

setup(
    name = 'extopen',
    version = '0.1.1',
    description = "Cross platform helper for opening a file with the default external application.",
    long_description = open('README.rst').read(),
    url='https://github.com/timsavage/extopen',
    author = 'Tim Savage',
    author_email = 'tim@savage.company',
    license = 'BSD',
    platforms = 'Posix; MacOS X; Windows',
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: BSD License',

        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    zip_safe = True,

    py_modules = ['extopen']
)
