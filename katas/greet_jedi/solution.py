def greet_jedi(first_name, last_name):
    jedi_name = last_name[:3].capitalize() + first_name[:2].capitalize()

    return f"Greetings, master {jedi_name}"
