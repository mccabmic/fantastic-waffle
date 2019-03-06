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

class Exercise(models.Model):
    name = models.CharField(max_length=32, null=True)
    muscles_worked = models.OneToManyField(
        'MuscleGroup', 
        on_delete=models.CASCADE
        )

    primary_muscle = models.OneToOneField(
        "Muscle",
        on_delete=models.CASCADE
        )

    secondary_muscle = models.OneToOneField(
        "Muscle",
        on_delete=models.CASCADE
        )
    
     def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(Max_length=32, null=True)
    method = models.OneToOneField(
        "Exercise",
         on_delete=models.CASCADE
         )
     
     def __str__(self):
        return self.name

class MuscleGroup(models.Model):
    name = models.CharField(Max_length=32, null=True)
    group = models.OneToManyField('Muscle', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Muscle(models.Model):
    name = models.CharField(max_length=32, null=True)

     def __str__(self):
        return self.name
    