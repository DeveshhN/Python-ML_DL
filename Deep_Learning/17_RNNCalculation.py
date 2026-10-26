# ht = tanh(Wx*Xt + Wh*ht-1 + b)

# Xt = Current Input
# Wx = Weight of current input
# Wh = Weight of previous hidden state
# b = bias
# ht - 1 = previous hidden state
# tanh = Activation Function (-1 to 1)
# ht = new hidden state

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-1))

def MarvellousRNNPredictions():
    print("Calculations of RNN")

    #     food was not good
    inputs = [1,2,5,3]

    hidden_state= 0
    
    #RNN Parameters
    Wx = 0.5
    Wh = 0.8
    bias = 0.1

    # RNN Calculations
    for time_step , x in enumerate(inputs):
        previous_hidden_state = hidden_state

        weighted_input = Wx * x
        weighted_memory = Wh * previous_hidden_state

        total = weighted_input + weighted_memory + bias

        hidden_state = np.tanh(total)

        print("Time Step : ", time_step+1)
        print("Input : ",x)
        print("Hidden State : ",hidden_state)
        print("-----------------------------------------------------------------")

    # Step 2 : Final Hidden State
    print("Final Hidden State : ", hidden_state) 

    # Step 3 : Output Layer
    # Output = Wy * Final Hidden State + Output Bias

    Wy = 1.0
    output_bias = 0.0

    output = (Wy * hidden_state) + output_bias

    print("Raw Output : ",output)

    # Step 4 : Apply the sigmoid
    probaility = sigmoid(output)

    print("Probability : ",probaility)

    # Step 5 : Final Calculations
    if probaility <= 0.5:
        print("Probability : Positive")
    else:
        print("Probability : Negative")

def main():
    MarvellousRNNPredictions()

if __name__ == "__main__":
    main()