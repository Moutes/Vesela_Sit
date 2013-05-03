from random import random as rand

def scal(v1, v2):
    output = 0
    for i in xrange(len(v1)):
        output += v1[i] * v2[i]
    return output


class Neuron():
    
    
    def __init__(self, n_inputs):
        self.weights = [rand() for _ in xrange(n_inputs)]
        self.bias = -1
        self.transfer_input = 0
        self.output = 0
    
    def transf_function(self):
        return max(self.tran_input, 0)
        
    def calculate_output(self, input_vector):
        
        self.tran_input = scal(input_vector, self.weights) + self.bias
        self.output = self.transf_function()
        
        
class Layer():
    
    
    def __init__(self, n_neurons, n_inputs):
        self.neurons = [Neuron(n_inputs) for _ in xrange(n_neurons)]
        
    def evaluate_neurons(self, prev_out):
        output = []
        for neuron in self.neurons:
            neuron.calculate_output(prev_out)
            output.append(neuron.output)
        return output
        
    

class Network():
    
    
    def __init__(self, config):
        self.layers = []
        for i in xrange(len(config) - 1):
            self.layers.append(Layer(config[i + 1], config[i]))
    
    def calc_net_out(self, in_put):
        for layer in self.layers:
            layer_out = layer.evaluate_neurons(in_put)
            in_put = layer_out
        return layer_out
            
        
            
a = Neuron(3)
a.calculate_output([10,11,38])

net = Network([3,20,140,1])

print net.calc_net_out([1,0,1])
