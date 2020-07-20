"""Dessert classes."""


class Cupcake:
    """A cupcake."""

    cache = {}

    def __repr__(self):
        """Human-readable printout for debugging."""
        return f'<Cupcake name="{self.name}" qty={self.qty}>' 

    def __init__(self, name, flavor, price):
        self.name = name 
        self.flavor = flavor 
        self.price = price
        self.qty = 0

        self.cache[self.name] = self
    

    def add_stock(self, amount):
        self.qty += amount 

    def sell(self, amount):
        if self.qty == 0:
            print("Sorry these cupcakes are all out.")
        else:
            self.qty > 1

    @staticmethod
    def scale_recipe(ingredients, amount):
        #Ingredients list:
        # Example: Cupcake.scale_recipe([('flour', 1), ('eggs', 3)], 2)
        # [('flour', 2), ('eggs', 6)]

        # Return a list of tuples with the quantity for each ingredient 
        # multiplied by amount. 

        #Number of Ingredients produces x amount of cupcakes:
        for tuple_ing in ingredients:
            list_ing = list(tuple_ing) #changes tuples into lists
            for amount in list_ing:
                list_amt = [[list_ing[1]] * self.amount]
        
            # return list_amt
            # x = self.amount results in the number of cupcakes
        

            


        


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED') 
