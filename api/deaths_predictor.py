from pickle import load
from sklearn import linear_model
from sklearn import preprocessing

pop_hash = {'al': 4903185, 'ak': 731545, 'az': 7278717, 'ar': 3017804, 'ca': 39512223, 'co': 5758736, 'ct': 3565287, 'de': 973764, 'fl': 21477737, 'ga': 10617423, 'hi': 1415872, 'id': 1787065, 'il': 12671821, 'in': 6732219, 'ia': 3155070, 'ks': 2913314, 'ky': 4467673, 'la': 4648794, 'me': 1344212, 'md': 6045680, 'ma': 6892503, 'mi': 9986857, 'mn': 5639632, 'ms': 2976149, 'mo': 6137428, 'mt': 1068778, 'ne': 1934408, 'nv': 3080156, 'nh': 1359711, 'nj': 8882190, 'nm': 2096829, 'ny': 19453561, 'nc': 10488084, 'nd': 762062, 'oh': 11689100, 'ok': 3956971, 'or': 4217737, 'pa': 12801989, 'ri': 1059361, 'sc': 5148714, 'sd': 884659, 'tn': 6829174, 'tx': 28995881, 'ut': 3205958, 'vt': 623989, 'va': 8535519, 'wa': 7614893, 'wv': 1792147, 'wi': 5822434, 'wy': 578759}

class DeathsPredictor(object):

    def __init__(self):
        self.model = load(open("./model/deathsmodel.pkl", 'rb'))
        self.scaler = load(open("./model/deathsscaler.pkl", 'rb'))
    
    def get_state_population(self, state):
        return pop_hash[state]
    
    def scale_features(self, features_to_be_scaled):
        x = self.scaler.transform([features_to_be_scaled]).tolist()[0]
        return x
    
    def predict_deaths(self, cases, features_to_be_scaled, state):
        state_population = self.get_state_population(state)
        scaled_features = self.scale_features([state_population] + features_to_be_scaled)
        features = list(scaled_features) + [cases]
        all_weights = [i*x for i, x in zip(features, self.model.coef_)]
        weights = all_weights + [self.model.intercept_]
        weights = [int(x) for x in weights]
        deaths = self.model.predict([features])[0]
        print("DEATHS")
        print(self.model.coef_, self.model.intercept_)
        explanation = self.get_explanation(state)
        return int(deaths), weights, explanation
    
    def get_explanation(self, state):
        explanation = "All estimates start with a baseline value. The parameters you entered will increase or decrease the death count until all of them have been accounted for. "
        if pop_hash[state] > sum(pop_hash.values())/len(pop_hash):
            explanation += "The state you chose had a population higher than the average, so it contributed more to the death count. "
        else:
            explanation += "The state you chose had a population lower than the average, so it contributed less to the death count. "
        explanation += "Positive tests have an extremely association with COVID deaths, so the value you entered had no effect on the death count. "
        explanation += "Hospital admissions have an extremely positive association with COVID deaths, so the value you entered caused the death count to rise. "
        explanation += "Devices away from home have a positive association with COVID deaths, so the value you entered caused the death count to rise. "
        explanation += "Doctor's visits have a negative association with COVID deaths, so the value you entered caused the death count to decrease. "
        explanation += "Any reporting of COVID-like illness via the Facebook survey has been linked with a decrease in deaths, so the value you entered caused the death count to go down. "
        explanation += "Devices at home have a negative association with COVID deaths, so the value you entered caused the death count to go down. "
        return explanation
    

