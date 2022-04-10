"""This tests demonstrate that patching where imported from can lead to weird behaviours even with local imports
"""
from unittest import mock


def test_monkey():
    from mockexamples import monkey

    assert monkey.eat_banana() == "monkey eats banana"


@mock.patch("mockexamples.external_api_banana.banana")
def test_monkey_mock_wrong(mock_banana):
    """This test is sometimes green and sometimes red.

    __If I run this test alone__
    Green test, at the time of patching, monkey has not been imported in the test module yet.

    __If I run this test in a suite__
    At the time of patching, monkey has already been imported in the test module by another test.
    This means that the monkey module has been loaded and the non-patched
    version of banana has been imported. To patch it I now need to patch it in the scope of monkey."""
    from mockexamples import monkey

    mock_banana.return_value = "mango"

    assert monkey.eat_banana() == "monkey eats mango"
