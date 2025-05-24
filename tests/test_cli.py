import subprocess
import pytest


def test_fckappl_init():
    result = subprocess.run(['python', '-m', 'fckappl', 'init'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Initializing the fckappl package..." in result.stdout


def test_fckappl_run():
    result = subprocess.run(['python', '-m', 'fckappl', 'run'], capture_output=True, text=True)
    assert result.returncode == 0
    assert "Running the fckappl package..." in result.stdout 