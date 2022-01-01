#!/usr/bin/env python3
import praw  # Reddit API
#import pandas as pd  # allows to export to .csv file easily
import csv
import datetime as dt  # use of date and time
import sched, time  # use of scheduler for running code for a certain amount of time
from datetime import datetime

# use praw to log into reddit

reddit = praw.Reddit(
    client_id="XXXXXXXXXXXXXX",
    client_secret="-XXXXXXXXXXXXXXXXXXXXXXXXXX",
    user_agent="Users",
    username="username",
    password="password",
)

# define the subreddits you want to scrape

woodworking = reddit.subreddit("woodworking")
beginnerwoodworking = reddit.subreddit("beginnerwoodworking")
woodworkingplans = reddit.subreddit("woodworkingplans")
woodworkingvideos = reddit.subreddit("woodworkingvideos")
garageporn = reddit.subreddit("garageporn")
somethingimade = reddit.subreddit("somethingimade")
toolporn = reddit.subreddit("toolporn")
workbenches = reddit.subreddit("workbenches")

# Define the schedule

s = sched.scheduler(time.time, time.sleep)

# Create the dictionary that will be appended with each loop and then exported
field_names= ['woodworking active users' ,
              'beginnerwoodworking active users',
              'woodworkingplans active users' ,
              'woodworkingvideos active users',
              'garageporn active users',
              'somethingimade active users',
              'toolporn',
              'workbenches',
              'date'] 
users_dict = {
    "woodworking active users": [],
    "beginnerwoodworking active users": [],
    "woodworkingplans active users": [],
    "woodworkingvideos active users": [],
    "garageporn active users": [],
    "somethingimade active users": [],
    "toolporn active users": [],
    "workbenches active users": [],
    "date": [],
}

# Main loop: for a certain amount of minutes get the active accounts and append the dictionary.
# Wait some time, then loop again.


t_end = time.time() + 60 * 43801
while time.time() < t_end:
    now = datetime.now()
    woodworking._fetch()
    beginnerwoodworking._fetch()
    woodworkingplans._fetch()
    woodworkingvideos._fetch()
    garageporn._fetch()
    somethingimade._fetch()
    toolporn._fetch()
    workbenches._fetch()

    users_dict["woodworking active users"].append(woodworking.active_user_count)
    users_dict["beginnerwoodworking active users"].append(beginnerwoodworking.active_user_count)
    users_dict["woodworkingplans active users"].append(woodworkingplans.active_user_count)
    users_dict["woodworkingvideos active users"].append(woodworkingvideos.active_user_count)
    users_dict["garageporn active users"].append(garageporn.active_user_count)
    users_dict["somethingimade active users"].append(somethingimade.active_user_count)
    users_dict["toolporn active users"].append(toolporn.active_user_count)
    users_dict["workbenches active users"].append(workbenches.active_user_count)
    users_dict["date"].append(now)

    # Export to a csv file
    keys=sorted(users_dict.keys())
    with open ("userdataweek.csv" , "w") as outfile:
        writer=csv.writer(outfile, delimiter = "\t")
        writer.writerow(keys)
        writer.writerows(zip(*[users_dict[key] for key in keys]))

    print("woodworking active user count:",woodworking.active_user_count)
    print(now)
    time.sleep(3600)