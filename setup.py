from setuptools import setup

# Define the main script and options for py2app
APP = ['audio_converter.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'path/to/your/icon/symb.icns',  # Path to your .icns icon file
    'packages': ['pydub'],
}

# Setup configuration
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
