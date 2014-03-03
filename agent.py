import random


class node():

    def __init__(self, 
                 name = None, 
                 val = random.randrange(-5,6), 
                 function = random.randrange(0,2),
                 pulse_strength = random.randrange(-5,6),
                 axons = None
                 ):
        self.name = name #node name (not required)
        self.value = 0 #internal value, checked by _val_check()
        self.threshold_value = val  #what value is compared to in _val_check() 
        self.pulse_strength = 0 #ammout pulsed by pulse function
        
        self.value_change = 0 #change in value for iteration

        self.axons = axons #list of axons (connected neurons)


    def add_axon(self, node):
        '''adds an axon to the node'''
        self.axons.append(node)
        
    
    def pulse(self,value_mod):
        '''changes the nodes internal value by value_mod'''
        self.pulse_strength += value_mod
        
    def _val_check(self):
        '''checks internal value against threshold value'''
        if value > threshold_value:
            return True
        else:
            return False
        
    def pulse_check(self):
        '''readies all applicable neurons to fire'''
        if _val_check == True:
            for axon in axons:
                axon.pulse(pulse_strength)
    
    def value_set(self):
        '''fires all applicable neurons'''
        value += val_change
        
        

        
class input_node(node):
	'''immutable, unevovlable  nodes which contain input data from the environment'''
	pass


class output_node(node):
	'''mutable, unevolvable  nodes which pass information to whatever output format is desired'''
	pass

	##############################
	# justin,
	#	I think you might have been right about having nodes 'look back' rather than pulsing forward.
	#	It may be better to have a static set of input nodes with internal values that are examined 
	#	by the main network.  That seems more simple than 'pulsing' a set value constantly  into
	#	the network.  Also, it might be possible to just define a differet type of node interaction
	#	(ie, a lookback AND a pulse function), but that might be overly complicated.
	#
	#									-tadashi
	#############################

class main_node(node):
	'''mutable, evolvable nodes which allow the system to process data'''

	def evolve(self):
        	'''begins a random evolution process for this neuron'''
        	mutation = randrange(0,2)
        	random_value = randrange(-5,6)
        
        	if mutation = 0: #mutates threshold value
            		threshold_value += random_value
        	elif mutation = 1: #mutates pulse_strength
			pulse_strength += random_value


class network():
	'''a network of nodes which contain three general classes:
		1.  input nodes (nodes which function as sensory inputs for the environment)
		2.  main nodes (nodes which process data from input nodes and output data to the output nodes)
		3.  output nodes (nodes from which a final output is extracted)
	'''
    def __init__(self,size,in_set = None, out_set = None):
        self.ins = [in_set] #set of nodes from which input data comes
        self.nodes = []
        self.outs = [out_set]i #set of nodes from which output data is extracted
        
        #create in nodes
        for i in range(32):
            self.ins.append(Node(("IN",str(i))))  
        
        #create network nodes
        for i in range(size):
            self.nodes.append(Node(i))    #no connections
       
    def decision(self, board_state):
        i = 0;
        for row in board_state:
            for col in board_state:
                self.ins[i].pulse(board_state[row][col])
                
        self.check_and_pulse()
        self.change_values()
        return (self.out.value / 32, self.out.value % 32)
                
                
    def check_and_pulse(self):
        for n in nodes:
            n.pulse_check()
    
    def change_values(self):
        for n in nodes:
            n.value_set()













