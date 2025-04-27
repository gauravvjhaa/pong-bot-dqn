import tensorflow as tf

# Load your Keras model
model = tf.keras.models.load_model("/kaggle/input/pong-ai/keras/default/1/pong_best_hitrate.keras")

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save it
with open("your_model.tflite", "wb") as f:
    f.write(tflite_model)
