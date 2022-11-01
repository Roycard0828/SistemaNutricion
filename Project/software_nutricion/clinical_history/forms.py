from tkinter import E
from django.forms import ModelForm
from .models import *
from .helpers.enumerations import *

class ClinicalHistoryForm(ModelForm):

    class Meta:
        model = ClinicalHistory
        exclude = ['finished', 'steps']
        labels = {
            "motivo_consulta": ClinicalHistoryEnumeration.MOTIVO_CONSULTA.value,
            "dx_medico": ClinicalHistoryEnumeration.DX_MEDICO.value,
            "estado_salud": ClinicalHistoryEnumeration.ESTADO_SALUD.value
        }

class AntecedenteFamiliarPatologicoForm(ModelForm):

    class Meta:
        model = AntecendenteFamiliarPatologico
        fields = ["paterno", "materno"]
        labels = {
            "paterno": AntecedenteFamiliarPatologicoEnumeration.PATERNO.value,
            "materno": AntecedenteFamiliarPatologicoEnumeration.MATERNO.value
        }

class AntecedentePersonalPatologicoForm(ModelForm):
    class Meta:
        model = AntecedentePersonalPatologico
        exclude = ['historial_clinico', 'step']
        labels = {
            "enfermedades_infeccionas": AntecedentePersonalPatologicoEnumeration.ENFERMEDADES_INFECCIOSAS.value,
            "enfermedades_cronicas": AntecedentePersonalPatologicoEnumeration.ENFERMEDADES_CRONICAS.value,
            "intoleracia_glucosa": AntecedentePersonalPatologicoEnumeration.INTOLERANCIA_GLUCOSA.value,
            "enfermedades_cardiacas_cronarias": AntecedentePersonalPatologicoEnumeration.ENFERMEDADES_CARDIACAS_CRONARIAS.value,
            "osteoartritis": AntecedentePersonalPatologicoEnumeration.OSTEOATRITIS.value,
            "enfermedades_vesiculares_hepaticas": AntecedentePersonalPatologicoEnumeration.ENFERMEDADES_VESICULARES_HEPATICAS.value,
            "enfermdades_respiratorias": AntecedentePersonalPatologicoEnumeration.ENFERMEDADES_RESPIRATORIAS.value,
            "sustancias_nocivas": AntecedentePersonalPatologicoEnumeration.SUSTANCIAS_NOCIVAS.value,
            "alergias": AntecedentePersonalPatologicoEnumeration.ALERGIAS.value
        }

class HistorialPsiquiatricoQuirurgicoForm(ModelForm):
    class Meta:
        model = HistorialPsiquiatricoQuirurgico
        exclude = ['historial_clinico', 'step']
        labels = {
            "ansiedad": HistorialPsiquiatricoQuirurgicoEnumeration.ANSIEDAD.value,
            "depresion": HistorialPsiquiatricoQuirurgicoEnumeration.DEPRESION.value,
            "dx_psiquiatrico": HistorialPsiquiatricoQuirurgicoEnumeration.DX_PSIQUIATRICO.value,
            "tratamiento_psicologico": HistorialPsiquiatricoQuirurgicoEnumeration.TRATAMIENTO_PSICOLOGICO.value,
            "cirugias": HistorialPsiquiatricoQuirurgicoEnumeration.CIRUGIAS.value
        }

class AntecedenteGineticoObsetricoForm(ModelForm):
    class Meta:
        model = AntecedenteGineticoObsetrico
        exclude = ['historial_clinico', 'step']
        labels = {
            "embarazo": AntecedenteGineticoObsetricoEnumeration.EMBARAZO.value,
            "semanas_embarazo": AntecedenteGineticoObsetricoEnumeration.SEMANAS_EMBARAZO.value,
            "modo_embarazo": AntecedenteGineticoObsetricoEnumeration.MODO_EMBARAZO.value,
            "periodo_menstrual": AntecedenteGineticoObsetricoEnumeration.PERIODO_MENSTRUAL.value,
            "dias_sangrado": AntecedenteGineticoObsetricoEnumeration.DIAS_SANGRADO.value,
            "uso_anticonceptivos": AntecedenteGineticoObsetricoEnumeration.USO_ANTICONCEPTIVO.value,
            "nombre_anticonceptivo": AntecedenteGineticoObsetricoEnumeration.NOMBRE_ANTICONCEPTIVO.value,
            "dosis_anticonceptivo": AntecedenteGineticoObsetricoEnumeration.DIAS_SANGRADO.value,
            "tiempo_uso": AntecedenteGineticoObsetricoEnumeration.TIEMPO_USO.value,
            "controlados": AntecedenteGineticoObsetricoEnumeration.CONTROLADOS.value,
            "climatario": AntecedenteGineticoObsetricoEnumeration.CLIMATARIO.value,
            "fecha": AntecedenteGineticoObsetricoEnumeration.FECHA.value,
            "terapia_hormonal": AntecedenteGineticoObsetricoEnumeration.TERAPIA_HORMONAL.value,
            "dosis": AntecedenteGineticoObsetricoEnumeration.DOSIS.value,
            "nombre": AntecedenteGineticoObsetricoEnumeration.NOMBRE.value
        }

class TratamientoForm(ModelForm):
    class Meta:
        model = Tratamiento
        exclude = ['historial_clinico', 'step']
        labels = {
            "medicamentos": TratamientoEnumeration.MEDICAMENTOS.value,
            "toma": TratamientoEnumeration.TOMA.value,
            "tratamiento_haa" : TratamientoEnumeration.TRATAMIENTO_HAA.value,
            "suplementos": TratamientoEnumeration.SUPLEMENTOS.value
        }

class EfectoFarmacoNutricionForm(ModelForm):
    class Meta:
        model = EfectoFarmacoNutricion
        exclude = ['historial_clinico', 'step']
        labels = {
            "cambio_gusto": EfectoFarmacoNutricionEnumeration.CAMBIO_GUSTO.value,
            "cambio_apetito": EfectoFarmacoNutricionEnumeration.CAMBIO_APETITO.value,
            "boca_seca": EfectoFarmacoNutricionEnumeration.BOCA_SECA.value,
            "nauseas": EfectoFarmacoNutricionEnumeration.NAUSEAS.value,
            "diarrea": EfectoFarmacoNutricionEnumeration.DIARREA.value,
            "constipacion": EfectoFarmacoNutricionEnumeration.CONSTIPACION.value,
            "hiperglucemia": EfectoFarmacoNutricionEnumeration.HIPERGLUCEMIA.value,
            "modificacion_absorcion_lipidos": EfectoFarmacoNutricionEnumeration.MODIFICACION_ABSORCION_LIPIDOS.value
        }

class AntecedentePersonalNoPatologicoForm(ModelForm):
    class Meta:
        model = AntecedentePersonalNoPatologico
        exclude = ['historial_clinico', 'step']
        labels = {
            "via_nacimiento" : AntecedentePersonalNoPatologicoEnumeration.VIA_NACIMIENTO.value,
            "peso" : AntecedentePersonalNoPatologicoEnumeration.PESO.value,
            "semanas_gestacion" : AntecedentePersonalNoPatologicoEnumeration.SEMANAS_GESTACION.value,
            "contacto_momento" : AntecedentePersonalNoPatologicoEnumeration.CONTACTO_MOMENTO.value,
            "lactancia_materna" : AntecedentePersonalNoPatologicoEnumeration.LACTANCIA_MATERNA.value,
            "tiempo_lactancia" : AntecedentePersonalNoPatologicoEnumeration.TIEMPO_LACTANCIA.value,
            "exclusiva": AntecedentePersonalNoPatologicoEnumeration.EXCLUSIVA.value,
            "momento_combinacion" : AntecedentePersonalNoPatologicoEnumeration.MOMENTO_COMBINACION.value,
            "formula" : AntecedentePersonalNoPatologicoEnumeration.FORMULA.value,
            "meses_ablactacion" : AntecedentePersonalNoPatologicoEnumeration.MESES_ABLACTACION.value
        }

class SintomasActualesForm(ModelForm):
    class Meta:
        model = SintomasActuales
        exclude = ['historial_clinico', 'step']
        labels = {
            "dentadura_completa": SintomasActualesEnumeration.DENTADURA_COMPLETA.value,
            "veces_baño": SintomasActualesEnumeration.VECES_BAÑO.value,
            "calidad_heces": SintomasActualesEnumeration.CALIDAD_HECES.value,
            "alteracion_gastrointestinal": SintomasActualesEnumeration.ALTERACION_GASTROINTESTINAL.value            
        }

class AntecedentesClinicoAnormalesForm(ModelForm):
    class Meta:
        model = AntecedentesClinicoAnormales
        exclude = ['historial_clinico', 'step']
        labels = {
            "nombre": AntecedentesClinicoAnormalesEnumeration.NOMBRE.value
        }

class AntecedentesProblemasNutricionForm(ModelForm):
    class Meta:
        model = AntecedentesProblemasNutricion
        exclude = [ 'historial_clinico', 'step']
        labels = {
            "subida_peso": AntecedentesProblemasNutricionEnumeration.SUBIDA_PESO.value,
            "anos_cambio_peso": AntecedentesProblemasNutricionEnumeration.ANOS_CAMBIO_PESO.value,
            "dietas_tratamientos": AntecedentesProblemasNutricionEnumeration.DIETAS_TRATAMIENTOS.value,
            "transtornos_alimenticios": AntecedentesProblemasNutricionEnumeration.TRANSTARNOS_ALIMENTICIOS.value
        }

class ActividadFisicaForm(ModelForm):
    class Meta:
        model = ActividadFisica
        exclude = [ 'historial_clinico', 'step']
        labels = {
            "actividad_fisica": ActividadFisicaEnumeration.ACTIVIDAD_FISICA.value,
            "tipo_ejercicio": ActividadFisicaEnumeration.TIPO_EJERCICIO.value,
            "fecha_inicio": ActividadFisicaEnumeration.FECHA_INICIO.value
        }

class CronoHabitosForm(ModelForm):
    class Meta:
        model = CronoHabitos
        exclude = ['historial_clinico', 'step']
        labels = {
            "hora_dormir": CronoHabitosEnumeration.HORA_DORMIR.value,
            "hora_despertar": CronoHabitosEnumeration.HORA_DESPERTAR.value,
            "descripcion_despertares_noche": CronoHabitosEnumeration.DESCRIPCION_DESPERTARES_NOCHE.value,
            "condiciones": CronoHabitosEnumeration.CONDICIONES.value,
            "ruido_dormir": CronoHabitosEnumeration.RUIDO_DORMIR.value,
            "horas_promedio": CronoHabitosEnumeration.HORAS_PROMEDIO.value,
            "descanso_extra": CronoHabitosEnumeration.DESCANSO_EXTRA.value,
            "sueño_reparador": CronoHabitosEnumeration.SUEÑO_REPARADOR.value,
            "poca_luz_natural": CronoHabitosEnumeration.POCA_LUZ_NATURAL.value,
            "luces_prendidas_noche": CronoHabitosEnumeration.LUCES_PRENDIDAS_NOCHE.value,
            "hora_luces_apagadas": CronoHabitosEnumeration.HORA_LUCES_APAGADAS.value,
            "hora_apagado_total": CronoHabitosEnumeration.HORA_APAGADO_TOTAL.value,
            "comer_noche": CronoHabitosEnumeration.COMER_NOCHE.value,
            "apnea_sueño": CronoHabitosEnumeration.APNEA_SUEÑO.value
        }

class IndicadoresDieteticosForm(ModelForm):

    class Meta:
        model = IndicadoresDieteticos
        exclude = ['historial_clinico', 'step']
        labels = {
            "comidas_dia": IndicadoresDieteticosEnumeration.COMIDAS_DIA.value,
            "quien_prepara_alimentos": IndicadoresDieteticosEnumeration.QUIEN_PREPARA_ALIMENTOS.value,
            "cambio_radical": IndicadoresDieteticosEnumeration.CAMBIO_RADICAL.value,
            "apetito": IndicadoresDieteticosEnumeration.APETITO.value,
            "estres": IndicadoresDieteticosEnumeration.ESTRES.value,
            "hora_mas_hambre": IndicadoresDieteticosEnumeration.HORA_MAS_HAMBRE.value,
            "hora_menos_hambre": IndicadoresDieteticosEnumeration.HORA_MENOS_HAMBRE.value,
            "alimentos_preferidos": IndicadoresDieteticosEnumeration.ALIMENTOS_PREFERIDOS.value,
            "alimentos_disgustan":IndicadoresDieteticosEnumeration.ALIMENTOS_DISGUSTAN.value,
            "alimentos_malestar_alergia": IndicadoresDieteticosEnumeration.ALIMENTOS_MALESTAR_ALERGIA.value,
            "variacion_animo": IndicadoresDieteticosEnumeration.VARIACION_ANIMO.value,
            "picoteos": IndicadoresDieteticosEnumeration.PICOTEOS.value,
            "sal_extra": IndicadoresDieteticosEnumeration.SAL_EXTRA.value,
            "tipo_grasa": IndicadoresDieteticosEnumeration.TIPO_GRASA.value,
            "tratamiento_control_peso": IndicadoresDieteticosEnumeration.TRATAMIENTO_CONTROL_PESO.value,
            "veces_tratamiento":IndicadoresDieteticosEnumeration.VECES_TRATAMIENTO.value,
            "tipo_dieta": IndicadoresDieteticosEnumeration.TIPO_DIETA.value,
            "hace_cuanto": IndicadoresDieteticosEnumeration.HACE_CUANTO.value,
            "razon": IndicadoresDieteticosEnumeration.RAZON.value,
            "apego": IndicadoresDieteticosEnumeration.APEGO.value,
            "resultado_esperado": IndicadoresDieteticosEnumeration.RESULTADO_ESPERADO.value,
            "medicamento_bajar_peso": IndicadoresDieteticosEnumeration.MEDICAMENTO_BAJAR_PESO.value,
            "fluctuacion_peso": IndicadoresDieteticosEnumeration.FLUCTUACION_PESO.value,
            "cirugia_peso": IndicadoresDieteticosEnumeration.CIRUGIA_PESO.value,
            "consumo_agua_simple":IndicadoresDieteticosEnumeration.CONSUMO_AGUA_SIMPLE.value
        }
    
class Recordatorio24HorasForm(ModelForm):
    class Meta:
        model = Recordatorio24Horas 
        exclude = ['historial_clinico', 'step']
        labels = {
            "despertar": Recordatorio24HorasEnumeration.DESPERTAR.value,
            "desayuno": Recordatorio24HorasEnumeration.DESAYUNO.value,
            "almuerzo": Recordatorio24HorasEnumeration.ALMUERZO.value,
            "comida": Recordatorio24HorasEnumeration.COMIDA.value,
            "merienda": Recordatorio24HorasEnumeration.MERIENDA.value,
            "cena": Recordatorio24HorasEnumeration.CENA.value,
            "dormir": Recordatorio24HorasEnumeration.DORMIR.value,
        }

class FrecuenciaAlimentosForm(ModelForm):
    class Meta:
        model = FrecuenciaAlimentos
        exclude = ['historial_clinico', 'step']
        labels = {
            "lacteos": FrecuenciaAlimentosEnumeration.LACTEOS.value,
            "carnes": FrecuenciaAlimentosEnumeration.CARNES.value,
            "verduras": FrecuenciaAlimentosEnumeration.VERDURAS.value,
            "frutas": FrecuenciaAlimentosEnumeration.FRUTAS.value,
            "cereales": FrecuenciaAlimentosEnumeration.CEREALES.value,
            "grasa": FrecuenciaAlimentosEnumeration.GRASA.value,
            "azucares": FrecuenciaAlimentosEnumeration.AZUCARES.value,
            "leguminosas": FrecuenciaAlimentosEnumeration.LEGUMINOSAS.value,
            "oleaginosas": FrecuenciaAlimentosEnumeration.OLEAGINOSAS.value
        }

class MotivacionForm(ModelForm):
    class Meta:
        model = Motivacion
        exclude = ['historial_clinico', 'step']
        labels = {
            "pregunta1": MotivacionEnumeration.PREGUNTA1.value,
            "pregunta2":  MotivacionEnumeration.PREGUNTA2.value,
            "pregunta3":  MotivacionEnumeration.PREGUNTA3.value,
            "pregunta4":  MotivacionEnumeration.PREGUNTA4.value,
            "pregunta5":  MotivacionEnumeration.PREGUNTA5.value
        }

class MetasForm(ModelForm):
    class Meta:
        model = Metas
        exclude = ['historial_clinico', 'step']
        labels = {
            "corto_plazo": MetasEnumeration.CORTO_PLAZO.value,
            "largo_plazo": MetasEnumeration.LARGO_PLAZO.value,
            "red_apoyo": MetasEnumeration.RED_APOYO.value,
            "apoyo_familiar": MetasEnumeration.APOYO_FAMILIAR.value,
            "ventajas_modificacion": MetasEnumeration.VENTAJAS_MODIFICACION.value,
            "desventajas_modificacion": MetasEnumeration.DESVENTAJAS_MODIFICACION.value
        }