def poly_to_string(poly):
    if all(x == 0 for x in poly):
        print("0+")
        return
    elif len(poly) == 0:
        print("0")
    full_string = ""
    i = len(poly) - 1
    for term in poly:
        if term != 0:
            if term > 0 and i != len(poly) - 1:
                full_string += "+ "
            if term == 1 and i not in [0, 1]:
                full_string += f"x^{i} "
            elif term != 1 and i == 0:
                full_string += f"{term}"
            elif term == 1 and i == 1:
                full_string += f"x "
            elif term != 1 and i == 1:
                full_string += f"{term}x"
            elif term > 1 and i not in [0, 1]:
                full_string += f"{term}x^{i} "
        i -= 1

    return full_string


# x^5 + 3x^4 + 5x^3 + 2x^2 + x - 1

print(poly_to_string([1, 0, 0, 1, -2]))
