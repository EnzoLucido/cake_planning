import circle

def find_factor(pan, new_pan):
    area = circle.total_area(pan)
    new_area = circle.total_area(new_pan)

    return new_area/area

def scale(amount, factor):
    return amount * factor
