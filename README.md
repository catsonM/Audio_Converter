# Audio Converter Usage Guide

## Running the Application

To run the application, navigate to the directory containing `audio_converter.py` and execute the following command:

```
python audio_converter.py

```

Using the Audio Converter

1. Select Files
Click on the Select Files button to choose the audio files you want to convert. You can select multiple files.

2. Choose Conversion Format and Bitrate
Use the dropdown menus to select the desired conversion format and bitrate for your audio files.

Conversion Format: Choose from MP3, WAV, AAC, FLAC, OGG, or AIFF.
Bitrate Selection: Choose from various bitrates specific to the selected format.
3. Select Output Path
Click on the Select Output Path button to specify the directory where the converted files will be saved.

4. Create Subfolder (Optional)
Check the Create subfolder option if you want the converted files to be saved in a subfolder within the specified output path.

5. Convert
Click the Convert button to start the conversion process. Once the conversion is complete, you will receive a success message. If there are any errors, an error log will be created in the specified output path.

6. Help
Click the Help button for in-app instructions on how to use the application.

Exiting the Application
Click the Close button to exit the application.

Build the Executable
Run PyInstaller:

Navigate to the directory containing audio_converter.py and run the following command:

pyinstaller --onefile --windowed --icon=audio_converter.ico audio_converter.py

--onefile: This option packages the application into a single executable file.
--windowed: This option prevents a terminal window from appearing when the application is run.
--icon=audio_converter.ico: This option sets the icon for the executable file.
Locate the Executable
After running the PyInstaller command, the executable file will be created in the dist directory. You can distribute this executable file as needed.
