import pytest

from mockexamples.monkey_testable import Monkey, create_monkey


def test_monkey_eats_fruit():
    monkey = Monkey(lambda: "dummy_fruit")

    assert "monkey eats dummy_fruit" == monkey.eat_fruit()


@pytest.mark.parametrize("fruit", ["banana", "papaya"])
def test_create_monkey(fruit):
    fruit_eater_monkey = create_monkey(fruit)

    assert f"monkey eats {fruit}" == fruit_eater_monkey.eat_fruit()
