def main():
    print("Please write down a year from 1900 to 3000")
    year = int(input())
    if 1900 <= year <= 3000:
        if year % 4 == 0 and year % 100 > 0 or year % 400 == 0:
            print("Leap year")
        elif year % 4 != 0 and year % 100 <= 0 or year % 400 != 0:
            print("Simple year")
    else:
        print("Year should be in between 1900 to 3000")


if __name__ == "__main__":
    main()
