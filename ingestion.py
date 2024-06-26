import pandas as pd
import os
def csv_generator(input_file, output_file, target_variable, identifier_col, problem_type):
    file_ext = os.path.splitext(input_file)[1].lower()
    if file_ext in ['.xls', '.xlsx']:
        df = pd.read_excel(input_file)
    elif file_ext == '.csv':
        df = pd.read_csv(input_file)
    elif file_ext == '.json':
        df = pd.read_json(input_file)
    elif file_ext in ['.txt', '.tsv']:
        df = pd.read_csv(input_file, delimiter='\t')
    elif file_ext == '.parquet':
        df = pd.read_parquet(input_file)
    else:
        raise ValueError(f"Unsupported file type: {file_ext}")
    df.to_csv(output_file, index=False)
    print(f"File converted to CSV and saved as {output_file}")
    
    exp_config = {'prob_type': problem_type, 'target_var':target_variable,'identifier_column': identifier_col }
    return df, exp_config
#Returning both dataframe and csv for pre-processing