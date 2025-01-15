from django.db import models




class Question(models.Model):
    LEVEL1='Easy'
    LEVEL2='Difficult'
    LEVEL3='Intermediate'

    LEVEL_QUESTION = [
        (LEVEL1, 'Easy'),
        (LEVEL2, 'Difficult'),
        (LEVEL3, 'Intermediate'),
    ]


    STATUS1='Answered'
    STATUS2='Not Answered'

    RESPONSE_STATUS=[
    (STATUS1,'Answered'),
    (STATUS2,'Not Answered'),
    ]

    title=models.CharField(max_length=100)
    published=models.DateField(auto_now_add=True)
    response=models.TextField()
    level=models.CharField(max_length=15,choices=LEVEL_QUESTION,default=LEVEL1)
    response_status=models.CharField(max_length=15,choices=RESPONSE_STATUS,default=STATUS2)


    def __str__(self):
        return self.title
