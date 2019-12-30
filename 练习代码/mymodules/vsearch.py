
def search4vowels(phrase:str)->set:
    """Return any vowels found in a supplied phrase."""
    vowels={'a','e','i','o','u'}
    return vowels.intersection(set(phrase))

def search4letters(phrase:str,letters:str)->set:
    """Return a set of the 'letter' found in 'phrase'."""
    return set(phrase).intersection(set(letters))


