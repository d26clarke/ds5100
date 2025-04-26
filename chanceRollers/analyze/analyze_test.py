import sys
sys.path.append("/Users/ddclarke/development/python/uvaMSDS/DS5100/finalProject")

from analyzer import Analyzer
import unittest
import numpy as np

from chanceRollers.theDie.die import Die
from chanceRollers.game.game import Game



# Create variable to capture results when necessary
results: str = ""

class AnalyzeTestSuite(unittest.TestCase):
  
    def test_1_check_is_game_object(self): 

        with self.assertRaises(ValueError):
            #Generate ValueError by passing an invalid game object
            # The Die
            listDieOne: np.array = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
            listDieTwo: np.array = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
            listDieThree: np.array = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=float)
            #listDieFour: np.array = np.array([1.0, 2.0], dtype=float)

            dieOneInstance: Die = Die(listDieOne)
            dieTwoInstance: Die = Die(listDieTwo)
            dieThreeInstance: Die = Die(listDieThree)
            #dieFourInstance: Die = Die(listDieFour)

            #Manage Die weighting
            dieOneInstance.change_die_weight('Face2', .20)
            dieTwoInstance.change_die_weight('Face2', .20)
            dieThreeInstance.change_die_weight('Face2', .20)

            diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance]

            myErrorInstance: list = list(diceList)
            
            myAnalyerErr: Analyzer = Analyzer(myErrorInstance)

                    

if __name__ == '__main__':
    unittest.main(verbosity=3)