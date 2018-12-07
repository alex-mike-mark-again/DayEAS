# Stores data for entires
import numpy

class Entry:
    def __init__(self,date,mood,activities,note):
        self.mood = mood
        self.note = note
        self.date = date
        self.activities = activities  # Should be a set of strings

    #does a dot product between the activities of two entries.
    def dot(self, other):
        return None

    def add(self,other):
        return None