import unittest as ut
import importlib.util
import sys
import os
from flask import Flask, request


def import_from_path(module_name, module_path):
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module

module_path = os.path.join('C:/code/python', 'app.py')
ao = import_from_path('app', module_path)


def client():
         test_app = Flask(ao)
         client = test_app.test_client()
         landing = client.get("/store")
         html = landing.data.decode()
         print(html)

class TestApp(ut.TestCase):

    def setUp(self):
        test_app = Flask(ao)
        self.app = test_app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_route(self):
        result = self.app.get('/store')
        self.assertEqual(result.status_code, 200)
        self.assertIn(b'Welcome', result.data)

    def test_post_route(self):
        data = {'key': 'value'}
        result = self.app.post('/store', data=data)
        self.assertEqual(result.status_code, 200)
        # Add assertions based on the expected behavior of your post route

if __name__ == '__main__':
    ut.main()         