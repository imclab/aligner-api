# -*- coding: utf-8 -*-
'''
{
"p_tokens": ["bob", "ate", "cake", "."],
"h_tokens": ["bob", "ate", "food", "."],
"weights": "default"
}

[
    {
        "edit_type": "EQ",
        "h_index": 0,
        "h_penn_tag": "NN",
        "h_token": "bob",
        "h_wn_tag": "n",
        "lexical_entailment": "NONE",
        "monotonicity": "NONE",
        "p_index": 0,
        "p_penn_tag": "NN",
        "p_token": "bob",
        "p_wn_tag": "n",
        "tag_conversion_dict": {
            "JJ": "a",
            "NN": "n",
            "RB": "r",
            "VB": "v"
        }
    },
    {
        "edit_type": "EQ",
        "h_index": 3,
        "h_penn_tag": ".",
        "h_token": ".",
        "h_wn_tag": "SKIP",
        "lexical_entailment": "NONE",
        "monotonicity": "NONE",
        "p_index": 3,
        "p_penn_tag": ".",
        "p_token": ".",
        "p_wn_tag": "SKIP",
        "tag_conversion_dict": {
            "JJ": "a",
            "NN": "n",
            "RB": "r",
            "VB": "v"
        }
    },
    {
        "edit_type": "SUB",
        "h_index": 2,
        "h_penn_tag": "NN",
        "h_token": "food",
        "h_wn_tag": "n",
        "lexical_entailment": "NONE",
        "monotonicity": "NONE",
        "p_index": 2,
        "p_penn_tag": "NN",
        "p_token": "cake",
        "p_wn_tag": "n",
        "tag_conversion_dict": {
            "JJ": "a",
            "NN": "n",
            "RB": "r",
            "VB": "v"
        }
    },
    {
        "edit_type": "EQ",
        "h_index": 1,
        "h_penn_tag": "VBP",
        "h_token": "ate",
        "h_wn_tag": "v",
        "lexical_entailment": "NONE",
        "monotonicity": "NONE",
        "p_index": 1,
        "p_penn_tag": "VBP",
        "p_token": "ate",
        "p_wn_tag": "v",
        "tag_conversion_dict": {
            "JJ": "a",
            "NN": "n",
            "RB": "r",
            "VB": "v"
        }
    }
]

'''
import json
import urllib2
import unittest


class Test_summarizer(unittest.TestCase):

    def runTest(self):
        text = """
        """
        text.decode('utf-8', 'ignore')
        print 'Starting test'
        d = {
            "p_tokens": ["bob", "ate", "cake", "."],
            "h_tokens": ["bob", "ate", "pie", "."],
            "weights": "default"
            }
        #req = urllib2.Request('http://ec2-50-17-103-0.compute-1.amazonaws.com/aligner')
        req = urllib2.Request('http://127.0.0.1/align')
        req.add_header('Content-Type', 'application/json')
        response = urllib2.urlopen(req, json.dumps(d)).read()
        response = json.loads(response)
        #summary = response['summary'].encode('utf-8', 'ignore')
        #print 'Summary:\n%s' % summary
        #self.assertEqual(best_answer.lower(), 'harold ramis')
        print response

if __name__ == '__main__':
    unittest.main()