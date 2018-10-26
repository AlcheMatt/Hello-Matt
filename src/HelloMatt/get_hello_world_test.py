import unittest
import get_hello_world


class TestGetHelloWorld(unittest.TestCase):

    def test_get_hello_world(self):
        my_string_list = ['', 'Hello my world!']
        result_list = ['Hello World!', 'Hello my world!']
        for my_string, result in zip(my_string_list, result_list):
            self.assertEqual(get_hello_world.get_string(my_string), result)
        return True
