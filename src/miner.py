import pdb

class Miner:
    def __init__(self,journal):
        self.journal = journal
        self.createMoodAndActivityDictionary()

    def createMoodAndActivityDictionary(self): #crammed into one method as to avoid scanning journal twice
        self.moods = []
        self.activities = []
        for entry in self.journal:
            if not entry.mood in self.moods:
                self.moods.append(entry.mood)

            for activity in entry.activities: #oh wow this is fucking bad.
                if not activity in self.activities and not activity is '' :
                    self.activities.append(activity)

    def apriori(self,sup,conf):
        freqPatterns = {} #both are gonna be arrays of itemsets basically.
        interestingRules = {}
        candidateSets = {}
        setSize = 1

        for activity in self.activities:
            candidateSets[frozenset({activity})] = 0

        for mood in self.moods:
            candidateSets[frozenset({mood})] = 0

        while candidateSets:
            newFreqSets = {}
            newCandidateSets = {}
            
            for entry in self.journal:
                for itemset in candidateSets:
                    if itemset.issubset(entry.activities.union(entry.mood)):
                        candidateSets[itemset]+=1

            # pdb.set_trace()
            for itemset in candidateSets:
                if candidateSets[itemset]>=sup:
                    newFreqSets[itemset]=candidateSets[itemset]

            setSize+=1

            for itemset in newFreqSets:
                # del candidateSets[itemset] #ERR: dictionary changes size!
                for otherset in newFreqSets:
                    potentialSet = frozenset(itemset.union(otherset))
                    if(len(potentialSet) is setSize):

                        if setSize > 2:
                            subsetCount=0
                            for compSet in newFreqSets: #oh y god 
                                if compSet.issubset(potentialSet):
                                    subsetCount+=1

                            if subsetCount is setSize:
                                newCandidateSets[potentialSet]=0                               
                        else:
                            newCandidateSets[potentialSet]=0                                                           
                        
            candidateSets = newCandidateSets
            freqPatterns.update(newFreqSets)
            
            # go through candidate sets. Add freq ones to freqPatterns, erase them all.
            # based on freq patterns, generate new ones


        #Now that we have patterns, let's figure some rules.
        each itemset in freqPatterns:
            #time to find some interesting rules.

        return freqPatterns


class Itemset:
    def __init__(self,items):
        self.items = frozenset(items)
        self.count = 0

class Rule:
    def __init__(self):
        self.rule = "wow"