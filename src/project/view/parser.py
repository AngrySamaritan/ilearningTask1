"""Module to parse arguments from command line"""
import argparse
from src.project.control.main import control


def initParser():
    """
    Function for parser initialisation
    """
    regions = ("ru_RU", "en_US", "by_BY")
    parser = argparse.ArgumentParser()
    parser.add_argument("amount", type=int)
    parser.add_argument("locale", choices=regions)
    parser.add_argument("mistakes", type=float)
    return parser


def parse():
    """
    Function, which call parser initialisation and get values of arguments
    """
    parser = initParser()
    args = parser.parse_args()
    control(int(args.amount), args.locale, float(args.mistakes))
