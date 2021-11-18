import csv
import matplotlib.pyplot as plt
import numpy as np

# csv with data on economic costs of wildfire in USA from 1985 to 2020
with open('Federal Firefighting Costs (Suppression Only).csv', mode='r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    header_row = next(reader)  # parsing headers
    for index, column_header in enumerate(header_row):
        print(index, column_header)  # print each header and its position

    years = []  # extract data under each header
    fires = []  # number of fires
    acres = []  # acres burned by fires
    forest_service = []  # forest service cost
    interior_dept = []  # DOI cost
    totals = []  # total cost
    for row in reader:  # read the rows from csv
        year = str(row[0])
        fire = str(row[1])
        acre = str(row[2])
        fs_cost = str(row[3])
        doi_cost = str(row[4])
        total_cost = str(row[5])
        years.append(year)  # append each list to contain extracted data
        fires.append(fire)
        acres.append(acre)
        forest_service.append(fs_cost)
        interior_dept.append(doi_cost)
        totals.append(total_cost)

fires = [int(''.join(i.split(','))) for i in fires]  # remove commas from numeric data
acres = [int(''.join(i.split(','))) for i in acres]

year_data = [int(i) for i in years]  # list comprehension to cast values in each list to integers
acres_data = [int(i) for i in acres]
fires_data = [int(i) for i in fires]

# replace commas and dollar signs with blank characters for three monetary data lists
fs_data = []
for i in forest_service:
    a = i.replace('$', "")
    fs_data.append(a)

fs_data = [int(''.join(i.split(','))) for i in fs_data]
forest_service_data = [int(i) for i in fs_data]  # list comprehension after $'s removed

doi_data = []
for j in interior_dept:
    b = j.replace('$', "")
    doi_data.append(b)

doi_data = [int(''.join(i.split(','))) for i in doi_data]
interior_dept_data = [int(i) for i in doi_data]

tot_data = []
for k in totals:
    c = k.replace('$', "")
    tot_data.append(c)

tot_data = [int(''.join(i.split(','))) for i in tot_data]
totals_data = [int(i) for i in tot_data]

# first plot
# line plot for acres and total fires sharing x axis (years)
y = acres_data
y2 = fires_data
x = year_data

fig, ax1 = plt.subplots()  # twin x axis plot

color = 'tab:blue'
ax1.set_xlabel('Years', fontsize=18, font='Times New Roman')
ax1.set_ylabel('Acres', color=color, rotation=360, fontsize=24, font='Times New Roman')
ax1.plot(x, y, color=color, linewidth=2)
ax1.tick_params(axis='y')
ax1.ticklabel_format(axis='y', style='plain')

ax2 = ax1.twinx()  # second y axis sharing an x axis

color = 'tab:red'
ax2.set_ylabel('Fires', color=color, rotation=360, fontsize=18, font='Times New Roman')
ax2.plot(x, y2, color=color, linewidth=2)

fig.tight_layout()
plt.title('Total US Fires and Acres Burned', fontsize=20, font='Times New Roman')
plt.show()

# second plot
# forest service and interior department costs
x = np.arange(len(totals_data))
width = 0.4

fig, ax = plt.subplots()
bars1 = ax.bar(x - width/2, forest_service_data, width, label='Forest Service')
bars2 = ax.bar(x + width/2, interior_dept_data, width, label='Department of the Interior')

ax.set_ylabel('Cost ($s)', font='Times New Roman')
ax.set_xlabel('Time (years)', font='Times New Roman')
ax.set_title('Cost of US Wildfires (1985 - 2020)', font='Times New Roman')
ax.set_xticks(x)
ax.bar_label(bars1, labels=None, label_type='center', rotation=90, fontsize=5)
ax.bar_label(bars2, labels=None, label_type='center', rotation=90, fontsize=5)
ax.ticklabel_format(axis='y', style='plain')
ax.legend()

plt.show()
