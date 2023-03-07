# Primer jednog custom module koji ce da se importuje u moduli.py

def validate_jmbg(jmbg):
    return jmbg.isdigit() and len(jmbg) == 13
