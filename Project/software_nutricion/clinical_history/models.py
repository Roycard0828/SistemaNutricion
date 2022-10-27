from email.policy import default
from random import choices
from django.db import models

from patients.models import Patient

# Create your models here.

class ClinicalHistory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    paciente = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    motivo_consulta = models.TextField(blank=True)
    dx_medico = models.CharField(max_length=200)
    estado_salud = models.CharField(max_length=200)

    def __str__(self) -> str:
        return "Historial clinico de: " + str(self.paciente.nombre)

class AntecendenteFamiliarPatologico(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    paterno = models.TextField(null=True)
    materno = models.TextField(null=True)

class AntecedentePersonalPatologico(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    enfermedades_infeccionas = models.CharField(max_length=200, default="")
    enfermedades_cronicas = models.CharField(max_length=200, default="")
    intoleracia_glucosa = models.BooleanField(default=False)
    enfermedades_cardiacas_cronarias = models.BooleanField(default=False)
    osteoartritis = models.BooleanField(default=False)
    enfermedades_vesiculares_hepaticas = models.CharField(max_length=200, default="no")
    enfermdades_respiratorias = models.CharField(max_length=200, default="no")
    sustancias_nocivas = models.CharField(max_length=100, default="no")
    alergias = models.CharField(max_length=100, default="no")

class HistorialPsiquiatricoQuirurgico(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    ansiedad = models.BooleanField(default=False)
    depresion = models.BooleanField(default=False)
    dx_psiquiatrico = models.TextField(null=True)
    tratamiento_psicologico = models.BooleanField(default=False)
    cirugias = models.BooleanField(default=False)

class AntecedenteGineticoObsetrico(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    embarazo = models.BooleanField(default=False)
    semamanas_embarazo = models.IntegerField(default=0,  null=True)
    EMBARAZO_CHOICE = (
        ("Aborto", "Aborto"),
        ("Carto", "Parto"),
        ("Cesarea", "Cesarea")
    )
    modo_embarazo = models.CharField(choices=EMBARAZO_CHOICE, max_length=50)
    MENSTRUACION_CHOICE = (
        ("Regulares", "Regulares"),
        ("Irregulares", "Irregulares")
    )
    periodo_menstrual = models.CharField(choices=MENSTRUACION_CHOICE, null=True, default="", max_length=50)
    dias_sangrado = models.IntegerField(default=0)
    uso_anticonceptivos = models.BooleanField(default=False)
    nombre_anticonceptivo = models.CharField(max_length=30, default="")
    dosis_anticonceptivo = models.CharField(max_length=30, default="")
    tiempo_uso = models.CharField(max_length=30, null=True, default="")
    controlados = models.BooleanField(default=False)
    climatario = models.BooleanField(default=False)
    fecha = models.CharField(max_length=50, default="")
    terapia_hormonal = models.BooleanField(default=False)
    dosis = models.CharField(max_length=20,default="")
    nombre = models.CharField(max_length=50, default="")

class Tratamiento(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    medicamentos = models.TextField(blank=True, default="")
    TOMA_CHOICES = (
        ("Laxantes", "Laxantes"),
        ("Diureticos", "Diureticos"),
        ("Antiacidos", "Antiacidos"),
        ("Analgesicos", "Analgesicos")
    )
    toma = models.CharField(null=True, choices=TOMA_CHOICES, default="", max_length=50)
    tratamiento_haa = models.CharField(max_length=30, default="")
    suplementos = models.CharField(max_length=30, default="no")

class EfectoFarmacoNutricion(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    cambio_gusto = models.BooleanField(default=False)
    cambio_apetito = models.BooleanField(default=False)
    boca_seca = models.BooleanField(default=False)
    nauseas = models.BooleanField(default=False)
    diarrea = models.BooleanField(default=False)
    constipacion = models.BooleanField(default=False)
    hiperglucemia = models.BooleanField(default=False)
    modificacion_absorcion_lipidos = models.BooleanField(default=False)

class AntecedentePersonalNoPatologico(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    NACIMIENTO_CHOICES = (
        ("Parto", "Parto"),
        ("Cesarea", "Cesarea")
    )
    via_nacimiento = models.CharField(choices=NACIMIENTO_CHOICES, null=True, max_length=20)
    peso = models.IntegerField(default=0)
    semanas_gestacion = models.IntegerField(default=0)
    contacto_momento = models.BooleanField(default=False)
    lactancia_materna = models.BooleanField(default=False)
    tiempo_lactancia = models.CharField(max_length=10, default="no")
    exclusiva = models.BooleanField(default=False)
    momento_combinacion = models.CharField(max_length=20, default="")
    formula = models.CharField(max_length=20, default="")
    meses_ablactacion = models.IntegerField(default=0)

class SintomasActuales(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    dentadura_completa = models.CharField(max_length=50)
    veces_baño = models.IntegerField(default=0)
    calidad_heces = models.IntegerField(default=1)
    alteracion_gastrointestinal = models.CharField(max_length=50, default="no")

class AntecedentesClinicoAnormales(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nombre = models.TextField(blank=True, null=True)

class AntecedentesProblemasNutricion(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    subida_peso = models.TextField(max_length=100, blank=True, default="")
    anos_cambio_peso = models.TextField(max_length=20, blank=True, default="")
    dietas_tratamientos = models.TextField(max_length=150, blank=True, default="")
    transtornos_alimenticios = models.TextField(max_length=150, blank=True, default="")
    
class ActividadFisica(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    actividad_fisica = models.CharField(max_length=50, default="")
    tipo_ejercicio = models.CharField(max_length=100, default="")
    fecha_inicio = models.DateTimeField(null=True)

class CronoHabitos(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    hora_dormir = models.TimeField(null=True)
    hora_despertar = models.TimeField(null=True)
    descripcion_despertares_noche = models.CharField(max_length=200, default='no tiene')
    condiciones = models.TextField(blank=True, max_length=255, null=True)
    ruido_dormir = models.CharField(max_length=100, null=True)
    horas_promedio = models.IntegerField()
    descanso_extra = models.CharField(max_length=50)
    sueño_reparador = models.BooleanField()
    poca_luz_natural = models.CharField(max_length=50)
    luces_prendidas_noche = models.BooleanField()
    hora_luces_apagadas = models.TimeField()
    hora_apagado_total = models.TimeField()
    comer_noche = models.CharField(max_length=50)
    apnea_sueño = models.CharField(max_length=50)

class IndicadoresDieteticos(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    comidas_dia = models.IntegerField()
    quien_prepara_alimentos = models.CharField(max_length=50)
    cambio_radical = models.TextField(blank=True)
    apetito = models.CharField(max_length=50)
    estres = models.CharField(max_length=50)
    hora_mas_hambre = models.CharField(max_length=20)
    hora_menos_hambre = models.CharField(max_length=20)
    alimentos_preferidos = models.TextField(blank=True)
    alimentos_disgustan = models.TextField(blank=True)
    alimentos_malestar_alergia = models.TextField(blank=True)
    variacion_animo = models.CharField(max_length=50)
    picoteos = models.BooleanField(default=False)
    sal_extra= models.BooleanField(default=False)
    tipo_grasa = models.CharField(max_length=20)
    tratamiento_control_peso = models.BooleanField(default=False)
    veces_tratamiento = models.IntegerField()
    tipo_dieta = models.CharField(max_length=50)
    hace_cuanto = models.CharField(max_length=50)
    razon = models.CharField(max_length=50)
    apego = models.CharField(max_length=50)
    resultado_esperado = models.CharField(max_length=50)
    medicamento_bajar_peso = models.CharField(max_length=50)
    fluctuacion_peso = models.CharField(max_length=50)
    cirugia_peso = models.CharField(max_length=50)
    consumo_agua_simple = models.CharField(max_length=10)

class Recordatorio24Horas(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    despertar = models.CharField(max_length=100)
    desayuno = models.CharField(max_length=100)
    almuerzo = models.CharField(max_length=100)
    comida = models.CharField(max_length=100)
    merienda = models.CharField(max_length=100)
    cena = models.CharField(max_length=100)
    dormir = models.CharField(max_length=100)

class FrecuenciaAlimentos(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    lacteos = models.IntegerField(default=0)
    carnes = models.IntegerField(default=0)
    verduras = models.IntegerField(default=0)
    frutas = models.IntegerField(default=0)
    cereales = models.IntegerField(default=0)
    grasa = models.IntegerField(default=0)
    azucares = models.IntegerField(default=0)
    leguminosas = models.IntegerField(default=0)
    oleaginosas = models.IntegerField(default=0)

class Motivacion(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    pregunta1 = models.TextField(blank=True)
    pregunta2 = models.TextField(blank=True)
    pregunta3 = models.TextField(blank=True)
    pregunta4 = models.TextField(blank=True)
    pregunta5 = models.TextField(blank=True)

class Metas(models.Model):
    historial_clinico = models.OneToOneField(
        ClinicalHistory,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    corto_plazo = models.TextField(blank=True)
    largo_plazo = models.TextField(blank=True)
    red_apoyo = models.CharField(max_length=100)
    apoyo_familiar = models.TextField(blank=True)
    ventajas_modificacion = models.TextField(blank=True)
    desventajas_modificacion = models.TextField(blank=True)
