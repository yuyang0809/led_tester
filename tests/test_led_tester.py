import sys
import pytest
from click.testing import CliRunner
from led_tester import cli
from led_tester import main

import numpy as np


def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = main.readFile(ifile)
    assert N == 10
    ifile = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    N, instructions = main.readFile(ifile)
    assert N == 1000

def test_count():
    ifile = "./data/test_data.txt"
    N, instructions = main.readFile(ifile)
    number = main.mainFunction(ifile,N)
    assert number == 36

def test_initial():
    ifile = "./data/test_data.txt"
    N, instructions = main.readFile(ifile)
    lights = main.LightTester(N)
    count = np.count_nonzero(lights.lights)
    assert count == 0