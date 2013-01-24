# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:25:40 2012

@author: gavin
"""


class Ins:

    def __init__(self, h_token):
        self.edit_type = 'INS'
        self.h_token = h_token
        self.lexical_entailment = 'NONE'
        self.monotonicity = 'NONE'

    def __str__(self):
        return 'Type %s\np: %s\nMonotonicity: %s\nLexent: %s\n' % (
            self.edit_type,
            self.h_token,
            self.monotonicity,
            self.lexical_entailment
        )
