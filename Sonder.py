print("Hello")



# Your last Python code is saved below:
# # The code below implements a simple event pricing worker whose job is to
# # adjust the prices of events once per day until the date of the event is reached.
# # Some events are special and have unique rules to update their price.
# #
# # Rules:
# #  - By default, the price of an event should be decreased by $10 per day until the date of the event.
# #  - We should increase the price of events with the type "Music Festival" by $10 per day,
# #      since demand is high.
# #  - We should never adjust the price of events with the type "Corporate Convention", since
# #      demand is constant.
# #  - If there are less than 7 days until the event, the price of that event should
# #      be adjusted twice as quickly.
# #  - The price of an event should never exceed $500
# #  - The price of an event should never be less than $50
# #
# # The challenge:
# #  - Add support for a "Ballroom Dancing" event type. The price of these events should be adjusted twice as quickly as the default case.
# #  - Refactor or rewrite the update function so that we can easily add more event types in the future.

class Event(object):
    def __init__(self, event_type, days_until_date, price):
        self.event_type = event_type
        self.days_until_date = days_until_date
        self.price = price

        self.basePrice = 10

    def __repr__(self):
        return "Event: %s, Days until date: %s, Price: $%s" % (self.event_type, self.days_until_date, self.price)

    def adjustPrice(self):
        print("self.price: {}".format(self.price))
        if self.price < 50:
          print("Expected adjust price is {}. Price cannot be below $50. Adjusting price to $50".format(self.price))
          self.price = 50
        elif self.price > 500:
          print("Expected adjust price is {}. Price cannot be above $500. Adjusting price to $500".format(self.price))
          self.price = 500

class MusicFestival(Event):
    def adjustPrice(self):
        if self.days_until_date < 7:
          self.price += self.basePrice * 2
        else:
          self.price += self.basePrice

        super(MusicFestival, self).adjustPrice()
    
class CorporateConvention(Event):
    pass

class BallRoomDancing(Event):
    def adjustPrice(self):
        if self.days_until_date < 7:
          self.price -= self.basePrice * 4
        else:
          self.price -= self.basePrice * 2
        
        super(BallRoomDancing, self).adjustPrice()

class OtherEvent(Event):
    def adjustPrice(self):
        if self.days_until_date < 7:
          self.price -= self.basePrice * 2
        else:
          self.price -= self.basePrice

        super(OtherEvent, self).adjustPrice()

class EventUpdater:
    def __init__(self, events): # List of Event objects
        self.events = events

    def update(self):
        for event in self.events:
            event.adjustPrice()

            print("event.event_type: {}".format(event.event_type))
            print("event.price: {}".format(event.price))
            print("event.days_until_date: {}".format(event.days_until_date))
            print("\n")

            event.days_until_date = event.days_until_date - 1

events = [OtherEvent(event_type="FooBar Event", days_until_date=9, price=250)]

musicFestivalEvent1 = MusicFestival(event_type="Music Festival", days_until_date=7, price=500)

corporateConventionEvent1 = CorporateConvention(event_type="Corporate Convention", days_until_date=100, price=1000)

ballRoomDancingEvent1 = BallRoomDancing(event_type="BallRoom Dancing", days_until_date=2, price=20)

events.append(musicFestivalEvent1)
events.append(corporateConventionEvent1)
events.append(ballRoomDancingEvent1)

EventUpdater(events).update()
EventUpdater(events).update()

print(events)

