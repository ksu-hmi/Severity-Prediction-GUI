import pandas as pd
from numpy import loadtxt
from keras.models import load_model
import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD


def call_model(string, cl_gen, phys_gen):
    #Convert inputs to dataframes for processing
    xterms_string = string.lower()
    xterms_list = xterms_string.split()
    xterms_pred_df = pd.DataFrame(columns=['Terms'])
    xterms_pred_df = xterms_pred_df.append({'Terms': xterms_list}, ignore_index = True)
    genders = {'Phys_Gender_Code': [phys_gen], 'CL_Gender_Code': [cl_gen]}
    x45_pred_df = pd.DataFrame(data=genders)

    #import pipeline save files
    x1_pipe1 = pickle.load(open('x1_pipe1.sav', 'rb'))
    x1_pipe2 = pickle.load(open('x1_pipe2.sav', 'rb'))
    x2_pipe1 = pickle.load(open('x2_pipe1.sav', 'rb'))
    x2_pipe2 = pickle.load(open('x2_pipe2.sav', 'rb'))
    x3_pipe1 = pickle.load(open('x3_pipe1.sav', 'rb'))
    x3_pipe2 = pickle.load(open('x3_pipe2.sav', 'rb'))

    #put inputs through pipeline for prediction
    x1_p1 = x1_pipe1.transform(xterms_pred_df)
    x1_p2 = x1_pipe2.transform(x1_p1)
    x1_pred_df = pd.DataFrame(x1_p2)

    x2_p1 = x2_pipe1.transform(xterms_pred_df)
    x2_p2 = x2_pipe2.transform(x2_p1)
    x2_pred_df = pd.DataFrame(x2_p2)

    x3_p1 = x3_pipe1.transform(xterms_pred_df)
    x3_p2 = x3_pipe2.transform(x3_p1)
    x3_pred_df = pd.DataFrame(x3_p2)

    #import model
    model = load_model("model.h5")

    #run prediction

    y_pred=model.predict([x1_pred_df, x2_pred_df, x3_pred_df, x45_pred_df])

    y_pred= (y_pred>0.5)

    y_pred_df=pd.DataFrame(data=y_pred)

    for i in range(y_pred_df.shape[0]):
        if y_pred_df.loc[i, 0] == 1:
            return 0
        if y_pred_df.loc[i, 1] == 1:
            return 1
        if y_pred_df.loc[i, 2] == 1:
            return 2

    