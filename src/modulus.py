# STD modules
import argparse
import os
import subprocess
import shutil

# Personal modules
from logger import logger
from shell import is_admin

def main():
    # Basic declarations
    base_path = "packages"
    configure = ["cmake", "-B", "build"]
    build = ["cmake", "--build", "build"]
    install = ["cmake", "--build", "build", "--target", "install"]
    
    # Check if C++ library is in the archive
    if not os.path.isdir(f"{base_path}/{args.package}"):
        logger.error(f"\"{args.package}\" package is not in the archive. Please visit https://github.com/JustWhit3/modulus/tree/main/packages for a list of the available packages.")
        return
    
    # Install the library
    if is_admin():
        for package in os.listdir(base_path):
            if package == args.package:
                for version in os.listdir(f"{base_path}/{package}"):
                    if version == args.version:
                        complete_path = f"{base_path}/{package}/{version}"

                        res = subprocess.run(configure, check=True, cwd=complete_path, text=True, capture_output=True)
                        if not "is already installed" in res.stdout and not "is already installed" in res.stderr:
                            print(res.stdout)
                            subprocess.run(build, check=True, cwd=complete_path)
                            subprocess.run(install, check=True, cwd=complete_path)
                        else:
                            logger.info(f"package \"{package}\" with version \"{version}\" is already installed.")
                        shutil.rmtree(f"{complete_path}/build")
    else:
        logger.error("admin privileges are required to install packages.")


if __name__ == "__main__":
    # Parser settings
    parser = argparse.ArgumentParser(description="Modulus is an open-source package manager for C++ libraries.")
    parser.add_argument("-p", "--package", help="The package name to be installed.", type=str, default="None")
    parser.add_argument("-v", "--version", help="The package version to be installed.", type=str, default="0.0.0")
    args = parser.parse_args()
    
    # Main code
    main()
    