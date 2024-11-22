# STD modules
import argparse
import os

# Personal modules
import my_logger
import my_shell
import core


def main():
    # Basic declarations
    base_path = "packages"

    # Check if C++ library is in the archive
    core.check_if_in_archive(base_path, args.package, args.version)

    # Install the library
    if my_shell.is_admin():
        core.install_package(base_path, args.package, args.version, args.install)
    else:
        my_logger.logger.error("admin privileges are required to install packages.")


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
