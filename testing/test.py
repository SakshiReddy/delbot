import pandas as pd

data = pd.read_csv (r'db_dell.csv')
user_ID = int(input('Enter user_ID'))

arr=[]

input_string = input("Enter array separated by commas: ")   #must include emp_ID
arr  = input_string.split(",")
# print("Printing array")
# for i in arr:
#     print(i)

df = pd.DataFrame(data, columns = arr)
df.set_index("Emp ID", inplace = True)
result = df.loc[user_ID]
print(result)
print("\n")
