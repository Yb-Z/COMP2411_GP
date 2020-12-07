#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import pandas as pd
'''
Functions
    1. Get personal info.
    ...
TODO
'''

class Student(object):
    '''
    corresponding table
    stuID       CHAR(9)         NOT NULL,
    stuName     VARCHAR(100)    NOT NULL,
    stuPW       VARCHAR(25)     NOT NULL,
    stuEmail    VARCHAR(100)    NOT NULL,
    stuMajor    VARCHAR(100)    NOT NULL,
    PRIMARY KEY                 (stuID)
    '''
    def __init__(self, config):
        self.id
    def __init__(self, id, name, pw, email, major):
        self.id = id
        self.name = name
        self.pw = pw
        self.email = email
        self.major = major
    def __str__(self):
        return self.name
