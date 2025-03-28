import numpy as np 
import pygame
from animation_functions import *

def handle_line_param_a(a_param):
    if a_param > 0:
        if a_param > 90:
            diff = a_param - 90
            a_param = 90 - diff
            a_param *= -1
        elif a_param < 0:
            a_param *= -1
            
    elif a_param <0:
        if a_param < -90:
            diff = - 90 - a_param 
            a_param = 90 - diff
            
        elif a_param > 0:
            a_param *= -1
            
    return a_param


def handle_key_commands(data_processing):

    
    if not data_processing.mode_statuses_dict['Steps change'][1]:
      
        updates_dict = data_processing.booleans.update_booleans_dict    
        const_params_dict = data_processing.constants.constants_dict
        line_params_dict = data_processing.constants.line_constants_dict
        var_params_dict = data_processing.variables.variables_dict
        steps_dict_constants = data_processing.constants.steps_constants_dict
        factors_dict = data_processing.variables.factors_dict
        
        # unit_scaler = data_processing.variables.unit_scaler


        updates_dict['shift_coords'] = False    

        # Check for key combinations
        keys = pygame.key.get_pressed()
        
            
        if keys[pygame.K_SPACE]:
            print('Space')
            pygame.image.save(data_processing.animation_layers.win, 'fig_.png')
            pygame.time.delay(1000)



        if keys[pygame.K_z]:

            # Zoom-in 
            if keys[pygame.K_UP]:
                var_params_dict['l'] += steps_dict_constants['l'] * factors_dict['l']

                updates_dict['update_screen'], updates_dict['update_spiral'],\
                updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True

            # Zoom-out
            elif keys[pygame.K_DOWN]:

                possible_length = const_params_dict['l'] + var_params_dict['l'] - steps_dict_constants['l'] * factors_dict['l']

                if possible_length > 0:
                    var_params_dict['l'] -= steps_dict_constants['l'] * factors_dict['l']

                updates_dict['update_screen'], updates_dict['update_spiral'],\
                updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True

        elif keys[pygame.K_h]:

            # Move the screen up along the y-axis.
            if keys[pygame.K_UP]:
                var_params_dict['c'][1] -= steps_dict_constants['c']

                updates_dict['update_screen'], updates_dict['update_spiral'],\
                updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True

            # Move the screen down along the y-axis.    
            elif keys[pygame.K_DOWN]:
                var_params_dict['c'][1] += steps_dict_constants['c']

                updates_dict['update_screen'], updates_dict['update_spiral'],\
                updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True

            # Move the screen left along the y-axis.    
            elif keys[pygame.K_LEFT]:
                var_params_dict['c'][0] -= steps_dict_constants['c']

                updates_dict['update_screen'], updates_dict['update_spiral'],\
                updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True

            # Move the screen right along the y-axis. 
            elif keys[pygame.K_RIGHT]:
                var_params_dict['c'][0] += steps_dict_constants['c']

                updates_dict['update_screen'], updates_dict['update_spiral'],\
                updates_dict['update_line'], updates_dict['shift_coords'] = True, True, True, True
                
 
        if not data_processing.mode_statuses_dict['Algorithm mode'][1]:    


            if keys[pygame.K_x]:

                # Right movement of the line
                if keys[pygame.K_RIGHT]:

                    var_params_dict['x'] += steps_dict_constants['x'] * factors_dict['x']          

                    updates_dict['update_screen'], updates_dict['update_line'] = True, True

                # Left movement of the line
                elif keys[pygame.K_LEFT]:
                    var_params_dict['x'] -= steps_dict_constants['x'] * factors_dict['x']

                    updates_dict['update_screen'], updates_dict['update_line'] = True, True

            elif keys[pygame.K_w]:

                # Increase angular velocity `w`    
                if keys[pygame.K_UP]:
                    var_params_dict['w'] += steps_dict_constants['w'] * factors_dict['w']

                    updates_dict['update_screen'], updates_dict['update_spiral'] = True, True
                    
                    var_params_dict['w'] = round(var_params_dict['w'], 14)

                # Decrease angular velocity `w`  
                elif keys[pygame.K_w] and keys[pygame.K_DOWN]:

                    var_params_dict['w'] -= steps_dict_constants['w'] * factors_dict['w']

                    updates_dict['update_screen'], updates_dict['update_spiral'] = True, True

                    var_params_dict['w'] = round(var_params_dict['w'], 14)
                    
            elif keys[pygame.K_k]:

                # Increase initial spiral angle coefficient `k`
                if keys[pygame.K_UP]:

                    var_params_dict['k'] += steps_dict_constants['k'] * factors_dict['k']


                    if const_params_dict['k'] + var_params_dict['k'] >= 4:         
                        var_params_dict['k'] = 0
                        
                    var_params_dict['k'] = round(var_params_dict['k'], 14)

                    updates_dict['update_screen'], updates_dict['update_spiral'] = True, True


                # Decrease initial spiral angle coefficient `k`
                elif keys[pygame.K_DOWN]:

                    var_params_dict['k'] -= steps_dict_constants['k'] * factors_dict['k']

                    if const_params_dict['k'] + var_params_dict['k'] <= 0:         
                        var_params_dict['k'] = 4
                        
                    var_params_dict['k'] = round(var_params_dict['k'], 14)

                    updates_dict['update_screen'], updates_dict['update_spiral'] = True, True


            elif keys[pygame.K_v]:

                # Increase spiral radius velocity `v`
                if keys[pygame.K_UP]:
                    var_params_dict['v'] += steps_dict_constants['v'] * factors_dict['v']          


                    updates_dict['update_screen'], updates_dict['update_spiral'] = True, True

                # Decrease spiral radius velocity `v`
                elif keys[pygame.K_DOWN]:      
                    
                    possible_v = const_params_dict['v'] + (var_params_dict['v'] - steps_dict_constants['v'] * 
                                 factors_dict['v'])
                    if possible_v >= 0:
                    
                        var_params_dict['v'] -= steps_dict_constants['v'] * factors_dict['v']

                        updates_dict['update_screen'], updates_dict['update_spiral'] = True, True



            elif keys[pygame.K_t]:

                # Increase time `t`
                if keys[pygame.K_UP]:
                    var_params_dict['t'] += steps_dict_constants['t'] * factors_dict['t']            

                    updates_dict['update_screen'], updates_dict['update_spiral'] = True, True

                # Decrease time `t`
                elif keys[pygame.K_DOWN]:  

                    possible_t = const_params_dict['t'] + (var_params_dict['t'] - steps_dict_constants['t'] * 
                                 factors_dict['t']) 
                    
                    if possible_t >= 0:
                        var_params_dict['t'] -= steps_dict_constants['t'] * factors_dict['t']

                        updates_dict['update_screen'], updates_dict['update_spiral'] = True, True
                        
            # Line parameters
            elif keys[pygame.K_a]:

                # Increase slope `a`
                if keys[pygame.K_UP]:
                    
                    
                    line_params_dict['a'] += steps_dict_constants['a'] * factors_dict['a']
                    
                    line_params_dict['a'] = round(line_params_dict['a'], 14)
                    
                    line_params_dict['a'] = handle_line_param_a(line_params_dict['a'])
                    
                    

                    updates_dict['update_screen'], updates_dict['update_line'] = True, True

                # Decrease slope `a`
                elif keys[pygame.K_DOWN]:  

                    line_params_dict['a'] -= steps_dict_constants['a'] * factors_dict['a']
                    
                    line_params_dict['a'] = round(line_params_dict['a'], 14)
                    
                    line_params_dict['a'] = handle_line_param_a(line_params_dict['a'])



                    updates_dict['update_screen'], updates_dict['update_line'] = True, True
                    
            elif keys[pygame.K_b]:

                # Increase line constant `b`
                if keys[pygame.K_UP]:
                    line_params_dict['b'] += steps_dict_constants['b'] * factors_dict['b']
                    
                    line_params_dict['b'] = round(line_params_dict['b'], 14)

                    updates_dict['update_screen'], updates_dict['update_line'] = True, True

                # Decrease line constant `b`
                elif keys[pygame.K_DOWN]:  

                    line_params_dict['b'] -= steps_dict_constants['b'] * factors_dict['b']  

                    line_params_dict['b'] = round(line_params_dict['b'], 14)


                    updates_dict['update_screen'], updates_dict['update_line'] = True, True


def handle_shift_key_commands(event, data_processing):
     
    if not data_processing.mode_statuses_dict['Steps change'][1]:    
        updates_dict = data_processing.booleans.update_booleans_dict    
        const_params_dict = data_processing.constants.constants_dict    
        var_params_dict = data_processing.variables.variables_dict
        mode_statuses_dict = data_processing.mode_statuses_dict

        # Turn the direction of the spiral
        if event.type == pygame.KEYDOWN:

            updates_dict['update_screen'] = True

            if (pygame.key.get_mods() & pygame.KMOD_SHIFT) and event.key == pygame.K_w:
                const_params_dict['w'] *= -1

                var_params_dict['w'] *= -1

                updates_dict['update_spiral'] = True 


            # Reset variables to their initial values
            elif (pygame.key.get_mods() & pygame.KMOD_SHIFT):

                if event.key == pygame.K_r:

                    data_processing.reset_dicts()
              
                    updates_dict['update_spiral'], updates_dict['update_line'], updates_dict['reset_background'] = True, True, True

                keys = pygame.key.get_pressed()

                # Change the degree of the spiral curve
                if keys[pygame.K_e]:

                    add_num = data_processing.constants.steps_constants_dict['deg']

                    if keys[pygame.K_UP]:
                        var_params_dict['deg'][1] += add_num

                    elif keys[pygame.K_DOWN]:
                        var_params_dict['deg'][1] -= add_num

                    elif keys[pygame.K_RIGHT]:
                        var_params_dict['deg'][0] += add_num

                    elif keys[pygame.K_LEFT]:
                        var_params_dict['deg'][0] -= add_num

                    updates_dict['update_spiral'] = True


def handle_ctrl_commands(event, data_processing):
    
    updates_dict = data_processing.booleans.update_booleans_dict
    mode_statuses_dict = data_processing.mode_statuses_dict
    
    updates_dict['is_turn_off'] = None
    updates_dict['is_t_diagram_change'] = False
    
    if event.type == pygame.KEYDOWN:
        
        mods = pygame.key.get_mods()
        updates_dict['update_screen'] = True
        
        if not mode_statuses_dict['Steps change'][1]:
        
            if (mods & pygame.KMOD_CTRL)  and event.key == pygame.K_a:

                if not mode_statuses_dict['T-diagram'][1]:
                    init_state = mode_statuses_dict['Algorithm mode'][1]
                    mode_statuses_dict['Algorithm mode'][1] = False if init_state else True
                    
                    if not mode_statuses_dict['Algorithm mode'][1]:
                        mode_statuses_dict['Equation mode'][1] = False

                    if init_state:
                        updates_dict['is_turn_off'] = True

                    if mode_statuses_dict['Algorithm mode'][1]:
                        mode_statuses_dict['T-diagram'][1] = False
                        mode_statuses_dict['Steps change'][1] = False

                    # Set the layers to True
                    for mode, (_, boolean) in mode_statuses_dict.items():
                        if mode not in ['Algorithm mode', 'T-diagram', 'Algorithm data mode',
                                        'Steps change', 'General solution', 
                                        'Zero missing point', 'X_line-X_s diff', 'Equation mode']:
                            if not boolean:
                                mode_statuses_dict[mode][1] = True 

            elif (mods & pygame.KMOD_CTRL) and event.key == pygame.K_t:

                if not mode_statuses_dict['Algorithm mode'][1]:
                    data_processing.switch_mode('T-diagram')
                    # mode_statuses_dict['T-diagram'][1] = not mode_statuses_dict['T-diagram'][1]
                    updates_dict['is_t_diagram_change'] = True
                    updates_dict['update_line'] = True

                    if mode_statuses_dict['T-diagram'][1]:

                        mode_statuses_dict['Algorithm mode'][1] = False
                        mode_statuses_dict['Vertical line'][1] = True
                        mode_statuses_dict['Derivatives'][1] = False
                        mode_statuses_dict['Y-intersects'][1] = True
                        mode_statuses_dict['Line-intersects'][1] = True
                        

        if not mode_statuses_dict['Algorithm mode'][1]:
            if (mods & pygame.KMOD_CTRL) and event.key == pygame.K_f:
                data_processing.switch_mode('Steps change')

                if mode_statuses_dict['Steps change'][1]:

                    mode_statuses_dict['Algorithm mode'][1] = False 
                    # mode_statuses_dict['T-diagram'][1] = False
                    
                else:
                    mode_statuses_dict['Y-intersects'][1] = True
                    mode_statuses_dict['Line-intersects'][1] = True

def handle_algorithm_mode_controls(event, data_processing, t_mth_aproxim_list):

    algorithm_variables_dict = data_processing.algorithm_vars.algorithm_vars_dict    

    n = algorithm_variables_dict['n'] 
    m = algorithm_variables_dict['m']
    total_n = algorithm_variables_dict['total_n']

    keys = pygame.key.get_pressed()
   
    if event.type == pygame.KEYDOWN:
        data_processing.booleans.update_booleans_dict['update_screen'] = True
        
        if keys[pygame.K_n] and keys[pygame.K_UP]:

            if n+1 <= total_n-1:

                algorithm_variables_dict['n'] +=1
                algorithm_variables_dict['m'] = 0

                t_mth_aproxim_list.clear()

               

        elif keys[pygame.K_n] and keys[pygame.K_DOWN]:

            if n > 0:
                algorithm_variables_dict['n'] -=1
                algorithm_variables_dict['m'] = 0

                t_mth_aproxim_list.clear()
           
        elif keys[pygame.K_m] and keys[pygame.K_UP]:

            algorithm_variables_dict['m'] +=1


        elif keys[pygame.K_m] and keys[pygame.K_DOWN]:

            if m-1 >= 0:
                algorithm_variables_dict['m'] -=1

                
    return t_mth_aproxim_list



def handle_switch_commands(event, data_processing):
    
    if not data_processing.mode_statuses_dict['Steps change'][1]:
    
        mode_statuses_dict = data_processing.mode_statuses_dict

        if event.type == pygame.KEYDOWN:

            if not mode_statuses_dict['Algorithm mode'][1]:

                if event.key == pygame.K_l:

                    data_processing.switch_mode('Vertical line')


                elif event.key == pygame.K_s:

                    data_processing.switch_mode('Spiral')

                elif event.key == pygame.K_n:

                    data_processing.switch_mode('Y-intersects')

                elif event.key == pygame.K_m:

                    data_processing.switch_mode('Line-intersects')

                elif event.key == pygame.K_p:

                    data_processing.switch_mode('Parameters')
                    # data_processing.switch_mode('Modes layer')
                    

                elif event.key == pygame.K_c:

                    data_processing.switch_mode('Coordinates')

                elif event.key == pygame.K_d:

                    data_processing.switch_mode('Derivatives')

                    if mode_statuses_dict['Derivatives'][1]:
                        mode_statuses_dict['Y-intersects'][1] = False
                        mode_statuses_dict['Line-intersects'][1] = False

                    else:
                        mode_statuses_dict['Y-intersects'][1] = True
                        mode_statuses_dict['Line-intersects'][1] = True
                        
                elif event.key == pygame.K_g:
                    data_processing.switch_mode('General solution')
                    data_processing.booleans.update_booleans_dict['update_line'] = True
                    data_processing.mode_statuses_dict['Equation mode'][1] = False
                    
                    data_processing.mode_statuses_dict['Modes layer'][1] = True
                    
                elif event.key == pygame.K_j:
                    data_processing.switch_mode('Rotated background')
                    data_processing.booleans.update_booleans_dict['update_line'] = True
                    
                elif event.key == pygame.K_y:
                    data_processing.switch_mode('Zero missing point')
                    data_processing.booleans.update_booleans_dict['update_screen'] = True
                    data_processing.booleans.update_booleans_dict['update_line'] = True
                    
                elif event.key == pygame.K_o:
                    data_processing.switch_mode('Circle layer')
                    data_processing.booleans.update_booleans_dict['update_screen'] = True
                    layer_status = data_processing.mode_statuses_dict['Circle layer'][1]
                    data_processing.mode_statuses_dict['Explanations layer'][1] = layer_status
                    data_processing.booleans.update_booleans_dict['update_circle'] = layer_status
                    
                    for layer, data in data_processing.mode_statuses_dict.items():
                        if layer in ['Vertical line', 'Spiral', 'Y-intersects', 'Line-intersects', 
                                     'Parameters']:
                            data[1] = True if not layer_status else False
                            
                elif event.key == pygame.K_1:
                    data_processing.switch_mode('X_line-X_s diff')
            
            else:
            
                if event.key == pygame.K_e:
                
                    if data_processing.mode_statuses_dict['Algorithm mode'][1]:
                     
                        data_processing.switch_mode('Equation mode')
                        data_processing.mode_statuses_dict['Modes layer'][1] = not data_processing.mode_statuses_dict['Equation mode'][1]     

                   
           

                        
                        
def get_factor_length(value):

    length_factor = 0
  
    if value < 1:
           
        string_value = str(value)
        
        if 'e' in string_value:
            length_factor = int(string_value.split('-')[1])
            
        else:
            string_value = string_value.split('.')[1]

            for index, symbol in enumerate(string_value):
                if symbol == '1':
                 
                    length_factor = index + 1
                
    if length_factor == 0:
        value = int(value)
    
    else:
        
        value = float(f'{value:.{length_factor}f}')
        
    return value
    

                        
def handle_steps_variables(event, data_processing):
    
    if data_processing.mode_statuses_dict['Steps change'][1]:
        
        updates_dict = data_processing.booleans.update_booleans_dict    
        # const_params_dict = data_processing.constants.constants_dict    
        # var_params_dict = data_processing.variables.variables_dict
        mode_statuses_dict = data_processing.mode_statuses_dict
        factors_dict = data_processing.variables.factors_dict
        
        
        if event.type == pygame.KEYDOWN:
            
            # Check for key combinations
            keys = pygame.key.get_pressed()
            
            updates_dict['update_screen'] = True
            updates_dict['update_spiral'] = False
            updates_dict['update_line'] = False
            mode_statuses_dict['Y-intersects'][1] = False
            mode_statuses_dict['Line-intersects'][1] = False
            
            max_step = data_processing.constants.max_step
            min_step = data_processing.constants.min_step
            
            # Increase and decrease `x_step`
            if keys[pygame.K_x]:
                
                if keys[pygame.K_UP]:
                
                    if factors_dict['x'] < max_step:

                        factors_dict['x'] *= 10

                        factors_dict['x'] = get_factor_length(factors_dict['x'])
                
                elif keys[pygame.K_DOWN]:

                    if min_step <factors_dict['x']: 

                        factors_dict['x'] /=10

                        factors_dict['x'] = get_factor_length(factors_dict['x'])
            
            # Increase and decrease `w_step`
            elif keys[pygame.K_w]:
                
                if keys[pygame.K_UP]:
                
                    if factors_dict['w'] < max_step:

                        factors_dict['w'] *= 10

                        factors_dict['w'] = get_factor_length(factors_dict['w'])
                
                elif keys[pygame.K_DOWN]:

                    if min_step <factors_dict['w']: 

                        factors_dict['w'] /=10

                        factors_dict['w'] = get_factor_length(factors_dict['w'])
            
            # Increase and decrease `k_step`
            elif keys[pygame.K_k]:
                
                if keys[pygame.K_UP]:
                
                    if factors_dict['k'] < max_step/10:

                        factors_dict['k'] *= 10

                        factors_dict['k'] = get_factor_length(factors_dict['k'])
                
                elif keys[pygame.K_DOWN]:

                    if min_step <factors_dict['k']: 

                        factors_dict['k'] /=10

                        factors_dict['k'] = get_factor_length(factors_dict['k'])
                        
            
            # Increase and decrease `v_step`
            elif keys[pygame.K_v]:
                
                if keys[pygame.K_UP]:
                
                    if factors_dict['v'] < max_step:

                        factors_dict['v'] *= 10

                        factors_dict['v'] = get_factor_length(factors_dict['v'])
                
                elif keys[pygame.K_DOWN]:

                    if min_step <factors_dict['v']: 

                        factors_dict['v'] /=10

                        factors_dict['v'] = get_factor_length(factors_dict['v'])
            
            
            # Increase and decrease `t_step`
            elif keys[pygame.K_t]:
                
                if keys[pygame.K_UP]:
                
                    if factors_dict['t'] < max_step:

                        factors_dict['t'] *= 10

                        factors_dict['t'] = get_factor_length(factors_dict['t'])
                
                elif keys[pygame.K_DOWN]:

                    if min_step <factors_dict['t']: 

                        factors_dict['t'] /=10

                        factors_dict['t'] = get_factor_length(factors_dict['t'])
                        
            # Increase and decrease `a_step`
            elif keys[pygame.K_a]:
                
                if keys[pygame.K_UP]:
                
                    if factors_dict['a'] < max_step:

                        factors_dict['a'] *= 10

                        factors_dict['a'] = get_factor_length(factors_dict['a'])
                
                elif keys[pygame.K_DOWN]:

                    if min_step <factors_dict['a']: 

                        factors_dict['a'] /=10

                        factors_dict['a'] = get_factor_length(factors_dict['a'])
                        
            # Increase and decrease `b_step`
            elif keys[pygame.K_b]:
                
                if keys[pygame.K_UP]:
                
                    if factors_dict['b'] < max_step:

                        factors_dict['b'] *= 10

                        factors_dict['b'] = get_factor_length(factors_dict['b'])
                
                elif keys[pygame.K_DOWN]:

                    if min_step <factors_dict['b']: 

                        factors_dict['b'] /=10

                        factors_dict['b'] = get_factor_length(factors_dict['b'])
