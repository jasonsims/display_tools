#!/usr/bin/env python
#
# author: sims.jrobert@gmail.com (Jason Sims)
#
# The purpose of this module is to handle common formatting tasks for text
# output to the console.
#
import os
import sys
import time

from color_codes import ColorCodes as colors

class TextOutput(object):
  """Outputs formatted text to the command line."""

  @staticmethod
  def msg(msg):
    sys.stdout.write('%s\n' % msg)

  @staticmethod
  def info(msg):
    """Outputs an information message."""
    sys.stdout.write('%s[ INFO ]%s %s\n' % (colors.GREEN, colors.RESET , msg))

  @staticmethod
  def error(msg):
    """Outputs an error message."""
    sys.stdout.write('%s[ ERROR ]%s %s\n' % (colors.RED, colors.RESET, msg))

  @staticmethod
  def warn(msg):
    """Outputs a warning message."""
    sys.stdout.write('%s[ WARN ]%s %s\n' % (colors.YELLOW, colors.RESET, msg))

  @staticmethod
  def success():
    """Outputs a pass message."""
    sys.stdout.write('%s[ pass ]%s\n' % (colors.GREEN, colors.RESET))

  @staticmethod
  def fail():
    """Outputs an fail message."""
    sys.stdout.write('%s[ fail ]%s\n' % (colors.RED, colors.RESET))

  @staticmethod
  def list(list_to_output):
    """Formats a list to more readable output."""
    sys.stdout.write('%s\n' % '\n'.join(list_to_output))

  @staticmethod
  def dict(dict_to_output, reverse=False):
    """Formats a dictionary to more readable output.

    Args:
      dict_to_output: dict Dictionary to output to console.
      reverse: bool Reverse direction of the key sort.
    """
    key_lengths = [ len(x) for x in dict_to_output.keys() ]
    key_lengths.sort()
    text_padding = key_lengths[-1] + 5

    for key, value in sorted(dict_to_output.iteritems(), reverse=reverse):
      sys.stdout.write('%-*s: %s\n' % (text_padding, key, value))

  @staticmethod
  def header(msg, header_char='x'):
    """Prints message with formatted header."""
    header_chars = header_char * 50
    sys.stdout.write('%s\n\n %s\n\n%s\n' % (header_chars, msg, header_chars))

  # Disabling until the color_codes module is fixed
  #def color(self, text_color, msg):
  #  """Outputs text in color."""
  #  sys.stdout.write(
  #      '%s%s%s' % (self.COLOR_MAP[text_color], msg, self.COLOR_MAP['reset']))

class ConsoleAnimations(object):
  """This class produces various console animations."""

  def __init__(self):
    self.last_spin = 0
    self.left_pad = 0
    self.right_pad = 10
    self.direction = 'right'

  def pin_wheel(self):
    """Displays a pinwheel animation."""
    spinner = '|/-\\'
    sys.stdout.write('%s \r' % spinner[self.last_spin])
    sys.stdout.flush()
    self.last_spin += 1
    if self.last_spin > len(spinner) - 1:
      self.last_spin = 0
    time.sleep(.2)

  def moving_bar(self, color='reset'):
    """Displays a moving bar animation."""
    progress_pill = ('%s%s%s' % (colors.GREEN, '==', colors.RESET))
    sys.stdout.write(' [ %-*s%s%*s ]\r' %
        (self.left_pad,'', progress_pill, self.right_pad, ''))
    sys.stdout.flush()

    if self.left_pad == 10:
      self.direction = 'left'
    elif self.right_pad == 10:
      self.direction = 'right'

    if self.direction == 'right':
      self.left_pad += 1
      self.right_pad -= 1
    elif self.direction == 'left':
      self.right_pad += 1
      self.left_pad -= 1

    time.sleep(.2)
