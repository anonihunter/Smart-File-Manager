# Smart File Organizer

A Python project that automatically organizes files into categorized folders, detects duplicate files, and monitors folders in real time.

## Features

- Organizes files based on their extensions.
- Supports Documents, Images, Videos, Audio, and Archive files.
- Automatically creates destination folders if they don't exist.
- Detects duplicate files using file hashing.
- Monitors a folder in real time and automatically organizes newly added files.
- Built using Python's `pathlib`, `shutil`, `hashlib`, and `watchdog` modules.

## Project Structure

- ✅ Phase 1: File Organization
- ✅ Phase 2: Duplicate File Detection
- ✅ Phase 3: Real-Time Folder Monitoring
- ⏳ Phase 4: Logging
- ⏳ Phase 5: Statistics
- ⏳ Phase 6: Configuration File
- ⏳ Phase 7: GUI

## Technologies Used

- Python
- pathlib
- shutil
- hashlib
- watchdog

## How to Run

1. Clone the repository.
2. Install the required dependencies.
3. Update the target directory path in the script.
4. Run the Python file.

## Future Improvements

- Activity logging
- Project statistics dashboard
- Configuration file (JSON)
- GUI interface
- Undo last organization operation

## Learning Outcomes

This project helped me practice:

- File handling in Python
- Directory and path management using `pathlib`
- File operations using `shutil`
- Hashing for duplicate file detection
- Real-time file system monitoring
- Writing modular and maintainable Python code