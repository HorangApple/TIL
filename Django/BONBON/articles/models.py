from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.TextField()
    content=models.TextField()
    def __repr__(self):
        return f"<{self.id}번글, {self.title}: {self.content}>"
    def __str__(self):
        return f"<{self.title}: {self.content}>"
        
class Comment(models.Model):
    content=models.TextField()
    article=models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="comments")
    def __repr__(self):
        return f"<{self.content}>"