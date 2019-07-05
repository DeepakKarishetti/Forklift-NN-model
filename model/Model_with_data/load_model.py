from keras.models import load_model
import sys

pred_value = sys.argv[1]

# denormalization
vel_scale = (2.48043818466 + 0.0720526864893)

model_1 = load_model("vel_model.h5")
pred_1 = model_1.predict([int(pred_value)])

prediction_1 = ((pred_1*vel_scale) - 0.0720526864893) / 255
print(prediction_1)
