import ReadData

class Competition(object):
    def __init__(self, id, caption, league, year, numberOfTeams, numberOfGames, lastUpdated):
        self.id = id
        self.caption = caption
        self.league = league
        self.year = year
        self.numberOfTeams = numberOfTeams
        self.numberOfGames = numberOfGames
        self.lastUpdated = lastUpdated

class Team(object):
    def __init__(self, id, name, shortName, squadMarketValue, crestUrl):
        self.id = id
        self.name = name
        self.shortName = shortName
        self.squadMarketValue = squadMarketValue
        self.crestUrl = crestUrl
        self.PastFixtures = []
        self.NextFixtures = []
    
    def GetPastFixtures(self, days):
        self.PastFixtures = ReadData.Reader.GetFixtures(self.id, 'p' + str(days))

    def GetNextFixtures(self, days):
        self.NextFixtures = ReadData.Reader.GetFixtures(self.id, 'n' + str(days))



class Fixture(object):
    def __init__(self, id, competitionId, date, matchday, homeTeamName, homeTeamId, awayTeamName, awayTeamdId, result):
        self.id = id
        self.competitionId = competitionId
        self.date = date
        self.matchday = matchday
        self.homeTeamName = homeTeamName
        self.homeTeamId  = homeTeamId
        self.awayTeamName = awayTeamName
        self.awayTeamId = awayTeamdId
        self.result = Result(result)

class Result(object):
    def __init__(self, goalsHomeTeam, goalsAwayTeam):
        self.goalsAwayTeam = goalsAwayTeam
        self.goalsHomeTeam = goalsHomeTeam

    def __init__(self, dic):
        self.goalsAwayTeam = dic['goalsAwayTeam']
        self.goalsHomeTeam = dic['goalsHomeTeam']


import json
def ToCompetition(dct):
    return Competition(dct['id'], dct['caption'], dct['league'], dct['year'], dct['numberOfTeams'], dct['numberOfGames'], dct['lastUpdated'])

def ToTeam(dct):
    return Team(dct['id'], dct['name'], dct['shortName'], dct['squadMarketValue'], dct['crestUrl'])

def ToFixture(dct):
    return Fixture(dct['id'], dct['competitionId'], dct['date'], dct['matchday'], dct['homeTeamName'], dct['homeTeamId'], dct['awayTeamName'], dct['awayTeamId'], dct['result'])