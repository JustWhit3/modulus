import os
import ctypes


def is_admin():
    # Windows
    if os.name == "nt":
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    # Linux/MacOS
    elif os.name == "posix":
        return os.geteuid() == 0
    else:
        logger.error("unable to run Modulus, unsupported platform.")


def generate_cmakelists(template_path, output_path, version):
    with open(template_path, "r") as file:
        content = file.read()
    content = content.replace("@VERSION@", version)

    with open(output_path, "w") as file:
        file.write(content)
