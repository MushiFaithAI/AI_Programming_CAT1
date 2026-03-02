from math import pi

def area_of_circle(radius): 
    if radius <= 0:
        raise ValueError("Radius must be greater than 0.")
    return round(pi * radius ** 2, 2)

if __name__ == "__main__":
    try:
        r = float(input("Enter radius: "))
        print(f"Area of the circle: {area_of_circle(r)}")
    except ValueError as e:
        print(e)