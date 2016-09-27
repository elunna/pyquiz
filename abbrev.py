import re

abbreviations = {
    'protocol': 'pc',
    'message': 'msg',
    'network': 'nw',
    'service': 'svc',
    'memory': 'mem',
    'with': 'w',
    'technology': 'tech'
}


def abbreviate(answer):
    """
    Accept an abbreviated version of a word in the answer.
    """
    short_ans = answer[:]
    for k, v in abbreviations.items():
        short_ans = re.sub(k, v, short_ans.lower())

    if answer.lower() == short_ans:
        return None
    else:
        return short_ans
