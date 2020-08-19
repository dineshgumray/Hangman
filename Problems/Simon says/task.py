def what_to_do(instructions):
    instructions = instructions.strip()
    if not instructions.startswith("Simon says") and not instructions.endswith("Simon says"):
        return "I won't do it!"
    else:
        return "I " + instructions.replace('Simon says', "").strip()
