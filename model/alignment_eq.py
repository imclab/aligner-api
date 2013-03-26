# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:25:40 2012

@author: gavin
"""
from nltk.corpus import wordnet as wn


class Eq:

    def __init__(self,
        p_token, p_lemma, p_penn_tag, p_index,
        h_token, h_lemma, h_penn_tag, h_index):
        self.tag_conversion_dict = {
            'NN': wn.NOUN, 'JJ': wn.ADJ, 'VB': wn.VERB, 'RB': wn.ADV}
        self.edit_type = 'EQ'
        self.p_token = p_token
        self.p_lemma = p_lemma
        self.p_penn_tag = p_penn_tag
        self.p_wn_tag =self.get_wn_tag(self.p_penn_tag)
        self.p_index = p_index
        self.h_token = h_token
        self.h_lemma = h_lemma
        self.h_penn_tag = h_penn_tag
        self.h_wn_tag = self.get_wn_tag(self.h_penn_tag)
        self.h_index = h_index

    def get_wn_tag(self, penn_tag):
        if penn_tag[:2] in self.tag_conversion_dict.keys():
            return self.tag_conversion_dict[penn_tag[:2]]
        else:
            return 'SKIP'

    def __str__(self):
        return 'Type %s\np: %s\nh: %s\n' % (
            self.edit_type, self.p_token, self.h_token
        )

