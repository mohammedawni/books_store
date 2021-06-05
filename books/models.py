from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid
# Create your models here.
class Book(models.Model):
    """Model definition for Book."""

    # TODO: Define fields here
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Book."""
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])

class Review(models.Model):
    """Model definition for Review."""

    # TODO: Define fields here
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    review = models.CharField(max_length=256)

    class Meta:
        """Meta definition for Review."""

        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        """Unicode representation of Review."""
        return self.review
