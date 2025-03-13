import zipfile
import os
from manifest_read import read_manifest

def install_package(package_name):
    package_path = f'packages/{package_name}.zip'
    try:
        with zipfile.ZipFile(package_path, 'r') as zip_ref:
            zip_ref.extractall(f'packages/{package_name}')
            manifest = read_manifest(f'packages/{package_name}/manifest.hcl')
            print(f"Installed {manifest['name']}")
    except Exception as e:
        print(f"Error installing package: {e}")

def remove_package(package_name):
    package_dir = f'packages/{package_name}'
    if os.path.exists(package_dir):
        os.rmdir(package_dir)
        print(f"Removed package: {package_name}")
    else:
        print(f"Package not found: {package_name}")

def update_cache():
    print("Cache updated.")