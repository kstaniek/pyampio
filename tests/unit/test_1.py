# -*- coding: utf-8 -*-
"""Test function."""


from unittest import TestCase
from pyampio.modules import module_info
from pprint import pprint

class Test1(TestCase):
    def test_modules_schema_validation(self):
        print(module_info)
        for item in module_info:
            pprint(item)
        pprint(module_info)
        return True
