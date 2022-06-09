
import numpy as np
import json

def app(target_height):
    '''
        app function: load and tranform a JSON file with players full name
        and height in, both, inches and meters; and find which pairs of players'
        heights match a target height. 
        
        ex. 
            app(139) 
            >> [('Brevin Knight', 'Nate Robinson'), ('Nate Robinson', 'Mike Wilks')]
        
        input -> target_height: Int
        output -> players: List of Tuples
    '''
# Data loading and transformation
    file = "playerlist.json"
    data = json.load(open(file))
    values = data['values']
    
# Data Transformation
    full_names = [' '.join([dict_['first_name'], dict_['last_name']]) for dict_ in values]
    heights_in = [int(dict_['h_in']) for dict_ in values]
    
# Create triangular matrix with all possible sums of pair of heights
    mtx_heights = np.array(np.zeros((len(heights_in), len(heights_in))))
    for i, h in enumerate(heights_in):
        for j, h_ in enumerate(heights_in):
            mtx_heights[i,j] = h + h_

    mtx_heights = np.triu(mtx_heights)
    
# delete data and values to release some memory space
    del data
    del values
    
# find indeces where the target height is met
# comprise the pairs of players in tuples inside a list
    indeces = np.argwhere(mtx_heights == target_height)
    players = [(full_names[i], full_names[i_]) for i, i_ in indeces if i != i_]
    
    return players

if __name__ == "__main__":
    target_height = 139 # default value, Change here for another target height
    [print(pair) for pair in app(target_height)] # print results 
    
    
