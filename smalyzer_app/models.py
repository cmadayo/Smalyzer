from django.db import models
from django.core.validators import FileExtensionValidator


class UploadFile(models.Model):
    """ uplaod file model class  """
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(
            upload_to='uploads/%Y/%m/%d/',
            verbose_name='添付ファイル',
            validators=[FileExtensionValidator(['pdf', ])],
        )
