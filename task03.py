import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(path, indent=""):
    path = Path(path)
    
    if not path.exists():
        print(Fore.RED + f"Error: Path '{path}' does not exist.")
        return
    
    if not path.is_dir():
        print(Fore.RED + f"Error: Path '{path}' is not a directory.")
        return

    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + indent + "📂 " + item.name)
            print_directory_structure(item, indent + " ┃ ")
        else:
            print(Fore.GREEN + indent + "📜 " + item.name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python task03.py <path_to_directory>")
    else:
        directory_path = sys.argv[1]
        print_directory_structure(directory_path)
