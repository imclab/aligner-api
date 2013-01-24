# -*- coding: utf-8 -*-
import logging
from flask import Flask
from flask import request
import json
import aligner

app = Flask(__name__)
#file_handler = logging.FileHandler('app.log')
#app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/align', methods=['POST'])
def api_align():
    if request.headers['Content-Type'] == 'application/json':
        app.logger.info('Request: %s' % request.json)
        p_tokens = request.json['p_tokens']
        h_tokens = request.json['h_tokens']
        weights = request.json['weights']

        # return a list of objects
        alignments, score = aligner.align(p_tokens, h_tokens, weights)

        for a in alignments:
            app.logger.info(a)

        # serialize the objects to JSON
        return json.dumps(
            [vars(a) for a in alignments], sort_keys=True, indent=4)

    else:
        # TODO change status code
        return "415 Unsupported Media Type"


if __name__ == '__main__':
    # TODO make aligner an object to avoid reloading resources
    #aligner = aligner_mock.Aligner_mock()
    app.run(debug=True)
