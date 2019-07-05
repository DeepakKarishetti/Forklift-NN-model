import pickle
from keras.models import Sequential
from keras.layers import Dense, Input
from keras.utils import plot_model


with open('pwm_data.pkl', 'rb') as f:
        pwm_data = pickle.load(f)
        x = pwm_data

with open('vel_data.pkl', 'rb') as g:
        velo_data = pickle.load(g)
        vel_data = velo_data[0:-3]
        y = vel_data

with open('ster_data.pkl', 'rb') as h:
        ster_data = pickle.load(h)
        z = ster_data

model = Sequential()
model.add(Dense(2, input_dim=1, activation='relu'))
model.add(Dense(2, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x, z, epochs=1000, verbose=0)

# save model

model.save("ster_model.h5")
print("Model saved")

