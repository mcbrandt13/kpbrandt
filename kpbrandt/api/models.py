from django.db import models
import random


class WordManager(models.Manager):
    def random(self):
        count = self.aggregate(count=models.Count('id'))['count']
        random_index = random.randint(0, count - 1)
        return self.all()[random_index]


class BaseWordModel(models.Model):
    objects = WordManager()

    class Meta:
        abstract = True


class Adverb(BaseWordModel):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word


class Verb(BaseWordModel):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word


class Adjective(BaseWordModel):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word


class Noun(BaseWordModel):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word


class Quotes(BaseWordModel):
    created = models.DateTimeField(auto_now_add=True)
    phrase = models.CharField(max_length=500, blank=False, null=False, unique=True)
    author = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.phrase

    class Meta:
        ordering = ('created',)
