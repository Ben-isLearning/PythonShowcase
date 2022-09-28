class Menu:

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"{self.name} is available from {self.start_time}, untill {self.end_time}"

    def calculate_bill(self, purchased_items):
        total = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                print(purchased_item)
                total += self.items[purchased_item]
        return total


brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
                         }, 1100, 1600)

print(brunch.name)

early_bird = Menu("Early Bird", {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, 1500, 1800)

print(early_bird.name)

dinner = Menu("Dinner", {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, 1700, 2300)

print(dinner.name)

kids = Menu("Kids", {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, 1700, 2300)

print(kids.name)

print(brunch)

print(brunch.calculate_bill(['pancakes', 'waffles']))


class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f"We're located at {self.address}"

    def available_menus(self, time):
        if time > 2300 or time < 1100:
            return "Sorry, we're closed."
        if time >= 1800:
            return "The Dinner and Kids menus are available."
        if time >= 1700:
            return "The Early-Bird, Dinner and Kids menus are available"
        if time >= 1600:
            return "The Earlybird menu is available"
        if time >= 1500:
            return "The Brunch and Early Bird menus are available"
        if time >= 1100:
            return "The Brunch menu is avaliable"


flagship_store = Franchise("1232 West End Road", [
                           brunch, early_bird, kids, dinner])

new_installment = Franchise("12 Easy Mulberry Street", [dinner, kids])


print(flagship_store)

print(flagship_store.available_menus(1700))


class Buisness:
    def __init__(self, name, franchise):
        self.name = name
        self.franchise = franchise


first = Buisness("Basta Fazoolin' with my Heart", [
                 flagship_store, new_installment])

arepas_menu = Menu("All Day", {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, 1000, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)


srs_bsns = Buisness("Take a' Arepa", arepas_place)
