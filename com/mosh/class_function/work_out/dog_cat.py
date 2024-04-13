class Pet:
    num_of_dogs = 0  # Class attributes
    num_of_cats = 0

    def __init__(self, **pets):  # Instance Method
        self.pets = pets  # Instance attributes
        for key in pets.keys():
            if key == "dog":
                Pet.num_of_dogs += 1
            elif key == "cat":
                Pet.num_of_cats += 1
            else:
                print("Other animals are not allowed")

    @classmethod
    def display_info(cls):  # Class Method 
        print(f"Number of Dogs presented in daycare : {Pet.num_of_dogs}")
        print(f"Number of Cats presented in daycare : {Pet.num_of_cats}")


owner_pet_1 = Pet(dog="Max", cat="chad")
owner_pet_2 = Pet(cat="Broski")
# owner_pet_3 = Pet(dog="Red",dog="Dominator") # key cannot be duplicate
Pet.display_info()
