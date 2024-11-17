import argparse
import os
import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s]: %(message)s",
)

logger = logging.getLogger(__name__)

def main():
    base_path = "packages"
    
    if not os.path.isdir(f"{base_path}/{args.package}"):
        logger.error(f"\"{args.package}\" package is not in the archive. Please visit https://github.com/JustWhit3/modulus/tree/main/packages for a list of the available packages.")
        return
    
    configure = ["cmake", "-B", "build"]
    build = ["cmake", "--build", "build"]
    clean = ["rm", "--rf", "build"]
    
    for package in os.listdir(base_path):
        if package == args.package:
            for version in os.listdir(f"{base_path}/{package}"):
                if version == args.version:
                    subprocess.run(configure, check=True, cwd=f"{base_path}/{package}/{version}")
                    subprocess.run(build, check=True, cwd=f"{base_path}/{package}/{version}")
                    subprocess.run(configure, check=True, cwd=f"{base_path}/{package}/{version}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modulus is an open-source package manager for C++ libraries.")
    parser.add_argument("-p", "--package", help="The package name to be installed.", type=str, default="None")
    parser.add_argument("-v", "--version", help="The package version to be installed.", type=str, default="0.0.0")
    args = parser.parse_args()
    
    main()
    