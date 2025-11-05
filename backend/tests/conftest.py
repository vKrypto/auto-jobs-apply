import sys
import os

# todo: we will use this later to write testcases for the backend

# Add parent directory to path to import app modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_1():
    assert 1 == 1