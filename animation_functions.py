import pygame 
import numpy as np
from scipy.integrate import quad

from formula_functions import *


def create_background(data_processing, font_small):
    
    background_surface = data_processing.animation_layers.layers_dict['background_surface']
    screen_width = data_processing.constants.screen_width
    screen_height = data_processing.constants.screen_height
    length = data_processing.get_curr_param('l')
    
    background_surface.fill(data_processing.bg_color)

    line_color = (200,200,200)
    center_point = data_processing.get_curr_param('c')

    # Coordinate x-line parameters
    x_line_start = 0
    x_line_end = screen_width
    
    #Coordinate y-line parameters
    y_line_start = 0
    y_line_end = screen_height
    
    # Height of the numbers lines
    y_line = center_point[1]
    
    # Width of the numbers lines
    x_line = center_point[0]
    

    
    pygame.draw.line(background_surface, color=line_color, start_pos=(x_line_start, y_line),
                         end_pos = (x_line_end, y_line), width=2)
    
    pygame.draw.line(background_surface, color=line_color, start_pos=(x_line, y_line_start),
                         end_pos = (x_line, y_line_end), width=2)

    pygame.draw.circle(background_surface, color='darkgrey', center=center_point, radius=4)
    
    # Upper and lower bounds of the vertical divisions of the x-axis
    vertical_line_start = y_line - 5
    vertical_line_end = y_line + 5
    
    # Upper and lower bounds of the horizontal divisions of the y-axis
    horizontal_line_start = x_line - 5
    horizontal_line_end = x_line + 5
    
    # Positions of the numbers relative to the corresponding axis line.
    number_y = vertical_line_end + 15
    number_x = horizontal_line_end + 15
        
    
    # Number of numbers that need to be displayed on the screen.
    pos_x_axis_nums_count = int(np.ceil((screen_width - center_point[0])/length))
    neg_x_axis_nums_count = int(np.ceil(center_point[0]/length))
    pos_y_axis_nums_count = int(np.ceil(center_point[1]/length))
    neg_y_axis_nums_count = int(np.ceil(screen_height - center_point[1]/length))


    
    #Draw positive x-axis numbers
    if pos_x_axis_nums_count >= 0:    
        
        for i in range(pos_x_axis_nums_count):

            draw_x_axis_pos_values(background_surface, center_point[0], screen_width, screen_height,
                                   i, length, x_line_start,vertical_line_start, vertical_line_end,
                                   line_color, font_small, number_y)
            
    # Draw negative x-axis numbers 
    if neg_x_axis_nums_count >= 0:
           
        for i in range(neg_x_axis_nums_count):
            draw_x_axis_neg_values(background_surface, center_point[0], screen_width, screen_height,
                                i, length, x_line_start,vertical_line_start, vertical_line_end, line_color,
                               font_small, number_y)

        
    #Draw positive y-axis numbers
    if pos_y_axis_nums_count >= 0:
        
        for i in range(pos_y_axis_nums_count):
            
            draw_y_axis_pos_values(background_surface, center_point[1], screen_width, screen_height,
                                   i, length, y_line_start,horizontal_line_start, horizontal_line_end, 
                                   line_color,font_small,number_x)
        
    #Draw negative y-axis numbers
    if neg_y_axis_nums_count >=0:
        
        for i in range(neg_y_axis_nums_count):

            draw_y_axis_neg_values(background_surface, center_point[1], screen_width, screen_height,
                    i, length, y_line_start,horizontal_line_start,
                    horizontal_line_end, line_color,font_small, number_x) 

            
def draw_x_axis_pos_values(background_surface, center_point_x, screen_width, screen_height,
                i, length, x_line_start,vertical_line_start,
                vertical_line_end, line_color,font_small,number_y):
    
    
    vertical_line_x_pos = center_point_x + i*length
   
    
    if vertical_line_x_pos <= screen_width:
        
        #Draw unit lines for positive x-axis
        pygame.draw.line(background_surface, color = line_color, start_pos=(vertical_line_x_pos, vertical_line_start),
                     end_pos = (vertical_line_x_pos, vertical_line_end), width=1)  

        #Draw zero
        if i == 0:
            pos_number_text = font_small.render(f'{i}', True, line_color)
            background_surface.blit(pos_number_text, (vertical_line_x_pos-15,number_y-4))

        else:
            #Draw positive numbers
            pos_number_text = font_small.render(f'{i}', True, line_color)
            background_surface.blit(pos_number_text, (vertical_line_x_pos-5,number_y-4))



            
            
def draw_x_axis_neg_values(background_surface, center_point_x, screen_width, screen_height,
                            i, length, x_line_start,vertical_line_start, vertical_line_end, line_color,
                           font_small,number_y):
    
    vertical_line_x_neg = center_point_x - i*length
    
    if vertical_line_x_neg >= 0:
        #Draw unit lines for negative x-axis
        pygame.draw.line(background_surface, color = line_color, start_pos=(vertical_line_x_neg, vertical_line_start),
                     end_pos = (vertical_line_x_neg, vertical_line_end), width=1)  
        
        if i != 0:
            #Draw negative numbers
            neg_number_text = font_small.render(f'-{i}', True, line_color)
            background_surface.blit(neg_number_text, (vertical_line_x_neg-12,number_y-4)) 

    
    
def draw_y_axis_pos_values(background_surface, center_point_y, screen_width, screen_height,
                i, length, y_line_start,horizontal_line_start,
                horizontal_line_end, line_color,font_small, number_x):

    horizontal_line_y_pos = center_point_y - i*length

    #Draw unit lines for positive y-axis
    pygame.draw.line(background_surface, color = line_color, start_pos=(horizontal_line_start, horizontal_line_y_pos),
             end_pos = (horizontal_line_end, horizontal_line_y_pos), width=1)

    if i >=1:

        #Draw positive numbers
        neg_number_text = font_small.render(f'{i}', True, line_color)
        background_surface.blit(neg_number_text, (number_x-46,horizontal_line_y_pos-4))
        
        
def draw_y_axis_neg_values(background_surface, center_point_y, screen_width, screen_height,
                i, length, y_line_start,horizontal_line_start,
                horizontal_line_end, line_color,font_small, number_x):
    
    horizontal_line_y_neg = center_point_y + i*length


    #Draw unit lines for negative y-axis
    pygame.draw.line(background_surface, color = line_color, start_pos=(horizontal_line_start, horizontal_line_y_neg),
             end_pos = (horizontal_line_end, horizontal_line_y_neg), width=1)


    if i >=1:
       
        #Draw negative numbers
        neg_number_text = font_small.render(f'-{i}', True, line_color)
        background_surface.blit(neg_number_text, (number_x-46,horizontal_line_y_neg-4)) 

        
        
            
def x_transform(x, curr_screen_width,length):
    
    return x* length + curr_screen_width


def x_inverse_transform(x, curr_screen_width,length):
    
    return (x - curr_screen_width) / length


def y_transform(y, curr_screen_height,length):
    
    return -y * length + curr_screen_height


def transform_to_t_diagram(x, curr_screen_width, curr_screen_height, length):
    
    x = x_inverse_transform(x, curr_screen_width, length)
    x = y_transform(x, curr_screen_height, length)
    
    return x

def calc_x_derivative(t, v, w, k):
    
    theta = k* np.pi/2 + w * t
    
    return v*( np.cos(theta) - w* t * np.sin(theta))


def calc_y_derivative(t, v, w, k):
    
    theta = k* np.pi/2 + w * t
    
    return v*( np.sin(theta) + w* t * np.cos(theta))





def calc_spiral_length(t, v, w, k):

    a = 0

    def f(t):
       
        dx_dt = calc_x_derivative(t, v, w, k)
        dy_dt = calc_y_derivative(t, v, w, k)
        
        return np.sqrt(dx_dt**2 + dy_dt **2)

    length, _ = quad(f, a, t)
    
    return length

      
def calc_spiral_coord(deg=0, t=1 ,v=1, w=1, k=0) -> tuple:
    
    theta_0 = k * np.pi/2

    lin_space = (0, t)
    
    num = 300

    T = np.linspace(*lin_space, num)
    
    x = np.array([get_nth_deg_x_derivative(deg,t, v,w,k) for t in T])
    y = np.array([get_nth_deg_y_derivative(deg,t, v,w,k) for t in T])
    
    return x, y, T 

def calc_y_intersects_t(t, w, k) -> list:
    
    is_bigger = False
    t_list = []
    
    
    if abs(w) == 0:
        is_bigger = True
  
    n = 1
    
    while not is_bigger:
        curr_t = get_nth_intersect(n, k, w)
        
        if abs(curr_t) <= abs(t):
            t_list.append(curr_t)
            n += 1
        else:
            is_bigger = True
            
    return t_list


def calc_line_intersections_t(t_nth_list,deg, x, v, w, k, correction_mech=False, f_binary=False, accuracy=5, i=200) -> list:
    
    t_mth_list = []
    for t_nth in t_nth_list:
        curr_t_mth = get_mth_aproximation(t_nth, deg, x, v, w, k, i=200, accuracy=5)
        t_mth_list.append(curr_t_mth)
        
    return t_mth_list


def calc_single_t_aproxim(deg, v, w, k, t, center_point_width, center_point_height, length, transform=True):
   
    x = get_nth_deg_x_derivative(deg, t, v, w, k)
    y = get_nth_deg_y_derivative(deg, t, v, w, k)
    
    
    if transform:
        x = x_transform(x, center_point_width, length)
        y = y_transform(y, center_point_height, length)

    return x, y


def draw_vertical_line(data_processing, x_axis_value=1):
    
    line_layer = data_processing.animation_layers.layers_dict['vertical_line_layer']
    screen_height = screen_height = data_processing.constants.screen_height
    length = data_processing.get_curr_param('l')
        
    line_layer.fill((0, 0, 0, 0))
    

    center_point_width = data_processing.get_curr_param('c')[0]

    x_up, y_up  = x_transform(x_axis_value, center_point_width, length),y_transform(0, screen_height, length)
    x_down, y_down = x_transform(x_axis_value, center_point_width, length),y_transform(screen_height, 0, length)
    
    pygame.draw.aalines(line_layer, 'blue',  False, [(x_up, y_up), (x_down, y_down)])
    
    

def draw_spiral(data_processing):
    
    spiral_layer = data_processing.animation_layers.layers_dict['spiral_layer']
    spiral_layer.fill((0, 0, 0, 0))
    
    # Get current coordinate center point position on the screen    
    center_point_width, center_point_height = data_processing.get_curr_param('c')
    
    half_screen_width, half_screen_height = data_processing.constants.half_screen_width, data_processing.constants.half_screen_height
    
    
    # Current unit length of the coordinate system
    length = data_processing.get_curr_param('l')
    
    # Current spiral degree
    deg = data_processing.get_curr_param('deg')
    
    # Curr time
    t = data_processing.get_curr_param('t')
    
    # Curr vector velocity
    v = data_processing.get_curr_param('v')
    
    # Curr angular velocity
    w = data_processing.get_curr_param('w')
    
    # Curr initial spiral angle
    k = data_processing.get_curr_param('k')

    if w != 0:
        x_spiral, y_spiral, T = calc_spiral_coord(deg=deg,t=t ,v=v, w=w, k=k)
        
        # Euclidеan distances list
        rad_vec_distances = np.sqrt(x_spiral**2 + y_spiral**2)
        rad_vec_distances = [y_transform(y, center_point_height, length) for y in rad_vec_distances]
        
        # Transform the x and y spiral coords into the screen coordinate system
        x_spiral = [x_transform(x, center_point_width, length) for x in x_spiral]
        y_spiral = [y_transform(y, center_point_height, length) for y in y_spiral]

        for i in range(len(x_spiral) -1):

            curr_sp_point_x, curr_sp_point_y = x_spiral[i], y_spiral[i]
            next_sp_point_x, next_sp_point_y = x_spiral[i+1], y_spiral[i+1]
            
            # Check if the points are within the screen boundaries.
            if not data_processing.mode_statuses_dict['T-diagram'][1]:
                if (0 <=abs(curr_sp_point_x)<=half_screen_width * 2) and \
                   (0 <=abs(curr_sp_point_y)<=half_screen_height * 2):

                    pygame.draw.aalines(spiral_layer, 'red',  False, [(curr_sp_point_x, curr_sp_point_y), \
                                                                      (next_sp_point_x, next_sp_point_y)])
            else:

                curr_t_point = T[i]
                curr_t_point = x_transform(curr_t_point, center_point_width, length)
                
                next_t_point = T[i+1]
                next_t_point= x_transform(next_t_point, center_point_width, length)

                backward_curr_sp_x = transform_to_t_diagram(curr_sp_point_x, center_point_width, center_point_height, length)
                backward_next_sp_x = transform_to_t_diagram(next_sp_point_x, center_point_width, center_point_height, length)
            
                # Euclidean distances 
                curr_rad_vec_dist = rad_vec_distances[i]
                next_rad_vec_dist = rad_vec_distances[i+1]
       
                # Check if the points are within the screen boundaries.
                if (0 <=abs(curr_t_point)<=half_screen_width * 2) and \
                   (0 <=abs(curr_sp_point_y) <=half_screen_height * 2 or \
                    0 <=abs(backward_next_sp_x) <= half_screen_height * 2 or \
                    0 <= abs(next_rad_vec_dist) <= half_screen_height * 2): 


                    pygame.draw.aalines(spiral_layer, 'red',  False, [(curr_t_point, backward_curr_sp_x), \
                                                                      (next_t_point, backward_next_sp_x)])

                    pygame.draw.aalines(spiral_layer, 'blue',  False, [(curr_t_point, curr_sp_point_y), \
                                                                      (next_t_point, next_sp_point_y)])
                    
                    pygame.draw.aalines(spiral_layer, 'green',  False, [(curr_t_point, curr_rad_vec_dist), \
                                                                       (next_t_point, next_rad_vec_dist)])
                    
                    
        if data_processing.mode_statuses_dict['T-diagram'][1]:

            last_t = x_transform(T[-1], center_point_width, length)
            
            last_rad_vec =  T[-1] * v
            
            last_spiral_x = get_nth_deg_x_derivative(deg, T[-1], v,w, k)
            last_spiral_y = get_nth_deg_y_derivative(deg, T[-1], v,w, k)
            
            last_rad_vec = np.sqrt(last_spiral_x**2 + last_spiral_y ** 2)
            last_rad_vec = y_transform(last_rad_vec, center_point_height, length)

            
            # Draw spiral radius vector
            start_pos = (last_t, y_transform(0 , center_point_height, length)) 
            end_pos = (last_t, last_rad_vec)            
            draw_vector(spiral_layer,start_pos, end_pos, color='black')
                                                                          
                
                
                
def draw_dots(data_processing, t_list, layer):
    
    color = 'black' if layer == 'Y-intersects' else 'purple'
    
    layer = data_processing.mode_statuses_dict[layer][0]
    layer.fill((0, 0, 0, 0))

    const_center_point = data_processing.constants.constants_dict['c']
    var_center_point = data_processing.variables.variables_dict['c']
    
    length = data_processing.get_curr_param('l')
    
    deg = data_processing.get_curr_param('deg')
    v = data_processing.get_curr_param('v')
    w = data_processing.get_curr_param('w')
    k = data_processing.get_curr_param('k')
    
    t_diagram = data_processing.mode_statuses_dict['T-diagram'][1]
    
    center_point_width = const_center_point[0] + var_center_point[0]
    center_point_height = const_center_point[1] + var_center_point[1]
    
    if t_list:
        theta_0 = k * np.pi/2

        for t in t_list:
 
            x = get_nth_deg_x_derivative(deg,t, v,w,k)
            y = get_nth_deg_y_derivative(deg,t, v,w,k)
            
            x = x_transform(x, center_point_width, length)
            y = y_transform(y, center_point_height, length)
            
            if not t_diagram:
            
                pygame.draw.circle(layer, color=color, center=(x, y), radius=4)
                
            else:
                
                t_trans = x_transform(t, center_point_width, length)
                x_new = transform_to_t_diagram(x, center_point_width, center_point_height, length)
             
                pygame.draw.circle(layer, color=color, center=(t_trans, y), radius=4)
                pygame.draw.circle(layer, color=color, center=(t_trans, x_new), radius=4) 
    
def get_line_boundary_points(length, angle, x, y):
    
    x_leg = length * np.cos(angle) 
    y_leg = length * np.sin(angle)
    
    front_xx = x + x_leg 
    front_xy = y - y_leg
    
    back_xx = x - x_leg
    back_xy = y + y_leg
    
    return front_xx, front_xy, back_xx, back_xy    
    
                
def draw_derivatives(layer, deg, t, v, w, k, const_center_point, var_center_point, 
                     screen_width, screen_height, length,
                     t_diagram= False, show_derivatives=False):
    
    if show_derivatives:
        
        layer.fill((0, 0, 0, 0))

        x_der_color = 'red'
        y_der_color = 'blue'

        # t-=1
        
        center_point_width = const_center_point[0] + var_center_point[0]
        center_point_height = const_center_point[1] + var_center_point[1]

        theta = k*np.pi/2 + w*t
        

        
        # Current point spiral coords 
        x = get_nth_deg_x_derivative(deg,t, v,w,k)
        y = get_nth_deg_y_derivative(deg,t, v,w,k)

        # Derivatives in this point 
        dx_dt = get_nth_deg_x_derivative(deg+1,t, v,w,k)
        dy_dt = get_nth_deg_y_derivative(deg+1,t, v,w,k)
        
        # Spiral derivative
        dx_dy = dy_dt/ dx_dt

        x_der_angle = np.arctan(dx_dt)
        y_der_angle = np.arctan(dy_dt)
        
        spiral_der_angle = np.arctan(dx_dy)

        x = x_transform(x, center_point_width, length)
        y = y_transform(y, center_point_height, length)

        ll = 3* length

        if t_diagram:
            t_trans = x_transform(t, center_point_width, length)
            x_new = transform_to_t_diagram(x, center_point_width, center_point_height, length)
            
            colors = iter([x_der_color, y_der_color])
            
            y_points = iter([x_new, y])
            
            for angle in [x_der_angle, y_der_angle]:

                front_xx, front_xy, back_xx, back_xy = get_line_boundary_points(ll, angle, t_trans, next(y_points))
                pygame.draw.aalines(layer, next(colors),  False, [(back_xx,  back_xy), (front_xx, front_xy)])

            pygame.draw.circle(layer, color=x_der_color, center=(t_trans, x_new), radius=4)
            pygame.draw.circle(layer, color=y_der_color, center=(t_trans, y), radius=4)
        


        else:
            colors = iter([x_der_color, y_der_color, 'green'])
            
            # Draw derivatives         
            for angle in [x_der_angle, y_der_angle, spiral_der_angle]:
            
                front_xx, front_xy, back_xx, back_xy = get_line_boundary_points(ll, angle, x, y)

                pygame.draw.aalines(layer, next(colors),  False, [(back_xx, back_xy), (front_xx, front_xy)])
                
            pygame.draw.circle(layer, color='purple', center=(x, y), radius=4)
    
        
def show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m, deg,  v, w, k,x_line,
                           const_center_point, var_center_point, length,
                           color, draw_leg_and_hip=False):
    
    center_point_width = const_center_point[0] + var_center_point[0]
    center_point_height = const_center_point[1] + var_center_point[1]
    
    curr_t = t_mth_aproxim_list[m]


    x, y = calc_single_t_aproxim(deg, v, w, k, curr_t, center_point_width, center_point_height, length)

    start_pos, end_pos = (center_point_width, center_point_height), (x, y)

    draw_vector(algorithm_layer, start_pos, end_pos, color=color)
    
    # Shows the step to construct the current radius vector based on the previous radius vector
    if draw_leg_and_hip:
        
        if m+1 <= len(t_mth_aproxim_list):
        
            x_line = x_transform(x_line, center_point_width, length)

            next_t = t_mth_aproxim_list[m+1]
            next_x, next_y = calc_single_t_aproxim(deg, v, w, k, next_t, center_point_width, center_point_height, length)


            # Draw horizontal leg
            pygame.draw.aalines(algorithm_layer, '#F2D9B2',  False, [(x, y), (x_line, y)])

            # Draw a part of the hipotenuse
            pygame.draw.aalines(algorithm_layer, '#F2D9B2',  False, [(next_x, next_y), (x_line, y)])

            # A point on the spiral curve
            pygame.draw.circle(algorithm_layer, color='red', center=(next_x, next_y), radius=4)

            # A crosspoint between horizontal leg and the hipotenuse 
            pygame.draw.circle(algorithm_layer, color='blue', center=(x_line, y), radius=4)
        
        
def draw_algorithm_steps(algorithm_layer, t_nth_list, deg, v, w, k, x, t_mth_aproxim_list, algorithm_variables_dict, 
                        const_center_point, var_center_point, length,
                         accuracy=5, curr_rad_vec_color='black', previous_rad_vec_color='lightgreen'):
    
    algorithm_layer.fill((0, 0, 0, 0))
    
    algorithm_variables_dict['total_n'] = len(t_nth_list) # Stores how many are the y-intersection points
  
    m = np.copy(algorithm_variables_dict['m'])

    if t_nth_list:
        
        if algorithm_variables_dict['n']  == 0:
            y_intersect_t = t_nth_list[0]
            algorithm_variables_dict['n']+=1
        else: 
            y_intersect_t = t_nth_list[algorithm_variables_dict['n'] -1]
        
        # Create list with interesection point aproximations and store it.
        if not t_mth_aproxim_list:
            '''t_nth, x_line, v, w, k, i=200, accuracy=5, correction_mech=False, f_binary=False'''
            zero_intersect_t = get_mth_aproximation(y_intersect_t, deg, x, v, w, k, i=1, accuracy=accuracy, correction_mech=False, f_binary=False)
            t_mth_aproxim_list.append(zero_intersect_t)
            
            # Show current radius-vector
            show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m, deg,  v, w, k,x,
                               const_center_point, var_center_point, length,
                               curr_rad_vec_color)
        
        else:
            if m +1 > len(t_mth_aproxim_list):
                
                
                next_t = get_mth_aproximation(y_intersect_t, deg, x, v, w, k, i=m+1,accuracy=accuracy,  correction_mech=False, f_binary=False)
                t_mth_aproxim_list.append(next_t)
                
                # Show previous radius vector if it exists
                if m -1>= 0:
                
                    show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m-1, deg,  v, w, k,x,
                                       const_center_point, var_center_point, length,
                                       previous_rad_vec_color, draw_leg_and_hip=True)
                
 
                # Show current radius-vector
                show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m, deg, v, w, k,x,
                                   const_center_point, var_center_point, length,
                                   curr_rad_vec_color)

                
            else:
              
                # Show previous radius vector if it exists
                if m -1>= 0:
                    show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m-1, deg, v, w, k,x,
                                       const_center_point, var_center_point, length,
                                       previous_rad_vec_color, draw_leg_and_hip=True)
                    
                # Show current radius-vector
                show_radius_vector_step(algorithm_layer, t_mth_aproxim_list, m, deg, v, w, k,x,
                                   const_center_point, var_center_point, length,
                                   curr_rad_vec_color)

    return t_mth_aproxim_list, algorithm_variables_dict




def draw_vector(layer, start_pos, end_pos, color=(255, 255, 255)):
  

    pygame.draw.aaline(layer, color, start_pos, end_pos)

    angle = np.arctan2(end_pos[1] - start_pos[1], end_pos[0] - start_pos[0])

    arrow_length = 10
    arrow_angle = np.pi / 6 


    arrow1 = (end_pos[0] - arrow_length * np.cos(angle - arrow_angle),
              end_pos[1] - arrow_length * np.sin(angle - arrow_angle))
    arrow2 = (end_pos[0] - arrow_length * np.cos(angle + arrow_angle),
              end_pos[1] - arrow_length * np.sin(angle + arrow_angle))

 
    pygame.draw.aaline(layer, color, end_pos, arrow1)
    pygame.draw.aaline(layer, color, end_pos, arrow2)

    