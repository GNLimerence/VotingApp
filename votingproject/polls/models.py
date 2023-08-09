from django.db import models

# Create your models here.
class Poll (models.Model):
    question_text = models.TextField(max_length=1000, blank=False, null=False)
    op_one = models.CharField(max_length=30, blank=False, null=False)
    op_two = models.CharField(max_length=30, blank=False, null=False)
    op_three = models.CharField(max_length=30, blank=False, null=False)
    op_four = models.CharField(max_length=30, blank=False, null=False)
    op_one_count = models.IntegerField(default=0)
    op_two_count = models.IntegerField(default=0)
    op_three_count = models.IntegerField(default=0)
    op_four_count = models.IntegerField(default=0)
    def total(self):
        return self.op_one_count + self.op_two_count + self.op_three_count +self.op_four_count

