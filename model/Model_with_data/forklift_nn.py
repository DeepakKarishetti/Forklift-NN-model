# Import modules

import tensorflow as tf
import keras
#import sklearn.svm import SVR
tf.logging.set_verbosity(tf.logging.ERROR)
import numpy as np
import matplotlib.pyplot as plt
import pickle



# Import data

with open('pwm_data.pkl', 'rb') as f:
	pwm_data = pickle.load(f)

with open('vel_data.pkl', 'rb') as g:
	velo_data = pickle.load(g)
	vel_data = velo_data[0:-3]

with open('ster_data.pkl', 'rb') as h:
	ster_data = pickle.load(h)

#print(len(pwm_data), len(vel_data), len(ster_data))

# Create a model

layer_0 = tf.keras.layers.Dense(units=1, input_shape=[1])
layer_1 = tf.keras.layers.Dense(units=1, input_shape=[1])
#layer_2 = tf.keras.layers.Dense(units=1, input_shape=[1])

# Assemble layers into model

model = tf.keras.Sequential([layer_0, layer_1])

# compile the model
model.compile(loss='mean_squared_error', optimizer = tf.keras.optimizers.Adam(0.1))

# Train model

train = model.fit(pwm_data, vel_data, epochs=750, verbose=False)

# save the model

model.save('f_nn_model.h5')

plt.xlabel('Epoch number')
plt.ylabel('Loss')
plt.plot(train.history['loss'])
plt.show()

vel_scale = ((2.48043818466 + -0.0720526864893) - -0.0720526864893) / 255
vel_scalo = 1/255
r = model.predict([255])
prediction = r*vel_scale 
print(prediction)


#new_model = keras.models.load_model('f_nn_model.h5')
#pred = (new_model.predict([0])

