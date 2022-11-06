import time
import helpers


def main():
    print("How long do you sleep at night? (In hours)")
    hours = int(input())
    print("Now enter how long do you sleep at the daytime (In minutes)")
    minutes = int(input())
    print('Please wait... I multiply in my mind')
    time.sleep(1.0)
    total_sleep_time = helpers.calc_sleep_time(hours, minutes)
    print("There is how much do you sleep in the one day: {}".format(total_sleep_time))


if __name__ == "__main__":
    main()
