import os
import threading
from tkinter import Tk, Label, Entry, Button, messagebox, ttk
from pytube import YouTube

# Function to download the video
def download_video():
    # Disable the download button to prevent multiple downloads
    download_button.config(state='disabled')

    def download():
        try:
            url = YouTube(str(link.get()))
            video = url.streams.get_highest_resolution()
            video.download(targetdir)
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            # Re-enable the download button after download completes or fails
            download_button.config(state='normal')

    # Start the download process in a separate thread
    threading.Thread(target=download).start()

# GUI setup
root = Tk()
root.title("YouTube Video Downloader")

# Font settings
tfont = ("Verdana", 12)

# Default directory for download
userdir = os.path.join(os.path.join(os.environ['USERPROFILE']))
targetdir = os.path.join(userdir, 'Desktop')

# Video link input
Label(root, text="Video Link:", font=tfont).grid(row=0, column=0, padx=10, pady=10)
link = Entry(root, width=40, font=tfont)
link.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

# Download button
download_button = Button(root, text="Download", font=tfont, command=download_video)
download_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Progress bar
progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=300)
progress_bar.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Function to update progress bar
def update_progress(stream, chunk, bytes_remaining):
    progress = (float(bytes_remaining) / float(stream.filesize)) * 100
    progress_bar["value"] = 100 - progress

# Start the GUI
root.mainloop()
