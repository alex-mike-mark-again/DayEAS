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
        interestingRules =  []
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
        #So, sets that don't have a superset in freqPatterns are candidates for getting a whole bunch of cool thing.
        #
        for itemset in freqPatterns:
            for otherset in freqPatterns:
                if itemset.isdisjoint(otherset):
                    confidence = freqPatterns[itemset.union(otherset)]/freqPatterns[otherset]
                    if confidence >= sup:
                        interestingRules.append(Rule(itemset,otherset,confidence,freqPatterns[frozenset(itemset.union(otherset))]))

            #time to find some interesting rules.

        return freqPatterns

class Rule:
    def __init__(self,ant,con,conf,freq):
        self.ant = ant
        self.con = con
        self.conf = conf
        self.freq = freq

    def __srt__(self):
        return str(self.ant)+"=>"+str(self.con)+" : "+str(self.conf)+", "+str(self.freq)+" occurences"

    def __eq__(self, other):
        return self.ant is other.ant and self.con is other.con