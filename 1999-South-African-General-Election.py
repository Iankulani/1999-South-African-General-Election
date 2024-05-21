# -*- coding: utf-8 -*-
"""

Created on Mon May  6 15:47:35 2024

@author: IAN CARTER KULANI
Phone:+265(0)988061969
E-mail:iancarterkulani@gmail.com
Purpose: The software prompts the user to enter total number of published centers,total 
number of registered  voters, total number of null and void votes, total number of valid votes and total valid votes for each candidate. Afterward,it determines the candidate with the majority of votes 
and displays the results on the screen.
#NOTE:For a candidate to be a majority winner of an election, the candidate total valid votes should 
be greater than majority votes, which is Fifty plus one. 

"""


print("=========================================SOUTH AFRICA 1999 PRESIDENTIAL ELECTION=========================================\n\n")

percent=100
#Get total number of published centers
Totalpublishedcenters=int(input("Enter Total published centers:"))
#Get the total number of registered votes
TotalRegisteredvotes=int(input("Enter Total Registered Voters/Turnout:"))
Totalvotescast=int(input("Enter Total Votes Cast/Total Votes:"))
#Get total number of Null_&_Void votes
Nullandvoid=int(input("Enter Total Null_&_Void Votes/Invalid Votes:"))
#Get Total Valid Votes
Totalvalidvotes=int(input("Enter Total Valid Votes:"))
#Get Total Vald Votes for African National Congress
Totalvalidvotesfor_African_National_Congress=int(input("Enter Total Valid Votes for African National Congress:"))
#Get Total Vald Votes for Democratic Party
Totalvalidvotesfor_Democratic_Party=int(input("Enter Total Valid Votes for Democratic Party:"))
#Get Total Vald Votes for Inkatha Freedom Party  
Totalvalidvotesfor_Inkatha_Freedom_Party=int(input("Enter Total Valid Votes for Inkatha Freedom Party:"))
#Get Total Valid Votes for New National Party
Totalvalidvotesfor_New_National_Party=int(input("Enter Total Valid Votes for New National Party:"))
#Get Total Vald Votes for  United Democratic Movement
Totalvalidvotesfor_United_Democratic_Movement=int(input("Enter Total Valid Votes for United Democratic Movement:"))
#Get Total Valid Votes For African Christian Democratic Party
Totalvalidvotesfor_African_Christian_Democratic_Party=int(input("Enter Total Valid Votes for African Christian Democratic Party:"))
#Get Total Vald Votes for Freedom Front
Totalvalidvotesfor_Freedom_Front=int(input("Enter Total Valid Votes for Freedom Front:"))
#Get Total Vald Votes for United Christian Democratic Party
Totalvalidvotesfor_United_Christian_Democratic_Party=int(input("Enter Total Valid Votes for United Christian Democratic Party:"))
#Get Total Vald Votes for Pan Africanist Congress
Totalvalidvotesfor_Pan_Africanist_Congress=int(input("Enter Total Valid Votes for Pan Africanist Congress:"))
#Get Total Vald Votes for Federal Alliance
Totalvalidvotesfor_Federal_Alliance=int(input("Enter Total Valid Votes for Federal Alliance:"))
#Get Total Vald Votes for Minolity Front
Totalvalidvotesfor_Minolity_Front=int(input("Enter Total Valid Votes for Minolity Front:"))
#Get Total Vald Votes for Afrikaner Eenhelds Beweging
Totalvalidvotesfor_Afrikaner_Eenhelds_Beweging=int(input("Enter Total Valid Votes for Afrikaner EenheldsBeweging:"))
#Get Total Vald Votes for Azanian People's Organisation
Totalvalidvotesfor_Azanian_Peoples_Organisation=int(input("Enter Total Valid Votes for Azanian People's Organisation:"))
#Get Total Valid Votes for Abolition of Income Tax and Usury Party
Totalvalidvotesfor_Abolition_of_Income_Tax_and_Usury_Party=int(input("Enter Total Valid Votes for Abolition of Income Tax and Usury Party:"))
#Get Total Valid Votes for Government by the People Green Party
Totalvalidvotesfor_Government_by_the_People_Green_Party=int(input("Enter Total Valid Votes for Government by the People Green Party:"))
#Get Total Valid Votes for Socialist Party of Azania
Totalvalidvotesfor_Socialist_Party_of_Azania=int(input("Enter Total Valid Votes for Socialist Party of Azania:"))

#Decision Making
if Totalvalidvotesfor_African_National_Congress>Totalvalidvotes/2+1 :
     print("Congratulations to the African National Congress For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_Democratic_Party>Totalvalidvotes/2+1: 
     print("Congratulations to theto the Democratic Alliance For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_Inkatha_Freedom_Party>Totalvalidvotes/2+1 :
     print("Congratulations  to the Inkatha Freedom Party  For Winning 1999  Election\n\n")
elif Totalvalidvotesfor_New_National_Party>Totalvalidvotes/2+1: 
     print("Congratulations to the New National Party For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_United_Democratic_Movement>Totalvalidvotes/2+1: 
     print("Congratulations to the United Democratic Movement For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_African_Christian_Democratic_Party>Totalvalidvotes/2+1 :
     print("Congratulations to the African Christian Democratic Party For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_Freedom_Front>Totalvalidvotes/2+1: 
     print("Congratulations to the Freedom Front For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_United_Christian_Democratic_Party>Totalvalidvotes/2+1: 
     print("Congratulations  to the United Christian Democratic Party For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_Pan_Africanist_Congress>Totalvalidvotes/2+1:
     print("Congratulations to the Pan Africanist Congress For Winning 1999 ElectionElection\n\n")
elif Totalvalidvotesfor_Federal_Alliance>Totalvalidvotes/2+1: 
     print("Congratulations  to the Federal Alliance For Winning 1999 Election Election\n\n")
elif Totalvalidvotesfor_Minolity_Front>Totalvalidvotes/2+1: 
     print("Congratulations  to the Minolity Front Party For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_Afrikaner_Eenhelds_Beweging>Totalvalidvotes/2+1 :
     print("Congratulations to the Afrikaner Eenhelds Beweging For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_Azanian_Peoples_Organisation>Totalvalidvotes/2+1: 
     print("Congratulations to the Azanian People's Organisation For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_Abolition_of_Income_Tax_and_Usury_Party>Totalvalidvotes/2+1: 
     print("Congratulations  to the Abolition of Income Tax and Usury Party For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_Government_by_the_People_Green_Party>Totalvalidvotes/2+1 :
     print("Congratulations to the Government by the People Green Party For Winning 1999 Election\n\n")
elif Totalvalidvotesfor_Socialist_Party_of_Azania>Totalvalidvotes/2+1: 
     print("Congratulations to the Socialist Party of Azania For Winning 1999 Election\n\n")

else:
    print("No majority winner was found RUNOFF may be required\n")

print("__________________________________________________________ELECTION STATISTICS__________________________________________________________\n")
#calculating percentage 
#Calculating percentage for total votes cast
Percentage=round(Totalvalidvotes*percent/Totalvalidvotes, 2);
print("Total Votes Cast in percentage=",Percentage)
#Calculating percentage for total valid votes for all canidates
Percentage=round(Totalvalidvotes*percent/Totalvotescast, 2);
print("Total Valid Votes for all candidtes in percentage=",Percentage)
#Calculating percentage for null_&_void votes
Percentage=round(Nullandvoid*percent/Totalvalidvotes, 2);
print("Total Null_&_Void votes in percentage=",Percentage)
#Calculating percentage for Total Registered voters/turnout
Percentage=round(Totalvotescast*percent/TotalRegisteredvotes, 2);
print("Total Registered voters/turnout in percentage=",Percentage)
#Calculating percentage for African National Congress
Percentage=round(Totalvalidvotesfor_African_National_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African National Congress in Percentage=",Percentage)
#Calculating percentage for Democratic Alliance
Percentage=round(Totalvalidvotesfor_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Democratic Alliance in percentage=",Percentage) 
#Calculating percentage for Inkatha Freedom Party
Percentage=round(Totalvalidvotesfor_Inkatha_Freedom_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Inkatha Freedom Party in percentage=",Percentage) 
#Calculating percentage for New National Party
Percentage=round(Totalvalidvotesfor_New_National_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for New National Party in Percentage=",Percentage)
#Calculating percentage for United Democratic Movement
Percentage=round(Totalvalidvotesfor_United_Democratic_Movement*percent/Totalvalidvotes, 2);
print("Total Valid Votes for United Democratic Movement in percentage=",Percentage)
#Calculating percentage for African Christian Democratic Party
Percentage=round(Totalvalidvotesfor_African_Christian_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for African Christian Democratic Party in percentage=",Percentage)
#Calculating percentage for Freedom Front
Percentage=round(Totalvalidvotesfor_Freedom_Front*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Freedom Front in percentage=",Percentage)
#Calculating percentage for United Christian Democratic Party
Percentage=round(Totalvalidvotesfor_United_Christian_Democratic_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for United Christian Democratic Party in percentage=",Percentage)
#Calculating percentage for Pan Africanist Congress
Percentage=round(Totalvalidvotesfor_Pan_Africanist_Congress*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Pan Africanist Congress in percentage=",Percentage)  
#Calculating percentage for Federal Alliance
Percentage=round(Totalvalidvotesfor_Federal_Alliance*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Federal Alliance in percentage=",Percentage) 
#Calculating percentage for Minolity Front
Percentage=round(Totalvalidvotesfor_Minolity_Front*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Minolity Front in percentage=",Percentage)  
#Calculating percentage for Afrikaner Eenhelds Beweging
Percentage=round(Totalvalidvotesfor_Afrikaner_Eenhelds_Beweging*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Afrikaner Eenhelds Beweging in percentage=",Percentage) 
#Calculating percentage for Azanian Peoples Organisation
Percentage=round(Totalvalidvotesfor_Azanian_Peoples_Organisation*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Azanian Peoples Organisation in percentage=",Percentage)
#Calculating percentage for Abolition of Income Tax and Usury Party
Percentage=round(Totalvalidvotesfor_Abolition_of_Income_Tax_and_Usury_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Abolition of Income Tax and Usury Party in percentage=",Percentage)  
#Calculating percentage for Government by the People Green Party 
Percentage=round(Totalvalidvotesfor_Government_by_the_People_Green_Party*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Government by the People Green Party in percentage=",Percentage) 
#Calculating percentage for Socialist Party of Azania
Percentage=round(Totalvalidvotesfor_Socialist_Party_of_Azania*percent/Totalvalidvotes, 2);
print("Total Valid Votes for Socialist Party of Azania in percentage=",Percentage)  


print("=========================================================================================================================\n")   













