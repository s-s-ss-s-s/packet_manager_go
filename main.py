import sys
from package import install_package, remove_package, update_cache

def main():
    if len(sys.argv) < 2:
        print("Usage: pkgmanager [command] [options]")
        return

    command = sys.argv[1]

    if command == "install":
        package_name = sys.argv[2]
        install_package(package_name)
    elif command == "remove":
        package_name = sys.argv[2]
        remove_package(package_name)
    elif command == "update":
        update_cache()
    else:
        print("Unknown command.")

if __name__ == "__main__":
    main()