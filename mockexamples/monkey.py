from mockexamples.external_api_banana import banana


def eat_banana():
    return f"monkey eats {banana()}"


if __name__ == "__main__":
    eat_banana()
