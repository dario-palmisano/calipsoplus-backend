from django.db import models
from simple_history.models import HistoricalRecords

from apprest.models.user import CalipsoUser


class CalipsoExperiment(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    proposal_id = models.CharField(max_length=50, blank=True)
    beam_line = models.CharField(max_length=200, blank=True)

    calipso_users = models.ManyToManyField(CalipsoUser, through='CalipsoUserExperiment',
                                           through_fields=('calipso_experiment', 'calipso_user'))

    uid = models.CharField(max_length=255, blank=True)
    gid = models.CharField(max_length=255, blank=True)

    history = HistoricalRecords()

    def create(self, subject, body, proposal_id, beam_line, uid, gid):
        self.subject = subject
        self.body = body
        self.proposal_id = proposal_id
        self.beam_line = beam_line
        self.uid = uid
        self.gid = gid

    class Meta:
        db_table = 'calipso_experiments'

    def __str__(self):
        return self.proposal_id


class CalipsoUserExperiment(models.Model):
    calipso_user = models.ForeignKey(CalipsoUser, on_delete=models.CASCADE)
    calipso_experiment = models.ForeignKey(CalipsoExperiment, on_delete=models.CASCADE)
    favorite = models.BooleanField(default=False, )

    history = HistoricalRecords()

    class Meta:
        unique_together = ('calipso_user', 'calipso_experiment')
        db_table = 'calipso_user_experiment'

    def __str__(self):
        return str(self.calipso_user) + "-" + str(self.calipso_experiment)