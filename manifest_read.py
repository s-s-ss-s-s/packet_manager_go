import hcl

def read_manifest(file_path):
    with open(file_path, 'r') as file:
        data = hcl.load(file)
        return data