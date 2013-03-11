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

  COLOR_MAP = {
    'red':    '\x1b\x5b1;31;22m',
    'green':  '\x1b\x5b1;32;22m',
    'yellow': '\x1b\x5b1;33;40m',
    'reset':  '\x1b\x5b1;0m'
  }

  def info(self, msg):
    """Outputs and logs an information message."""
    sys.stdout.write('%s[INFO]%s %s\n' %
                     (self.COLOR_MAP['green'], self.COLOR_MAP['reset'], msg))

  def error(self, msg):
    """Outputs and logs an error message."""
    sys.stdout.write('%s[ERROR]%s %s\n' %
                     (self.COLOR_MAP['red'], self.COLOR_MAP['reset'], msg))

  def warn(self, msg):
    """Outputs and logs a warning message."""
    sys.stdout.write('%s[WARN]%s %s\n' %
                     (self.COLOR_MAP['yellow'], self.COLOR_MAP['reset'], msg))

  def success(self):
    """Outputs a pass message."""
    sys.stdout.write('%s[ pass ]%s\n' %
                     (self.COLOR_MAP['green'], self.COLOR_MAP['reset']))

  def fail(self):
    """Outputs an fail message."""
    sys.stdout.write('%s[ fail ]%s\n' %
                     (self.COLOR_MAP['red'], self.COLOR_MAP['reset']))

  def list(self, list_to_output):
    """Formats a list to more readable output."""
    sys.stdout.write('%s\n' % '\n'.join(list_to_output))

  def dict(self, dict_to_output):
    """Formats a dictionary to more readable output."""
    key_lengths = [ len(x) for x in dict_to_output.keys() ]
    key_lengths.sort()
    text_padding = key_lengths[-1] + 5

    for key, value in dict_to_output.iteritems():
      sys.stdout.write('%-*s: %s\n' % (text_padding, key, value))

  def color(self, text_color, msg):
    """Outputs text in color."""
    sys.stdout.write(
        '%s%s%s' % (self.COLOR_MAP[text_color], msg, self.COLOR_MAP['reset']))

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
    progress_pill = ('%s%s%s' % 
        (colors.COLOR_MAP[color], '==', colors.COLOR_MAP['reset']))
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