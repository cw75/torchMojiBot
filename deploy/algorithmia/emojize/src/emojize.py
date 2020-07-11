import Algorithmia
import json
import numpy as np

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

def top_elements(array, k):
    ind = np.argpartition(array, -k)[-k:]
    return ind[np.argsort(array[ind])][::-1]

client = Algorithmia.client()

# First, upload the vocabulary and model weights to the Algorithmia data store.
# The following lines retreive them using the Algorithmia data API.
# Replace the path placeholder with your Algorithmia file upload paths.
vocab = client.file("data://path/to/vocabulary.json").getFile()
model_weights = client.file("data://path/to/pytorch_model.bin").getFile().name

max_sentence_length = 100

vocabulary = json.load(vocab)
st = SentenceTokenizer(vocabulary, max_sentence_length)

model = torchmoji_emojis(model_weights)

# API calls will begin at the apply() method, with the request body passed as 'input'
# For more details, see algorithmia.com/developers/algorithm-development/languages
def apply(input):
    if not isinstance(input, list):
        input = [input]
    tokenized, _, _ = st.tokenize_sentences(input)
    prob = model(tokenized)[0]
    # Only keep the emoji with the highest confidence
    emoji_ids = top_elements(prob, 1)
    emojis = list(map(lambda x: EMOJIS[x].strip(':'), emoji_ids))

    return emojis[0]