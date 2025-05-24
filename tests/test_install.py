import subprocess
import sys


def test_installation():
    try:
        # Attempt to install the package in editable mode
        result = subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-e', '.'
        ], check=True, capture_output=True, text=True)
        print("Installation succeeded:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Installation failed:", e.stderr)
        assert False, "Installation failed with error: " + e.stderr


if __name__ == "__main__":
    test_installation() 