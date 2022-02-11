import pickle
from sklearn import datasets


#with open('model.pkl', 'wb') as model_file:
#    pickle.dump(regressor, model_file)
loaded_model = pickle.load(open('model.pkl','rb'))



