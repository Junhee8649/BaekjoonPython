year = 60 * 24 * 365
day = 60 * 24
hour = 60

for _ in range(int(input())):
    game_year, game_day, game_hour = 0,0,0
    game, minute = input().split(",")
    minute = int(minute)
    if minute >= year:
        game_year = minute // year
        minute -= game_year * year
    if minute >= day:
        game_day = minute // day
        minute -= game_day * day
    if minute >= hour:
        game_hour = minute // hour
        minute -= game_hour * hour
    if game_year != 0:
        print(f"{game} - {game_year} year(s) {game_day} day(s) {game_hour} hour(s) {minute} minute(s)")
    elif game_day != 0:
        print(f"{game} - {game_day} day(s) {game_hour} hour(s) {minute} minute(s)")
    elif game_hour != 0:
        print(f"{game} - {game_hour} hour(s) {minute} minute(s)")
    else:
        print(f"{game} - {minute} minute(s)")