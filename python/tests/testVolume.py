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

module_path = os.path.join('C:/code/python', 'Volume.py')
ao = import_from_path('Volume', module_path)

class TestVolume(ut.TestCase):
     def test_VolumeOfSphere(self):
        self.assertEqual(ao.VolumeOfSphere(10), 4186.67)

     def test_VolumeOfCube(self):
        self.assertEqual(ao.VolumeOfCube(10), 1000)

     def test_VolumeOfCylinder(self):
        self.assertEqual(ao.VolumeOfCylinder(10, 5), 1570.0)

     def test_VolumeOfRectangularPrism(self):
        self.assertEqual(ao.VolumeOfRectangularPrism(10, 5, 2), 100)

     def test_VolumeOfPyramid(self):
        self.assertEqual(ao.VolumeOfPyramid(10, 5, 2), 33.33)

     def test_VolumeOfCone(self):
        self.assertEqual(ao.VolumeOfCone(10, 5), 523.33)

if __name__ == '__main__':
    ut.main()