import json
lst = []
def dict_tmp(): return {"A": False}

lst.append(dict_tmp())
lst.append(dict_tmp())
lst.append(dict_tmp())
lst.append(dict_tmp())
lst.append(dict_tmp())
print(lst)

lst[0]["A"] = True
print(lst)