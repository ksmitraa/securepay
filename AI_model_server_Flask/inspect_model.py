import pickle
m = pickle.load(open("best_rf_model (1).pkl","rb"))
print(type(m))
print('n_features_in_', getattr(m, 'n_features_in_', None))
print('feature_names_in_', getattr(m, 'feature_names_in_', None))
