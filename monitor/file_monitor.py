import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

MONITOR_PATH = "test_folder"

class FileMonitorHandler(FileSystemEventHandler):

def on_modified(self, event):
    print(f"[MODIFIED] {event.src_path}")

def on_created(self, event):
    print(f"[CREATED] {event.src_path}")

def on_deleted(self, event):
    print(f"[DELETED] {event.src_path}")

def start_monitoring():
event_handler = FileMonitorHandler()
observer = Observer()

observer.schedule(event_handler, MONITOR_PATH, recursive=True)
observer.start()

print(f"Monitoring started on: {MONITOR_PATH}")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
