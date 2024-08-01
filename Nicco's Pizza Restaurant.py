#here is where i organised the input
how_many_are_in_the_party = int(input("how many are in your party?"))

#here is where i sorted the pizza
Large_pizza = 7
Medium_pizza = 3
Small_pizza = 1

#here is where i calculate
number_of_large_pizza_to_order = how_many_are_in_the_party // Large_pizza
number_of_large_pizza_remainder = how_many_are_in_the_party % Large_pizza

number_of_medium_pizza_to_order = number_of_large_pizza_remainder // Medium_pizza
number_of_medium_pizza_remainder = number_of_large_pizza_remainder % Medium_pizza

number_of_small_pizza_to_order = number_of_medium_pizza_remainder // Small_pizza

#here is where i print the statements
print("you have " + str(how_many_are_in_the_party) + " people in your party")
print("You ordered " + str(number_of_large_pizza_to_order) + " large pizzas.")
print("You ordered " + str(number_of_medium_pizza_to_order) + " medium pizzas.")
print("You ordered " + str(number_of_small_pizza_to_order) + " small pizzas.")
