""""Main control class"""


from src.project.model.personGenerator import PersonGenerator
from src.project.model.mistakesGenerator import MistakesGenerator
from src.project.view.outPersons import output


# def


def control(amount, locale, mistakes=0):
    """

    :param amount:
    :param locale:
    :param mistakes:
    """
    records = PersonGenerator.getPersons(amount, locale)
    mistakes_count = MistakesGenerator.getMistakesList(amount, mistakes)
    for index in range(len(records)):
        records[index] = (MistakesGenerator.generateMistake(records[index], mistakes_count[index], locale))
    output(records)
