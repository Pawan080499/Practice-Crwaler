import pandas as pd

df = pd.DataFrame(
    {
        "name": [
            "anil",
            "aman",
            "karan",
             
        ],
        "age" : [22,23,24],
        "sex" : ["male","male","male"],
    }
)
# ages = pd.Series([22, 35, 58], name="Age")
# sex = pd.Series(["male","male","male"], name="sex")
# df = ["age"].max()
# print(sex)
print(df)
df.to_excel("prac.xlsx", sheet_name="cal",index=False)
sugar=pd.read.xlsx("sugar.xlsx")
