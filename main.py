import pandas as pd

# df = pd.read_csv('test.csv')
# dfJson = pd.read_json('test.json')
# print(pd.options.display.max_rows) 
# pd.options.display.max_rows = 100 #setting max number of rows to display the entire DataFrame
# print(df) 
# print(dfJson.to_string())
# print(df.to_string()) 


# studentData = {
#   'names': ["dallu", "santu", "pannu"],
#   'position': [3, 1, 2]
# }

# print(pd.Series(studentData))  #series is like a column in table
# aframe = pd.DataFrame(studentData)  #creating dataframe of studentData
# print(aframe)
# print("Starting loc")
# print(aframe.loc[0])  #data from row 0
# print(aframe.loc[[0,1]])  #data from row 0 and 1

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)
print(df.head(2)) #get first 2 rows in DF default no is 5
print(df.tail()) #get last 5 rows Def 5
print(df.info()) # gives more information of datas