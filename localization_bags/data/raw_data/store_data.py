import numpy as np
import pickle

with open('final_pwm_data.txt', 'r') as r:
        a = (" ".join(line.strip() for line in r))
        b = a.replace('data: ', "")
        c = b.replace(' ---', "")
        v_1 = [float(i) for i in c.split(' ')]

        for i, j in enumerate(v_1):
                v_1[i] = (j - min(v_1))/(max(v_1) - min(v_1))	
        print(len(v_1))

        print("\n")	

        #with open('pwm_data.pkl', 'wb') as f:
                #pickle.dump(v_1, f)

with open('final_vel_data.txt', 'r') as s:
        p = (" ".join(line.strip() for line in s))
        q = p.replace('data: ', "")
        r = q.replace(' ---', "")
        v_2 = [float(i) for i in r.split(' ')]

        for i, j in enumerate(v_2):
                v_2[i] = (j - min(v_2))/(max(v_2) - min(v_2))

        print(len(v_2))

        print("\n")

        #with open('vel_data.pkl', 'wb') as g:
                #pickle.dump(v_2, g)

with open('final_ster_data.txt', 'r') as t:
        x = (" ".join(line.strip() for line in t))
        y = x.replace('data: ', "")
        z = y.replace(' ---', "")
        v_3 = [float(i) for i in z.split(' ')]

        for i, j in enumerate(v_3):
                v_3[i] = (j - min(v_3))/(max(v_3) - min(v_3))

        print(len(v_3))

        print("\n")

        #with open('ster_data.pkl', 'wb') as h:
                #pickle.dump(v_1, h)

