from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Note Title: {self.title}  Body: {self.body} Created: {self.created_at}  Updated: {self.updated_at}'
