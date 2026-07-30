# Smart File Organizer

A modular Python command-line application that automatically organizes files, detects duplicates, monitors folders in real time, maintains activity logs, generates execution statistics, and supports configuration through a JSON file.

## Features

* 📂 Automatically organizes files based on their extensions.
* 🖼️ Supports Documents, Images, Videos, Audio, Archives, and other file categories.
* 📁 Creates destination folders automatically when needed.
* 🔍 Detects duplicate files using file hashing.
* 👀 Monitors folders in real time and organizes newly added files automatically.
* 📝 Records application activities using Python's logging module.
* 📊 Generates execution statistics after each run.
* ⚙️ Uses a JSON configuration file for customizable behavior.
* 🧩 Modular project structure for improved readability and maintainability.

---

## Project Structure

```
Smart-File-Organizer/
│
├── main.py
├── organizer.py
├── duplicates.py
├── monitor.py
├── logger.py
├── statistics.py
├── config.py
├── config.json
├── requirements.txt
├── README.md
└── logs/
```

---

## Completed Phases

* ✅ Phase 1 – File Organization
* ✅ Phase 2 – Duplicate File Detection
* ✅ Phase 3 – Real-Time Folder Monitoring
* ✅ Phase 4 – Activity Logging
* ✅ Phase 4.5 – Modular Refactoring
* ✅ Phase 5 – Statistics Dashboard
* ✅ Phase 6 – Configuration System

---

## Technologies Used

* Python
* pathlib
* shutil
* hashlib
* watchdog
* logging
* json

---

## How to Run

1. Clone the repository.
2. Install the required dependencies.
3. Configure the application using `config.json`.
4. Run the application.

---

## What I Learned

This project helped me practice:

* File and directory handling
* Modern path management with `pathlib`
* File operations using `shutil`
* Hashing for duplicate detection
* Real-time file system monitoring
* Application logging
* JSON configuration management
* Modular software design
* Refactoring existing code
* Debugging and problem solving

---

## Future Improvements

* Undo last organization operation
* Export reports in CSV or PDF
* Scheduled automatic organization
* Unit tests
* Cross-platform packaging

---

## License

This project is open source and available under the MIT License.
