from django.db import models


# Create your models here.
def get_last_season_id():
    last_season = Seasons.objects.last()
    return last_season.id if last_season else None


class Seasons(models.Model):

    class Meta:
        verbose_name_plural = "Seasons"

    season = models.PositiveIntegerField()

    def __str__(self):
        return f"Season: {self.season - 1}/{self.season - 2000}"


class Matches(models.Model):

    class Meta:
        verbose_name_plural = "Matches"

    VENUE_CHOICES = {
        "Home": "Home",
        "Away": "Away"
    }

    opponent = models.CharField(max_length=30)
    venue = models.CharField(max_length=4, choices=VENUE_CHOICES, default="Home")
    date = models.DateField(auto_now=False, auto_now_add=False)
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE, default=get_last_season_id)

    def __str__(self):
        return f'{self.venue} v {self.opponent} on {self.date}'


class Players(models.Model):

    class Meta:
        verbose_name_plural = "Players"

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Games(models.Model):

    class Meta:
        verbose_name_plural = "Games"

    RESULT_CHOICES = {
        "W": "Won",
        "L": "Lost",
        "S": "Set"
    }
    match = models.ForeignKey(Matches, on_delete=models.CASCADE)
    player = models.ForeignKey(Players, on_delete=models.CASCADE)
    points = models.PositiveSmallIntegerField()
    darts = models.PositiveSmallIntegerField()
    result = models.CharField(max_length=1, choices=RESULT_CHOICES)
