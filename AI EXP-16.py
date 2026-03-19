import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Derivative of sigmoid
def sigmoid_derivative(x):
    return x*(1-x)

# Input dataset
X = np.array([[0,0],
              [0,1],
              [1,0],
              [1,1]])

# Output dataset
y = np.array([[0],[1],[1],[0]])

# Seed for reproducibility
np.random.seed(1)

# Initialize weights
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

wh = np.random.uniform(size=(input_neurons,hidden_neurons))
bh = np.random.uniform(size=(1,hidden_neurons))
wo = np.random.uniform(size=(hidden_neurons,output_neurons))
bo = np.random.uniform(size=(1,output_neurons))

lr = 0.1

# Training
for i in range(5000):

    # Forward propagation
    hidden_input = np.dot(X,wh) + bh
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output,wo) + bo
    final_output = sigmoid(final_input)

    # Backpropagation
    error = y - final_output
    d_output = error * sigmoid_derivative(final_output)

    error_hidden = d_output.dot(wo.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_output)

    # Update weights
    wo += hidden_output.T.dot(d_output) * lr
    bo += np.sum(d_output,axis=0,keepdims=True) * lr
    wh += X.T.dot(d_hidden) * lr
    bh += np.sum(d_hidden,axis=0,keepdims=True) * lr

# Output
print("Predicted Output:")
print(final_output)
