"""This tests demonstrate how to patch a function imported with from...import...
"""
from unittest import mock

from mockexamples import monkey


def test_monkey_eats_papaya():
    assert monkey.eat_papaya() == "monkey eats papaya"


@mock.patch("mockexamples.external_api_papaya.papaya")
def test_monkey_mock_wrong(mock_papaya):
    """This test is green because I am patching where the object is looked up,
    which in this case is the module external_api_papaya."""
    mock_papaya.return_value = "mango"

    assert monkey.eat_papaya() == "monkey eats mango"


@mock.patch("mockexamples.monkey.papaya")
def test_monkey_mock_wronga(mock_papaya):
    """This test is red because in the scope of monkey no function papaya has been
    imported"""
    mock_papaya.return_value = "mango"

    assert monkey.eat_papaya() == "monkey eats mango"


@mock.patch("mockexamples.monkey.external_api_papaya.papaya")
def test_monkey_mock_correct(mock_papaya):
    """This test is green because I am patching the function of the reference of the module
    imported by monkey."""
    mock_papaya.return_value = "mango"

    assert monkey.eat_papaya() == "monkey eats mango"
