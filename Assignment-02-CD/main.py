from app.calculator import add, subtract


def main():
    print("Calculator container is running")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")


if __name__ == "__main__":
    main()
