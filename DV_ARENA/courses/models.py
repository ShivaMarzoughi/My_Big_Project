from django.db import models




# جدولی برای نام مدرس دوره
class Teacher_of_course(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name

# جدولی برای جزییات دوره
class CoursesCardModel(models.Model):
    teacher_of_course=models.ForeignKey(Teacher_of_course,on_delete=models.PROTECT)
    card_photo=models.ImageField(upload_to='card_photo/%Y/%m/%d')
    course_name=models.CharField(max_length=20,blank=True)
    short_description=models.CharField(max_length=50,blank=True)
    long_description=models.TextField()
    number_of_lecture=models.IntegerField()
    time_of_course=models.IntegerField()
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course_name


# جدولی برای سرفصل های دوره
class Course_Details(models.Model):
    name_of_course=models.ForeignKey(CoursesCardModel,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    time_of_video=models.IntegerField()
    # file_url=models.FileField(upload_to='download_file/%Y/%m/%d')
    url_file=models.URLField(verbose_name="لینک دانلود",null=True, blank=True)

    def __str__(self):
        return self.title




