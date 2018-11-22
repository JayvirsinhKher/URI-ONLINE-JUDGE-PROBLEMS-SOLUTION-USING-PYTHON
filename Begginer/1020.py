

days = int(input())

year = int(days/365)

t_days = days%365

months = int(t_days/30)

t_t_days = t_days%30

print(year,"ano (s)",end="\n")
print(months,"mes (es)",end="\n")
print(t_t_days,"dia (s)",end="\n")
