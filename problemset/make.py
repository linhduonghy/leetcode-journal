import sys
import os

if __name__ == "__main__":
    name = sys.argv[1]
    arr = name.split(" ")
    arr = [s.replace(".", "") for s in arr]
    dir = "_".join(arr)
    print(dir)
    os.mkdir(dir)
    file_path = os.path.join(dir, "sol.py")
    if not os.path.exists(file_path):
        with open(file_path, "w"): pass