"""Project Recipe Organizer To Add And Manage Recipe's By Ali Morsal(40113161061)"""
import pickle


class Recipe:
    recipe_list = []

    def __init__(self, name: str, ingredient_list: list, category: object, preparation: str):
        self._name = name
        self._ingredient_list = ingredient_list
        self._category = category
        self._preparation = preparation

    @property
    def name(self):
        return self._name

    @property
    def ingredient_list(self):
        return self._ingredient_list

    @property
    def category(self):
        return self._category

    @property
    def preparation(self):
        return self._preparation

    def name_getter(self):
        return self.name

    def add_ingredient(self, ingr):
        self.ingredient_list.append(ingr)

    def del_ingredient(self, ingredt):
        self.ingredient_list.remove(ingredt)

    def get_ingredient(self):
        return self.ingredient_list

    def get_category(self):
        return self.category

    def show_recipe(self):
        print(f"Name: {self.name}\nCategory: {self.category.name_getter()}")
        print("Ingredients: ")
        for iindex, iingredient in enumerate(self.ingredient_list):
            print(
                f'  {iindex + 1}: {iingredient.name_getter()} ({iingredient.amount_getter()} {iingredient.unit_getter()})')
        print(f'Preparation: {self.preparation}')


class Ingredient:
    ingredients_list = []

    def __init__(self, name: str, unit: str, amount: float):
        self._name = name
        self._unit = unit
        self.amount = amount

    @property
    def name(self):
        return self._name

    @property
    def unit(self):
        return self._unit

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        if amount < 0:
            raise ValueError("the Amount Can Not Be Negative")
        self._amount = amount

    def amount_update(self, amount):
        self.amount = amount

    def unit_update(self, unit):
        self._unit = unit  # only amount has setter

    def name_getter(self):
        return self.name

    def amount_getter(self):
        return self.amount

    def unit_getter(self):
        return self.unit


class Category:
    categories_list = []

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    def name_getter(self):
        return self.name

    def del_category(self):
        del self


class RecipeOrganizer:
    recipe_organizer_list = []
    recipe_organizer_names_list = []

    def __init__(self, recipe_list: list):
        self._recipe_list = recipe_list

    @property
    def recipe_list(self):
        return self._recipe_list

    def recipe_list_getter(self):
        return self.recipe_list

    def add_recipe(self, recipe: object):
        self.recipe_list.append(recipe)

    def del_recipe(self, recipe: object):
        self.recipe_list.remove(recipe)

    def search_by_name(self, name):
        found_recipes = []
        for recipe in self.recipe_list:
            if name == recipe.name:
                found_recipes.append(recipe)
        return found_recipes

    def search_by_ingredient(self, ingredi):
        found_recipes = []
        for recipe in self.recipe_list:
            if ingredi in recipe.ingredient_list:
                found_recipes.append(recipe)
        return found_recipes

    def search_by_category(self, category):
        found_recipes = []
        for recipe in self.recipe_list:
            if recipe.category == category:
                found_recipes.append(recipe)
        return found_recipes

    def creat_shopping_list(self):
        shopping_list = list()
        shopping_dict = dict()
        for recipe in self.recipe_list:
            for ingredien in recipe.ingredient_list:
                if ingredien in shopping_dict.keys():
                    shopping_dict[ingredien] += ingredien.amount_getter()
                else:
                    shopping_dict[ingredien] = ingredien.amount_getter()
        for key in shopping_dict.keys():
            shopping_list.append((key.name_getter(), shopping_dict[key], key.unit_getter()))
        return shopping_list


def load_data():
    try:
        with open("RecipeOrganizerByAliMorsal.pickle", "rb") as file:
            load_list = pickle.load(file)
        Recipe.recipe_list, Ingredient.ingredients_list, Category.categories_list, RecipeOrganizer.recipe_organizer_list, RecipeOrganizer.recipe_organizer_names_list = load_list
    except:
        pass


def save_date():
    save_list = [Recipe.recipe_list, Ingredient.ingredients_list, Category.categories_list,
                 RecipeOrganizer.recipe_organizer_list, RecipeOrganizer.recipe_organizer_names_list]
    with open("RecipeOrganizerByAliMorsal.pickle", "wb") as file:
        pickle.dump(save_list, file)


load_data()
print("\nWelcome To Recipe Organizer!\nPlease Enter The Number Of Submenu You Would Like To "
      "Choose")
while True:
    print(
        "\n------------Menu------------\n  1:Add "
        "Category\n  2:Add "
        "Ingredient\n  3:Add Recipe\n  4:Search\n  5:Display All Recipe's\n  6:Display All "
        "Categories\n  7:Create Shopping List\n  8:Quit\n----------------------------", )
    input_number = input("Enter The Number: ")

    if input_number == '1':
        Category.categories_list.append(Category(input("Please Enter The Name Of Category: ")))
        print("Category Has Been Added Successfully")

    elif input_number == '2':
        Ingredient.ingredients_list.append(
            Ingredient(input("Enter The Name Of Ingredient: "), input("Enter The Unit: "), float(input("Enter The "
                                                                                                       "Amount(Must "
                                                                                                       "Be Digit): "))))
        print("Ingredient Added Successfully")
    elif input_number == '3':
        food_name = input("Enter The Recipe Name: ")
        print("Ingredients: ")
        for index, ingredient in enumerate(Ingredient.ingredients_list):
            print(f'  {index + 1}: {ingredient.name_getter()} ({ingredient.amount} {ingredient.unit})')
        ing_indexes = input("Choose The Ingredients Needed(Type Ingredients Numbers Without Any Space For "
                            "Example:12478): ")
        ing_list = []
        for ind in ing_indexes:
            ing_list.append(Ingredient.ingredients_list[int(ind) - 1])
        print("Categories: ")
        for index, category_obj in enumerate(Category.categories_list):
            print(f"  {index + 1}: {category_obj.name_getter()}")
        categ = Category.categories_list[(int(input("Enter The Number Of Category: ")) - 1)]
        preparations = input("How To Cook? : ")
        Recipe.recipe_list.append(Recipe(food_name, ing_list, categ, preparations))
        organizer_name = input("Enter The Name Of The List For This Food: ")
        if organizer_name not in RecipeOrganizer.recipe_organizer_names_list:
            RecipeOrganizer.recipe_organizer_names_list.append(organizer_name)
            RecipeOrganizer.recipe_organizer_list.append(RecipeOrganizer([]))
            RecipeOrganizer.recipe_organizer_list[-1].add_recipe(Recipe.recipe_list[-1])
        else:
            RecipeOrganizer.recipe_organizer_list[
                RecipeOrganizer.recipe_organizer_names_list.index(organizer_name)].add_recipe(Recipe.recipe_list[-1])
        print("Recipe Created Successfully")

    elif input_number == '4':
        print("Lists: ")
        for index, list_name in enumerate(RecipeOrganizer.recipe_organizer_names_list):
            print(f'  {index + 1}: {list_name}')
        recipe_list_index = int(input("Choose A List: ")) - 1

        print("1: Search By Name\n2: Search By Ingredient\n3: Search By Category")
        search_case = input("Enter The Number: ")
        if search_case == '1':
            search_name = input("Enter The Name: ")
            found_list = RecipeOrganizer.recipe_organizer_list[recipe_list_index].search_by_name(search_name)

        elif search_case == '2':
            for index, ingredient in enumerate(Ingredient.ingredients_list):
                print(f'  {index + 1}: {ingredient.name_getter()} ({ingredient.amount} {ingredient.unit})')
            ing_index = int(input("Enter The Ingredient Number: ")) - 1
            found_list = RecipeOrganizer.recipe_organizer_list[recipe_list_index].search_by_ingredient(
                Ingredient.ingredients_list[ing_index])

        elif search_case == '3':
            for index, category_obj in enumerate(Category.categories_list):
                print(f"  {index + 1}: {category_obj.name_getter()}")
            category_index = int(input("Enter The Category Number: ")) - 1
            found_list = RecipeOrganizer.recipe_organizer_list[recipe_list_index].search_by_category(
                Category.categories_list[category_index])

        search_option = input(
            f"{len(found_list)} Recipe/Recipe's Has Been Found.\n  1: Show Ingredients\n  2: Show Category\n  3: "
            f"Return To"
            f" Main Menu\nEnter The Number: ")
        if search_option == '1':
            for found_recipe in found_list:
                print(f"\nIngredients Of {found_recipe.name_getter()}:")
                for index, ingree in enumerate(found_recipe.get_ingredient()):
                    print(f"  {index + 1}: {ingree.name_getter()}")
        elif search_option == '2':
            for found_recipe in found_list:
                print(f"The Category Of {found_recipe.name_getter()} Is {found_recipe.get_category().name_getter()}")

        elif search_option == '3':
            continue

    elif input_number == '5':
        if len(RecipeOrganizer.recipe_organizer_names_list) == 0:
            print("There Is No List Of Recipe's")
            continue
        else:
            print("Choose A List To Display Its Recipes")
            for index, list_name in enumerate(RecipeOrganizer.recipe_organizer_names_list):
                print(f'  {index + 1}: {list_name}')
        list_index = int(input("Enter The Number: ")) - 1
        print("Recipe's:")
        for print_index, recipe2 in enumerate(RecipeOrganizer.recipe_organizer_list[list_index].recipe_list_getter()):
            print(f"  {print_index + 1}: {recipe2.name_getter()}")
        input_case = input("What Do You Want To Do? 1:Display Recipe - 2:Delete A Recipe - 3:Back To Main-Menu : ")
        if input_case == '1':
            index = int(input("Enter The Number Of Recipe You Would Like To See: ")) - 1
            RecipeOrganizer.recipe_organizer_list[list_index].recipe_list_getter()[index].show_recipe()
        if input_case == '2':
            index = int(input("Enter The Number Of Recipe You Would Like To Delete: ")) - 1
            Recipe.recipe_list.remove(RecipeOrganizer.recipe_organizer_list[list_index].recipe_list_getter()[index])
            RecipeOrganizer.recipe_organizer_list[list_index].del_recipe(
                RecipeOrganizer.recipe_organizer_list[list_index].recipe_list_getter()[index])
            print("Recipe Deleted Successfully")
        elif input_case == '3':
            continue

    elif input_number == '6':
        if len(Category.categories_list) == 0:
            print("There Are No Categories.")
        else:
            print("List of All Categories:")
            for index, category_obj in enumerate(Category.categories_list):
                print(f"  {index + 1}: {category_obj.name_getter()}")
            print("What Do You Want To Do? 1:Delete Category - 2:Back To Menu")
            category_case = input("Enter The Number: ")
            if category_case == '1':
                category_num = (int(input("Enter The Number Of Category You Would Like To Delete: ")) - 1)
                Category.categories_list[category_num].del_category()
                Category.categories_list.remove(Category.categories_list[category_num])
                print("Category Deleted Successfully")

            elif category_case == '2':
                continue
    elif input_number == '7':
        if len(RecipeOrganizer.recipe_organizer_names_list) == 0:
            print("There Is No List Of Recipe's")
            continue
        else:
            print("Lists: ")
            for index, list_name in enumerate(RecipeOrganizer.recipe_organizer_names_list):
                print(f'  {index + 1}: {list_name}')
            recipe_list_index = int(input("Choose A List: ")) - 1
            print("Here Is Your Shopping List: ")
            for item in RecipeOrganizer.recipe_organizer_list[recipe_list_index].creat_shopping_list():
                print(f"  {item[1]} {item[2]} Of {item[0]}")

    elif input_number == '8':
        save_date()
        quit()

    else:
        print("Please Enter A Number Between 1 And 8")
