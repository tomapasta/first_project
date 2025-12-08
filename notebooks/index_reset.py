"""this function reset the hidden index into start from 1, not 0"""

#reset index 
def index_reset () : 
    df.reset_index(drop=True, inplace=True)

    df.index = df.index + 1
    df.index.name = None

    return df 
    
index_reset ()

