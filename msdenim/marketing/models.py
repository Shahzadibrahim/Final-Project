from django.db import models


MALE, FEMALE = range(2)
GENDER = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE')
)

DARKDENIM, MEDIUMDEIM, LIGHTDENIM, INDIGO, COLORFUL, STRETCH, COTTON = range(7)
COLORS = (
    (DARKDENIM, 'DARKDENIM'),
    (MEDIUMDEIM, 'MEDIUMDENIM'),
    (LIGHTDENIM, 'LIGHTDENIM'),
    (INDIGO, 'COLORFUL'),
    (COLORFUL, 'COLORFUL'),
    (STRETCH, 'STRETCH'),
    (COTTON, 'COTTON'),
)

class Origins(models.Model):
    Origin = models.CharField('Origin', max_length=50,)
    gender = models.PositiveSmallIntegerField('Gender', choices=GENDER, default=MALE)
    Color = models.PositiveSmallIntegerField('Color', choices=COLORS, default=COLORS)
    Percentage =  models.TextField('Percentage', max_length=10)

    def __str__(self):
        return self.Origin

    class Meta:
        verbose_name = ('Origins')
