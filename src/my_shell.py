import os
import ctypes

def is_admin():
    # Windows
    if os.name == 'nt':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    # Linux/MacOS
    elif os.name == 'posix':
        return os.geteuid() == 0
    else:
        logger.error("unable to run Modulus, unsupported platform.")