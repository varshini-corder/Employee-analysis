import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("Employee Sample Data 1.csv" , encoding="latin1")
print(df.head())

print(df.info())
print(df.shape)

print(df.isnull().sum())

#salary range
df["Annual Salary"] = (
    df["Annual Salary"]
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)


df["Annual Salary"] = pd.to_numeric(df["Annual Salary"], errors="coerce")
salary_range = pd.cut(
    df["Annual Salary"],
    bins=[0, 30000, 60000, 100000, 200000],
    labels=["Low", "Medium", "High", "Very High"]
)


salary_range.value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Salary Range")
plt.show()


#Department
department = df["Department"].value_counts()


department.plot(kind= "bar")
plt.title("Department")
plt.xlabel("Department")
plt.ylabel("Gender")
plt.show()


#gende

job_gender = pd.crosstab(df["Job Title"], df["Gender"])

print(job_gender)

job_gender.plot(kind="bar", figsize=(10,5))

plt.title("Male and Female Employees by Job Role")
plt.xlabel("Job Role")
plt.ylabel("Count")
plt.show()

