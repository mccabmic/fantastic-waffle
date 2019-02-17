from django.db import models


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_location = models.CharField(max_length=32, null=True)
    team_nickname = models.CharField(max_length=32, null=True)
    team_abbrv = models.CharField(max_length=8, null=True)


class TeamOwner(models.Model):
    team = models.OneToOneField('Team', on_delete=models.CASCADE)
    fname = models.CharField(max_length=32, null=True)
    lname = models.CharField(max_length=32, null=True)


class Matchup(models.Model):
    week = models.IntegerField()
    winner = models.BooleanField(help_text='1 for home team, 0 for away team')
    home_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='+')
    home_score = models.FloatField()
    away_team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='+')
    away_score = models.FloatField()

    def winning_team(self):
        if self.winner:
            return self.home_team
        return self.away_team
