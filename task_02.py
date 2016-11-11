#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""task 2"""

class CustomError(Exception):
    """ CustomError """

def __init__(self, message, cause):
    Exception.__init__(self, message)
    self.cause = cause
    
