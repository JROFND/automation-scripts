import os
import sys
from pathlib import Path

# Keywords to identify conda-related files/folders
KEYWORDS = ["conda", "anaconda", "miniconda", "miniforge", ".condarc"]

# Where to search (adjust if needed)
if sys.platform.startswith("win"):
    SEARCH_ROOTS = ["C:\\Users", "C:\\ProgramData"]
else:
    SEARCH_ROOTS = [str(Path.home()), "/opt", "/usr/local"]

results = []

def is_conda_related(path):
    path_lower = str(path).lower()
    return any(keyword in path_lower for keyword in KEYWORDS)

def scan_directory(root):
    for dirpath, dirnames, filenames in os.walk(root, topdown=True):
        try:
            # Check directories
            for d in dirnames:
                full_path = os.path.join(dirpath, d)
                if is_conda_related(full_path):
                    results.append(full_path)

            # Check files
            for f in filenames:
                full_path = os.path.join(dirpath, f)
                if is_conda_related(full_path):
                    results.append(full_path)

        except (PermissionError, OSError):
            continue

def main():
    print("🔍 Scanning for Conda-related files...\n")

    for root in SEARCH_ROOTS:
        print(f"Scanning: {root}")
        if os.path.exists(root):
            scan_directory(root)

    unique_results = sorted(set(results))

    print("\n✅ Scan complete.")
    print(f"Found {len(unique_results)} conda-related items.\n")

    # Output results
    for item in unique_results:
        print(item)

    # Save to file
    output_file = "conda_inventory.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        for item in unique_results:
            f.write(item + "\n")

    print(f"\n📄 Results saved to: {output_file}")

if __name__ == "__main__":
    main()
