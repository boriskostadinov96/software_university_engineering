from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            total_cost = room.expenses + room.room_cost
            if room.expenses >= total_cost:
                room.budget -= total_cost
                result.append(f"{room.name} paid {total_cost:.2f}$ and have {room.budget:.2f}$ left.")

            else:
                self.rooms.remove(room)
                result.append(f"{room.name} does not have enough budget and must leave the hotel.")

        return "\n".join(result)

    def status(self):
        result = []
        result += f"Total population: {sum([r.members_count for r in self.rooms])}\n"

        for r in self.rooms:
            result += f"{r.name} with {r.members_count} members. Budget: {r.budget:.2f}$, Expenses: {r.expenses:.2f}$\n"
            if r.children:
                counter = 0
                for c in r.children:
                    counter += 1
                    result += f"--- Child {counter} monthly cost: {(c.cost * 30):.2f}$\n"