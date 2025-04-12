"""sach mal so"""

#import pytest

from doro.hallo import sag_hallo_und_gib_drei_zurueck
from doro.hallo import double_number

def test_sag_hallo_und_gib_drei_zurueck():
    """ test mal so"""
    assert sag_hallo_und_gib_drei_zurueck() == 3

def test_doule_number():
    """ tests for function "double_number" """
    assert double_number(1) == 2
    assert double_number(2) == 4
