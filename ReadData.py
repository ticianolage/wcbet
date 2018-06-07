import http.client
import json
from FootballClasses import Competition
import FootballClasses

class Reader(object):
    key = 'dbaa97253c1d43c481f7714a4e3fed52'
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': key, 'X-Response-Control': 'minified' }

    @staticmethod
    def GetCompetitions():
        Reader.connection.request('GET', '/v1/competitions', None, Reader.headers )
        response = json.loads(Reader.connection.getresponse().read().decode(), object_hook=FootballClasses.ToCompetition)
        return response

    @staticmethod
    def GetTeams(id=467):
        Reader.connection.request('GET', '/v1/competitions/' + str(id) + '/teams', None, Reader.headers )
        response = json.loads(Reader.connection.getresponse().read().decode())
        teamsDic = response['teams']
        teams = []
        for dic in teamsDic:
            teams.append(FootballClasses.ToTeam(dic))
        return teams

    @staticmethod
    def GetFixtures(TeamId, TimeFrameFilter):
        Reader.connection.request('GET', '/v1/teams/' + str(TeamId) + '/fixtures?timeFrame=' + TimeFrameFilter, None, Reader.headers )
        response = json.loads(Reader.connection.getresponse().read().decode())
        fixturesDic = response['fixtures']
        fixtures = []
        for dic in fixturesDic:
            fixtures.append(FootballClasses.ToFixture(dic))
        return fixtures
