def test_number(a):
    try:
        float(a)
        print(f"{a} is a number")
        return True
    except ValueError:
        print'f"{a} isn't a number")
        exit()
