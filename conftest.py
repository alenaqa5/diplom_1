import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from praktikum.bun import Bun
import pytest
import data

@pytest.fixture()
def create_bun():
    bun = Bun(data.data_for_bun['name'], data.data_for_bun['price'])
    return bun

