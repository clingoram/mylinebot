from django.db import models

# Create your models here.
class LatestNews(models.Model):
    '''
    爬蟲新聞暫存表
    '''
    title = models.CharField(max_length=230,blank=False)
    url = models.URLField(max_length=500, blank=True, null=True)
    scrapedAt = models.DateTimeField(auto_now_add=True)