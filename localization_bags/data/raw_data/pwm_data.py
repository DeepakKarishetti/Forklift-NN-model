import numpy as np

with open('pwm_pedal_31.txt', 'r') as r:
        a = (" ".join(line.strip() for line in r))
        b = a.replace('data: ', "")
        c = b.replace(' ---', "")
        v_1 = [int(i) for i in c.split(' ')]

        for i, j in enumerate(v_1):
                v_1[i] = (j - min(v_1))/(max(v_1) - min(v_1))
        #np.array(d).dump(open('array.npy', 'wb')) 	
with open('pwm_pedal_35.txt', 'r') as r:
        d = (" ".join(line.strip() for line in r))
        e = d.replace('data: ', "")
        f = e.replace(' ---', "")
        v_2 = [int(i) for i in f.split(' ')]

        for i, j in enumerate(v_2):
                v_2[i] = (j - min(v_2))/(max(v_2) - min(v_2))

with open('pwm_pedal_36.txt', 'r') as r:
        g = (" ".join(line.strip() for line in r))
        h = g.replace('data: ', "")
        o = h.replace(' ---', "")
        v_3 = [int(i) for i in o.split(' ')]

        for i, j in enumerate(v_3):
                v_3[i] = (j - min(v_3))/(max(v_3) - min(v_3))	

with open('pwm_pedal_38.txt', 'r') as r:
        x = (" ".join(line.strip() for line in r))
        y = x.replace('data: ', "")
        z = y.replace(' ---', "")
        v_4 = [int(i) for i in z.split(' ')]

        for i, j in enumerate(v_4):
                v_4[i] = (j - min(v_4))/(max(v_4) - min(v_4))

vel = v_1 + v_2 + v_3 + v_4
print((vel))
