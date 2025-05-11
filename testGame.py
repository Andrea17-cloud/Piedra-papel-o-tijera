import unittest
from game import Play

class TestVs(unittest.TestCase):
    
    def testPiedraVsTijera(self):
        self.assertEqual(Play.processGanador("piedra","tijera"),1)
        
    def testTijeraVsPapel(self):
        self.assertEqual(Play.processGanador("tijera","papel"),1)
        
    def testPapelVsPiedra(self):
        self.assertEqual(Play.processGanador("papel","piedra"),1)
        
    def testTijeraVsPiedra(self):
        self.assertEqual(Play.processGanador("tijera","piedra"),-1)
    
    def testPapelVsTijera(self):
        self.assertEqual(Play.processGanador("papel","tijera"),-1)
        
    def testPiedraVsPapel(self):
        self.assertEqual(Play.processGanador("piedra","papel"),-1)
    
    def testEmpate(self):
        self.assertEqual(Play.processGanador("papel","papel"),0)
        



if __name__ == '__main__':
    unittest.main()