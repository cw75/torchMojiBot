from flask import Flask, request, Response

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

with open(vocab_file_path, 'r') as f:
    vocabulary = json.load(f)

max_sentence_length = 100

st = SentenceTokenizer(vocabulary, max_sentence_length)
model = torchmoji_emojis(model_weights_path)

def predict(text):
    if not isinstance(text, list):
        text = [text]
    tokenized, _, _ = st.tokenize_sentences(text)
    prob = model(tokenized)[0]
    # Only keep the emoji with the highest confidence.
    emoji_ids = top_elements(prob, 1)
    emojis = list(map(lambda x: EMOJIS[x].strip(':'), emoji_ids))
    return emojis[0]

def top_elements(array, k):
    ind = np.argpartition(array, -k)[-k:]
    return ind[np.argsort(array[ind])][::-1]

app = Flask(__name__)

@app.route('/ping', methods = ['GET'])
def ping():
    # Respond to SageMaker's health check requests.
    return Response(status=200)

@app.route('/invocations', methods = ['POST'])
def invoke():
    # Respond to subscription messages sent from Slack
    # and routed by our Lambda function.
    text = request.data.decode()
    emoji = predict(text)
    return Response(emoji.encode(), status=200)