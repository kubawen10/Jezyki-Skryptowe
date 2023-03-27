def entry_to_dict(entry):
    return {"ip": entry[0],
            "datetime": entry[1],
            "path": entry[2],
            "code": entry[3],
            "bytes": entry[4]}
    
def log_to_dict(log):
    dictionary = {}
    for entry in log:
        entry_dict = entry_to_dict(entry)
        ip = entry_dict["ip"]
        
        if(ip in dictionary):
            dictionary[ip].append(entry_dict)
        else:
            dictionary[ip] = [entry_dict]
            
    return dictionary

def get_addrs(log_dict):
    return list(log_dict.keys())

def print_dict_entry_dates(log_dict):
    for k,v in log_dict.items():
        requests_num = len(v)
        code_302_entries_num = sum(x["code"] == 302 for x in v)
        
        first = min(v, key = lambda x : x["datetime"])["datetime"]
        last = max(v, key = lambda x : x["datetime"])["datetime"]
        print(f"Address: {k} - Number Of Requests: {requests_num} - First Request: {first} - Last Request: {last} - Ratio: {code_302_entries_num/requests_num}")
