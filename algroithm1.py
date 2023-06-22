
from tabulate import tabulate
table = [['Harsh', 21,'CS'],['Shreya', 22, 'CS'],['Manish', 22, 'CIVIL'],['Alisha', 22, 'IT'],['Vipin', 20, 'CS']]
print(tabulate(table, headers=["Name", "Age", "Branch"]))


