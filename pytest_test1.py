from funcs_to_test import sum_to_test, dictionary_test

class TestClass:

    def test_sum(self):
        result = sum_to_test(10, 10)
        assert result == 20
        assert isinstance(result , int)

    def test_dictionary(self):
        dictionary = dictionary_test()
        assert 'first' in dictionary
        assert dictionary == {'first': 1, 'second': 2}