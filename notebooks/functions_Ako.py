"""this function reset the hidden index into start from 1, not 0"""

#reset index 
def index_reset () : 
    df.reset_index(drop=True, inplace=True)

    df.index = df.index + 1
    df.index.name = None

    return df 
    
index_reset ()

#cleaning datetime 
"""this function convert Release Year columns from data type 'object' to date-time"""

def datetime (): 
 df["release_year"] = pd.to_datetime(df["release_year"],errors="coerce")
 return df 
#df["Release Year"] = pd.to_numeric(df["Release Year"], errors='coerce')
#df["Release Year"] = df["Release Year"].astype("Int64")
datetime () 