def ounces_to_grams(weight):
    new_weight = weight * 28.3495
    return new_weight

weight_in_ounces = int(input())

weight_in_grams = ounces_to_grams(weight_in_ounces)

print(f"{weight_in_grams} g")

