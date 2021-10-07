import pandas as pd
import warnings

with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    df = pd.read_excel(
        "/Users/dayong/project/algorithm/cvstest/cvsdata/부산환경_2020_사원등록_20211001_111155_.xlsx", engine="openpyxl", header=int(9), usecols="B,C,D")

data = df.dropna(how='all')


test = pd.DataFrame(data)
list_from_df = test.values.tolist()
# print(list_from_df)
# print(test.shape[0])
# print(test.shape)
# for i in list_from_df:
#     result = i.columns
# print(test)
# print(list_from_df[3][0])
no_list = []
number_list = []
name_list = []
iny_list = []
tny_list = []

for i in range(1, test.shape[0]):
    if i % 2 != 0:
        no_list.append(int(list_from_df[i][0]))
        # print(list_from_df[i][0])

for i in range(1, test.shape[0]):
    if i % 2 != 0:
        # print(list_from_df[i][1])
        number_list.append(list_from_df[i][1])
for i in range(1, test.shape[0]):
    if i % 2 != 0:
        # print(list_from_df[i][2])
        name_list.append(list_from_df[i][2])

for i in range(1, test.shape[0]):
    if i % 2 == 0:
        iny_list.append(list_from_df[i][1])
        tny_list.append(list_from_df[i][2])

# print(iny_list)

test1 = pd.DataFrame(no_list)
test2 = pd.DataFrame(number_list)
test3 = pd.DataFrame(name_list)
test4 = pd.DataFrame(iny_list)
test5 = pd.DataFrame(tny_list)
result = pd.concat([test1, test2, test3, test4, test5], axis=1)
result.columns = ["NO", "사번", "성명", "입사년월일", "퇴사년월일"]

result.to_excel('succes.xlsx')

print(result)

# print(result)
# test.to_excel('test.xlsx')

# list_from_df = df.values.tolist()
# result = []
# result2 = []

# for i in list_from_df:
#     if i != 'nan':
#         result += [i]

# test = pd.DataFrame(result)
# data = test.dropna(how='all')
# print(data)
