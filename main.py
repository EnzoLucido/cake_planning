import recipe.kendall_chantilly as recipe
import cake

previous_pan = [4,4]
new_pan = [3,3,4,4,5,5]


factor = cake.find_factor(previous_pan, new_pan)

print(factor)

with open("out.txt", "w") as file:
    file.write("Title: " + recipe.title + "\n")

    for ingredient, amount in recipe.ingredients.items():
        amount = cake.scale(amount, factor)
        file.write(ingredient + ": " + str(amount) + "\n")
        
print(recipe.ingredients)
