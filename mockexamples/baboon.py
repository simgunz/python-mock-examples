from mockexamples import external_api_papaya
from mockexamples.external_api_banana import banana


def eat_banana():
    return f"baboon eats {banana()}"


def eat_papaya():
    return f"baboon eats {external_api_papaya.papaya()}"
