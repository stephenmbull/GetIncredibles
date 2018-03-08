#!/usr/bin/python

from __future__ import print_function  # bring the print function from Python 3 into Python 2.6+
from random import randint
import sys

class stack(list):
  def isEmpty(self):
    return not self

  def push(self, item):
    self.append(int(item))

  def getMinimum(self):
    return min(self)


def read_input():
  """
  Reads user keyboard input.

  @return:  the user input string
  """
  if sys.version_info[0] < 3:
    return raw_input("> ")  # Python2.x
  else:
    return input("> ")      # Python3


def add_to_stack(stack, val):
  # Check for a full stack first
  if (len(stack)>=20):
    print("Stack is full!")
    remove_from_stack(stack)

  stack.push(val)
  print("Added",val,"to stack")


def remove_from_stack(stack):
  val = stack.pop()
  print("Removed",val,"from stack")


# ------------------------------------------------------------------------------


def display_instructions():
  print("\nThe stack will hold a maximum of 20 non-negative integer values.")
  print("\nIf a new value is added to the stack when it is full, the last number on the stack will be automatically removed.")
  display_input_options()


def display_input_options():
  print("\nUser input options:")
  print("  a - Add a random value to the stack.")
  print("  r - Remove the last value from the stack.")
  print("  d - Display these instructions.")
  print("  q - Quit.\n")


def main():
  print("Problem 1: Stack of Non-Negative Integers")
  display_instructions()

  this_stack = stack()

  while(1):
    instr = read_input()

    if (instr=='a'):
      val = randint(0,99)
      add_to_stack(this_stack, val)
    elif (instr=='r'):
      if not (this_stack.isEmpty()):
        val = remove_from_stack(this_stack)
    elif (instr=='d'):
      display_instructions()
    elif (instr=='q'):
      break
    else:
      print("Invalid input!")
      display_input_options()

    if (this_stack.isEmpty()):
      print("Stack is currently empty")
    else:
      print("Stack contents:",this_stack)
      print("Smallest value is",this_stack.getMinimum())

  print("Goodbye!")


if __name__ == '__main__':
  try:
    main()

  except:
    print('Exception traceback:', traceback.format_exc())
    sys.exit(-1)
