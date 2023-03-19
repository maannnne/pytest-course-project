import string
import random

def generate_random_string(string_length: int = 8) -> str:
    letters = string.ascii_letters + string.digits
    rnd_str = ''.join(random.choice(letters) for i in range(string_length))
    return rnd_str.lower()
