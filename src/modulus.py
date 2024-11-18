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
    if not os.path.isdir(f"{base_path}/{args.package}/{args.version}"):
        logger.error(
            f'"{args.package}" package v{args.version} is not in the archive. Please visit https://github.com/JustWhit3/modulus/tree/main/packages for a list of the available packages and send a PR if you want.'
        )
        return

    # Install the library
    if is_admin():
        for package in os.listdir(base_path):
            if package == args.package:
                for version in os.listdir(f"{base_path}/{package}"):
                    if version == args.version:
                        complete_path = f"{base_path}/{package}/{version}"
                        logger.info("configuring...")
                        subprocess.run(configure, check=True, cwd=complete_path)

                        logger.info("building...")
                        subprocess.run(build, check=True, cwd=complete_path)

                        if args.install == "yes":
                            logger.info("installing...")
                            subprocess.run(install, check=True, cwd=complete_path)

                        # logger.info(
                        #     f'package "{package}" with version "{version}" is already installed.'
                        # )
                        logger.info("cleaning...")
                        shutil.rmtree(f"{complete_path}/build")
                        logger.info("process complete.")
    else:
        logger.error("admin privileges are required to install packages.")


if __name__ == "__main__":
    # Parser settings
    parser = argparse.ArgumentParser(
        description="Modulus is an open-source package manager for C++ libraries."
    )
    parser.add_argument(
        "-p",
        "--package",
        help="The package name to be installed.",
        type=str,
        default="None",
    )
    parser.add_argument(
        "-v",
        "--version",
        help="The package version to be installed.",
        type=str,
        default="0.0.0",
    )
    parser.add_argument(
        "-i",
        "--install",
        help="Choose if installing or not.",
        type=str,
        default="yes",
    )
    args = parser.parse_args()

    # Main code
    main()
