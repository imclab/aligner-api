# -*- coding: utf-8 -*-
"""
Created on Thur Nov 29 11:25:40 2012

@author: gavin
"""


class Token:

    def __init__(self, token, index, penn_tag):
        self.token = token
        # index is token index, including DEL and INS
        self.index = index
        # str_index does not include DEL and INS
        #self.str_index = str_index
        self.penn_tag = penn_tag
        self.wn_tag = 'SKIP'
        self.lemma = token

    def __str__(self):
        return '''
        Token %s
        Index: %s
        Penn Tag: %s
        WN Tag: %s
        Lemma: %s''' % \
        (self.token, self.index, self.penn_tag, self.wn_tag, self.lemma)

    def __repr__(self):
        return 'Token %s, Index: %s' % (self.token, self.index)

