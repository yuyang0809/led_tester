import sys
import pytest
from click.testing import CliRunner
from led_tester import cli
from led_tester import main



def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = main.readFile(ifile)
    assert N == 10


    