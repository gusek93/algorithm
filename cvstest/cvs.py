import pandas as pd
import warnings

# 엑셀 읽어오기
with warnings.catch_warnings(record=True):
    warnings.simplefilter("always")
    df = pd.read_excel(
        "/Users/dayong/project/algorithm/cvstest/cvsdata//사원등록_20211001_111155_.xlsx", engine="openpyxl", header=int(9), usecols="B,C,D")

# NaN 데이터 제외한 데이터 출력
data = df.dropna(how='all')

list_from_df = data.values.tolist()

# 리스트 선언
no_list = []
number_list = []
name_list = []
iny_list = []
tny_list = []

# 데이터 정제
for i in range(1, data.shape[0]):
    if i % 2 != 0:
        no_list.append(int(list_from_df[i][0]))
        number_list.append(list_from_df[i][1])
        name_list.append(list_from_df[i][2])

    elif i % 2 == 0:
        iny_list.append(list_from_df[i][1])
        tny_list.append(list_from_df[i][2])


# 데이터 join
no = pd.DataFrame(no_list)
number = pd.DataFrame(number_list)
name = pd.DataFrame(name_list)
iny = pd.DataFrame(iny_list)
ony = pd.DataFrame(tny_list)

result = pd.concat([no, number, name, iny, ony], axis=1)
result.columns = ["NO", "사번", "성명", "입사년월일", "퇴사년월일"]

print(result)
# result.to_excel('succes.xlsx')
