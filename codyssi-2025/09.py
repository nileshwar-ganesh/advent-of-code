import re
import copy

with open("../data-files/d1") as file:
    content = file.readlines()

accounts = {}
transactions = []
for line in content:
    if "HAS" in line:
        key, value = line.strip().split("HAS")
        accounts[key.strip()] = int(value.strip())
    if "FROM" in line:
        match = re.search(r"FROM (.+?) TO (.+?) AMT (\d+)", line)
        transactions.append([match.group(1).strip(), match.group(2).strip(), int(match.group(3).strip())])

accounts_copy = copy.deepcopy(accounts)
for detail in transactions:
    sender, receiver, amount = detail
    accounts[sender] -= amount
    accounts[receiver] += amount

balances = sorted([value for value in accounts.values()], reverse=True)
print(sum(balances[:3]))

accounts = copy.deepcopy(accounts_copy)
for detail in transactions:
    sender, receiver, amount = detail
    accounts[receiver] += min(amount, accounts[sender])
    accounts[sender] -= min(amount, accounts[sender])


balances = sorted([value for value in accounts.values()], reverse=True)
print(sum(balances[:3]))


accounts = copy.deepcopy(accounts_copy)
debts = {}
for detail in transactions:
    sender, receiver, amount = detail
    debt = max(0, amount - accounts[sender])
    if debt > 0:
        if sender not in debts.keys():
            debts[sender] = [[receiver, debt]]
        else:
            debts[sender].append([receiver, debt])
    accounts[receiver] += min(amount, accounts[sender])
    if receiver in debts.keys():
        debt_list = copy.deepcopy(debts[receiver])
        while len(debt_list) > 0:
            if accounts[receiver] >= debt_list[0][1]:
                accounts[debt_list[0][0]] += debt_list[0][1]
                accounts[receiver] -= debt_list[0][1]
                debt_list.pop(0)
            else:
                accounts[debt_list[0][0]] += accounts[receiver]
                debt_list[0][1] -= accounts[receiver]
                accounts[receiver] = 0
                break
        debts[receiver] = copy.deepcopy(debt_list)
    accounts[sender] -= min(amount, accounts[sender])

for sender, details in debts.items():
    if accounts[sender] > 0:
        while len(details) > 0:
            if accounts[sender] >= details[0][1]:
                accounts[details[0][0]] += details[0][1]
                accounts[sender] -= details[0][1]
                details.pop(0)
            else:
                accounts[details[0][0]] += accounts[sender]
                details[0][1] -= accounts[sender]
                accounts[sender] = 0
                break

print(debts)

balances = sorted([value for value in accounts.values()], reverse=True)
print(accounts)
print(sum(balances[:3]))
