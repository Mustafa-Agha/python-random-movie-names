import unicodedata
import re


def normalize(string: str) -> str:
    """
    Takes a string and normalize it.

    :param string: containing accents chars
    :return: normalized string
    """
    return ''.join([c for c in unicodedata.normalize('NFD', re.sub("""[\u0300-\u036f`~!#$-@%^&*()|+=÷¿?;.:'"\\s,<>{}]"""
                                                                   , "", string)) if not unicodedata.combining(c)])
