import lib_import as lib

def match():
    df = lib.pd.read_csv('Stock_symbol.csv')
    symbols = df['Symbol'].values.tolist()
    name = df['Name'].values.tolist()
    comp_dict = dict(zip(name, symbols))
    return comp_dict

def get_name(val, comp_dict):
    for key, value in comp_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"

comp_list = match()
print(get_name('TSLA',comp_list))
