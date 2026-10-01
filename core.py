import json


def new_game():
    return {'paused': False, 'balance': 10, 'events': {}, 'clock': 0, 'next_id': 1, 'audit': [('a', 1), ('b', 2)], 'used': 1, 'cap': 2, 'snapshot': 5, 'value': 5, 'log': [], 'settled': False}

def bug_27(state):
    return state.get("src") != state.get("dst")

def bug_4(state):
    return not state["paused"]

def bug_11(state):
    if state["balance"] < 20:
        return False
    state["balance"] -= 20
    return True

def bug_18(state):
    event_id = state.get("event_id", "evt")
    if event_id in state["events"]:
        return False
    state["events"][event_id] = True
    return True

def bug_25(state):
    if state["paused"]:
        return state["clock"]
    state["clock"] += 1
    return state["clock"]

def bug_2(state):
    return None

def bug_9(state):
    allocated = state["next_id"]
    state["next_id"] += 1
    return allocated

def bug_16(state):
    return [row for row in state["audit"] if row[0] == "a"]

def bug_23(state):
    return state["cap"] - state["used"]

def bug_0(state):
    processed = state.setdefault("processed", set())
    element = state.get("element", "x")
    if element in processed:
        return False
    processed.add(element)
    return True

def bug_30(state):
    if any(entry[1] == "failed" for entry in state["log"]):
        state["value"] = state["snapshot"]
        return False
    return True

def bug_31(state):
    return not state["settled"]

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
