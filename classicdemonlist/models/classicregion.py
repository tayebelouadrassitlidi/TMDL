from django.db import models

class ClassicRegion(models.Model):
    name = models.CharField(max_length=100)
    points = models.FloatField(default=0)

    def calculate_points(self):
        total_points = 0

        for player in self.classicplayer_set.all():
            total_points += player.points

        self.points = total_points
        self.save(update_fields=['points'])
        return total_points
    
    class Meta:
        verbose_name = "Classic Region"
        verbose_name_plural = "Classic Regions"

    def __str__(self):
        return f"{self.name} - {round(self.points, 2)} points"