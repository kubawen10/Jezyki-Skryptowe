def entry_to_dict(entry):
    return {"ip" : entry[0], 
            "datetime": entry[1], 
            "path": entry[2], 
            "code": entry[3], 
            "bytes": entry[4]}

def log_to_dict(log):
    dictiononary = {}

    for entry in log:
        entry_dict = entry_to_dict(entry)
        ip = entry_dict["ip"]

        if(ip in dictiononary):
            dictiononary[ip].append(entry_dict)

        else:
            dictiononary[ip] = [entry_dict]

    return dictiononary

def get_addrs(log_dict):
    return log_dict.keys()

def print_dict_entry_dates(log_dict):
    for k,v in log_dict.items():
        num_of_entries = len(v)
        code_200_entries = sum(x["code"] == 200 for x in v)

        first = min(v, key = lambda x: x["datetime"])["datetime"]
        last = max(v, key = lambda x: x["datetime"])["datetime"]

        print(f"addr: {k} - number_of_entries: {num_of_entries} - first_entry: {first} - last_entry: {last} - 200_ratio: {code_200_entries/num_of_entries}")



        

