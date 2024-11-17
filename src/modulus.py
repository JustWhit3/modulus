import argparse

def main():
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modulus is an open-source package manager for C++ libraries.")
    parser.add_argument("-p", "--package", help="The package name to be installed.", type=str)
    # parser.add_argument("-w", "--where", help="The location of the package installation.", type=str)
    args = parser.parse_args()
    
    main()