import json
import pickle
import nltk
import numpy as np
from keras.models import load_model
model=load_model('traffic')


amendes=pickle.load(open('amendes.pkl','rb'))
classes=pickle.load(open('classes.pkl','rb'))

ignore_words=['.',',','?','!','bonjour','probleme','par','des','à','sur','est','de','du','si','les','Le','le','la','La','en','Les','non',')','(','ou','un','’']
def clean(sentence):
    sentence_words=nltk.word_tokenize(sentence)
    sentence_words=[word.lower() for word in sentence_words if word not in ignore_words]
    return sentence_words
def bag_of_words(sentence):
    words=pickle.load(open('amendes.pkl','rb'))
    sentence_words=clean(sentence)
    bag=[0]*len(words)
    for w in sentence_words:
         for i,word in enumerate(words):
                if word==w:
                    bag[i]=1
    return np.array(bag)
#bag=[0,1,0,1,0,0,0,0,1,0,0]
def predict_class(sentence):
    bow=bag_of_words(sentence)
    res=model.predict(np.array([bow]))
    return res
def get_response(pred):
    tag=classes[np.argmax(pred)]
    return tag.replace('\n','<br>')