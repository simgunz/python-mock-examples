"""This tests demonstrate how to patch a function imported with from...import...
"""
from unittest import mock

from mockexamples import monkey


def test_monkey():
    assert monkey.eat_banana() == "monkey eats banana"


@mock.patch("mockexamples.external_api_banana.banana")
def test_monkey_mock_wrong(mock_banana):
    """This tests is red because I am patching where the object is imported from."""
    mock_banana.return_value = "mango"

    assert monkey.eat_banana() == "monkey eats mango"


@mock.patch("mockexamples.monkey.banana")
def test_monkey_mock_correct(mock_banana):
    """This tests is green because I am patching where the object is imported to."""
    mock_banana.return_value = "mango"

    assert monkey.eat_banana() == "monkey eats mango"


def test_monkey_mocker_correct(mocker):
    """This tests shows the alternative syntax using the mocker fixture (pytest-mock)."""
    mock_banana = mocker.patch("mockexamples.monkey.banana")
    mock_banana.return_value = "mango"

    assert monkey.eat_banana() == "monkey eats mango"
