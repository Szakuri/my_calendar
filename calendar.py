class ListingStrategy:
    def begin(self):
        pass

    def event(self, title, date, time):
        pass

    def end(self):
        pass


    def list_calendar(calendar, listing_strategy):
        listing_strategy.begin()

        for event in calendar:
            ...
            pass

        listing_strategy.end()