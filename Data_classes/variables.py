from Data_classes.data_abstract import Data
import inspect

class Variables(Data):
   
    # Variables for parameter changes.
    deg_additional =  0
    t_additional =  0
    v_additional =  0
    w_additional =  0
    x_additional =  0
    k_additional =  0
    l_additional =  0
    coord_additional = [0, 0]
    
    def __init__(self):
        super().__init__()
        self.variables_dict = {}
        self.excluded_methods_names = [name[0] for name in inspect.getmembers(Variables, predicate=inspect.isfunction)] + ['_abc_impl']

    
    def create_dict(self):        
        
        for name, value in Variables.__dict__.items():
            if not name.startswith('__') and name not in self.excluded_methods_names:
                
                self.variables_dict[name] = value