import random
import string


def random_string(n: int = 10):
    return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(n))
