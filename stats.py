import time

start_time = time.time()

stats = {
    "files_scanned": 0,
    "files_organized": 0,
    "duplicate_files": 0,
    "files_skipped": 0,
    "folders_created": 0,
    "errors": 0,

    "category": {
        "Docs": 0,
        "Images": 0,
        "Videos": 0,
        "Audio": 0,
        "Zip File": 0,
        "Others": 0
    }
}


def print_report():
    runtime = time.time() - start_time

    print("\n=========================================")
    print("      SMART FILE MANAGER REPORT")
    print("=========================================\n")

    print(f"Files Scanned        : {stats['files_scanned']}")
    print(f"Files Organized      : {stats['files_organized']}")
    print(f"Duplicate Files      : {stats['duplicate_files']}")
    print(f"Files Skipped        : {stats['files_skipped']}")
    print(f"Folders Created      : {stats['folders_created']}")
    print(f"Errors               : {stats['errors']}")

    print("\nCategory Summary")
    print("----------------")

    for key, value in stats["category"].items():
        print(f"{key:<20}: {value}")

    print(f"\nProgram Runtime      : {runtime:.2f} seconds")

    print("\n=========================================")