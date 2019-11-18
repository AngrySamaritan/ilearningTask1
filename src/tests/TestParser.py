""""Unit tests for parser.py"""

import unittest
import time
from src.project.model.personGenerator import PersonGenerator
from src.project.model.mistakesGenerator import MistakesGenerator
import src.project.control.main


def timer(func):
    """

    :param func:
    :return:
    """


class TestFull(unittest.TestCase):
    """Full test"""

    # def testEN(self):
    #     """
    #     Test
    #     """
    #     self.assertEqual(src.project.control.main.control(1000000, "en_US", 6), None)

    def testRU(self):
        self.assertEqual(src.project.control.main.control(1000000, "ru_RU", 5), None)


class TestMistakes(unittest.TestCase):
    @staticmethod
    def testMistakes():
        print(MistakesGenerator.generateMistake(["Test", "Record", "SomeText"], 4, "en_US"))

    @staticmethod
    def testMistakeList():
        print(MistakesGenerator.getMistakesList(100, 0.2))
        print(MistakesGenerator.getMistakesList(100, 0.2))
