import drugs
list_of_report = drugs.get_reports()
import json
import numpy as np
import matplotlib.pyplot as plt


for item in list_of_report:
    if item["State"] == "California" and item["Year"] == 2002:
        age_group1 = item["Rates"]["Pain Relievers Abuse Past Year"]["12-17"]
    #if item["State"] == "California" and item["Year"] == 2014:
        age_group2 = item["Rates"]["Pain Relievers Abuse Past Year"]["18-25"]
    #if item["State"] == "California" and item["Year"] == 2014:
        age_group3 = item["Rates"]["Pain Relievers Abuse Past Year"]["26+"]



performance = [age_group1, age_group2, age_group3]
objects = ('12-17', '18-25', '26+')
y_pos = np.arange(len(objects))
plt.bar(y_pos, performance)
plt.xticks(y_pos, objects)
plt.xlabel("Age group")
plt.ylabel("Percent")
plt.title("Pain Relievers Abuse in California 2002")
plt.show()
