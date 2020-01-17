# class Book:

#     def __init__(self):
#         # Establish the properties of each book
#         # with a default value
#         self.title = ""
#         self.publisher = ""
#         self.author = ""
#         self.current_page = 1
#         self.year_published = 0
#         self.currently_reading = False

#     def start_reading(self):
#         self.currently_reading = True
#         print(f'You start reading {self.title} at page {self.current_page}')

#     def stop_reading(self, page):
#         self.current_page = page



# mockingbird = Book()
# for prop, value in mockingbird.__dict__.items():
#     print(f'{prop}:\n{value}\n')




class  Pizza:

   
    def __init__(self):
        self.size = ""
        self.crust_type = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    
    def print_order(self):
        print(f'I would like a {self.size}-inch, deep-dish pizza with {self.toppings} ') 


your_pizza = Pizza()
your_pizza.size = 16
your_pizza.crust_type = "thin"
your_pizza.add_topping("Olives")
your_pizza.print_order()