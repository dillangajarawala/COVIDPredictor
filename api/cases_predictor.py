from pickle import load
from sklearn import linear_model
from sklearn import preprocessing

class CasesPredictor(object):

    def __init__(self):
        self.model = load(open("./../model/casesmodel.pkl", 'rb'))
        self.encoder = load(open("./../model/casesenc.pkl"), 'rb')
    
    def get_encoded_categorical(self, categorical):
        x = self.encoder.transform([categorical]).toarray()[0]
        return x
    
    def predict_cases(self, categorical_vars, numerical_vars):
        encoded = self.get_encoded_categorical(categorical_vars)
        features = encoded + numerical_vars
        cases = self.model.predict([features])[0]
        return cases
    

