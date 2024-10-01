"""
Student name:Krishna Priyanka Garikapati
Student Number:W0502117
Assignment # 1
"""
#Program 1 – Hipster's Local Vinyl Records
#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.


######Pseudocode########
#input the customer name and assign it to a variable.
#input the distance in kms and assign it to a variable. The output of input command is always string so change the datatype using float.
#input the cost of records purchased and assign it to a variable. The output of input command is always string so change the datatype of assigned variable using float.
#As delivery charge is contant assign valur to variable.
#Total delivery charge=input of distance in kms * deivery charge
#print delivery charge of customer for the distance in kms.
#sales tax=(14/100)*cost of records purchased
#Total purchase cost=Sales tax + cost of records purchased.
#print the total purchase cost
#total cost=total purchase cost + total deivery charge
#print the total cost

def main():
    customername=input("Enter customer name:")
    Distance=float(input("Enter the distance for destination in km:"))
    costofrecords=float(input("Enter cost of records purchased: $"))
    deliveryCharge=15
    TotalDelCharge=Distance*deliveryCharge
    print("Purchase summary for", customername, "is")
    print("Deivery cost $", TotalDelCharge)
    Salestax=(14/100)*costofrecords
    purchasecost=costofrecords+Salestax
    totalpurchasecost=round(purchasecost,2)
    print("Purchase cost $", totalpurchasecost)
    Totalcost=(totalpurchasecost+TotalDelCharge)
    print("Total cost $",Totalcost)

main()