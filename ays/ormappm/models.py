from django.db import models

# Create your models here.

from django.contrib import admin

class bookdetail(models.Model):
    student_name=models.CharField(max_length=20);
    reg_no=models.IntegerField();
    dep=models.CharField(max_length=30);
    book_name=models.CharField(max_length =30,primary_key=True);
    author_name=models.CharField(max_length=30);
    book_refno=models.IntegerField();
    dateof_taken=models.DateField();
    dateof_return=models.DateField();

class bookdetailAdmin(admin.ModelAdmin):
    list_display=("student_name","reg_no","dep","book_name","author_name","book_refno","dateof_taken","dateof_return");
