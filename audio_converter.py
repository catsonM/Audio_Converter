import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pydub import AudioSegment
from pydub.utils import which

# Manually set the paths for ffmpeg and ffprobe
ffmpeg_path = "/opt/homebrew/bin/ffmpeg"
ffprobe_path = "/opt/homebrew/bin/ffprobe"

# Add ffmpeg and ffprobe to the system path
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)
os.environ["PATH"] += os.pathsep + os.path.dirname(ffprobe_path)

AudioSegment.converter = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

# Function to display the help window with usage instructions
def show_help():
    help_window = tk.Toplevel(root)
    help_window.title("Help")

    help_text = (
        "Author: Catoglu\n\n"
        "Welcome! This application allows you to easily convert your audio files. "
        "Here are some basic steps and features:\n\n"
        "1. File Selection: You can select a single file or multiple files.\n\n"
        "2. Conversion Format and Bitrate Selection: Use the respective menus to select the format and bitrate you want to convert to.\n\n"
        "3. Specify File Path: You can choose the path where the conversion will take place.\n\n"
        "4. Conversion Process: After selecting the files and settings, start the conversion process.\n\n"
        "5. Error Handling: If any errors occur during the conversion process, error logs are stored in the specified path.\n\n"
    )

    help_label = tk.Label(help_window, text=help_text, justify="left", padx=10, pady=10)
    close_button = tk.Button(help_window, text="Close", command=help_window.destroy)
    
    help_label.pack()
    close_button.pack()

# Function to allow users to select files for conversion
def select_files():
    global files
    files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav *.aac *.flac *.ogg *.aiff")])
    if files:
        file_label.config(text=f"{len(files)} files selected.")
        file_listbox.delete(0, tk.END)
        for file in files:
            file_listbox.insert(tk.END, file)

# Function to set the output path based on selected file
def set_output_path_from_file(event):
    selected_file = file_listbox.get(tk.ANCHOR)
    if selected_file:
        parent_dir = os.path.dirname(selected_file)
        path_var.set(parent_dir)

# Function to update bitrate options based on selected format
def update_bitrate_options(event):
    format_selected = format_var.get()
    if format_selected == "mp3":
        bitrate_menu.config(values=["96k", "128k", "192k", "256k", "320k"], state='readonly')
        bitrate_var.set("320k")  # Default bitrate for mp3
    elif format_selected == "wav":
        bitrate_menu.config(values=["16-bit", "24-bit", "32-bit"], state='readonly')
    elif format_selected == "aac":
        bitrate_menu.config(values=["96k", "128k", "192k", "256k", "320k"], state='readonly')
    elif format_selected == "flac":
        bitrate_menu.config(values=["16-bit", "24-bit", "32-bit"], state='readonly')
    elif format_selected == "ogg":
        bitrate_menu.config(values=["96k", "128k", "192k", "256k", "320k"], state='readonly')
    elif format_selected == "aiff":
        bitrate_menu.config(values=["16-bit", "24-bit", "32-bit"], state='readonly')
    else:
        bitrate_menu.config(values=["96k", "128k", "192k", "256k", "320k"], state='readonly')  # Default values
        bitrate_var.set(bitrate_menu.cget('values')[0])

# Function to handle the conversion of selected files
def convert_files():
    global files
    if not files:
        messagebox.showwarning("Warning", "Please select files to convert.")
        return
    
    target_format = format_var.get()
    bitrate = bitrate_var.get()
    output_dir = path_var.get() or os.path.join(os.path.expanduser("~"), "Desktop", "Converted_Audios")

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a subfolder if the checkbox is checked
    if subfolder_var.get():
        output_dir = os.path.join(output_dir, "Converted_Audios")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
    
    error_log = []
    for file in files:
        try:
            # Load the audio file
            audio = AudioSegment.from_file(file)
            output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(file))[0] + "." + target_format)
            # Export the file in the desired format and bitrate
            audio.export(output_file, format=target_format, bitrate=bitrate)
        except Exception as e:
            # Log any errors that occur during conversion
            error_log.append(f"Error converting {file}: {str(e)}")
    
    # If there are errors, write them to a log file
    if error_log:
        error_log_path = os.path.join(output_dir, "error_log.txt")
        with open(error_log_path, "w") as f:
            for error in error_log:
                f.write(error + "\n")
        messagebox.showwarning("Completed", "Conversion completed with errors. Check error_log.txt for details.")
    else:
        messagebox.showinfo("Completed", "All files were converted successfully.")

# Main window setup
root = tk.Tk()
root.title("Audio Converter")

# Calculate window position to center on the screen
window_width = 500
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Frame for all widgets to manage spacing
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Title label
title_label = tk.Label(main_frame, text="Audio Converter", font=("Helvetica", 16))
title_label.pack(pady=10)

# File selection button
file_button = tk.Button(main_frame, text="Select Files", command=select_files)
file_button.pack(pady=5)

# Label to show the number of selected files
file_label = tk.Label(main_frame, text="No files selected.")
file_label.pack(pady=5)

# Listbox to show selected files
file_listbox = tk.Listbox(main_frame, height=6, selectmode=tk.SINGLE, width=60)
file_listbox.pack(pady=5)
file_listbox.bind('<Double-1>', set_output_path_from_file)

# Frame for format and bitrate selection
options_frame = tk.Frame(main_frame)
options_frame.pack(pady=5)

format_label = tk.Label(options_frame, text="Conversion Format:")
format_label.grid(row=0, column=0, padx=5, pady=5, sticky='e')
format_var = tk.StringVar(value="mp3")
format_menu = ttk.Combobox(options_frame, textvariable=format_var, values=["mp3", "wav", "aac", "flac", "ogg", "aiff"], state='readonly', width=20)
format_menu.grid(row=0, column=1, padx=5, pady=5, sticky='w')
format_menu.bind("<<ComboboxSelected>>", update_bitrate_options)

bitrate_label = tk.Label(options_frame, text="Bitrate Selection:")
bitrate_label.grid(row=1, column=0, padx=5, pady=5, sticky='e')
bitrate_var = tk.StringVar(value="320k")  # Default bitrate for mp3
bitrate_menu = ttk.Combobox(options_frame, textvariable=bitrate_var, state='readonly', width=20)
bitrate_menu.grid(row=1, column=1, padx=5, pady=5, sticky='w')
update_bitrate_options(None)  # Initialize with default values

# Frame for path selection
path_frame = tk.Frame(main_frame)
path_frame.pack(pady=5)

path_button = tk.Button(path_frame, text="Select Output Path", command=lambda: path_var.set(filedialog.askdirectory()))
path_button.grid(row=0, column=0, padx=5, pady=5)
path_var = tk.StringVar()
path_entry = tk.Entry(path_frame, textvariable=path_var, state="readonly", width=45)
path_entry.grid(row=0, column=1, padx=5, pady=5)

# Checkbox to decide if a subfolder should be created
subfolder_var = tk.BooleanVar()
subfolder_check = tk.Checkbutton(main_frame, text="Create subfolder", variable=subfolder_var)
subfolder_check.pack(pady=5)

# Frame for Convert, Help and Close buttons
button_frame = tk.Frame(main_frame)
button_frame.pack(pady=10)

# Button to start the conversion process
convert_button = tk.Button(button_frame, text="Convert", command=convert_files)
convert_button.grid(row=0, column=0, padx=10)

# Button to show help
help_button = tk.Button(button_frame, text="Help", command=show_help)
help_button.grid(row=0, column=1, padx=10)

# Close button to exit the application
close_button = tk.Button(button_frame, text="Close", command=root.quit)
close_button.grid(row=0, column=2, padx=10)

# Run the application
root.mainloop()
