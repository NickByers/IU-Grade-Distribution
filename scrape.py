import pandas as pd

#https://gradedistribution.registrar.indiana.edu/aggregate/export.php?reportID=GrdDistbyClsNbr&term=4212&school=&dept=&rept=1&sesn=&instrname=&subj=&crse=&result=XLS


# Took a minute to find the pattern but here it is:
# 4 is a constant, middle two digits signify calendar year, last digit is for semester. Fall = 8, Summer = 5, Spring = 2
# So, 4212 or 4-21-2 is Spring 2021

start = 4212 # value assigned to Spring 2021 (most recent data)
end = 4118 # oldest data available (Fall 2011)

years = [*range(21, 10, -1)] # 2011 - 2021
semesters = [8,5,2] # Fall, Summer, Spring
fileNames = []
fileName = "grades.csv"

df = pd.read_csv(fileName)

for i in range(len(years)):
    for j in range(len(semesters)):
        target = int("4"  + str(years[i]) + str(semesters[j]))
        if(target <= start and target >= end):
            URL = f"https://gradedistribution.registrar.indiana.edu/aggregate/export.php?reportID=GrdDistbyClsNbr&term={target}&school=&dept=&rept=1&sesn=&instrname=&subj=&crse=&result=XLS"
            print("Fetching " + str(i) + " " + str(j) + " " + str(target) + "...")
            grades=pd.read_csv(URL, skiprows=1) # skiprow 1 to avoid repeatedly appending baked in header row
            grades.to_csv(fileName, mode='a', header=False)
            print("Done!")

print("All semesters have been scraped!")
print("Pruning CSV for bad values...")
indexNames = df[df.iloc[:,25] == 'NR'].index # get classes too small to release grading info
df.drop(indexNames , inplace=True) # prune the small classes
df.to_csv("grades_pruned.csv") # output to a new csv
print("Done!")