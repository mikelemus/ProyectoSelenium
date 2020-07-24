import unittest


class PruebasDeStandars(unittest.TestCase):
    def test_suma(self):
        a = 2 + 2
        b = 3 + 1
        self.assertEqual(a, b)

    def test_otra_suma(self):
        a = 2 + 2
        b = 1 + 4
        self.assertNotEqual(a, b)

    def test_algo_es_verdadero(self):
        a = 2 + 2
        b = 3 + 1
        self.assertTrue(a==b)

    def test_algo_es_falso(self):
        self.assertFalse(2+2 == 5+5)

    def test_algo_es_mayor(self):
        a = 5
        b = 3
        self.assertTrue(a>b)

    def test_algo_es_mayorII(self):
        a = 5
        b = 30
        self.assertGreater(a, b)

    def test_algo_es_menor_o_igual(self):
        a = 5
        b = 5
        self.assertLessEqual(a,b)

    def test_comparar_listas(self):
        a = [1,2, 'frutas']
        b = [1,2, 'frutas']
        self.assertListEqual(a,b)

    def test_comparar_tuplas(self):
        a = (4, 2, 3)
        b = (1, 2, 3)
        self.assertTupleEqual(a, b)

    def test_comparar_diccionarios(self):
        a = {'id':2, 'Nombre':'Pepe', 'Apellido':'Suarez'}
        b = {'id':2, 'Nombre':'Pepe', 'Apellido':'Suarez'}
        self.assertDictEqual(a, b)


if __name__ == ('_main_'):
    unittest.main()


