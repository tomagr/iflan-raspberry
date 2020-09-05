from django.db import models

class Log(models.Model):
    log_name = models.CharField(max_length=200)
    def __str__(self):
        return self.log_name

    def amiguizar(self):
        return self.log_name[:-1] + "itis"

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)