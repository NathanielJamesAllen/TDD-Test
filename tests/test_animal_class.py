import unittest
from animal import Animal

class Test_animal(unittest.TestCase):

    def test_animal_cat(self):
        animal1 = Animal('cat')
        self.assertEqual(animal1.name, 'Seymour')

    def test_animal_dog(self):
        animal1 = Animal('dog')
        self.assertEqual(animal1.name, 'Spot')

    def test_animal_name(self):
        if(animal1.name != ""):
            animal1 = Animal()
            self.assertEqual(animal1.name, self.name) 
    
    def test_cat_speak(self):
        animal1 = Animal()
        if (self.type == 'cat' and self.size == 'small'):
            self.assertEqual(animal1.speak(), "meow")
        else:
            self.assertEqual(animal1.speak(), "MEOW")
            

    def test_dog_speak(self):
        animal1 = Animal()
        if (self.type == 'dog' and self.size == 'small'):
            self.assertEqual(animal1.speak(), "bow wow")
        elif(self.type == 'dog' and self.size == 'medium'):
            self.assertEqual(animal1.speak(), "Ruff ruff")
        else:
            self.assertEqual(animal1.speak(), "arf arf")

    def test_age_checker(self):
        animal1 = Animal()
        if (self.age < 10):
            self.assertEqual(animal1.describe(), "[name] is young")
        else:
            self.assertEqual(animal1.describe(), "[name] is old")
