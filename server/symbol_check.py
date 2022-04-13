import lib_import as lib

def inputProcess(inputs): 
# Process user input
    valid_input = []
    for input in inputs:
        df = lib.pd.read_csv(r'C:\Users\khangn\Desktop\stonkRecomm\server\data.csv')
        symbols = df['Symbol'].values.tolist()
        #print(symbols)
        user_input = input
        user_input = user_input.upper()
        if user_input not in symbols:
            print(user_input + ' not valid')
        else:
            valid_input.append(user_input)
    
    return valid_input

   

#stock_list = ['TsLA','NvdA','AMD', 'dfsjkl']
#stock_test = inputProcess(stock_list)

#print(stock_test)