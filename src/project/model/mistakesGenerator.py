"""Class for mistakesGenerator"""
import random


class MistakesGenerator:
    """Mistakes generator class"""

    @staticmethod
    def generateMistake(record, amount, locale):
        """
        Generates mistakes in record
        :param record:
        :param amount:
        :param locale:
        """
        mistake_types = {
            0: MistakesGenerator.__removeSymbol,
            1: MistakesGenerator.__addSymbol,
            2: MistakesGenerator.__swipeSymbol
        }

        for i in range(amount):
            if len(record[0]) <= 1 or len(record[1]) <= 1 or len(record[2]) <= 1:
                record = mistake_types[1](record, locale)
            else:
                record = mistake_types[random.randrange(3)](record, locale)

        return record

    @staticmethod
    def __removeSymbol(record, _):
        index = random.randrange(3)
        index1 = random.randrange(len(record[index]))
        record[index] = record[index][:index1:] + record[index][index1 + 1::]
        return record

    @staticmethod
    def __addSymbol(record, locale):
        symbols = {
            "en_US": "qwertyuiopasdfghjklzxcvbnm",
            "ru_RU": "йцукенгшщзхъфывапролджэячсмитьбю",
            "by_BY": "йцукенгшўзхфывапролджэячсмітьбю",
            "numbers": "1234567890"

        }
        index = random.randrange(3)
        index1 = random.randrange(len(record[index]))
        symbol = random.choice(symbols[locale] + symbols["numbers"])
        record[index] = record[index][:index1] + symbol + record[index][index1:]
        return record

    @staticmethod
    def __swipeSymbol(record, _):
        index = random.randrange(3)
        index1 = random.randrange(len(record[index]) - 1)
        record[index] = record[index][:index1] + record[index][index1 + 1] + record[index][index1] + record[index][
                                                                                                     index1 + 2:]
        return record

    @staticmethod
    def getMistakesList(amount, mistakes):
        """

        :param amount:
        :param mistakes:
        """
        m_list = [0] * amount
        for i in range(int(amount * mistakes)):
            m_list[random.randrange(amount)] += 1
        return m_list
