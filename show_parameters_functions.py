import pygame 
import numpy as np

def show_parameters(data_processing, font_small):
    
    params_layer = data_processing.mode_statuses_dict['Parameters'][0]
    params_layer.fill((0, 0, 0, 0))  
    
    const_params_dict = data_processing.constants.constants_dict
    var_params_dict = data_processing.variables.variables_dict
    
    text_x = data_processing.text_unit
    text_y = 3 * text_x
    
    for param  in data_processing.constants.constants_dict.keys():  
     
        if param != 'c' and param != 'l':
            curr_value = data_processing.get_curr_param(param)
            if param == 'k':
                theta_0 = (curr_value) * (np.pi /2) * 180 / np.pi 
                text = font_small.render(f'Start angle: {theta_0:.2f} deg', True, (0, 0, 0))

            else:
                
                if param == 'deg':
                    text = font_small.render(f'{param}: {curr_value}', True, (0, 0, 0))
                else:
                    text = font_small.render(f'{param}: {curr_value:.2f}', True, (0, 0, 0))

            params_layer.blit(text, (text_x, text_y))
            text_y += data_processing.text_unit



def show_mode_statuses(data_processing, font_small):
    
    if data_processing.mode_statuses_dict['Modes layer'][1]:
        
        show_modes_layer = data_processing.mode_statuses_dict['Modes layer'][0]
        show_modes_layer.fill((0, 0, 0, 0))

        text_x = data_processing.text_unit
        text_y = data_processing.text_unit

        for mode, status in data_processing.mode_statuses_dict.items():

            if mode not in ['Algorithm data mode','Modes layer']:

                statement = 'On' if status[1] else 'Off'
                expression = f'{mode}: {statement}'

                text = font_small.render(expression, True, (0, 0, 0))


                show_modes_layer.blit(text, (text_x, text_y))

                x_text_displacement = len(mode) * 12 + 25

                text_x += x_text_displacement
        

def show_algorithm_rows_and_cols(data_processing, x, y, font_small):
    
    show_algorithm_data_layer = data_processing.mode_statuses_dict['Algorithm data mode'][0]
    show_algorithm_data_layer.fill((0, 0, 0, 0))
    
    text_x = data_processing.text_unit
    text_y = 10 * data_processing.text_unit
    
    for param, value in data_processing.algorithm_vars.algorithm_vars_dict.items():

        text = font_small.render(f'{param}: {value}', True, (0, 0, 0))
        
        show_algorithm_data_layer.blit(text, (text_x, text_y))
        
        text_y += data_processing.text_unit
    
    text_y += data_processing.text_unit
    
    text = font_small.render(f'Spiral x: {x}', True, (0, 0, 0))
    show_algorithm_data_layer.blit(text, (text_x, text_y))
    
    text_y += data_processing.text_unit
    
    text = font_small.render(f'Spiral y: {y}', True, (0, 0, 0))
    
    show_algorithm_data_layer.blit(text, (text_x, text_y))