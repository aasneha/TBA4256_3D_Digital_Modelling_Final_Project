"""
Setup script 
"""

import importlib
import subprocess
import sys

# Required dependencies
required_packages = [
    "numpy",
    "pandas",
    "laspy",
    "open3d",
    "scikit-learn",
    "catboost",
    "scipy",
    "matplotlib"
]

def install_if_missing(package: str):
    """Check if a package is installed, and install it if missing."""
    module_name = package.replace("-", "_")
    try:
        importlib.import_module(module_name)
        print(f"{package} is already installed")
    except ImportError:
        print(f"Installing {package} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    print("\n=== Setting up Python environment for 3D Voxel Classification Pipeline ===\n")
    for pkg in required_packages:
        install_if_missing(pkg)
    print("\nAll dependencies are installed and up to date.\n")

if __name__ == "__main__":
    main()
