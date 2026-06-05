import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class ReloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.process = None
        self.start_app()

    def start_app(self):
        if self.process:
            self.process.kill()

        print("🚀 Starting app...")
        self.process = subprocess.Popen(["python", "main.py"])

    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            print("🔁 Change detected, restarting...")
            self.start_app()


if __name__ == "__main__":
    event_handler = ReloadHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()