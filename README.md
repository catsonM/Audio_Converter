Audio Converter Application

Author: Catoglu

Overview
This is a user-friendly audio converter application for macOS, built using Python and Tkinter. The application allows users to convert multiple audio files into various formats and select the desired bitrate. It includes several features for easy path selection and error handling.

Features
Multiple File Selection: Select multiple audio files for batch conversion.
Format and Bitrate Selection: Convert files to MP3, WAV, AAC, FLAC, OGG, and AIFF formats with customizable bitrates.
Output Path Selection: Specify the directory for saving converted files.
Subfolder Creation: Option to create a subfolder in the selected path for organizing converted files.
Error Logging: Logs errors during conversion to a .txt file in the specified path.
Help Section: Detailed instructions on using the application.
Requirements
Python 3.x
Tkinter
Pydub
Installation
Clone the repository:

bash
Kodu kopyala
git clone https://github.com/yourusername/audio-converter.git
cd audio-converter
Install the required packages:

bash
Kodu kopyala
pip install tk
pip install pydub
Run the application:

bash
Kodu kopyala
python audio_converter.py
Usage
Select Files: Click on the "Select Files" button to choose the audio files you want to convert.
Choose Format and Bitrate: Use the dropdown menus to select the desired format and bitrate for the conversion.
Specify Output Path: Click on the "Select Output Path" button to choose where the converted files will be saved.
Subfolder Option: Check the "Create subfolder" checkbox if you want the converted files to be saved in a subfolder.
Convert Files: Click on the "Convert" button to start the conversion process.
View Results: After the conversion is complete, a message will indicate whether the process was successful or if there were any errors.
Help Section
Click on the "Help" button for detailed instructions on using the application. This section includes information on file selection, format and bitrate options, output path selection, and error handling.
Error Handling
If any errors occur during the conversion process, they will be logged in an error_log.txt file in the specified output directory. Check this file for details on any conversion issues.
Contributions
Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

