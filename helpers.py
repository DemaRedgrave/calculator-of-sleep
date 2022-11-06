def calc_sleep_time(hours: int, minutes: int) -> int:
    """
    Calculate Sleep Time.
    Parameters:
      hours: int - amount of hours you sleep through the night
      minutes: int - amount of minutes you sleep during the day
    Return:
        Sleep Time in moinutex as int
    """
    return hours * 60 + minutes
