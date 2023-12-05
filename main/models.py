from django.db import models as m


class Element(m.Model):
    name = m.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Elements"


class WeaponType(m.Model):
    name = m.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Weapon types"


class Region(m.Model):
    name = m.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Rarity(m.Model):
    rarity = m.CharField(max_length=42)

    def __str__(self):
        return self.rarity

    class Meta:
        verbose_name_plural = "Rarities"


class Character(m.Model):
    name = m.CharField(max_length=124, unique=True)
    image = m.ImageField(upload_to="media/characters/images/", blank=True, null=True)
    elements = m.ManyToManyField(Element)
    weapon_type = m.ForeignKey(WeaponType, on_delete=m.CASCADE)
    region = m.ForeignKey(Region, on_delete=m.CASCADE)
    rarity = m.ForeignKey(Rarity, on_delete=m.CASCADE)
    added_at = m.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
