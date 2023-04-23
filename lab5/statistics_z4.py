from parser_z2 import log_entry, get_user_from_entry, get_message_type, MessageType
import random
from typing import List
import statistics

def get_user_entries(entries: List[log_entry]):
    user_entries = dict()

    for entry in entries:
        user = get_user_from_entry(entry)

        if user and user in user_entries:
            user_entries[user].append(entry)
        elif user:
            user_entries[user] = [entry]

    return user_entries

def get_n_random_entries_from_random_user(entries: List[log_entry]):
    user_entries = get_user_entries(entries)

    user, entries = random.choice(list(user_entries.items()))
    random_entries_num = random.randint(1, len(entries))

    random_entries = random.sample(entries, random_entries_num)
    return user, random_entries

def get_session_time_mean_and_stddev(entries: List[log_entry]):
    connection_opened = dict()
    connection_times = []

    for entry in entries:
        msg_type = get_message_type(entry.message)
        # sometimes there is one line that is other and it doesnt have close, eg PAM service...
        # sometimes there is connection closed without starting one
        if msg_type != MessageType.OTHER and msg_type != MessageType.SESSION_CLOSED and entry.pid not in connection_opened:
            connection_opened[entry.pid] = entry.date
        elif msg_type == MessageType.SESSION_CLOSED and entry.pid in connection_opened:
            #abs because it goes from Dec to Jan and year isnt specified so it is 1900 by default so difference is negative
            connection_time_seconds = abs((entry.date - connection_opened[entry.pid]).total_seconds())

            connection_times.append(connection_time_seconds)
            del connection_opened[entry.pid]

    return statistics.mean(connection_times), statistics.stdev(connection_times)
        
def get_user_session_time_mean_and_stddev(entries: List[log_entry]):
    connection_opened = dict()
    user_connection_times = dict()

    for entry in entries:
        user = get_user_from_entry(entry)
        msg_type = get_message_type(entry.message)

        # sometimes there is one line that is other and it doesnt have close, eg PAM service...
        # sometimes there is connection closed without starting one
        if user and msg_type != MessageType.OTHER and msg_type != MessageType.SESSION_CLOSED and entry.pid not in connection_opened:
            connection_opened[entry.pid] = (user, entry.date)
        elif get_message_type(entry.message) == MessageType.SESSION_CLOSED and entry.pid in connection_opened:
            user, connection_open = connection_opened[entry.pid]
            connection_time_seconds = abs((entry.date - connection_open).total_seconds())

            if user in user_connection_times:
                user_connection_times[user].append(connection_time_seconds)
            else:
                user_connection_times[user] = [connection_time_seconds]

            del connection_opened[entry.pid]

    return {user: (statistics.mean(connection_times), statistics.stdev(connection_times)) 
            for user, connection_times in user_connection_times.items() if len(connection_times) > 1}

def get_least_and_most_logged_in_users(entries: List[log_entry]):
    user_entries = get_user_entries(entries)
    user_logins = dict()

    for user, entries in user_entries.items():
        sum = 0

        for entry in entries:
            if get_message_type(entry.message) == MessageType.SUCCESSFUL_LOGIN:
                sum += 1

        user_logins[user] = sum

    min_user = min(user_logins, key=user_logins.get)
    max_user = max(user_logins, key=user_logins.get)

    print(user_logins)
    return min_user, max_user
