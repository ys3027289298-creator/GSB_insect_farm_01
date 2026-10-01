import json


def new_game():
    return {'paused': False, 'balance': 10, 'events': {}, 'clock': 0, 'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'used': 1, 'cap': 2}

def bug_27(state):
    return True

def bug_4(state):
    return True

def bug_11(state):
    state["balance"] -= 20
    return True

def bug_18(state):
    return True

def bug_25(state):
    state["clock"] += 1
    return state["clock"]

def bug_2(state):
    return "empty"

def bug_9(state):
    state["next_id"] += 1
    return state["next_id"]

def bug_16(state):
    return state["audit"]

def bug_23(state):
    return state["cap"] - state["used"] - 1

def bug_0(state):
    return True

def main():
    print("命令: run/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
