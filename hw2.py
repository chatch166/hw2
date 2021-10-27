import json
import pprint
import matplotlib.pyplot as plt

with open('usagdp.json', 'r', encoding = 'ASCII') as f:
    usa = f.read()
    usagdp = json.loads(usa)
with open('chinagdp.json', 'r', encoding = 'ASCII') as f:
    china = f.read()
    chinagdp = json.loads(china)
with open('indiagdp.json', 'r', encoding = 'ASCII') as f:
    india = f.read()
    indiagdp = json.loads(india)
    
usagdpdata = usagdp[1]
chinagdpdata = chinagdp[1]
indiagdpdata = indiagdp[1]

# USA CODE

usdict = {year['date']: year['value'] for year in usagdpdata}
usdates = sorted(usdict.keys())
usvalues = sorted(usdict.values())

# plot the data
fig, ax = plt.subplots()
ax.bar(usdates, usvalues)
plt.xticks(rotation=45)
plt.xlabel('Date', color = 'blue', fontsize='10')
ax.set_xticks(usdates[::5])
ax.set(title = 'National Gross Domestic Product (GDP)\n United States - 1960-2020', xlabel = 'Date', ylabel = 'Gross Domestic Product (GDP)\nin American Dollars')

plt.ylabel('Gross Domestic Product (GDP) in American Dollars', color = 'blue', fontsize='10', rotation = 90)
plt.show()

# INDIA AND CHINA CODE

chinadict = {year['date']: year['value'] for year in chinagdpdata}
chinadates = sorted(chinadict.keys())
chinavalues = sorted(chinadict.values())

indiadict = {year['date']: year['value'] for year in indiagdpdata}
indiadates = sorted(indiadict.keys())
indiavalues = sorted(indiadict.values())

# plot the data
fig, ax = plt.subplots()
ax.plot(chinadates, chinavalues, color="b", label = 'China')
ax.plot(indiadates, indiavalues, color="r", label  = "India")
plt.xticks(rotation=45)
plt.xlabel('Date', color = 'blue', fontsize='10')
ax.set_xticks(indiadates[::5])
ax.set(title = 'National Gross Domestic Products (GDP)\nChina vs. India - 1960-2020', xlabel = 'Date', ylabel = 'Gross Domestic Product (GDP)\nin American Dollars')
plt.ylabel('GDP in American Dollars', color = 'blue', fontsize='10', rotation = 90)
plt.legend(loc='upper left')
plt.show()