import gspread

gc = gspread.service_account()
sh = gc.open("Legislators 2017")
worksheet = sh.get_worksheet(0)

list_of_hashes = worksheet.get_all_records()
print(list_of_hashes)


# https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# https://github.com/burnash/gspread
# https://docs.gspread.org/en/latest/oauth2.html
# https://docs.gspread.org/en/latest/api.html?highlight=append#gspread.worksheet.Worksheet.append_row

"""
for each one of the metrics calculate the delta
consider start_date, end_date, and week number
gather weekly data
generate graphic of the last 7 weeks
save goal
"""

"""
Week    Metrics


"""
