# scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from django.utils import timezone
from datetime import timedelta
from agenda.models import Agenda

def borrar_citas_antiguas():
    limite = timezone.now() - timedelta(days=30)
    citas_borradas = Agenda.objects.filter(fecha_creacion__lt=limite).delete()
    print(f"🧹 Se borraron citas antiguas: {citas_borradas}")

def start():
    scheduler = BackgroundScheduler(timezone="America/Mexico_City")
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Ejecutar cada día a las 2:00 AM
    @register_job(scheduler, "interval", days=1, id="borrar_citas_antiguas", replace_existing=True)
    def scheduled_job():
        borrar_citas_antiguas()

    register_events(scheduler)
    scheduler.start()
    print("✅ Scheduler iniciado.")
