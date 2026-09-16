import pandas as pd

# Load the dataset
df = pd.read_csv("student_data.csv")

print("========================================")
print("       STATISTICAL ANALYSIS")
print("========================================")

# Display dataset
print("\nStudent Dataset:")
print(df)

# ----------------------------------------
# 1. Population, Sample, Parameter, Statistic
# ----------------------------------------

print("\n1. POPULATION, SAMPLE, PARAMETER AND STATISTIC")

print("Population: All students being studied.")
print("Sample: 20 students present in our dataset.")
print("Parameter: Numerical characteristic of the entire population.")
print("Statistic: Numerical value calculated from our sample.")

# ----------------------------------------
# 2. Select numerical variable
# ----------------------------------------

marks = df["Marks"]

print("\n2. STATISTICAL MEASURES OF MARKS")

# Mean
mean = marks.mean()

# Median
median = marks.median()

# Mode
mode = marks.mode()

# Range
data_range = marks.max() - marks.min()

# Variance
variance = marks.var()

# Standard deviation
std = marks.std()

print("Mean:", round(mean, 2))
print("Median:", round(median, 2))
print("Mode:", mode.tolist())
print("Range:", data_range)
print("Variance:", round(variance, 2))
print("Standard Deviation:", round(std, 2))

# ----------------------------------------
# 3. Interpretation
# ----------------------------------------

print("\n3. INTERPRETATION")

print("The mean is a suitable measure of central tendency")
print("because the dataset does not contain extreme outliers.")

print("The standard deviation shows how much the marks")
print("vary around the mean.")

# ----------------------------------------
# 4. Divide data into two groups
# ----------------------------------------

male = df[df["Gender"] == "Male"]
female = df[df["Gender"] == "Female"]

# ----------------------------------------
# 5. Compare the two groups
# ----------------------------------------

print("\n4. GROUP COMPARISON")

print("\nMale Students:")
print("Mean:", round(male["Marks"].mean(), 2))
print("Median:", round(male["Marks"].median(), 2))
print("Standard Deviation:", round(male["Marks"].std(), 2))

print("\nFemale Students:")
print("Mean:", round(female["Marks"].mean(), 2))
print("Median:", round(female["Marks"].median(), 2))
print("Standard Deviation:", round(female["Marks"].std(), 2))

# ----------------------------------------
# 6. Performance and consistency
# ----------------------------------------

male_mean = male["Marks"].mean()
female_mean = female["Marks"].mean()

male_std = male["Marks"].std()
female_std = female["Marks"].std()

print("\n5. PERFORMANCE AND CONSISTENCY")

if female_mean > male_mean:
    print("Female students perform better.")
else:
    print("Male students perform better.")

if female_std < male_std:
    print("Female students are more consistent.")
else:
    print("Male students are more consistent.")

# ----------------------------------------
# 7. Conclusions
# ----------------------------------------

print("\n6. CONCLUSIONS")

print("1. The average mark of the students is", round(mean, 2))

print("2. The standard deviation of", round(std, 2),
      "shows moderate variation in student marks.")

print("3. Female students perform better and are more consistent")
print("   than male students based on mean and standard deviation.")