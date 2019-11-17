"""Output module"""


def output(personsList):
    """
    output
    :param personsList:
    """
    res = str()
    for person in personsList:
        res += person[0] + "   |   " + person[1] + "   |   " + person[2] + "\n"
    print(res)
