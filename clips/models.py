from typing import Any, Dict, Iterable, Optional, Tuple
from django.db import models
import uuid
from datetime import datetime
from .storage import delete_clip_oci

# Create your models here.


class Clip(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    uuid = models.CharField(max_length=200, unique=True, default=uuid.uuid4().hex)
    created_at = models.DateTimeField("date created")
    updated_at = models.DateTimeField("date updated")
    url = models.CharField(max_length=200)
    url_expiration = models.DateTimeField("date url expires")
    thumbnail_url = models.CharField(max_length=200)
    view_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs) -> None:
        self.created_at = self.created_at or datetime.now()
        self.updated_at = datetime.now()

        return super().save(*args, **kwargs)
    
    def delete(self, using: Any = ..., keep_parents: bool = ...) -> Tuple[int, Dict[str, int]]:
        delete_clip_oci(self.uuid)

        return super().delete(using, keep_parents)

    def __str__(self):
        return f"{self.title} by {self.user.username}"


class Like(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField("date created")
