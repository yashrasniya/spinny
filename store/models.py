from django.db import models
import datetime


# Create your models here.
class Box(models.Model):
    max_Area=100
    max_Volume=1000
    Total_week_limit=100
    Total_user_week_limit=5
    Length = models.FloatField(max_length=20,default=1,blank=True,)
    width = models.FloatField(max_length=20,default=1,blank=True)
    Height = models.FloatField(max_length=20,default=1,blank=True)
    Area = models.FloatField(max_length=20,default=1,blank=True)
    Volume = models.FloatField(max_length=20,default=1,blank=True)
    Created_by = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    Last_Updated = models.DateTimeField()

    def check_value(self):

        if self.Area>=self.max_Area:
            raise Exception("Area will not be more then "+str(self.max_Area))
        if self.Volume>=self.max_Volume:
            raise Exception("Volume will not be more then "+str(self.max_Volume))

    def check_limits(self):
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=7)
        obj=Box.objects.filter(Last_Updated__gt=week_ago)
        if obj.count()>=self.Total_week_limit:
            raise Exception(f"This week we are out of limit")
        obj = Box.objects.filter(Created_by=self.Created_by)
        if obj.count()>=self.Total_user_week_limit:
            raise Exception(f"This week you are out of limit")



    def save(self,force_insert=False, force_update=False, using=None, update_fields=None):
        self.Area=2*(self.Length+self.width+self.Height)
        self.Volume=self.Length* self.width*self.Height
        self.check_value()
        self.check_limits()
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
