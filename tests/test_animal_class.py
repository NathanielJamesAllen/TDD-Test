import unittest
from animal import Animal

class Test_animal(unittest.TestCase):

    def test_animal_cat(self):
        #GIVEN: A new instance of a cat
        animal1 = Animal("cat")
        #WHEN pass 
        #THEN assert that animal's name is Seymour
        self.assertEqual(animal1.name, 'Seymour')

    def test_animal_dog(self):
        animal1 = Animal("dog")
        self.assertEqual(animal1.name, 'Spot')

    def test_animal_name(self):
        animal1 = Animal()
        self.assertEqual(animal1.name, self.name) 
    
    def test_cat_speak(self):
        cat1 = Animal("cat")
        cat1.size = "small"
        words1 = cat1.speak()
        self.assertEqual(words1, "meow")

        cat2 = Animal("cat")
        cat2.size = "medium"
        words2 = cat2.speak()
        self.assertEqual(words2, "MEOW")
        
    def test_dog_speak(self):
        dog1 = Animal("dog") 
        dog1.size = "small"
        words1 = dog1.speak()
        self.assertEqual(words1, "bow wow")

        dog2 = Animal("dog")
        dog2.size = "medium"
        words2 = dog2.speak()
        self.assertEqual(words2, "Ruff ruff")

        dog3 = Animal()
        words3 = dog3.speak()
        self.assertEqual(words3, "arf arf")

    def test_age_checker(self):
        animal1 = Animal()
        animal1.age < 10
        age1 = animal1.describe()
        young = self.name + " is young"
        self.assertEqual(age1, young)
        animal2 = Animal()
        animal2.age >= 10
        age2 = animal2.describe()
        old = self.name + "is old"
        self.assertEqual(age2, old)
