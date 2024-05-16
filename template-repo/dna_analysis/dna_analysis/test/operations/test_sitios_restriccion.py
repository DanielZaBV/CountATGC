# tests/test_sitios_restriccion.py

import unittest
from dna_analysis.operations.sitios_restriccion import identificar_sitios_restriccion

class TestSitiosRestriccion(unittest.TestCase):

    def test_identificar_sitios_restriccion(self):
        secuencia = "GAATTCGCGGAATTCTAGGAATTCTT"
        enzimas = {"EcoRI": "GAATTC", "BamHI": "GGATCC"}
        resultado_esperado = {
            "EcoRI": [0, 8, 18],
            "BamHI": []
        }
        self.assertEqual(identificar_sitios_restriccion(secuencia, enzimas), resultado_esperado)

    def test_sin_sitios(self):
        secuencia = "ATGCATGCATGC"
        enzimas = {"EcoRI": "GAATTC", "BamHI": "GGATCC"}
        resultado_esperado = {
            "EcoRI": [],
            "BamHI": []
        }
        self.assertEqual(identificar_sitios_restriccion(secuencia, enzimas), resultado_esperado)

if __name__ == '__main__':
    unittest.main()
