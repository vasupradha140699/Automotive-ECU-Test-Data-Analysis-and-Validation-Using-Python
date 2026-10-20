# -----------------------------Dictionary and list------------------------------------

# 1. Create a dictionary
ecu_data = {"ecu1": {
    "voltage" : 12,
    "temperature" : 30,
    "Test_executed" : 50,
    "Test_passed": 20,
    "Test_failed":30,
    
    },
"ecu2" : {
    "voltage" : 9,
    "temperature" : 80,
    "Test_executed" : 50,
    "Test_passed": 30,
    "Test_failed":20,
   
    },
"ecu3" : {
    "voltage" : 12,
    "temperature" : 90,
    "Test_executed" : 30,
    "Test_passed": 20,
    "Test_failed":10,
    
    },
"ecu4" : {
    "voltage" : 12,
    "temperature" : 120,
    "Test_executed" : 55,
    "Test_passed": 25,
    "Test_failed":30,
    
    },
"ecu5" : {
    "voltage" : 10,
    "temperature" : 40,
    "Test_executed" : 50,
    "Test_passed": 40,
    "Test_failed":10,
   
    }
}
Ecu_List = []
for name,data in ecu_data.items():
    Ecu_List.append({
        "name": name,
        "voltage" : data["voltage"],
        "temperature" : data["temperature"],
        "Test_executed" : data["Test_executed"],
        "Test_passed": data["Test_passed"],
        "Test_failed":data[ "Test_failed"],
       
    })
print(Ecu_List)
# for i in range(5):
count=0
for ecu in Ecu_List:
    count= count+1
    print(f"-------------------ecu{count}---------------------------------------")
    print("Name", ":", ecu["name"])
    print("voltage", ":", ecu["voltage"])
    print("temperature", ":", ecu["temperature"])
    print("Test_executed", ":", ecu["Test_executed"])
    print("Test_passed", ":", ecu["Test_passed"])
    print("Test_failed", ":", ecu[ "Test_failed"])
    
    
print("-------------checking voltage is under valid range-------------------")
for ecu in Ecu_List:
   
    voltage = ecu["voltage"]

    if 11 <= voltage <= 14:
        print(ecu["voltage"], "Voltage is valid")
    else:
        print(ecu["voltage"], "Voltage is invalid")
print("-------------checking temperature is under valid range-------------------")
for ecu in Ecu_List:
   
    temperature = ecu["temperature"]

    if 0 <=temperature <= 80:
        print(ecu["temperature"], "temperature is valid")
    else:
        print(ecu["temperature"], "temperature is invalid")
print("----------------------pass_percentage calculation-----------------------")
for name,data in ecu_data.items():
    test_executed = int(data["Test_executed"])
    test_passed = int(data["Test_passed"])
    pass_percentage = (test_executed/test_passed)*100
    data["Pass_percentage"] = round(pass_percentage,2)
    print(f"pass_percentage of {["name"]} is: ", pass_percentage)
print("-----------------checking dictionary after adding pass percentage----")
for i,v in ecu_data.items():
    print(i,v)
print("-----------------checking list after adding pass percentage----------")

# for ecu in Ecu_List:
for ecu in Ecu_List:
    test_executed = int(ecu["Test_executed"])
    test_passed = int(ecu["Test_passed"])
    pass_percentage = (test_executed/test_passed)*100
    ecu["Pass_percentage"] = round(pass_percentage,2)
    print(f"pass_percentage of {ecu["name"]} is: ", pass_percentage)
for e in Ecu_List:
    print(e)

# print("---------- Updated ECU List ----------")
# print(Ecu_List)
print("----------------------checking the status of ecu------------------------")
for ecu in Ecu_List:
    test_executed = ecu["Test_executed"]
    test_passed = ecu["Test_passed"]
    pass_percentage = (test_executed/test_passed)*100
    temperature = ecu["temperature"]
    voltage = ecu["voltage"]
    if 11 <= voltage <= 14 and 0 <=temperature <= 80 and pass_percentage>=80:
        status = "passed"
        ecu["status"] = "passed"
        print(f"{ecu["status"]} is pass")
        
    else:
        ecu["status"] = "failed"
        print(f"{ecu["name"]} is fail")
        
       
ecu_data["ecu6"] ={
        "voltage" : 19,
        "temperature" : 120,
        "Test_executed" : 50,
        "Test_passed": 0,
        "Test_failed":50,
        "Pass_percentage" : 150,
        
}
print("--------------------------ecu6 added data in dictionary---------------------")
print(ecu_data)
Ecu_List.append({
    "name" : "ecu6",
    "voltage" : 19,
    "temperature" : 120,
    "Test_executed" : 50,
    "Test_passed": 0,
    "Test_failed":50,
    "Pass_percentage": 90,
    "status": "Fail"
    
})
print("------------------------ecu6 added data in ecu list----------------------")
for ecu in Ecu_List:
    print(ecu)
print("-----------------------Modifying the temperature of one ecu-----------------")
ecu_data["ecu5"]["temperature"] = 90
data = ecu_data["ecu5"]
print(data)
del ecu_data["ecu3"]
print("--------------------------deleting ecu3 in dictionary------------------------------")
for ecu in ecu_data:
    print(ecu)
print("--------------------------deleting ecu3 from list----------------------------------")
for e in Ecu_List:
    print(e)
Ecu_List.pop(2)
print("________________________after removing ecu3 from the list---------------------")
for e in Ecu_List:
    print(e)
print("-----------------------printing eveything-------------------------------------")
for ecu in Ecu_List:
    # count= count+1
    # print(f"-------------------ecu{count}---------------------------------------")
    print(ecu["name"])
    print("voltage", ":", ecu["voltage"])
    print("temperature", ":", ecu["temperature"])
    print("Test_executed", ":", ecu["Test_executed"])
    print("Test_passed", ":", ecu["Test_passed"])
    print("Test_failed", ":", ecu[ "Test_failed"])
    print("pass_percentage", ":", ecu["Pass_percentage"])
    print("status", ":",ecu["status"] )

