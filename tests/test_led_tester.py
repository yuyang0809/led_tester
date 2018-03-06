import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
from led_tester import led_tester
from led_tester import cli
from led_tester import utils


def test_command_line_interface():
    ifile = "./data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None

def parseFile(input):

    if input.startswith('http'):
        # use requests
        pass
    else:
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        # haven't written the code yet...
        return N, instructions
    return