from parser_z2 import log_entry, get_user_from_log, get_message_type, MessageType
import random

def get_user_accumulation_function():
    user_entries = dict()

    def accumulate(entry: log_entry):
        if not entry:
            return user_entries
        
        user = get_user_from_log(entry)
        

        if user and user in user_entries:
            user_entries[user].append(entry)
        elif user:
            user_entries[user] = [entry]

        return user_entries
    
    return accumulate

def get_n_random_entries_from_random_user(user_entries: dict):
    user, entries = random.choice(list(user_entries.items()))
    random_entries_num = random.randint(1, len(entries))

    random_entries = random.sample(entries, random_entries_num)
    return user, random_entries

def get_least_and_most_logged_in_users(user_entries: dict):
    user_logins = dict()

    for user, entries in user_entries.items():
        sum = 0

        for entry in entries:
            if get_message_type(entry.message) == MessageType.SUCCESSFUL_LOGIN:
                sum += 1

        user_logins[user] = sum

    min_user = min(user_logins, key=user_logins.get)
    max_user = max(user_logins, key=user_logins.get)

    return min_user, max_user
