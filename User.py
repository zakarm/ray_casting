import pandas as pd
import numpy as np


class User:
    # data
    def __init__(self, username, firstname, lastname):
        self.__username = username
        self.__firstname = firstname
        self.__lastname = lastname

    # getters
    def get_username(self):
        return self.__username

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    # setters
    def set_username(self, username):
        self.__username = username

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def set_lastname(self, lastname):
        self.__lastname = lastname

