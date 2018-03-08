#!/usr/bin/python

from __future__ import print_function  # bring the print function from Python 3 into Python 2.6+
from datetime import timedelta
import time, datetime

def read_input():
  """
  Reads user keyboard input.

  @return:  the user input string
  """
  if sys.version_info[0] < 3:
    return raw_input("> ")  # Python2.x
  else:
    return input("> ")      # Python3


def get_arrival_times():
  """
  Gets and validates a string of arrival times from user.

  @return:  sum of arrival times in seconds, number of days covered
  """
  print("\nEnter up to 4 arrival times separated by spaces. Only the first 4 arrival times will be used.")
  print("Use the time format HH:MM (e.g. 10:05 10:15 9:30).")

  valid_time = False
  total_seconds = 0  # for sum of times in seconds

  while not valid_time:
    arrival_times = read_input().split()
    if (len(arrival_times) > 4):
      arrival_times = arrival_times[0:4]  # only use the first 4 arrival times

    # Validate each arrival time entered and convert to seconds for averaging later
    for atime in arrival_times:
      try:
        time.strptime("%s" % (atime), "%H:%M")

        h, m = atime.split(':')
        total_seconds += (int(h)*3600 + int(m)*60)

        valid_time = True
      except ValueError:
        print(atime,"is an invalid time. Please enter your arrival times again.")
        valid_time = False
        break

  return total_seconds, len(arrival_times)


def calc_average_time():
  """
  Calculates an average arrival time from the times entered, and a time
  expectation to meet the average (where applicable).
  """
  total_seconds, num_days = get_arrival_times()

  avg_seconds = total_seconds / num_days
  avg_time = str(datetime.timedelta(seconds=avg_seconds))
  days_left = 5 - num_days

  # Calculate the difference between the required and average arrival times
  req_time = "10:00"
  time.strptime("%s" % (req_time), "%H:%M")
  h, m = req_time.split(':')
  req_time_seconds = int(h)*3600#(int(h)*3600 + int(m)*60)
  time_diff_seconds = req_time_seconds - avg_seconds

  # Get a formatted HH:MM average time string
  l_avg_time = avg_time.split(":")
  avg_time_hm = str(l_avg_time[0] + ":" + l_avg_time[1])

  if (time_diff_seconds < 0):
    # Get the remaining day goal time and a formatted HH:MM string
    #avg_seconds_over = (int(l_avg_time[0])*3600 + int(l_avg_time[1])*60 + int(l_avg_time[2])) - req_time_seconds#int(h)*3600
    avg_seconds_over = avg_seconds - req_time_seconds
    daily_make_up_seconds = avg_seconds_over / (days_left / num_days)
    goal_time_seconds = req_time_seconds - daily_make_up_seconds
    goal_time = str(datetime.timedelta(seconds=goal_time_seconds))
    #print("goal_time:",str(goal_time))

    l_goal_time = goal_time.split(":")
    goal_time_hm = str(l_goal_time[0] + ":" + l_goal_time[1])

    print("current average: " + str(avg_time_hm) + "; days to bring it down: " + str(days_left) + ". aim for " + goal_time_hm + ".")
  else:
    print("current average: " + str(avg_time_hm) + ", days left this week: " + str(days_left) + ".")


if __name__ == '__main__':
  import sys, traceback

  print("Problem 3: Average Office Time")

  try:
    calc_average_time()

  except:
    print('Exception traceback:', traceback.format_exc())
    sys.exit(-1)
