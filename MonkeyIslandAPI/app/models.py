from django.db import models

class Character(models.Model):

    ROLES = (
        ('MC', 'Main Character'),
        ('SC', 'Secondary Character'),
    )

    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    role = models.CharField(max_length=2, choices=ROLES, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Character"
        verbose_name_plural = "Characters"

class Pirate(Character):
    
    is_pirate = models.BooleanField(default=True)
    is_captain = models.BooleanField(default=False)

    def __str__(self) -> str:
        if not self.is_captain:
            title = "Pirate"
        else:
            title = "Captain"

        return f"{title} {self.name}"

    class Meta:
        verbose_name = "Pirate"
        verbose_name_plural = "Pirates"

class Insult(models.Model):

    insult = models.CharField(max_length=200)
    comeback = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.insult

    class Meta:
        verbose_name = "Insult"
        verbose_name_plural = "Insults"