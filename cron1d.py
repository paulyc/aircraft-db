import spider
import statistics

"""
Script to run every day
"""

# update aircraft where type and operator is missing
spider.update_new_acs_info()

# aggregate statistics of mdl, typ, and airlines
statistics.aggregate()

# TODO: generate CSV data
