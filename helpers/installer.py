import subprocess

def install_software(package):
    try:
        subprocess.check_call(['pip', 'install', package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")