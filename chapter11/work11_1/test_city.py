import unittest
#from city import city_info
import city

class TestCity(unittest.TestCase):
    def test_city_country(self):
        info = city.city_info('beijing','china')
        self.assertEqual(info,"Beijing,China")
    
    def test_city_country_population(self):
        info = city.city_info('beijing','china',21542000)
        self.assertEqual(info,'Beijing,China - population 21542000')

unittest.main()