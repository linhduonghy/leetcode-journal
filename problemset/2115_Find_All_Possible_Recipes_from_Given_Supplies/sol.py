from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        n = len(recipes)
        supplies = set(supplies)
        recipes_done = [False] * n
        result = []
        
        def get_recipe_can_make():
            for i in range(n):
                if not recipes_done[i] and all(ingredient in supplies for ingredient in ingredients[i]):
                     return i
            return -1
                
                
        while True:
            pos = get_recipe_can_make()
            if pos == -1:
                break
            recipes_done[pos] = True
            supplies.add(recipes[pos])
            result.append(recipes[pos])
            
        return result