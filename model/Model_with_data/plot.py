import pickle
import matplotlib.pyplot as plt

with open('pwm_data.pkl', 'rb') as f:
        pwm_data = pickle.load(f)

with open('vel_data.pkl', 'rb') as g:
        velo_data = pickle.load(g)
        vel_data = velo_data[0:-3]

with open('ster_data.pkl', 'rb') as h:
        ster_data = pickle.load(h)


plt.plot(vel_data, pwm_data)
plt.show()

plt.plot(ster_data, pwm_data)
plt.show()
