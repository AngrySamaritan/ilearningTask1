"""Module to generate random person"""
import random


class PersonGenerator:
    """Random person generator"""

    @staticmethod
    def __getDataList(path):
        """
        Function returns list with all strings from ini file from section
        :param path file path:
        :return list():
        """
        try:
            data_list = list()
            file = open(path)
            for line in file:
                line = line[:line.rfind("\n")]
                data_list.append(line)
            file.close()

            return data_list

        except Exception as error:
            print(error)
            # log(error)

    @staticmethod
    def __generateName(region, amount):
        """
        :param amount:
        :param region:
        """

        if region in ["ru_RU", "by_BY"]:
            first_name_list_man = PersonGenerator.__getDataList("resources/" + region + "/name/man/firstNames.txt")
            last_name_list_man = PersonGenerator.__getDataList("resources/" + region + "/name/man/lastNames.txt")
            father_name_list_man = PersonGenerator.__getDataList("resources/" + region + "/name/man/fatherNames.txt")
            first_name_list_woman = PersonGenerator.__getDataList("resources/" + region + "/name/woman/firstNames.txt")
            last_name_list_woman = PersonGenerator.__getDataList("resources/" + region + "/name/woman/lastNames.txt")
            father_name_list_woman = PersonGenerator.__getDataList("resources/" + region +
                                                                   "/name/woman/fatherNames.txt")

            name_list = list()

            for i in range(amount):
                if random.choice([True, False]):  # true = man
                    name_list.append(random.choice(last_name_list_man) + " " +
                                     random.choice(first_name_list_man) + " " +
                                     random.choice(father_name_list_man) + " ")
                else:
                    name_list.append(random.choice(last_name_list_woman) + " " +
                                     random.choice(first_name_list_woman) + " " +
                                     random.choice(father_name_list_woman) + " ")

        else:
            first_name_list = PersonGenerator.__getDataList("resources/" + region + "/name/firstNames.txt")
            last_name_list = PersonGenerator.__getDataList("resources/" + region + "/name/lastNames.txt")

            name_list = list()
            for i in range(amount):
                name_list.append(random.choice(first_name_list) + " " + random.choice(last_name_list))

        return name_list

    @staticmethod
    def __generateAddress(region, amount):
        """
        :param amount:
        :param region:
        """

        cities = PersonGenerator.__getDataList("resources/" + region + "/address/cities.txt")
        streets = PersonGenerator.__getDataList("resources/" + region + "/address/streets.txt")
        chances = list()
        for index, city in enumerate(cities):
            chances.append(int(city[city.rfind("|") + 1:]))
            cities[index] = city[:city.rfind("|")]

        address_list = list()

        for i in range(amount):
            # random number
            number = str(random.randrange(1, 400))
            # building
            if random.randrange(0, 10) == 0:
                if random.randrange(0, 2) == 0:
                    number += "/" + str(random.randrange(1, 15))
                else:
                    number += random.choice(["A", "B", "C", "D"])
            address_list.append(random.choices(cities, weights=chances)[0] + ", "
                                + random.choice(streets) + ", " + number)

        return address_list

    @staticmethod
    def __generateNumber(region, amount):
        """
        Function generates phone number for current region
        :param amount:
        :param region:
        """
        number_list = list()
        for i in range(amount):
            if region == "en_US":
                number_list.append(
                    "+1 " + str(random.randrange(200, 1000)) + " (" + str(random.randrange(200, 1000)) + ") " +
                    str(random.randrange(10000, 20000))[1::])
            if region == "ru_RU":
                number_list.append(
                    "+7 " + " (" + str(random.randrange(901, 1000)) + ") " +
                    str(random.randrange(1000000, 9999999)))
            if region == "by_BY":
                number_list.append(
                    "+375 " + " (" + random.choice(("29", "25", "33", "44")) + ") " +
                    str(random.randrange(1000000, 9999999)))
        return number_list

    @staticmethod
    def getPersons(amount, region):
        """
        Get persons
        :param amount:
        :param region:
        """
        persons_list = list()

        names = PersonGenerator.__generateName(region, amount)
        numbers = PersonGenerator.__generateNumber(region, amount)
        address = PersonGenerator.__generateAddress(region, amount)

        for index in range(amount):
            persons_list.append([names[index], address[index], numbers[index]])

        return persons_list
