def valid_time(friends_length):
    valid_types = ['year', 'minute', 'second', 'hour', 'decade', 'week', 'day', 'month', 'decade', 'century', 'eons',
                   'forever', 'millennia']

    for word in friends_length.split():
        word = word.lower().rstrip('s')
        if word in valid_types:
            return True
    return False


def strip_identifiers(phrase):
    words = phrase.split()
    for word in words:
        if word not in ['a', 'an', 'my']:
            return word.strip()
    return phrase
