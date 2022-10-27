from tkinter import E
from django.forms import ModelForm
from .models import *
from .helpers.enumerations import *

class ClinicalHistoryForm(ModelForm):

    class Meta:
        model = ClinicalHistory
        fields = '__all__'
        labels = {
            "motivo_consulta": ClinicalHistoryEnumeration.MOTIVO_CONSULTA,
            "dx_medico": ClinicalHistoryEnumeration.DX_MEDICO,
            "estado_salud": ClinicalHistoryEnumeration.ESTADO_SALUD
        }

class AntecedenteFamiliarPatologicoForm(ModelForm):

    class Meta:
        model = AntecendenteFamiliarPatologico
        fields = ["paterno", "materno"]
        labels = {
            "paterno": AntecedenteFamiliarPatologicoEnumeration.PATERNO,
            "materno": AntecedenteFamiliarPatologicoEnumeration.MATERNO
        }

class AntecedentePersonalPatologicoForm(ModelForm):
    class Meta:
        model = AntecedentePersonalPatologico
        exclude = ['historial_clinico']
        labels = {
            "enfermedades_infeccionas": AntecedentePersonalPatologicoEnumeration.ENFERMEDADES_INFECCIOSAS,
            "enfermedades_cronicas": AntecedentePersonalPatologicoEnumeration.ENFERMEDADES_CRONICAS,
            "intoleracia_glucosa": AntecedentePersonalPatologicoEnumeration.INTOLERANCIA_GLUCOSA,
            "enfermedades_cardiacas_cronarias": AntecedentePersonalPatologicoEnumeration.ENFERMEDADES_CARDIACAS_CRONARIAS,
            "osteoartritis": AntecedentePersonalPatologicoEnumeration.OSTEOATRITIS,
            "enfermedades_vesiculares_hepaticas": AntecedentePersonalPatologicoEnumeration.ENFERMEDADES_VESICULARES_HEPATICAS,
            "enfermdades_respiratorias": AntecedentePersonalPatologicoEnumeration.ENFERMEDADES_RESPIRATORIAS,
            "sustancias_nocivas": AntecedentePersonalPatologicoEnumeration.SUSTANCIAS_NOCIVAS,
            "alergias": AntecedentePersonalPatologicoEnumeration.ALERGIAS
        }

class HistorialPsiquiatricoQuirurgicoForm(ModelForm):
    class Meta:
        model = HistorialPsiquiatricoQuirurgico
        exclude = ['historial_clinico']
        labels = {
            "ansiedad": HistorialPsiquiatricoQuirurgicoEnumeration.ANSIEDAD,
            "depresion": HistorialPsiquiatricoQuirurgicoEnumeration.DEPRESION,
            "dx_psiquiatrico": HistorialPsiquiatricoQuirurgicoEnumeration.DX_PSIQUIATRICO,
            "tratamiento_psicologico": HistorialPsiquiatricoQuirurgicoEnumeration.TRATAMIENTO_PSICOLOGICO,
            "cirugias": HistorialPsiquiatricoQuirurgicoEnumeration.CIRUGIAS
        }

class AntecendeteGineticoObsetricoForm(ModelForm):
    class Meta:
        model = AntecedenteGineticoObsetrico
        exclude = ['historial_clinico']
        labels = {
            "embarazo": AntecedenteGineticoObsetricoEnumeration.EMBARAZO,
            "semanas_embarazo": AntecedenteGineticoObsetricoEnumeration.SEMANAS_EMBARAZO,
            "modo_embarazo": AntecedenteGineticoObsetricoEnumeration.MODO_EMBARAZO,
            "periodo_menstrual": AntecedenteGineticoObsetricoEnumeration.PERIODO_MENSTRUAL,
            "dias_sangrado": AntecedenteGineticoObsetricoEnumeration.DIAS_SANGRADO,
            "uso_anticonceptivos": AntecedenteGineticoObsetricoEnumeration.USO_ANTICONCEPTIVO,
            "nombre_anticonceptivo": AntecedenteGineticoObsetricoEnumeration.NOMBRE_ANTICONCEPTIVO,
            "dosis_anticonceptivo": AntecedenteGineticoObsetricoEnumeration.DIAS_SANGRADO,
            "tiempo_uso": AntecedenteGineticoObsetricoEnumeration.TIEMPO_USO,
            "controlados": AntecedenteGineticoObsetricoEnumeration.CONTROLADOS,
            "climatario": AntecedenteGineticoObsetricoEnumeration.CLIMATARIO,
            "fecha": AntecedenteGineticoObsetricoEnumeration.FECHA,
            "terapia_hormonal": AntecedenteGineticoObsetricoEnumeration.TERAPIA_HORMONAL,
            "dosis": AntecedenteGineticoObsetricoEnumeration.DOSIS,
            "nombre": AntecedenteGineticoObsetricoEnumeration.NOMBRE
        }

class TratamientoForm(ModelForm):
    class Meta:
        model = Tratamiento
        exclude = ['historial_clinico']
        labels = {
            "medicamentos": TratamientoEnumeration.MEDICAMENTOS,
            "toma": TratamientoEnumeration.TOMA,
            "tratamiento_haa" : TratamientoEnumeration.TRATAMIENTO_HAA,
            "suplementos": TratamientoEnumeration.SUPLEMENTOS
        }

class EfectoFarmacoNutricionForm(ModelForm):
    class Meta:
        model = EfectoFarmacoNutricion
        exclude = ['historial_clinico']
        labels = {
            "cambio_gusto": EfectoFarmacoNutricionEnumeration.CAMBIO_GUSTO,
            "cambio_apetito": EfectoFarmacoNutricionEnumeration.CAMBIO_APETITO,
            "boca_seca": EfectoFarmacoNutricionEnumeration.BOCA_SECA,
            "nauseas": EfectoFarmacoNutricionEnumeration.NAUSEAS,
            "diarrea": EfectoFarmacoNutricionEnumeration.DIARREA,
            "constipacion": EfectoFarmacoNutricionEnumeration.CONSTIPACION,
            "hiperglucemia": EfectoFarmacoNutricionEnumeration.HIPERGLUCEMIA,
            "modificacion_absorcion_lipidos": EfectoFarmacoNutricionEnumeration.MODIFICACION_ABSORCION_LIPIDOS 
        }

class AntecedentePersonalNoPatologicoForm(ModelForm):
    class Meta:
        model = AntecedentePersonalNoPatologico
        exclude = ['historial_clinico']
        labels = {
            "via_nacimiento" : AntecedentePersonalNoPatologicoEnumeration.VIA_NACIMIENTO,
            "peso" : AntecedentePersonalNoPatologicoEnumeration.PESO,
            "semanas_gestacion" : AntecedentePersonalNoPatologicoEnumeration.SEMANAS_GESTACION,
            "contacto_momento" : AntecedentePersonalNoPatologicoEnumeration.CONTACTO_MOMENTO,
            "lactancia_materna" : AntecedentePersonalNoPatologicoEnumeration.LACTANCIA_MATERNA,
            "tiempo_lactancia" : AntecedentePersonalNoPatologicoEnumeration.TIEMPO_LACTANCIA,
            "exclusiva": AntecedentePersonalNoPatologicoEnumeration.EXCLUSIVA,
            "momento_combinacion" : AntecedentePersonalNoPatologicoEnumeration.MOMENTO_COMBINACION,
            "formula" : AntecedentePersonalNoPatologicoEnumeration.FORMULA,
            "meses_ablactacion" : AntecedentePersonalNoPatologicoEnumeration.MESES_ABLACTACION
        }

class SintomasActualesForm(ModelForm):
    class Meta:
        model = SintomasActuales
        exclude = ['historial_clinico']
        labels = {
            "dentadura_completa": SintomasActualesEnumeration.DENTADURA_COMPLETA,
            "veces_baño": SintomasActualesEnumeration.VECES_BAÑO,
            "calidad_heces": SintomasActualesEnumeration.CALIDAD_HECES,
            "alteracion_gastrointestinal": SintomasActualesEnumeration.ALTERACION_GASTROINTESTINAL            
        }

class AntecedentesClinicoAnormalesForm(ModelForm):
    class Meta:
        model = AntecedentesClinicoAnormales
        exclude = ['historial_clinico']
        labels = {
            "nombre": AntecedentesClinicoAnormalesEnumeration.NOMBRE
        }

class AntecedentesProblemasNutricionForm(ModelForm):
    class Meta:
        model = AntecedentesProblemasNutricion
        exclude = [ 'historial_clinico']
        labels = {
            "subida_peso": AntecedentesProblemasNutricionEnumeration.SUBIDA_PESO,
            "anos_cambio_peso": AntecedentesProblemasNutricionEnumeration.ANOS_CAMBIO_PESO,
            "dietas_tratamientos": AntecedentesProblemasNutricionEnumeration.DIETAS_TRATAMIENTOS,
            "transtornos_alimenticios": AntecedentesProblemasNutricionEnumeration.TRANSTARNOS_ALIMENTICIOS
        }

class ActividadFisicaForm(ModelForm):
    class Meta:
        model = ActividadFisica
        exclude = [ 'historial_clinico']
        labels = {
            "actividad_fisica": ActividadFisicaEnumeration.ACTIVIDAD_FISICA,
            "tipo_ejercicio": ActividadFisicaEnumeration.TIPO_EJERCICIO,
            "fecha_inicio": ActividadFisicaEnumeration.FECHA_INICIO
        }

class CronoHabitosForm(ModelForm):
    class Meta:
        model = CronoHabitos
        exclude = ['historial_clinico']
        labels = {
            "hora_dormir": CronoHabitosEnumeration.HORA_DORMIR,
            "hora_despertar": CronoHabitosEnumeration.HORA_DESPERTAR,
            "descripcion_despertares_noche": CronoHabitosEnumeration.DESCRIPCION_DESPERTARES_NOCHE,
            "condiciones": CronoHabitosEnumeration.CONDICIONES,
            "ruido_dormir": CronoHabitosEnumeration.RUIDO_DORMIR,
            "horas_promedio": CronoHabitosEnumeration.HORAS_PROMEDIO,
            "descanso_extra": CronoHabitosEnumeration.DESCANSO_EXTRA,
            "sueño_reparador": CronoHabitosEnumeration.SUEÑO_REPARADOR,
            "poca_luz_natural": CronoHabitosEnumeration.POCA_LUZ_NATURAL,
            "luces_prendidas_noche": CronoHabitosEnumeration.LUCES_PRENDIDAS_NOCHE,
            "hora_luces_apagadas": CronoHabitosEnumeration.HORA_LUCES_APAGADAS,
            "hora_apagado_total": CronoHabitosEnumeration.HORA_APAGADO_TOTAL,
            "comer_noche": CronoHabitosEnumeration.COMER_NOCHE,
            "apnea_sueño": CronoHabitosEnumeration.APNEA_SUEÑO
        }

class IndicadoresDieteticosForm(ModelForm):

    class Meta:
        model = IndicadoresDieteticos
        exclude = ['historial_clinico']
        labels = {
            "comidas_dia": IndicadoresDieteticosEnumeration.COMIDAS_DIA,
            "quien_prepara_alimentos": IndicadoresDieteticosEnumeration.QUIEN_PREPARA_ALIMENTOS,
            "cambio_radical": IndicadoresDieteticosEnumeration.CAMBIO_RADICAL,
            "apetito": IndicadoresDieteticosEnumeration.APETITO,
            "estres": IndicadoresDieteticosEnumeration.ESTRES,
            "hora_mas_hambre": IndicadoresDieteticosEnumeration.HORA_MAS_HAMBRE,
            "hora_menos_hambre": IndicadoresDieteticosEnumeration.HORA_MENOS_HAMBRE,
            "alimentos_preferidos": IndicadoresDieteticosEnumeration.ALIMENTOS_PREFERIDOS,
            "alimentos_disgustan":IndicadoresDieteticosEnumeration.ALIMENTOS_DISGUSTAN,
            "alimentos_malestar_alergia": IndicadoresDieteticosEnumeration.ALIMENTOS_MALESTAR_ALERGIA,
            "variacion_animo": IndicadoresDieteticosEnumeration.VARIACION_ANIMO,
            "picoteos": IndicadoresDieteticosEnumeration.PICOTEOS,
            "sal_extra": IndicadoresDieteticosEnumeration.SAL_EXTRA,
            "tipo_grasa": IndicadoresDieteticosEnumeration.TIPO_GRASA,
            "tratamiento_control_peso": IndicadoresDieteticosEnumeration.TRATAMIENTO_CONTROL_PESO,
            "veces_tratamiento":IndicadoresDieteticosEnumeration.VECES_TRATAMIENTO,
            "tipo_dieta": IndicadoresDieteticosEnumeration.TIPO_DIETA,
            "hace_cuanto": IndicadoresDieteticosEnumeration.HACE_CUANTO,
            "razon": IndicadoresDieteticosEnumeration.RAZON,
            "apego": IndicadoresDieteticosEnumeration.APEGO,
            "resultado_esperado": IndicadoresDieteticosEnumeration.RESULTADO_ESPERADO,
            "medicamento_bajar_peso": IndicadoresDieteticosEnumeration.MEDICAMENTO_BAJAR_PESO,
            "fluctuacion_peso": IndicadoresDieteticosEnumeration.FLUCTUACION_PESO,
            "cirugia_peso": IndicadoresDieteticosEnumeration.CIRUGIA_PESO,
            "consumo_agua_simple":IndicadoresDieteticosEnumeration.CONSUMO_AGUA_SIMPLE,
        }
    
class Recordatorio24HorasEnumeration(ModelForm):
    class Meta:
        model = Recordatorio24Horas 
        exclude = ['historial_clinico']
        labels = {
            "despertar": Recordatorio24HorasEnumeration.DESPERTAR,
            "desayuno": Recordatorio24HorasEnumeration.DESAYUNO,
            "almuerzo": Recordatorio24HorasEnumeration.ALMUERZO,
            "comida": Recordatorio24HorasEnumeration.COMIDA,
            "merienda": Recordatorio24HorasEnumeration.MERIENDA,
            "cena": Recordatorio24HorasEnumeration.CENA,
            "dormir": Recordatorio24HorasEnumeration.DORMIR,
        }

class FrecuenciaAlimentos(ModelForm):
    class Meta:
        model = FrecuenciaAlimentos
        exclude = ['historial_clinico']
        labels = {
            "lacteos": FrecuenciaAlimentosEnumeration.LACTEOS,
            "carnes": FrecuenciaAlimentosEnumeration.CARNES,
            "verduras": FrecuenciaAlimentosEnumeration.VERDURAS,
            "frutas": FrecuenciaAlimentosEnumeration.FRUTAS,
            "cereales": FrecuenciaAlimentosEnumeration.CEREALES,
            "grasa": FrecuenciaAlimentosEnumeration.GRASA,
            "azucares": FrecuenciaAlimentosEnumeration.AZUCARES,
            "leguminosas": FrecuenciaAlimentosEnumeration.LEGUMINOSAS,
            "oleaginosas": FrecuenciaAlimentosEnumeration.OLEAGINOSAS
        }

class Motivacion(ModelForm):
    class Meta:
        model = Motivacion
        exclude = ['historial_clinico']
        labels = {
            "pregunta1": MotivacionEnumeration.PREGUNTA1,
            "pregunta2":  MotivacionEnumeration.PREGUNTA2,
            "pregunta3":  MotivacionEnumeration.PREGUNTA3,
            "pregunta4":  MotivacionEnumeration.PREGUNTA4,
            "pregunta5":  MotivacionEnumeration.PREGUNTA5
        }

class Metas(ModelForm):
    class Meta:
        model = Metas
        exclude = ['historial_clinico']
        labels = {
            "corto_plazo": MetasEnumeration.CORTO_PLAZO,
            "largo_plazo": MetasEnumeration.LARGO_PLAZO,
            "red_apoyo": MetasEnumeration.RED_APOYO,
            "apoyo_familiar": MetasEnumeration.APOYO_FAMILIAR,
            "ventajas_modificacion": MetasEnumeration.VENTAJAS_MODIFICACION,
            "desventajas_modificacion": MetasEnumeration.DESVENTAJAS_MODIFICACION
        }