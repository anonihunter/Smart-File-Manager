import sys
import logging
from config import config
from logger import logger
from stats import print_report
from organize import classify_file
from duplicates import duplicateFile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


logger = logging.getLogger(__name__)

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    path = config["default_directory"]

classify_file(path)
duplicateFile(path)


class fileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            logger.info(f"New File Detected: {event.src_path}")
            classify_file(path)


if __name__ == '__main__':
    event_handler = fileHandler()
    observer = Observer()

    observer.schedule(
        event_handler,
        path,
        recursive=config["monitoring"]["recursive"]
    )

    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)

    finally:
        observer.stop()
        observer.join()
        print_report()