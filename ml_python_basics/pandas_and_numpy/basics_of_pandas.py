import pandas
data_frame = pandas.DataFrame([[1,2,3], [4,5,6], [7,8,9]])
print(data_frame)
df1 = pandas.DataFrame([['19','22112015','22112019'],
                        ['4.99', '05012010', 'NaN'],
                        ['7.25', '08081988', '09091999']],
                       columns= ['price', 'DoM', 'DoE'],
                       index=['688001', '688002', '688003'])
print(df1)
print(df1.price)
print(df1.DoM)


