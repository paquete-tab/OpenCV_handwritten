from keras.datasets import mnist
from keras.models   import Sequential
from keras.layers.core import Dense, Activation, Flatten
from keras.layers import Conv2D, Reshape, MaxPooling2D
from keras.utils import np_utils
import numpy as np

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = np.array(X_train)/255
X_test = np.array(X_test)/255

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

model = Sequential()

model.add(Reshape((28, 28, 1), input_shape=(28, 28)))
model.add(Conv2D(32, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D((2,2)))

model.add(Flatten())
model.add(Dense(784))
model.add(Activation("relu"))

model.add(Dense(10))
model.add(Activation("softmax"))

model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

hist = model.fit(X_train, y_train, batch_size=200, verbose=1, epochs=10, validation_split=0.1)

score = model.evaluate(X_test, y_test, verbose=1)
print("acc:",score[1])

model.save("MNIST.h5")
