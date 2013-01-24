# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:25:40 2012

@author: gavin
"""
import logging
from nltk.corpus import wordnet as wn


class Sub:

    def __init__(self,
        p_token, p_penn_tag, p_index,
        h_token, h_penn_tag, h_index):

        self.tag_conversion_dict = {
            'NN': wn.NOUN, 'JJ': wn.ADJ, 'VB': wn.VERB, 'RB': wn.ADV
        }
        self.edit_type = 'SUB'
        self.p_token = p_token
        self.p_penn_tag = p_penn_tag
        self.p_wn_tag = self.get_p_wn_tag()
        self.p_index = p_index
        self.h_token = h_token
        self.h_penn_tag = h_penn_tag
        self.h_wn_tag = self.get_h_wn_tag()
        self.h_index = h_index
        self.lexical_entailment = 'NONE'
        self.monotonicity = 'NONE'

    def get_p_wn_tag(self):
        if self.p_penn_tag[:2] in self.tag_conversion_dict.keys():
            return self.tag_conversion_dict[self.p_penn_tag[:2]]
        else:
            logging.info('WN tag could not be found for %s' % self.p_penn_tag)
            return 'SKIP'

    def get_h_wn_tag(self):
        if self.h_penn_tag[:2] in self.tag_conversion_dict.keys():
            return self.tag_conversion_dict[self.h_penn_tag[:2]]
        else:
            logging.info('WN tag could not be found for %s' % self.h_penn_tag)
            return 'SKIP'

    def __str__(self):
        return 'Type %s\np: %s, p_index: %s\nh: %s, h_index: %s\np_pos: %s\nh_pos: %s\nMonotonicity: %s\nLexent: %s\n' % (
            self.edit_type,
            self.p_token,
            self.p_index,
            self.h_token,
            self.h_index,
            self.p_penn_tag + ' ' + self.p_wn_tag,
            self.h_penn_tag + ' ' + self.h_wn_tag,
            self.monotonicity,
            self.lexical_entailment
        )

