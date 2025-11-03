# Launcher

import subprocess
import sys

def main():
    print("\nAssignment 2")
    print("\n1. Registration (MVC)")
    print("2. Invoice (Layered)")
    print("3. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == "1":
        subprocess.run([sys.executable, "Student Course Registration System.py"])
    elif choice == "2":
        subprocess.run([sys.executable, "Invoice Processing System.py"])
    elif choice == "3":
        exit()
    else:
        print("Invalid")

if __name__ == "__main__":
    main()
