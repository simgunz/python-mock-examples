from mockexamples import external_api_papaya
from mockexamples.external_api_banana import banana


class Monkey:
    def __init__(self, fruit_func):
        self._fruit = fruit_func

    def eat_fruit(self):
        return f"monkey eats {self._fruit()}"


def create_monkey(fruit):
    if fruit == "banana":
        return Monkey(banana)
    elif fruit == "papaya":
        return Monkey(external_api_papaya.papaya)
    raise ValueError(f"monkeys do not eat {fruit}")
