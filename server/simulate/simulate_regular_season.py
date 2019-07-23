from server.external_apis.cf_data import CFData


class SimulateRegularSeason:
    def __init__(self, year: int):
        self.schedule = CFData().get_schedule(year=year)

    def run(self):
        print(self.schedule)


s = SimulateRegularSeason(2019)

s.run()
