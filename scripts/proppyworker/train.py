import logging
import codecs
import numpy as np
import optparse
import pickle
from setup import *
from features import *
from document import document
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.preprocessing import MaxAbsScaler
import datetime

def train_model(ds_file,param):
    logging.info('████████████████  𝕋 ℝ 𝔸 𝕀 ℕ 𝕀 ℕ 𝔾  ████████████████')
    train = load_myds(ds_file)
    feats = features(train)
    features_pipeline = construct_pipeline(train, feats, param) # call the methods that extract features to initialize transformers

    model = LogisticRegression(penalty='l2', class_weight='balanced') # creating an object from the max entropy with L2 regulariation
    logging.info("Computing features")
    X = features_pipeline.transform([doc.text for doc in train]) # calling transform method of each transformer in the features pipeline to transform data into vectors of features
    pickle.dump(X, open("../data/model/transformed_train.pickle", "wb"))
    X = maxabs_scaler.fit_transform(X)
    Y = [doc.gold_label for doc in train]
    logging.info ('fitting the model according to given data ...')
    model.fit(X, Y)
    now= datetime.datetime.now().strftime("%I:%M%S%p-%B-%d-%Y")
    model_file_name= '../data/model/'+now+'maxentr_model.pkl'
    joblib.dump(model,model_file_name ) #pickle the model
    logging.info ('model pickled at : '+ model_file_name)
    return model_file_name

param= dict()
param['baseline'] = True
param['char_grams'] = True
param['lexical'] = True
param['style'] = True
param['readability'] = True
param['nela'] = False
train_model('../data/datasets/train.dist.converted.txt',param)