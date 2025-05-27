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
            else:
                subprocess.run([sys.executable, "-m", "pip", "install", package])

# Read the current version from the toml file
def get_current_version():
    try:
        data = toml.load("pyproject.toml")
        return data["project"]["version"]
    except Exception as e:
        print(f"Error by reading pyproject.toml: {e}")
        return None
    
# Apply a version update
def bump_version(level:str)
    current_version = get_current_version()
    if not current_version:
        print("Cant load the current version, check the pyproject.toml please.")
        return
    subprocess.run([
        "bump2version",
        level,
        "--current-version", current_version,
        "--commit", "--tag",
        "pyproject.toml", "main.py"
    ])