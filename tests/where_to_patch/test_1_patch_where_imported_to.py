"""Patch a function where imported to with from...import...
"""
from unittest import mock

from mockexamples import baboon, monkey


def test_monkey():
    assert monkey.eat_banana() == "monkey eats banana"


@mock.patch("mockexamples.external_api_banana.banana")
def test_mock_patch_where_imported_from_fails(mock_banana):
    """This test is red because I am patching where the object is imported from.

    At the time of patching, monkey has already been imported in the test module.
    This means that the monkey module has been loaded and it has imported the
    non-patched version of banana. To patch it I now need to patch it in the scope
    of monkey.
    """
    mock_banana.return_value = "mango"

    assert monkey.eat_banana() == "monkey eats mango"


@mock.patch("mockexamples.monkey.banana")
def test_mock_patch_where_imported_to_works_and_does_not_affect_other_imports(
    mock_banana,
):
    """This test is green because I am patching where the object is imported to.

    The imports of banana in other modules are not affected by the mock."""
    mock_banana.return_value = "mango"

    assert monkey.eat_banana() == "monkey eats mango"
    assert baboon.eat_banana() == "baboon eats banana"


def test_mocker_patch_where_imported_to_works(mocker):
    """This test shows the alternative syntax using the mocker fixture (pytest-mock)."""
    mock_banana = mocker.patch("mockexamples.monkey.banana")
    mock_banana.return_value = "mango"

    assert monkey.eat_banana() == "monkey eats mango"
