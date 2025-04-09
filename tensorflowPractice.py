import tensorflow as tf
from tensorflow import keras
import numpy as np

# Generate dummy data
x_train = np.random.rand(100, 10)  # 100 samples, 10 features
print(x_train)
y_train = np.random.randint(2, size=(100,))  # Binary labels (0 or 1)
print(y_train)

# Build a simple model
model = keras.Sequential([
    keras.layers.Dense(16, activation='relu', input_shape=(10,)),
    keras.layers.Dense(8, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, batch_size=10)

# Make predictions
predictions = model.predict(x_train[:5])
print("Predictions:", predictions)