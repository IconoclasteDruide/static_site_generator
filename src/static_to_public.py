import os
from shutil import copy, rmtree

def static_to_public(source_dir, dest_dir):
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir, 0o755)
    old_dest = os.listdir(dest_dir)
    print(old_dest)
    if len(old_dest):
        for path in old_dest:
            full_path = os.path.join(dest_dir, path)
            if os.path.isfile(full_path):
                os.remove(full_path)
            elif os.path.isdir(full_path):
                rmtree(full_path)
    source_files = os.listdir(source_dir)
    for path in source_files:
        if path.startswith("."):
            continue
        full_path = os.path.join(source_dir, path)
        if os.path.isfile(full_path):
            print(copy(full_path, os.path.join(dest_dir, path)))
        elif os.path.isdir(full_path):
            new_dest_dir = os.path.join(dest_dir, path)
            os.mkdir(new_dest_dir)
            static_to_public(full_path, new_dest_dir)
        # else:
        #     print('fail')