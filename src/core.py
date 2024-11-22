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


def generate_template(path, version):
    my_logger.logger.info("creating CMakeLists.txt...")
    my_shell.generate_cmakelists(
        f"{path}/CMakeLists.txt.in",
        f"{path}/CMakeLists.txt",
        version,
    )


def configure_pkg(path):
    my_logger.logger.info("configuring...")
    subprocess.run(["cmake", "-B", "build"], check=True, cwd=path)


def build_pkg(path):
    my_logger.logger.info("building...")
    subprocess.run(["cmake", "--build", "build"], check=True, cwd=path)


def install_pkg(path, install):
    if install == "yes":
        my_logger.logger.info("installing...")
        subprocess.run(
            ["cmake", "--build", "build", "--target", "install"], check=True, cwd=path
        )


def clean_env(path):
    my_logger.logger.info("cleaning...")
    shutil.rmtree(f"{path}/build")
    my_logger.logger.info("process complete.")


def install_package(base_path, package, version, install):

    for pkg in os.listdir(base_path):
        if pkg == package:
            complete_path = f"{base_path}/{pkg}"
            generate_template(complete_path, version)
            configure_pkg(complete_path)

            is_installed = is_package_installed(complete_path)
            if not is_installed:
                build_pkg(complete_path)
                install_pkg(complete_path, install)
            else:
                my_logger.logger.info("Package is already installed. Skipping.")

            clean_env(complete_path)
