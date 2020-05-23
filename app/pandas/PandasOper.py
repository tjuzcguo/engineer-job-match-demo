import pandas as pd


# 读取文件

origin = pd.read_csv(r'../data/train.csv')

# print(origin.head())


data1 = origin[['GarageArea','1stFlrSF', 'YearBuilt', 'YrSold', 'BedroomAbvGr','KitchenAbvGr','KitchenQual','SalePrice']]

index = [0,1]

# print(data1.loc[index].head())

print(data1.loc[index,['GarageArea', '1stFlrSF']])

print(data1.iloc[0:10, 0:10])

print(data1[data1.YearBuilt > 2005])
