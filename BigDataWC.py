import pandas as pd
import numpy as np
import ReadData
import FootballClasses

class WCData(object):
    
    @staticmethod
    def ReadFile():
        rawData = pd.read_csv('data/results')
        WCTeams = ReadData.Reader.GetTeams()
        sLength = len(rawData.index)
        rawData = rawData.assign(homeTeamId=np.zeros(sLength))
        rawData = rawData.assign(awayTeamId=np.zeros(sLength))
        WCFinals = {
            'Date' : '1928-07-30',
            ''
        }
        for team in WCTeams:
            team.GetNextFixtures(60)
        
        rawDataFiltered = rawData[rawData['date'] > '1970-01-01']
        print(rawData)

        #input array: [{
        # 'home-wins' : last 20 matches
        # 'home-losses': last 20 matches
        # 'home-draws' : last 20 matches
        # 'home-goals' : last 20 matches
        # 'home-conceived' : last 20 matches
        # 'home-world-cup-wins' : from all time until
        # 'home-world-cup-losses' : from all time until
        # 'home-world-cup-titles' : from all time until
        # 'home-world-cup-runner-up' : from all time until
        # 'home-world-cup-matches' : from all time until
        # 'away-wins' : last 20 matches
        # 'away-losses': last 20 matches
        # 'away-draws' : last 20 matches
        # 'away-goals' : last 20 matches
        # 'away-conceived' : last 20 matches
        # 'away-world-cup-wins' : from all time until
        # 'away-world-cup-losses' : from all time until
        # 'away-world-cup-titles' : from all time until
        # 'away-world-cup-runner-up' : from all time until
        # 'away-world-cup-matches' : from all time until
        # }]