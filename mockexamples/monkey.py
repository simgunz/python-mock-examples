from mockexamples import external_api_papaya
from mockexamples.external_api_banana import banana


def eat_banana():
    return f"monkey eats {banana()}"


def eat_papaya():
    return f"monkey eats {external_api_papaya.papaya()}"
