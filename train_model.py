# load dataset
from pycaret.datasets import get_data
insurance = get_data('insurance')

# init environment
from pycaret.regression import *

# Setup with PyCaret 3.x syntax
r1 = setup(data=insurance, 
           target='charges', 
           session_id=123,
           normalize=True,
           polynomial_features=True,
           train_size=0.8)

# train a model
lr = create_model('lr')

# save pipeline/model
save_model(lr, model_name='deployment_28042020') 