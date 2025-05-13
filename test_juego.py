import unittest
from Juego import Juego

class TestVs(unittest.TestCase):
    
    def test_piedra_vs_tijera(self):
        self.assertEqual(Juego.determinar_ganador("piedra","tijera"), 1)
        
    def test_tijera_vs_papel(self):
        self.assertEqual(Juego.determinar_ganador("tijera","papel"), 1)
        
    def test_papel_vs_piedra(self):
        self.assertEqual(Juego.determinar_ganador("papel","piedra"), 1)
        
    def test_tijera_vs_piedra(self):
        self.assertEqual(Juego.determinar_ganador("tijera","piedra"), -1)
    
    def test_papel_vs_tijera(self):
        self.assertEqual(Juego.determinar_ganador("papel","tijera"), -1)
        
    def test_piedra_vs_papel(self):
        self.assertEqual(Juego.determinar_ganador("piedra","papel"), -1)
    
    def test_empate(self):
        self.assertEqual(Juego.determinar_ganador("papel","papel"), 0)
        


if __name__ == '__main__':
    unittest.main()