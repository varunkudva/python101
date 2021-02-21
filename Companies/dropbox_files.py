
import os

def find_duplicates(base_path):

    def dfs_paths(path):
        if is_file(path):
            path.get_size()
            size_map[size].append(path)
        else:
            for child in path.list_dir():
                dfs(child)
