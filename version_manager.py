""" This script is for the version management. """

# Import modules
import subprocess
import shutil
import os
import sys
import toml

# Detect the installed packagemanager

def get_active_package_manager():
    """ Check the packagemanager of the project."""
    if os.path.exists("uv.lock"):
        return "uv"
    
    elif os.path.exists("pdm.lock"):
        return "pdm"
    
    else:
        return "pip"
    
# Install bump2version and toml if not installed
def ensure_packages():
    package_manager = get_active_package_manager()
    required_packages = ["bump2version", "toml"]

    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{package} not installed, package wil be installed.")
            if package_manager == "uv":
                subprocess.run(["uv", "add", package])
            elif package_manager == "pdm":
                subprocess.run(["pdm", "add", package])
                