import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/danna/Downloads"
to_dir = "/Users/danna/Documents/Documents/Danna"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"¡Oye, {event.src_path} ha sido creado!")
    
    def on_deleted(self, event):
        print(f"¡Lo siento! ¡Alguien borró {event.src_path}!")
    
    def on_modified(self, event):
        print(f"¡{event.src_path} ha sido modificado!")
    
    def on_moved(self, event):
        print(f"¡Han movido o cambiado de nombre a {event.src_path}!")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("Ejecutando...")
except KeyboardInterrupt:
    print("¡Detenido!")
    observer.stop()