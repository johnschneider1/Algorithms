#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

    total_made = []
    # loop over ingredients dict to pull out keys/values
    for k, v in ingredients.items():


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

    # write a function that receives a recipe in the form of a dictionary, as well as all of the ingredients you have available to you,
    # also in the form of a dict, both dicts will have the same form
    # the keys will be the ingredient name, and their values with be the amounts
    # recipe dict the value/amounts will be the amount of each ingredient needed for the recipe
    # the ingredients value/amounts represent the total amount of that ingredient available for use
    # the function should output the maximum number of whole recipes/batches that can be made with the supplied ingredients
    # need to divide the ingredients values with the recipe values to determine if we have enough, that result is the number of batches
    # best way to acces, key value pairs in python
