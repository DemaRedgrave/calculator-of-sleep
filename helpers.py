def calc_sleep_time(hours: int, minutes: int) -> int:
    """    
    Calculate Sleep Time.
    Parameters:
      hours: int - amount of hours you sleep through the night
      minutes: int - amount of minutes you sleep during the day
    Return:
        Sleep Time in moinutex as int
    """        
    if hours < 0:
      return -1
    if minutes < 0 or minutes > 24 * 60:
      return -1
    return hours * 60 + minutes

