#!/usr/bin/env python3
def main():
    # if...then...elseif...else example
    user_guess = int(input("time left in the oven"))
    if user_guess > 0:
        print("lasagna is not ready")
    elif user_guess < 0:
        print("lasagna is buring")
    elif user_guess == 0:
        print("lasagna is ready")


if __name__ == "__main__":
    main()
