from poly_to_string import poly_to_string


def eval_poly(poly, x):
    print(f"Polynomial: {poly_to_string(poly)}")
    degree = len(poly) - 1
    sum = 0
    for term in poly:
        if term != 0:
            sum += term * x**degree
        degree -= 1
    print(sum)


eval_poly([1, 0, 0, 1, -2], -2)
