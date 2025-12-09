# Add all the imports needed by the functions in the project here
#================================================================
#
#================================================================

# Remember to modify your functions to use the template shown below

def function_name(input1: data_type1, input2: data_type2,..., opt_arg: data_type_opt= default_value) -> output_data_type:
    """
    This functions uses a REGEX to clean the text on the rows, like especial characters, spaces, etc. 
     But in this case it's applied to text, leaving the 
    """
    
    # Your function code here
def clean_string_content(text):
    if pd.isna(text):
        return text
    text = str(text)
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s.]+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text
    
text_cols = df.select_dtypes(include="object").columns
df[text_cols] = df[text_cols].applymap(clean_string_content)
df = df.applymap(clean_string_content)
    
    
    return opuput
