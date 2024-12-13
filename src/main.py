import os
import shutil


current_path = os.getcwd()
def main():
    source_dir = "static"
    destination_dir = "public"
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)

if __name__ == "__main__":
    main()


