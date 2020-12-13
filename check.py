import  pandas  as pd
 
df = pd.read_excel('导出数据.xlsx')  
done = []
df2 = pd.read_csv('团员导出列表1607841759840.csv')  
for i in df["姓名"]:
    done.append(i)


for i in df2["姓名"]:
    # print(i)
    if i in done:
        pass
    else :
        print(i)
