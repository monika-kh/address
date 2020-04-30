from django.db import models


# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=40)
    state_code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=40)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="district")
    dis_code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Block(models.Model):
    name = models.CharField(max_length=40)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="block"
    )
    block_code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=40)
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name="ward")
    ward_code = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
