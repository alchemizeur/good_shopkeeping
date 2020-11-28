tps = ['year', 'minute', 'second', 'hour', 'decade', 'week', 'day', 'month', 'decade', 'century', 'eons', 'forever',
       'millennia']


def valid_time(friends_length):
    for word in friends_length.split():
        word = word.lower().rstrip('s')
        if word in tps:
            return True
    return False


def strip_identifiers(phrase):
    words = phrase.split()
    for word in words:
        if word not in ['a', 'an', 'my']:
            return word.strip()
    return phrase
