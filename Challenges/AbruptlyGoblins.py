
# gamer01 = {"name": "Mike", "availability": ["Magic Monday"]}
# print(gamer01)
# print(gamer01["name"])
# print(gamer01["availability"])

# gamer02 = {"name": "", "availability": []}
# print(gamer02)
# print(bool(gamer02["name"]))
# print(bool(gamer02["availability"]))

# gamer = {"name": "", "availability": []}
# gamer = {"name": "Mike", "availability": ["Magic Monday"]}

gamers = []


def add_gamer(gamer, gamers_list):
    if (gamer["name"] and gamer["availability"]):
        gamers_list.append(gamer)
        return gamers_list
    else:
        return "Error, please provide your name, and your availabilty."


add_gamer({'name': 'Thomas Nelson', 'availability': [
          "Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': [
          "Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Michelle Reyes', 'availability': [
          "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': [
          "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': [
          "Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': [
          "Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': [
          "Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': [
          "Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': [
          "Monday", "Tuesday", "Wednesday"]}, gamers)

# print(gamers)


def build_daily_frequency_table():
    return {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}


count_availability = build_daily_frequency_table()
# print(count_availability)


def calculate_availability(gamers_list, availible_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            availible_frequency[day] += 1
            # print(day)
    return availible_frequency


# print(calculate_availability(gamers, count_availability))

availability_table01 = calculate_availability(gamers, count_availability)

print(availability_table01)


def find_best_night(availability_table):
    max_num = 0
    for num in availability_table.values():
        if num > max_num:
            max_num = num
        best_night = list(availability_table.keys())[
            list(availability_table.values()).index(max_num)]
    return best_night


# print(find_best_night(availability_table01))
best_night = find_best_night(availability_table01)
print(best_night)
# test = {"george": 12, "amber": 15}
# max_num = 15
# print(test.keys())
# print(list(test.keys())[list(test.values()).index(max_num)])


def available_on_night(gamers_list, day):
    attendance_list = []
    for gamer in gamers_list:
        if day in gamer["availability"]:
            attendance_list.append(gamer.get("name"))
            # print(gamer.get("name"))
    return attendance_list


# print(available_on_night(gamers, best_night))
gamers_on_best_night = available_on_night(gamers, best_night)
print(gamers_on_best_night)

game = "Abruptly Goblins!"
name = "User"
form_email = """
Hello {name},
{best_night} is the most popular day to play.
Join us to play {game}.
""".format(name=name, best_night=best_night, game=game)

# print(form_email)


def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_on_best_night:
        game = "Abruptly Goblins!"
        name = gamer
        form_email = """
        Hello {name},
        {best_night} is the most popular day to play.
        Join us to play {game}
        """.format(name=name, best_night=best_night, game=game)
        print(form_email)
    return ("Success")


#print(send_email(gamers_on_best_night, best_night, "Abruptly Goblins!"))

print("---")


def remaining_players():
    unable_to_attend_best_night = []
    for gamer in gamers:
        if gamer.get("name") not in gamers_on_best_night:
            unable_to_attend_best_night.append(gamer)
    return(unable_to_attend_best_night)


unable_to_attend_best_night = remaining_players()
print(unable_to_attend_best_night)
# print(gamer.get("name"))
# print(gamers_on_best_night)


second_night_availability_table = build_daily_frequency_table()
print(second_night_availability_table)

second_night_availability = calculate_availability(
    unable_to_attend_best_night, second_night_availability_table)
print(second_night_availability)

second_night = find_best_night(second_night_availability)
print(second_night)


available_second_game_night = available_on_night(gamers, second_night)
print(available_second_game_night)


def send_email2(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        game = "Abruptly Goblins!"
        name = gamer
        form_email = """
        Hello {name},
        {best_night} is the most popular day to play.
        Join us to play {game}
        """.format(name=name, best_night=second_night, game=game)
        print(form_email)
    return ("Success")


print(send_email2(available_second_game_night, second_night, "Abruptly Goblins!"))
