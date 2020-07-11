from http.server import BaseHTTPRequestHandler, HTTPServer

import json
import numpy as np
import os

from torchmoji.sentence_tokenizer import SentenceTokenizer
from torchmoji.model_def import torchmoji_emojis

# A list of all the emojis the model might respond with.
EMOJIS = ":joy: :unamused: :weary: :sob: :heart_eyes: \
:pensive: :ok_hand: :blush: :heart: :smirk: \
:grin: :notes: :flushed: :100: :sleeping: \
:relieved: :relaxed: :raised_hands: :two_hearts: :expressionless: \
:sweat_smile: :pray: :confused: :kissing_heart: :heartbeat: \
:neutral_face: :information_desk_person: :disappointed: :see_no_evil: :tired_face: \
:v: :sunglasses: :rage: :thumbsup: :cry: \
:sleepy: :yum: :triumph: :hand: :mask: \
:clap: :eyes: :gun: :persevere: :smiling_imp: \
:sweat: :broken_heart: :yellow_heart: :musical_note: :speak_no_evil: \
:wink: :skull: :confounded: :smile: :stuck_out_tongue_winking_eye: \
:angry: :no_good: :muscle: :facepunch: :purple_heart: \
:sparkling_heart: :blue_heart: :grimacing: :sparkles:".split(' ')

# Specify the paths to the vocabulary and model weights files. 
vocab_file_path = '/model/vocabulary.json'
model_weights_path = '/model/pytorch_model.bin'

def top_elements(array, k):
    ind = np.argpartition(array, -k)[-k:]
    return ind[np.argsort(array[ind])][::-1]

class MyHTTPServer(HTTPServer):
    def __init__(self, *args, **kwargs):
        HTTPServer.__init__(self, *args, **kwargs)
        with open(vocab_file_path, 'r') as f:
            vocabulary = json.load(f)

        max_sentence_length = 100

        self.st = SentenceTokenizer(vocabulary, max_sentence_length)
        self.model = torchmoji_emojis(model_weights_path)

class Handler(BaseHTTPRequestHandler):
    def predict(self, text):
        if not isinstance(text, list):
            text = [text]
        tokenized, _, _ = self.server.st.tokenize_sentences(text)
        prob = self.server.model(tokenized)[0]
        # Only keep the emoji with the highest confidence.
        emoji_ids = top_elements(prob, 1)
        emojis = list(map(lambda x: EMOJIS[x].strip(':'), emoji_ids))
        return emojis[0]

    def do_GET(self):
        if '/ping' in self.path:
            # Respond to Sagemaker's health check requests.
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'')
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'')

    def do_POST(self):
        if '/invocations' in self.path:
            # Respond to subscription messages sent from Slack
            # and routed by our Lambda function.
            text = self.rfile.read(int(self.headers['Content-Length'])).decode()
            emoji = self.predict(text)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(emoji.encode())

if __name__ == '__main__':
    server_address = ('0.0.0.0', 8080)
    httpd = MyHTTPServer(server_address, Handler)
    httpd.serve_forever()