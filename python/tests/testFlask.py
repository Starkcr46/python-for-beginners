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

module_path = os.path.join('C:/code/python', 'app.py')
ao = import_from_path('app', module_path)


def client():
         client = ao.test_client()
         landing = client.get("/store")
         html = landing.data.decode()
         print(html)