

import requests
#https://gradedistribution.registrar.indiana.edu/aggregate/export.php?reportID=GrdDistbyClsNbr&term=4212&school=&dept=&rept=1&sesn=&instrname=&subj=&crse=&result=XLS


# Took a minute to find the pattern but here it is:
# 4 is a constant, middle two digits signify calendar year, last digit is for semester. Fall = 8, Summer = 5, Spring = 2
# So, 4212 or 4-21-2 is Spring 2021

start = 4212 # value assigned to Spring 2021 (most recent data)
end = 4118 # oldest data available (Fall 2011)

years = [*range(21, 10, -1)] # 2011 - 2021
semesters = [8,5,2] # Fall, Sumemer, Spring

for i in range(len(years)):
    for j in range(len(semesters)):
        target = int("4"  + str(years[i]) + str(semesters[j]))
        if(target <= start and target >= end):
            print(target)
            URL = f"https://gradedistribution.registrar.indiana.edu/aggregate/export.php?reportID=GrdDistbyClsNbr&term={target}&school=&dept=&rept=1&sesn=&instrname=&subj=&crse=&result=XLS"
            print(URL)
            fileName = f"{target}.csv"
            newFile = requests.get(URL, allow_redirects=True)
            open(fileName, 'wb').write(newFile.content)
            #TODO: combine all CSVs into one large CSV
            
