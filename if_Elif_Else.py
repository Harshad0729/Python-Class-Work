# Whenever you want to check for multiple  conditions you use
#if...elif...else

Team1 = int(input("Enter India Team Score: "))
Team2 = int(input("Enter Pakistan Team Score: "))
if(Team1>Team2):
    print("India Won THe Match!!!")
elif(Team2>Team1):
    print("Pakistan Won The Match!!!")
else:
    print("Match Draw!!!")