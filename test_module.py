import unittest  
from sea_level_predictor import draw_plot  

class TestSeaLevelPredictor(unittest.TestCase):  
    def test_plot(self):  
        plot = draw_plot()  
        self.assertEqual(plot.get_xlabel(), 'Year')  
        self.assertEqual(plot.get_ylabel(), 'Sea Level (inches)')  
        self.assertEqual(plot.get_title(), 'Rise in Sea Level')  

if __name__ == "__main__":  
    unittest.main()  
