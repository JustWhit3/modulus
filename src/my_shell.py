# STD modules
import os
import sys
import ctypes
import socket
import subprocess
import re

# Personal modules
import my_logger


def is_admin():
    # Windows
    if os.name == "nt":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            my_logger.logger.error("unable get user admin information.")
            sys.exit()

    # Linux/MacOS
    elif os.name == "posix":
        return os.geteuid() == 0
    else:
        my_logger.logger.error("unable to run Modulus, unsupported platform.")
        sys.exit()


def generate_cmakelists(template_path, output_path, version):
    with open(template_path, "r") as file:
        content = file.read()
    content = content.replace("@VERSION@", version)

    with open(output_path, "w") as file:
        file.write(content)


def is_connected():
    try:
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        return True
    except socket.error:
        my_logger.logger.error(
            "unable to run Modulus, there is no internet connection."
        )
        sys.exit()


def check_minimum_cmake_version(required):
    try:
        result = subprocess.run(
            ["cmake", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        output = result.stdout.strip()
        version_line = output.splitlines()[0]
        version = version_line.split()[2]
        if version < required:
            my_logger.logger.error(
                f"required CMake version is {required}, but you have CMake {version} installed. Please upgrade the package."
            )
            sys.exit()
    except (subprocess.CalledProcessError, IndexError, FileNotFoundError):
        my_logger.logger.error(
            "unable to get CMake version, check if CMake is installed."
        )
        sys.exit()


def find_github_link(base_path, package):
    cmake_file_path = f"{base_path}/{package}/CMakeLists.txt"
    try:
        with open(cmake_file_path, "r", encoding="utf-8") as file:
            content = file.read()

        match = re.search(r'https://github\.com/[^\s"]+', content)
        if match:
            return match.group(0)
        else:
            return None
    except FileNotFoundError:
        my_logger.logger.error(f"Unable to find file: {cmake_file_path}")
    except Exception as e:
        my_logger.logger.error(f"Error while reading file {cmake_file_path}: {e}")
    return None
