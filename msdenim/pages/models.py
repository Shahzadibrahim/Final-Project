from django.db import models



# Home Page

class Home(models.Model):
    backg = models.ImageField(upload_to='static/images')
    heading1 = models.CharField(max_length=50)
    heading2 = models.CharField(max_length=100)

# Concepts Page

class Concepts(models.Model):
    img1 = models.ImageField(upload_to='static/images', blank = True)
    img2 = models.ImageField(upload_to='static/images', blank = True)
    img3 = models.ImageField(upload_to='static/images', blank = True)
    img4 = models.ImageField(upload_to='static/images', blank = True)
    img5 = models.ImageField(upload_to='static/images', blank = True)
    img6 = models.ImageField(upload_to='static/images', blank = True)
    img7 = models.ImageField(upload_to='static/images', blank = True)
    img8 = models.ImageField(upload_to='static/images', blank = True)
    img9 = models.ImageField(upload_to='static/images', blank = True)
    img10 = models.ImageField(upload_to='static/images', blank = True)
    img11 = models.ImageField(upload_to='static/images', blank = True)
    img12 = models.ImageField(upload_to='static/images', blank = True)
    img13 = models.ImageField(upload_to='static/images', blank = True)
    img14 = models.ImageField(upload_to='static/images', blank = True)
    img15 = models.ImageField(upload_to='static/images', blank = True)
    img16 = models.ImageField(upload_to='static/images', blank = True)
    img17 = models.ImageField(upload_to='static/images', blank = True)
    img18 = models.ImageField(upload_to='static/images', blank = True)
    img19 = models.ImageField(upload_to='static/images', blank = True)
    img20 = models.ImageField(upload_to='static/images', blank = True)
    img21 = models.ImageField(upload_to='static/images', blank = True)
    img22 = models.ImageField(upload_to='static/images', blank = True)
    heading1 = models.CharField(max_length=20, blank = True)
    heading2 = models.CharField(max_length=20, blank = True)
    heading3 = models.CharField(max_length=20, blank = True)
    heading4 = models.CharField(max_length=20, blank = True)
    heading5 = models.CharField(max_length=20, blank = True)







