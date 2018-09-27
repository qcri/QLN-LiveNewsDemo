import os
import codecs
import numpy as np
import pickle
from features import *
from document import Document
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.pipeline import FeatureUnion
from sklearn.preprocessing import MaxAbsScaler
import json
from datetime import datetime, timedelta
import logging
import threading
from random import randint
import shutil
logging.basicConfig()
logger = logging.getLogger(__name__)

_DIR = os.path.dirname(os.path.abspath(__file__))

maxabs_scaler = MaxAbsScaler()

def construct_pipeline(ds, feats, param):
    feature_set =[]
    logger.info('constructing features pipeline ...')

    if param['baseline']:
        tfidf = feats.extract_baseline_feature(ds)  # each one of these is an sklearn object that has a transform method (each one is a transformer)
        feature_set.append(('tf-idf', tfidf))
    if param['char_grams']:
        char_n_g = feats.extract_char_n_grams(ds)
        feature_set.append(('char-n-g', char_n_g))
    if param['lexical']:
        lexical = feats.extract_lexical(ds)
        feature_set.append(('lexical', lexical))
    if param['style']:
        lexicalstyle_features = feats.extract_lexicalstyle_features(ds)
        feature_set.append(('lexicalstyle', lexicalstyle_features))
    if param['readability']:
        readability_features = feats.extract_readability_features(ds)
        feature_set.append( ('readability', readability_features))
    if param['nela']:
        nela_features = feats.extract_nela_features(ds)
        feature_set.append(('nela', nela_features))

    # feature union is used from the sklearn pipeline class to concatenate features
    features_pipeline =  FeatureUnion(feature_set)  # Pipeline([('vectorizer', vec), ('vectorizer2', vec),....])
    logger.info ('features pipeline ready !')
    return  features_pipeline


def predict (ds, features_pipeline, model):
    logger.info ('████████████████   PREDICTING PROPAGANDA SCORES   ████████████████')
    # calling transform method of each transformer in the features pipeline to transform 
    # data into vectors of features
    X = features_pipeline.transform([doc.text for doc in ds])  
    # scaling (normalizing vectors)
    X = maxabs_scaler.transform(X) 

    logger.info ('predicting Y for each given X ...')
    # predicting the labels in this ds via the trained model loaded in the variable 'model'
    Y_ = model.predict(X)  
    prediction_probabilities = model.predict_proba(X)
    for i, doc in enumerate(ds):
        doc.prediction_prob_1 = (prediction_probabilities[i])[1]
    return ds


class Proppy(object):
    def __init__(self, baseline=True, char_grams=True, lexical=True, style=True, readability=True, nela=False):
        self.feats = Features()  # creating an object from the class features to initialize important global variables such as lexicons and training ds
        logger.info('Loading pickled model from : '+ 'data/model/02:3857PM-July-03-2018maxentr_model.pkl')
        #self.model = joblib.load('data/model/02:3857PM-July-03-2018maxentr_model.pkl') #load the pickled model
        self.model = joblib.load(os.path.join(_DIR, 'data/model/03_5244PM-July-29-2018maxentr_model.pkl')) #load the pickled model
        param = dict()
        trans_train = pickle.load(open(os.path.join(_DIR, 'data/model/transformed_train.pickle'), 'rb'))
        maxabs_scaler.fit_transform(trans_train)
        param['baseline'] = False # baseline
        param['char_grams'] = char_grams
        param['lexical'] = lexical
        param['style'] = style
        param['readability'] = readability
        param['nela'] = False
        self.param = param

    def predict(self, text):
        doc = Document(text=text)
        pipeline = construct_pipeline([doc], self.feats, self.param)
        predicted_docs = predict([doc], pipeline, self.model)  
        return predicted_docs[0].prediction_prob_1
