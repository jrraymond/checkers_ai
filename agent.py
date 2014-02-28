import random



def Node():

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


    def addAxon(self, node):
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
        
    def step1(self):
        '''initiates step1 for this neuron'''
        if _val_check == True:
            for axon in axons:
                axon.pulse(pulse_strength)
    
    def step2(self):
        '''initiates step 2 for this neuron'''
        value += val_change
        
        
    def evolve(self):
        '''begins a random evolution process for this neuron'''
        mutation = randrange(0,2)
        random_value = randrange(-5,6)
        
        if mutation = 0: #mutates threshold value
            threshold_value += random_value
        elif mutation = 1: #mutates pulse_strength
            pulse_strength += random_value

        
    
def Network():

    def __init__(self,size):
        self.ins = []
        self.nodes = []
        self.out = Node("OUT")
        
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
            n.step1
    
    def change_values(self):
        for n in nodes:
            n.step2















