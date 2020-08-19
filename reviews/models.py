from django.db import models

class Review(models.Model):
    user       = models.ForeignKey('user.User', on_delete = models.CASCADE)
    product    = models.ForeignKey('product.Product', on_delete = models.CASCADE)
    content    = models.CharField(max_length = 500)
    scroe      = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = 'reviews'

class ReviewImage(models.Model):
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    image  = models.CharField(max_length = 2000)

    class Meta:
        db_table = 'review_images'

class ReviewReputation(models.Model):
    like    = models.IntegerField()
    dislike = models.IntegerField()
    total   = models.IntegerField()

    class Meta:
        db_table = 'review_reputations'

class ReviewReply(models.Model):
    user    = models.ForeignKey('user.User', on_delete = models.CASCADE)
    review  = models.ForeignKey(Review, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 500)

    class Meta:
        db_table = 'review_replies'

