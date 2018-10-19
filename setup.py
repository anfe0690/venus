from setuptools import setup, find_packages
import os
import sys


##------------------------------------------------------------------------------
##we don't need all the other platform specific files, so we remove them
#
##platform specific files
#platforms = ["venus/linux.py", "venus/windows.py", "venus/darwin.py"] 
#
#platform = sys.platform
#cwd = os.getcwd()
#
#for p in platforms:
#    if platform not in p:
#        if os.path.isfile(os.path.join(cwd, p)):
#            os.remove(os.path.join(cwd, p))
#
##------------------------------------------------------------------------------

platform = sys.platform
#os tools directory
platform_file = ''

if 'linux' in platform:
    platform_file = "os_tools/linux.py" 
elif 'windows' in platform:
    platform_file = "os_tools/windows.py" 
elif 'darwin' in platform:
    platform_file = "os_tools/darwin.py" 


setup(
    name='venus',
    version='0.0.1',
    author="Alfredo Sequeida",
    description="A cross platform tool for setting a random wallpaper image from unsplash.com",
    license="MIT",
    packages=['venus',],
    package_data={'venus': [platform_file]},
    install_requires=[
        'requests',
    ],
    entry_points={"console_scripts": ["venus = venus.venus:main"]},
)
