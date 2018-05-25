#Data Frames and Series

import pandas as pd
df = pd.DataFrame({"name":["Bob","Alex","Gary"],"age":[60,25,34]})

#reading from another file

odf = pd.read_csv("C:\Users\Nicholas\Documents\CPSCLastYear\Term2\CPSC303\Homework\Ass6\weatherstats_vancouver_normal_monthly.csv")


# some possible operations

df["age+1"] = df["age"]+1
df["ageOver30"] = (df["age"]>30) #collection of bools

# columns have buit in aggregate functions

total_age = df["age"].sum()
median_age = df["age"].quantile(0.5)

new_df = df[df["age"]<50]
df["age_squared"] = df["age"].apply(lambda x: x*x)


# set index as name

df_with_name = df.set_index("name")
B_row = df_with_name.ix["Bob"]

# Series

s = pd.Series([1,2,3])

m = s + pd.Series([4,5,6])

print m


# Joining and grouping

df_w_age = pd.DataFrame({
    "name": ["Tom", "Tyrell", "Claire"],
    "age": [60, 25, 33]
})
df_w_height = pd.DataFrame({
    "name": ["Tom", "Tyrell", "Claire"],
    "height": [6.2, 4.0, 5.5]
})

joined = df_w_age.set_index("name").join(df_w_height.set_index("name"))

print joined.reset_index()

df_mine = pd.DataFrame({
"name":["Bob","Jessica","Alan"],
"height":[12,32,17],
"gender":["M","F","M"]})

median_mine = df_mine.groupby("gender").quantile(0.5)

# Use a custom aggregate function
def agg(ddf):
    return pd.Series({
        "name": max(ddf["name"]),
        "mean_hieght": ddf["height"].mean()})

print df_mine.groupby("gender").apply(agg)






