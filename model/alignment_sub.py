# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 11:25:40 2012

@author: gavin
"""


class Sub:

    def __init__(self,
        p_token, p_penn_tag, p_wn_tag, p_index,
        h_token, h_penn_tag, h_wn_tag, h_index):
        self.edit_type = 'SUB'
        self.p_token = p_token
        self.p_penn_tag = p_penn_tag
        self.p_wn_tag = p_wn_tag
        self.p_index = p_index
        self.h_token = h_token
        self.h_penn_tag = h_penn_tag
        self.h_wn_tag = h_wn_tag
        self.h_index = h_index

    def __str__(self):
        return 'Type %s\np: %s, p_index: %s\nh: %s, h_index: %s\np_pos: %s\nh_pos: %s\n' % (
            self.edit_type,
            self.p_token,
            self.p_index,
            self.h_token,
            self.h_index,
            self.p_penn_tag + ' ' + self.p_wn_tag,
            self.h_penn_tag + ' ' + self.h_wn_tag,
        )

