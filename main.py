Scorecard = [
{'Name': "GT", "FullName": "Gujarat Titans", 'Points' : 20, 'ResultOfLast5Matches' : [1,1,0,0,1]},
{'Name': "LSG", "FullName": "Lucknow Super Giants", "Points" : 18, "ResultOfLast5Matches" : [1,0,0,1,1]},
{'Name': "RR", "FullName": "Rajasthan Royals", "Points" : 16, "ResultOfLast5Matches" : [1,0,1,0,0]},
{'Name': "DC", "FullName": "Delhi Capitals", "Points" : 14, "ResultOfLast5Matches" : [1,1,0,1,0]},
{'Name': "RCB", "FullName": "Royal challengers Bangalore", "Points" : 14, "ResultOfLast5Matches" : [0,1,1,0,0]},
{'Name': "KKR", "FullName": "Kolkata Knight Riders", "Points" : 12, "ResultOfLast5Matches" : [0,1,1,0,1]},
{'Name': "PBKS", "FullName": "Punjab Kings", "Points" : 12, "ResultOfLast5Matches" : [0,1,0,1,0]},
{'Name': "SRH", "FullName": "Sunrisers Hyderabad", "Points" : 12, "ResultOfLast5Matches" : [1,0,0,0,0]},
{'Name': "CSK", "FullName": "Chennai Super Kings", "Points" : 8, "ResultOfLast5Matches" : [0,0,1,0,1]},
{'Name': "MI", "FullName": "Mumbai Indians", "Points" : 6, "ResultOfLast5Matches" : [0,1,0,1,1]}
]

#Two consequetive wins /Losses
"""
TeamsWithConsequetiveLoss=[]
TeamsWithConsequetiveWins= []

for i in Scorecard:
    for j in range(len(i["ResultOfLast5Matches"])):
        if j<len(i["ResultOfLast5Matches"])-1:
            if i["ResultOfLast5Matches"][j] ==0 and i["ResultOfLast5Matches"][j+1]==0:
                TeamsWithConsequetiveLoss.append(i["Name"])
                #print(i["ResultOfLast5Matches"][j])
            
for i in Scorecard:
    for j in range(len(i["ResultOfLast5Matches"])):
        if j<len(i["ResultOfLast5Matches"])-1:
            if i["ResultOfLast5Matches"][j] ==1 and i["ResultOfLast5Matches"][j+1]==1:
                TeamsWithConsequetiveWins.append(i["Name"])

print(set(TeamsWithConsequetiveLoss))
"""
#Generalised solution
WinningStreak = []
Average =[]
LosingStreak = []
print("Enter win or lose u wnat to check (0 - Loss or 1 - Win)")
Result = int(input())
print("enter the number of winning streak or lossing streak you want to check (Minimum 0 and Maximum 5)")
Matches = int(input())
Streak = 0

if Result == 1:

    for i in Scorecard:
        for j in range(len(i["ResultOfLast5Matches"])):
            for k in range(Matches):
                if j+k<len((i["ResultOfLast5Matches"])):
                    Streak += i["ResultOfLast5Matches"][j+k]
                    #print(j,k,j+k)
            if Streak == Matches:
                WinningStreak.append(i["Name"])
                Average.append(i["Points"])
                break
            Streak =0
    print(f'Teams with Winning Streak of {Matches} is : {WinningStreak}')
    
    AveragePoints =0
    sum = 0
    for i in Average:
            sum += i
    if len(WinningStreak)!=0:
        AveragePoints = sum/len(WinningStreak)
        print(f'Average points of Teams with Winning Streak of {Matches} is : {AveragePoints}')
    else:
        print("None found")

else:
    for i in Scorecard:
        for j in range(len(i["ResultOfLast5Matches"])):
            for k in range(Matches):
                if j+k<len((i["ResultOfLast5Matches"])):
                    Streak += i["ResultOfLast5Matches"][j+k]
                elif j+k == len((i["ResultOfLast5Matches"])):
                    Streak+=1
            #print(Streak)
            if Streak == Result:
                LosingStreak.append(i["Name"])
                Average.append(i["Points"])
                break
            Streak =0

    print(f'Teams with Losing Streak of {Matches} is : {LosingStreak}')

    AveragePoints = 0
    sum = 0
    for i in Average:
        sum += i
    if len(LosingStreak)!=0:
        Average = sum/len(LosingStreak)
        print(f'Average points of Teams with Losing Streak of {Matches} is : {AveragePoints}')
    else:
        print("None found")
