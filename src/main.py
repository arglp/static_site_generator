import os
import shutil
from generate_page import generate_page, generate_pages_recursive

def copy_src_dir(src_dir, dst_dir):
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)
    os.mkdir(dst_dir)
    src_objects = os.listdir(src_dir)
    for object in src_objects:
        src_path = os.path.join(src_dir, object)
        dst_path = os.path.join(dst_dir, object)
        if os.path.isfile(src_path):
            print(f"copying: {src_path}")
            shutil.copy(src_path, dst_path)
        if os.path.isdir(src_path):
            print(f"copying: {src_path}")
            copy_src_dir(src_path, dst_path)        
        
def main():
    copy_src_dir("static", "public")
    generate_pages_recursive("content", "template.html", "public")

    

if __name__ == "__main__":
    main()


