class NationalPark:

    def __init__(self, name):
        self.name = name
        print(f"{self.name} has been created!")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and not hasattr(self, "name") and len(new_name) >= 3:
            self._name = new_name
        else:
            raise Exception("The name must be a string")
        
    def trips(self):
       return [trip for trip in Trip.all if trip.national_park == self if isinstance(trip, Trip)]
    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        return len([park for park in self.trips()])
    
    def best_visitor(self):
        visitors = {}
        for trip in self.trips():
            if trip.visitor.name not in visitors:
                visitors[trip.visitor.name] = 1
            else:
                visitors[trip.visitor.name] += 1
        # print(visitors)
        top = max(visitors, key= lambda name : visitors[name])
        # print(top)
        for trip in self.trips():
            if trip.visitor.name == top:
                print(trip.visitor.name)
                return trip.visitor
        if visitors == 0: 
            return 0




class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.__class__.all.append(self)
        print(f"{self.visitor.name} has vistited {self.national_park.name}")
    
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, new_visitor):
        if isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
        else:
            raise Exception("The visitor must be of class type Visitor")
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, new_park):
        if isinstance(new_park, NationalPark):
            self._national_park = new_park
        else:
            print('new park must be of class instance NationalPark')
    
    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, new_date):
        if isinstance(new_date, str) and len(new_date) >= 7:
            self._start_date = new_date
        else:
            raise Exception("The new date must be of class instance Str and formatted as Month, day.")
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, new_date):
        if isinstance(new_date, str) and len(new_date) >= 7:
            self._end_date = new_date
        else:
            raise Exception("the date must be a string.")

    



class Visitor:

    def __init__(self, name):
        self.name = name
        print(f"{self.name} has been created as a Visitor!")
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15:
            self._name = new_name
        else:
            raise Exception
        
    def trips(self):
       return [trip for trip in Trip.all if trip.visitor == self]

    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        if isinstance(park, NationalPark):
            return len([trip.national_park for trip in self.trips() if trip.national_park == park])