def translate(x, y, dx, dy):
    """Translates the point (x, y) by (dx, dy)."""
    return (x + dx, y + dy)

def main():
    """Translates the point (0, 0) by 1 unit to the right and 2 units down."""
    x, y = 0, 0
    translated_point = translate(x, y, 1, 2)
    print("The translated point is ({}, {})".format(translated_point[0], translated_point[1]))

if __name__ == "__main__":
    main()
