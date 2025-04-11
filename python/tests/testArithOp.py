import unittest as ut
import importlib.util
import sys
import os

def import_from_path(module_name, module_path):
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module

module_path = os.path.join('C:/code/python', 'ArithOp.py')
ao = import_from_path('ArithOp', module_path)

class TestArithmetic(ut.TestCase):
     def test_add(self):
        self.assertEqual(ao.addNum(2, 3), 5)
     def test_sub(self):
        self.assertEqual(ao.subNum(3, 2), 1)
     def test_mult(self):
        self.assertEqual(ao.multNum(3, 2), 6)
     def test_div(self):
        self.assertEqual(ao.divNum(4, 2), 2)
     def test_mod(self):
        self.assertEqual(ao.modNum(4, 2), 0)
     def test_floor(self):
        self.assertEqual(ao.floorNum(4, 2), 2)
     def test_exp(self):
        self.assertEqual(ao.expNum(4, 2), 16)

if __name__ == '__main__':
    ut.main()