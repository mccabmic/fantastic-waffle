from django.db import models

'''
A user will select a workout.  That workout will include:
    * - A name for the workout
    * - A set of exercises
    * - Number of repetitions per set
    * - Weight per set (lbs or kgs)
    * - An order in which to do the sets
'''

'''
An exercise has the following:
    * - A name for the exercise
    * - A method (equipment) of performing the exercise

I kinda want to change this so I could be like barbell.<exercise>
Feel like that'd be easier to  cope with. 
So a set would be barbell.exercise("bench press"), which would return
I guess a primary muscle group I'd be working
Vs something like dumbell.exercise("bench press")
'''

class Workout(models.Model):
    name = models.CharField(max_length=32, null=True)

class Set(models.Model):
    reps = models.IntegerField(default=5)
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE)

class Exercise(models.Model):
    name = models.CharField(max_length=32, null=True)
    set_owner = models.ForeignKey('Set', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Equipment(models.Model):
    name = models.CharField(max_length=32, null=True)
    method = models.ManyToManyField('Exercise')
    
    def __str__(self):
        return self.name

class Muscle(models.Model):
    name = models.CharField(max_length=32, null=True)
    exercise = models.ManyToManyField('Exercise')
    
    def __str__(self):
        return self.name
    