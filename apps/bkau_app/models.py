from __future__ import unicode_literals
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default=0)

    def __repr__(self):
        return "<Book: {} {}>".format(self.title, self.desc)


class Author(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField(default=0)
    book = models.ManyToManyField(Book, related_name="authors")

    def __repr__(self):
        return "<Author: {} {} {}>".format(self.fname, self.lname, self.email)
