# -*- coding: utf-8 -*-

# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'includes': 'atexit',
        'include_files': ['video icon.ico']
    }
}

executables = [
    Executable('video join tool.py', base=base, icon = 'video icon.ico')
]

setup(name='video join tool',
      version='1.0.0',
      author = "Knight Chan",
      description=u'目前在各大视频网站上下到的一个视频都被拆分为多段视频，本工具针对这种情况能非常快速的将这些分段视频拼接起来。本工具仅针对上面的情况且只支持mp4和flv两种格式。',
      options=options,
      executables=executables
      )
