"""Module to parse arguments from command line"""
import argparse
import sys
from src.project.control.main import control


def initParser():
    """
    Function for parser initialisation
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("amount")
    parser.add_argument("region")
    parser.add_argument("mistakes")
    return parser


def parse():
    """
    Function, which call parser initialisation and get values of arguments
    """
    parser = initParser()
    args = parser.parse_args()
    control(int(args.amount), args.region, float(args.mistakes))



