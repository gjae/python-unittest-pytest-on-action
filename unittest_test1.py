import unittest
from funcs_to_test import sum_to_test, dictionary_test

class TestToSum(unittest.TestCase):

    """
        Generando test unitario como prueba del modulo
        nativo unittest agregado en la libreria estandard
        de python
    """

    def test_sum(self):
        result = sum_to_test(10, 10)
        self.assertIsInstance( result, int )
        self.assertEqual(result, 20)


    def test_dictionary(self):
        dic = dictionary_test()
        self.assertIsInstance(dic, dict)
        self.assertEqual(dic, {'first': 1, 'second': 2})
        self.assertDictEqual(dic, {'first': 1, 'second': 2})


if __name__ == '__main__':
    unittest.main()