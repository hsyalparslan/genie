from django.db import models
from django.conf import settings
from django.contrib.sessions.models import Session
# Create your models here.




class SmartPhone(models.Model):
    # Do you own a Smartphone?
    YES_SMARTPHONE = 'Yes'
    NO_SMARTPHONE = 'No'
    MAYBE_SMARTPHONE = 'Maybe'


    SMART_PHONE_OWNERSHIP = (
        (YES_SMARTPHONE, 'Yes'),
        (NO_SMARTPHONE, 'No'),
        (MAYBE_SMARTPHONE, 'Maybe'),
               )    
    smart_phone_ownership = models.CharField(
        null=True, max_length=5,
        default=None, 
        choices=SMART_PHONE_OWNERSHIP, verbose_name='I can use wish statements to communicate what I would like to change about my life.')

    smart_phone_ownership2 = models.CharField(
        null=True, max_length=5,
        default=None, 
        choices=SMART_PHONE_OWNERSHIP, verbose_name='I can communicate my regrets over mistakes I made by using wish.')
    smart_phone_ownership3 = models.CharField(
        null=True, max_length=5,
        default=None, 
        choices=SMART_PHONE_OWNERSHIP, verbose_name='I am comfortable describing my feelings and emotions, particularly by using wish statements.')
    smart_phone_ownership4 = models.CharField(
        null=True, max_length=5,
        default=None, 
        choices=SMART_PHONE_OWNERSHIP, verbose_name='I can imagine the world differently than it is at this time.')
    smart_phone_ownership5 = models.CharField(
        null=True, max_length=5,
        default=None, 
        choices=SMART_PHONE_OWNERSHIP, verbose_name='I can convey discontent over my present situation.')
    smart_phone_ownership6 = models.CharField(
        null=True, max_length=5,
        default=None, 
        choices=SMART_PHONE_OWNERSHIP, verbose_name='I can talk about my past habits.')
    smart_phone_ownership7 = models.CharField(
        null=True, max_length=5,
        default=None, 
        choices=SMART_PHONE_OWNERSHIP, verbose_name='I can express how I do things differently than in the past.')
    smart_phone_ownership8 = models.CharField(
        null=True, max_length=5,
        default=None, 
        choices=SMART_PHONE_OWNERSHIP, verbose_name='I can assert agreement and disagreement.')
    smart_phone_ownership9 = models.CharField(
        null=True, max_length=5,
        default=None, 
        choices=SMART_PHONE_OWNERSHIP, verbose_name='I can describe my hopes and my future plans by using wish statements.')

#If 'Yes' How many hours a day do you access the Internet on it?
    SMART_PHONE_LESS_THAN_ONE_HOUR_A_DAY = 'Clueless'
    SMART_PHONE_ONE_TO_TWO_HOURS_A_DAY = 'Absolutely Baffled'
    SMART_PHONE_TWO_TO_FOUR_HOURS_A_DAY = 'Ill Informed'
    SMART_PHONE_FOUR_TO_SIX_HOURS_A_DAY = 'Slightly Capable'
    SMART_PHONE_SIX_TO_EIGHT_HOURS_A_DAY = 'Considerably Proficient'
    SMART_PHONE_EIGHT_PLUS_HOURS_A_DAY = 'PhD'


    SMART_PHONE_USAGE = (
        (SMART_PHONE_LESS_THAN_ONE_HOUR_A_DAY, 'Clueless'),
        (SMART_PHONE_ONE_TO_TWO_HOURS_A_DAY, 'Absolutely Baffled'),
        (SMART_PHONE_TWO_TO_FOUR_HOURS_A_DAY, 'Ill Informed'),
        (SMART_PHONE_FOUR_TO_SIX_HOURS_A_DAY, 'Slightly Capable'),
        (SMART_PHONE_SIX_TO_EIGHT_HOURS_A_DAY, 'Considerably Proficient'),
        (SMART_PHONE_EIGHT_PLUS_HOURS_A_DAY, 'PhD'),
               )

    smart_phone_usage = models.CharField(
        null=True, blank=True, max_length=500,
        choices=SMART_PHONE_USAGE,
        # default=None,
        verbose_name='Overall how would you evaluate yourself over the topics you learned in this track?'
        )