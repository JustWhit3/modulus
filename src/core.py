# STD modules
import os
import sys
import json
import subprocess
import shutil

# Personal modules
import my_logger
import my_shell


def check_if_in_archive(base_path, package):
    if not os.path.isdir(f"{base_path}/{package}"):
        my_logger.logger.error(
            f'"{package}" package is not in the archive. Please visit https://github.com/JustWhit3/modulus/tree/main/packages for a list of the available packages and send a PR if you want.'
        )
        sys.exit()


def is_package_installed(path):
    for filename in os.listdir(path):
        if filename.endswith(".json"):
            json_file_path = os.path.join(path, filename)
            try:
                with open(json_file_path, "r") as file:
                    data = json.load(file)
                    return data.get("found", "false").lower() == "true"
            except (json.JSONDecodeError, FileNotFoundError) as e:
                print(f"Error reading file {json_file_path}: {e}")
    return False


def install_package(base_path, package, version, install):
    configure = ["cmake", "-B", "build"]
    build = ["cmake", "--build", "build"]
    install = ["cmake", "--build", "build", "--target", "install"]

    for package in os.listdir(base_path):
        if package == package:
            complete_path = f"{base_path}/{package}"

            # Generate template file
            my_logger.logger.info("creating CMakeLists.txt...")
            my_shell.generate_cmakelists(
                f"{complete_path}/CMakeLists.txt.in",
                f"{complete_path}/CMakeLists.txt",
                version,
            )

            # Configure package
            my_logger.logger.info("configuring...")
            subprocess.run(configure, check=True, cwd=complete_path)

            # Check if already installed
            is_installed = is_package_installed(complete_path)
            if not is_installed:

                # Build package
                my_logger.logger.info("building...")
                subprocess.run(build, check=True, cwd=complete_path)

                # Install package
                if install == "yes":
                    my_logger.logger.info("installing...")
                    subprocess.run(install, check=True, cwd=complete_path)
            else:
                my_logger.logger.info("Package is already installed. Skipping.")

            # Remove build dir
            my_logger.logger.info("cleaning...")
            shutil.rmtree(f"{complete_path}/build")
            my_logger.logger.info("process complete.")
