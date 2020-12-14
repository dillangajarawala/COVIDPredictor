from pickle import load
from sklearn import linear_model
from sklearn import preprocessing

pop_hash = {'al': 4903185, 'ak': 731545, 'az': 7278717, 'ar': 3017804, 'ca': 39512223, 'co': 5758736, 'ct': 3565287, 'de': 973764, 'fl': 21477737, 'ga': 10617423, 'hi': 1415872, 'id': 1787065, 'il': 12671821, 'in': 6732219, 'ia': 3155070, 'ks': 2913314, 'ky': 4467673, 'la': 4648794, 'me': 1344212, 'md': 6045680, 'ma': 6892503, 'mi': 9986857, 'mn': 5639632, 'ms': 2976149, 'mo': 6137428, 'mt': 1068778, 'ne': 1934408, 'nv': 3080156, 'nh': 1359711, 'nj': 8882190, 'nm': 2096829, 'ny': 19453561, 'nc': 10488084, 'nd': 762062, 'oh': 11689100, 'ok': 3956971, 'or': 4217737, 'pa': 12801989, 'ri': 1059361, 'sc': 5148714, 'sd': 884659, 'tn': 6829174, 'tx': 28995881, 'ut': 3205958, 'vt': 623989, 'va': 8535519, 'wa': 7614893, 'wv': 1792147, 'wi': 5822434, 'wy': 578759}

class CasesPredictor(object):

    def __init__(self):
        self.model = load(open("./model/casesmodel.pkl", 'rb'))
        self.encoder = load(open("./model/casesenc.pkl", 'rb'))
    
    def get_encoded_categorical(self, categorical):
        x = self.encoder.transform([categorical]).toarray()[0]
        return x
    
    def predict_cases(self, categorical_vars, numerical_vars):
        encoded = self.get_encoded_categorical(categorical_vars)
        features = list(encoded) + numerical_vars
        all_weights = [i*x for i, x in zip(features, self.model.coef_)]
        weights = [sum(all_weights[:50])] + all_weights[50:] + [self.model.intercept_]
        weights = [int(x) for x in weights]
        cases = self.model.predict([features])[0]
        return int(cases), weights
    
    def get_explanation(self, state, feature_values, feature_labels):
        feature_weights = self.model.coef_[50:]
        explanation = "All estimates start with a baseline value. The parameters you entered will increase or decrease the case count until all of them have been accounted for. "
        if pop_hash[state] > sum(pop_hash.values())/len(pop_hash):
            explanation += "The state you chose had a population higher than the average, so it contributed more to the case count. "
        else:
            explanation += "The state you chose had a population lower than the average, so it contributed less to the case count. "
        
        for i in range(len(feature_weights)):
            sentence = ""
            if feature_labels[i] == "Facebook Survey":
                sentence += "Any reporting of COVID-like illness via the Facebook survey has"
            else:
                sentence += feature_labels[i] + " have "

            if feature_weights[i] > 0:
                sentence += "a positive association with COVID cases, "
            else:
                sentence += "a negative association with COVID cases, "

            if int(feature_values[i]*feature_weights[i]) == 0:
                sentence += "but the value you entered is not large enough to change the case count. "
            elif int(feature_values[i]*feature_weights[i]) > 0:
                sentence += "so the value you entered caused the case count to rise. "
            else:
                sentence += "so the value you entered caused the case count to drop. "
            explanation += sentence
        return explanation
    

    

