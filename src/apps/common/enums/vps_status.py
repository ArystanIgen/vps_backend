from django.db.models import TextChoices


class VPSStatuses(TextChoices):
    STARTED = 'STARTED', 'Запущен'
    BLOCKED = 'BLOCKED', 'Заблокирован'
    STOPPED = 'STOPPED', 'Остановлен'
