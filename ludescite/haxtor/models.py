from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic(models.Model):
    diffLevel_LIST=(
        ("1","easy"),
        ("2","medium"),
        ("3","hard")
        )
    topicID = models.CharField(max_length=50,unique=True,primary_key=True)
    name = models.CharField(max_length=256,unique=True)
    diffLevel = models.CharField(max_length=1,choices=diffLevel_LIST)
    

    def __str__(self):
        return str(str(self.topicID) + "     " + str(self.name))


class Questions(models.Model):
    diffLevel_LIST=(
        ("1","easy"),
        ("2","medium"),
        ("3","hard")
        )
    quesID = models.CharField(max_length=50,unique=True,primary_key=True)
    topicID = models.ForeignKey(Topic, on_delete=models.PROTECT)
    quesLevel = models.CharField(max_length=1,choices=diffLevel_LIST)
    quesText = models.CharField(max_length=256)
    quesImg = models.BooleanField()

    def __str__(self):
        return str(self.quesText)
    

class Answers(models.Model):
    ansID=models.CharField(max_length=50,unique=True,primary_key=True)
    quesID=models.ForeignKey(Questions,on_delete=models.PROTECT)
    ansText=models.CharField(max_length=254)
    ansCorrect=models.BooleanField()

    def __str__(self):
        return str(str(self.ansText) + "    " + str(self.ansCorrect) )

class UserProfile(models.Model):
    userCAT_LIST=(
        ("1","kids"),
        ("2","coder")
    )
    uID=models.CharField(max_length=50, unique=True, primary_key=True)
    user=models.OneToOneField(User,on_delete=models.DO_NOTHING)
    # name=models.CharField(max_length=30)
    # email=models.EmailField(max_length=254)
    # password=models.CharField(max_length=50)
    userCat = models.CharField(max_length=254,choices=userCAT_LIST)
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    

class UserProg(models.Model):
    EvolutionTable=(
        ("1","CupCake"),
        ("2","Pasterie"),
        ("3","FudgeCake")
    )
    uID=models.ForeignKey(User,on_delete=models.PROTECT)
    progScore=models.IntegerField()
    currEvolution=models.CharField(max_length=50,choices=EvolutionTable)
