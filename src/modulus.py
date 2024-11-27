# STD modules
import argparse
import os

# Personal modules
import my_logger
import my_shell
import core


def main():
    base_path = "packages"
    cmake_version = "3.15.0"

    print(my_shell.find_github_link(base_path, args.package))

    my_shell.is_connected()
    my_shell.check_minimum_cmake_version(cmake_version)
    core.check_if_in_archive(base_path, args.package)

    if my_shell.is_admin():
        core.install_package(
            base_path, args.package, args.version, args.install, args.jobs
        )
    else:
        my_logger.logger.error("admin privileges are required to install packages.")


if __name__ == "__main__":
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
    parser.add_argument(
        "-j",
        "--jobs",
        help="Maximum number of jobs to build in parallel.",
        type=str,
        default="max",
    )
    args = parser.parse_args()

    main()
