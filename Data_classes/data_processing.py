import pygame 
from numpy import tan, arctan, cos, pi, copy

from Data_classes.variables import Variables
from Data_classes.constants import Constants
from Data_classes.booleans import Booleans
from Data_classes.algorithm_variables import AlgorithmVariables
from Animation_layers.animation_layers import AnimationLayers

from formula_functions import E


class DataProcessing():

    bg_color = (255, 255, 255)
    

    def __init__(self):
        self.variables = Variables()
        self.variables.create_dict()
        
        self.constants = Constants()
        self.constants.create_dict()
        
        self.booleans = Booleans()
        self.booleans.create_dict()
        
        self.algorithm_vars = AlgorithmVariables()
        self.algorithm_vars.create_dict()
        
        self.animation_layers = AnimationLayers()
        self.animation_layers.create_dict()
        
        self.derivative_slopes = {'dx_dt': 0, 'dy_dt': 0, 'dy_dx': 0}
        self.spiral_coordinates = {'x': 0, 'y': 0}
        self.initialize_mode_status_dict()
        self.initialize_reduct_funcs_dict()
        
        self.x_deriv_list = []
 
         
        self.variable_dict_objects = [self.variables, self.booleans, self.constants, self.algorithm_vars]

    def blit_layers(self, win):

        win.fill(self.bg_color)

        for layer, boolean in self.mode_statuses_dict.values():
            if boolean and layer is not None:
                win.blit(layer, (0, 0))



    def get_curr_param(self, param):
        
        if param in ['c', 'deg']:
            return [self.constants.constants_dict[param][0] + self.variables.variables_dict[param][0],
                    self.constants.constants_dict[param][1] + self.variables.variables_dict[param][1]]
        
        elif param in ['a', 'b']:
            
            return self.constants.line_constants_dict[param] + self.variables.variables_dict[param]
        
        elif self.mode_statuses_dict['General solution'][1] and param == 'x':
            a = self.slope
            b = self.get_curr_param('b')
            
            a_turn_on = a/E(a)
            
            result = (1- a_turn_on)* b + a_turn_on * cos(pi/2 - abs(arctan(a))) * (-b)/E(a)
           
            return result
        
        result = self.constants.constants_dict[param] + self.variables.variables_dict[param]
        return float(f'{result:.{self.constants.accuracy + 9}f}')

    
    def initialize_reduct_funcs_dict(self):
        
        self.reduct_funcs_dict = {'ISSCDD': [0, (0, 0, 0), (100, 0)],
                                  '~NSwitch': [0, (0, 0, 0), (130, 0)],                                 
                                  'XMD': [0, (0, 0, 0), (62, 0)],
                                  'SCDD': [0, (0, 0, 0), (75, 0)],
                                  'KWL': [0, (0, 0, 0), (62, 0)],
                                  'KL': [0, (0, 0, 0), (35, 0)], 
                                  'LB-Alg': [0, (0, 0, 0), (85, 0)], 
                                  'NSwitch':[0, (0, 0, 0), (110, 30)],
                                  '~XYSwitch': [0, (0, 0, 0), (145, 30)],
                                  'ABSwitch': [0, (0, 0, 0), (125, 30)],
                                  'AB-Alg': [0, (0, 0, 0), (90, 30)],
                                  'XYSwitch': [0, (0, 0, 0), (120, 30)],
                                  'NLB-Alg': [0, (0, 0, 0), (100, 30)],
                                  'n': 0,
                                  'm': 0 }
    
    def initialize_mode_status_dict(self):

         self.mode_statuses_dict = {'Coordinates':[self.animation_layers.layers_dict['background_surface'],
                                         self.booleans.booleans_dict['background_mode']],
                          
                                    'Algorithm mode': [self.animation_layers.layers_dict['algorithm_layer'],
                                             self.booleans.booleans_dict['algorithm_mode']],
                          
                                    'Algorithm data mode': [self.animation_layers.layers_dict['show_algorithm_data_layer'],
                                                  self.booleans.booleans_dict['algorithm_data_mode']],
                          
                                    'T-diagram': [None,  self.booleans.booleans_dict['t_diagram_mode']],
                                    
                                    'Equation mode': [self.animation_layers.layers_dict['equation_layer'],    
                                                      self.booleans.booleans_dict['equation_mode']],
                                    'Vertical line': [self.animation_layers.layers_dict['vertical_line_layer'],
                                                    self.booleans.booleans_dict['vertical_line_mode']],

                                    'Spiral': [self.animation_layers.layers_dict['spiral_layer'],
                                             self.booleans.booleans_dict['spiral_mode']],

                                    'Y-intersects': [self.animation_layers.layers_dict['y_axis_intersects_layer'],
                                                   self.booleans.booleans_dict['y_axis_intersects_mode']],

                                    'Line-intersects': [self.animation_layers.layers_dict['line_intersects_layer'],
                                                      self.booleans.booleans_dict['line_intersects_mode']],

                                    'Parameters': [self.animation_layers.layers_dict['params_layer'],
                                                 self.booleans.booleans_dict['parameters_mode']],

                                    'Modes layer': [self.animation_layers.layers_dict['show_modes_layer'],
                                                 True],

                                    'Derivatives': [self.animation_layers.layers_dict['derivatives_layer'],
                                                 self.booleans.booleans_dict['derivatives_mode']],                         
                                   
                                    'Steps change': [None, self.booleans.booleans_dict['steps_change_mode']],
                                    
                                    'General solution': [None, self.booleans.booleans_dict['general_solution_mode']],
                                    
                                    'Rotated background': [None, self.booleans.booleans_dict['rotated_background_mode']],
                                    
                                    'Zero missing point': [None, self.booleans.booleans_dict['zero_missing_point_mode']],
                                    
                                    'X_line-X_s diff': [None, self.booleans.booleans_dict['x_l_x_s_diff_mode']],
                                    
                                    'Circle layer': [self.animation_layers.layers_dict['circle_layer'], 
                                                     self.booleans.booleans_dict['circle_mode']],
                                    
                                    'Explanations layer': [self.animation_layers.layers_dict['explanations_layer'], True],                                    
                                   }
            
    def update_reduct_funcs_dict(self):
        
        green = (0, 255, 0)
        red = (255, 0, 0)
        
        for word, value in self.reduct_funcs_dict.items():
            
            if word not in ['n', 'm']:
            
                if word == 'LB-Alg':
                    product = 1
                    for key in ['ISSCDD', '~NSwitch', 'SCDD', 'XMD']:
                        product *= self.reduct_funcs_dict[key][0]
                    product *= (self.reduct_funcs_dict['KWL'][0] + self.reduct_funcs_dict['KL'][0]) 

                    color = red if product == 0 else green

                elif word == 'AB-Alg':
                    product = 1
                    product = self.reduct_funcs_dict['NSwitch'][0]
                    product *= self.reduct_funcs_dict['ISSCDD'][0]
                    product *= self.reduct_funcs_dict['~XYSwitch'][0]
                    product *= self.reduct_funcs_dict['ABSwitch'][0]
                    
                    color = red if product == 0 else green
                    
                elif word == 'NLB-Alg':

                    product = 1
                    product = self.reduct_funcs_dict['NSwitch'][0]
                    product *= self.reduct_funcs_dict['ISSCDD'][0]
                    product *= self.reduct_funcs_dict['XYSwitch'][0]

                    color = red if product == 0 else green
                    

                else:
                    color = red if value[0] == 0 else green
                self.reduct_funcs_dict[word][1] = color
 

    def reset_dicts(self):
        
        for obj in self.variable_dict_objects:
            obj.reset_dict()
            
        '''
        Logic for retaining the 'general solution' in its current state despite the reinitialization of mode_statuses_dict.
        '''
        curr_status_gen_solution = self.mode_statuses_dict['General solution'][1]
        self.initialize_mode_status_dict()
        self.mode_statuses_dict['General solution'][1] = curr_status_gen_solution
        
           
    def switch_mode(self, mode):
        self.mode_statuses_dict[mode][1] = not self.mode_statuses_dict[mode][1]
        
    @property
    def slope(self):
        
        current_a_param = self.get_curr_param('a')
        current_a_param = current_a_param * pi/180
        slope = tan(current_a_param)
        
        return round(slope, 14)
    
    @property
    def background_params(self):
        
        background_surface = self.animation_layers.layers_dict['background_surface']
        screen_width = self.constants.screen_width
        screen_height = self.constants.screen_height
        length = self.get_curr_param('l')

        center_point = self.get_curr_param('c')

        return [background_surface, screen_width, screen_height, length, center_point, self.bg_color]
    
    @property
    def line_params(self):
        
        line_layer = self.animation_layers.layers_dict['vertical_line_layer']
        screen_height = self.constants.screen_height
        screen_width = self.constants.screen_width
        half_screen_width = self.constants.half_screen_width
        half_screen_height = self.constants.half_screen_height
        
        a = self.get_curr_param('a')
        b = self.get_curr_param('b')
        x = self.get_curr_param('x')
        length = self.get_curr_param('l')
        center_point_width, center_point_height = self.get_curr_param('c')
        slope_a = self.slope
        
        t_diagram = self.mode_statuses_dict['T-diagram'][1]
        general_solution = self.mode_statuses_dict['General solution'][1]
        rotated_background = self.mode_statuses_dict['Rotated background'][1]
        
        return [line_layer, screen_height, screen_width, half_screen_width, half_screen_height, 
                a, b, x, length, center_point_width, center_point_height, slope_a,
                t_diagram, general_solution, rotated_background]
    
    @property
    def derivatives_params(self):
        
        layer, derivative = self.mode_statuses_dict['Derivatives']
    
        center_point_width, center_point_height = self.get_curr_param('c')

        length = self.get_curr_param('l')

        deg_x, deg_y = self.get_curr_param('deg')
        t = self.get_curr_param('t')
        v = self.get_curr_param('v')
        w = self.get_curr_param('w')
        k = self.get_curr_param('k')
        
        screen_width = self.constants.screen_width
        screen_height = self.constants.screen_width
        
        derivative_slopes = self.derivative_slopes
        
        t_diagram = self.mode_statuses_dict['T-diagram'][1]
        
        return [layer, center_point_width, center_point_height, 
                length, deg_x, deg_y, t, v, w, k,
                screen_width, screen_height, t_diagram,
                derivative, derivative_slopes]
    
    @property
    def spiral_params(self):
        
        spiral_layer = self.animation_layers.layers_dict['spiral_layer']

        half_screen_width = self.constants.half_screen_width
        half_screen_height = self.constants.half_screen_height
  
        center_point_width, center_point_height = self.get_curr_param('c')
        length = self.get_curr_param('l')
        deg = self.get_curr_param('deg')
        t = self.get_curr_param('t')
        v = self.get_curr_param('v')
        w = self.get_curr_param('w')
        k = self.get_curr_param('k')
        
        spiral_coordinates = self.spiral_coordinates
        
        t_diagram = self.mode_statuses_dict['T-diagram'][1]
        
        text_unit = self.constants.text_unit
        
        return [spiral_layer, half_screen_width, half_screen_height, 
                center_point_width, center_point_height, length,
                deg, t, v, w, k, spiral_coordinates, t_diagram, text_unit] 
    
    @property
    def y_intersects_t_params(self):
        
        deg_x, deg_y  =  self.get_curr_param('deg')
        
        k = self.get_curr_param('k')
        w = self.get_curr_param('w')
        t = self.get_curr_param('t')
        v = self.get_curr_param('v')
        x_line = self.get_curr_param('x')

        a = self.slope
        b = self.get_curr_param('b')
        
        steps_change = self.mode_statuses_dict['Steps change'][1]
        zero_missing_point_mode = self.mode_statuses_dict['Zero missing point'][1]
        general_solution = self.mode_statuses_dict['General solution'][1]
        
        reduct_funcs_dict = self.reduct_funcs_dict
        
        return [deg_x, deg_y , t, v, w, k, x_line, a, b, 
                steps_change, zero_missing_point_mode,
                general_solution, reduct_funcs_dict]
    
    @property
    def draw_dots_params(self):
        
        const_center_point = self.constants.constants_dict['c']
        var_center_point = self.variables.variables_dict['c']

        length = self.get_curr_param('l')

        deg_x, deg_y = self.get_curr_param('deg')
        v = self.get_curr_param('v')
        w = self.get_curr_param('w')
        k = self.get_curr_param('k')

        t_diagram = self.mode_statuses_dict['T-diagram'][1]
        
        mode_statuses_dict = self.mode_statuses_dict
        
        return [deg_x, deg_y, v, w, k, length,
                const_center_point, var_center_point,
                t_diagram, mode_statuses_dict]
    
    @property
    def line_intersections_t_params(self):

        deg_x, deg_y = self.get_curr_param('deg')
        v = self.get_curr_param('v')
        w = self.get_curr_param('w')
        k = self.get_curr_param('k')
        x_line = self.get_curr_param('x')
        b_line = self.get_curr_param('b')
        
        a_slope = self.slope
        
        accuracy = self.constants.accuracy
        
        steps_change = self.mode_statuses_dict['Steps change'][1]
        zero_missing_point_mode = self.mode_statuses_dict['Zero missing point'][1] 
        general_solution = self.mode_statuses_dict['General solution'][1]
        x_l_x_s_diff_mode = self.mode_statuses_dict['X_line-X_s diff'][1]
        reduct_funcs_dict = self.reduct_funcs_dict
        x_deriv_list = self.x_deriv_list
        
        return [deg_x, deg_y, v, w, k, x_line, b_line, a_slope, accuracy,
                steps_change, zero_missing_point_mode, general_solution, x_l_x_s_diff_mode, reduct_funcs_dict, x_deriv_list]
    
    
    @property
    def show_steps_params(self):
        
        params_layer = self.mode_statuses_dict['Parameters'][0]
        text_unit = self.constants.text_unit
        factors_dict = self.variables.factors_dict
        var_params_dict = self.variables.variables_dict
        steps_const_params_dict = self.constants.steps_constants_dict 
        variables_factors_dict = self.variables.factors_dict
        
        steps_change = self.mode_statuses_dict['Steps change'][1]
        
        return [params_layer, text_unit, factors_dict, var_params_dict,
                steps_const_params_dict, variables_factors_dict,
                steps_change]
    
    @property
    def draw_algorithm_params(self):
        
        algorithm_layer = self.animation_layers.layers_dict['algorithm_layer']
        
        center_point_width, center_point_height = self.get_curr_param('c')
        screen_width = self.constants.screen_width
        screen_height = self.constants.screen_height
        length = self.get_curr_param('l')

        total_n = self.algorithm_vars.algorithm_vars_dict['total_n']
        
        start_n = self.algorithm_vars.n if self.mode_statuses_dict['Zero missing point'] else 1

        m = self.algorithm_vars.algorithm_vars_dict['m']
        n = self.algorithm_vars.algorithm_vars_dict['n'] + start_n

        reduct_funcs_dict = self.reduct_funcs_dict
        
        line_intersections_t_params = self.line_intersections_t_params
        
        del line_intersections_t_params[9]
        
        return [algorithm_layer, total_n, n, m, center_point_width, center_point_height,
                screen_width, screen_height, length] + line_intersections_t_params
    
    @property
    def calc_sigle_t_approxim_params(self):
        
        deg_x, deg_y = self.get_curr_param('deg')
        v = self.get_curr_param('v')
        w = self.get_curr_param('w')
        k = self.get_curr_param('k')  
        
        length = self.get_curr_param('l')
        
        center_point_width, center_point_height = self.get_curr_param('c')
   
        
        return [center_point_width, center_point_height, deg_x, deg_y, length, v, w, k]
        
  
