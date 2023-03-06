thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["model"]#'Mustang'
thisdict.get("model")#'Mustang'
thisdict.keys()#dict_keys(['brand', 'model', 'year'])
thisdict.values()#dict_values(['Ford', 'Mustang', 1964])
thisdict.items()#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")
  
thisdict["year"] = 2018
thisdict.update({"year": 2020})
thisdict.pop("model")
del thisdict["model"]

for x in thisdict:
  print(x)#brand   model  year
  
for x in thisdict:
  print(thisdict[x])#Ford   Mustang  1964  
  
for x in thisdict.values():
  print(x)#Ford   Mustang  1964

for x in thisdict.keys():
  print(x)#brand   model  year
  
for x, y in thisdict.items():
  print(x, y)  
  """
  brand Ford
  model Mustang
  year 1964
  """
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  