import os
import shutil

source_dir = input("Enter the source directory path: ") 
dest_dir = input("Enter the destination directory path: ")

extensions = (".jpg", ".png", ".jpeg", ".pdf", ".mp3", ".mp4", ".wav")

for filename in os.listdir(source_dir):
    if any(filename.endswith(ext) for ext in extensions):
        shutil.move(os.path.join(source_dir, filename), dest_dir)