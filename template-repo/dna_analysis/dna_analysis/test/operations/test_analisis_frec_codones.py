import unittest
from dna_analysis.operations.analisis_frec_codones import calcular_frecuencia_codones

class TestAnalisisCodones(unittest.TestCase):

    def test_calcular_frecuencia_codones(self):
        secuencia = "ATGCGATAGCTA"
        resultado_esperado = {'ATG': 1, 'CGA': 1, 'TAG': 1, 'CTA': 1}
        self.assertEqual(calcular_frecuencia_codones(secuencia), resultado_esperado)

    def test_longitud_invalida(self):
        secuencia = "ATGCGA"
        with self.assertRaises(ValueError):
            calcular_frecuencia_codones(secuencia)

if __name__ == '__main__':
    unittest.main()
