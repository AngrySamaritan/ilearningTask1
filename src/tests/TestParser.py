""""Unit tests for parser.py"""

import unittest
from src.project.model.personGenerator import PersonGenerator
from src.project.model.mistakesGenerator import MistakesGenerator
import src.project.control.main


class TestFull(unittest.TestCase):
    """Full test"""

    @staticmethod
    def testAll():
        """
        Test
        """
        src.project.control.main.control(1000000, "en_US", 5)


class TestMistakes(unittest.TestCase):
    @staticmethod
    def testMistakes():
        print(MistakesGenerator.generateMistake(["Test", "Record", "SomeText"], 4, "en_US"))

    @staticmethod
    def testMistakeList():
        print(MistakesGenerator.getMistakesList(100, 0.2))
        print(MistakesGenerator.getMistakesList(100, 0.2))
