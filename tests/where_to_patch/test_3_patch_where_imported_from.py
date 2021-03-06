"""This tests demonstrate how to patch a function imported with from...import...
"""
from unittest import mock

from mockexamples import baboon, monkey


def test_monkey_eats_papaya():
    assert monkey.eat_papaya() == "monkey eats papaya"


@mock.patch("mockexamples.external_api_papaya.papaya")
def test_mock_patch_where_looked_up_works(mock_papaya):
    """This test is green because I am patching where the object is looked up,
    which in this case is the module external_api_papaya."""
    mock_papaya.return_value = "mango"

    assert monkey.eat_papaya() == "monkey eats mango"
    assert baboon.eat_papaya() == "baboon eats mango"


@mock.patch("mockexamples.monkey.papaya")
def test_mock_patch_unexisting_reference_fails(mock_papaya):
    """This test is red because in the scope of monkey no function papaya has been
    imported"""
    mock_papaya.return_value = "mango"

    assert monkey.eat_papaya() == "monkey eats mango"


@mock.patch("mockexamples.monkey.external_api_papaya.papaya")
def test_mock_patch_function_of_module_where_imported_to_works(
    mock_papaya,
):
    mock_papaya.return_value = "mango"

    assert monkey.eat_papaya() == "monkey eats mango"


@mock.patch("mockexamples.monkey.external_api_papaya.papaya")
def test_mock_patch_function_of_module_where_imported_to_work_and_affects_other_imports(
    mock_papaya,
):
    """This test is green because I am patching the function of the reference of the
    module imported by monkey.

    Even though I am patching in the scope of monkey the mock affects also other places
    where the module has been imported."""
    mock_papaya.return_value = "mango"

    assert monkey.eat_papaya() == "monkey eats mango"
    assert baboon.eat_papaya() == "baboon eats mango"
