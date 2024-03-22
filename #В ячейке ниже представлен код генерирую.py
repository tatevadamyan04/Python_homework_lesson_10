#В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

#import random
#st = ['robot'] * 10
#st += ['human'] * 10
#andom.shuffle(lst)
#ata = pd.DataFrame({'whoAmI':lst})
#ata.head()

import random
import pandas as pd

# Creating a DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
# Unique values in column 'whoAmI'
unique_values = data['whoAmI'].unique()
# Creating a new DataFrame for one hot encoding
one_hot_data = pd.DataFrame(columns=unique_values)
# Filling new DataFrame with 0s
one_hot_data[unique_values] = 0
# Runing in columns and writing 1 where we need it
for idx, row in data.iterrows():
    one_hot_data.loc[idx, row['whoAmI']] = 1
# Printing the result
print(one_hot_data.head())