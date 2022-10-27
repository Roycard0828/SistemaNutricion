from enum import Enum 

class ClinicalHistoryEnumeration(Enum):
    MOTIVO_CONSULTA = "Motivo de consulta",
    DX_MEDICO = "DX Medico",
    ESTADO_SALUD = "Estado de Salud"

class AntecedenteFamiliarPatologicoEnumeration(Enum):
    PATERNO =  "Antecedente paterno",
    MATERNO =  "Antecedente materno",

class AntecedentePersonalPatologicoEnumeration(Enum):
    ENFERMEDADES_INFECCIOSAS =  "Enfermedades infecciosas"
    ENFERMEDADES_CRONICAS =  "Enfermedades cronicas"
    INTOLERANCIA_GLUCOSA =  "Intolerancia a la glucosa"
    ENFERMEDADES_CARDIACAS_CRONARIAS = "Enfermedades cardiacas o cronarias"
    OSTEOATRITIS = "Osteoartritis"
    ENFERMEDADES_VESICULARES_HEPATICAS = "Enfermedades vesiculares y hepaticas. ¿Cuales?"
    ENFERMEDADES_RESPIRATORIAS = "Enfermedades respiratorias. ¿Cuales?"
    SUSTANCIAS_NOCIVAS = "Tabaquismo, Consumo de alcohol o alguna otra droga, ¿Cual?"
    ALERGIAS = "¿Tiene alergias? ¿A que?"

class HistorialPsiquiatricoQuirurgicoEnumeration(Enum):
    ANSIEDAD = "Ansiedad: "
    DEPRESION = "Depresion: "
    DX_PSIQUIATRICO = "Dx. Psiquiatrico: "
    TRATAMIENTO_PSICOLOGICO = "¿Tiene tratamiento psicologico?"
    CIRUGIAS = "Cirugias, ¿Cuales?"

class AntecedenteGineticoObsetricoEnumeration(Enum):
    EMBARAZO = "Embarazo: "
    SEMANAS_EMBARAZO = "Numero de semanas de embarazo"
    MODO_EMBARAZO = "Aborto, Parto o Cesarea"
    PERIODO_MENSTRUAL = "Periodos mestruales"
    DIAS_SANGRADO = "Dias que dura el sangrado"
    USO_ANTICONCEPTIVO = "Uso de anticonceptivos"
    NOMBRE_ANTICONCEPTIVO = "¿Cuales?"
    DOSIS_ANTICONCEPTIVO = "Dosis "
    TIEMPO_USO = "Tiempo usandolos"
    CONTROLADOS = "¿Son controlados?"
    CLIMATARIO = "Climatario"
    FECHA = "Fecha"
    TERAPIA_HORMONAL = "Terapia de reemplazo hormonal"
    DOSIS = "Dosis"
    NOMBRE = "Nombre"

class TratamientoEnumeration(Enum):
    MEDICAMENTOS = "Medicamentos",
    TOMA = "¿Toma alguna de las siguiente opciones? Laxantes, Diureticos, Antiacidos, Analgesicos",
    TRATAMIENTO_HAA = "Tratamientos homeopaticos, alopatas o alternativa",
    SUPLEMENTOS = "¿Toma algun suplemento? ¿Cual?"

class EfectoFarmacoNutricionEnumeration(Enum):
    CAMBIO_GUSTO = "Cambio de gusto",
    CAMBIO_APETITO = "Cambio de apetito",
    BOCA_SECA = "Boca de seca",
    NAUSEAS = "Nauseas",
    DIARREA = "Diarrea",
    CONSTIPACION = "Constipacion",
    HIPERGLUCEMIA = "Hiperglucemia",
    MODIFICACION_ABSORCION_LIPIDOS = "Modificación de absorcion de lipidos"

class AntecedentePersonalNoPatologicoEnumeration(Enum):
    VIA_NACIMIENTO = "Via de nacimiento",
    PESO = "Peso al nacer",
    SEMANAS_GESTACION = "Semanas de gestacion",
    CONTACTO_MOMENTO = "Primer contacto en el momento",
    LACTANCIA_MATERNA = "Hubo lactancia materna",
    TIEMPO_LACTANCIA = "¿Por cuanto tiempo?",
    EXCLUSIVA = "¿Fue exclusiva?",
    MOMENTO_COMBINACION = "¿En que momento de combino con la formula?",
    FORMULA = "¿Que tipo de formula se uso?",
    MESES_ABLACTACION = "¿A los cuantos meses fue la ablactacion?"

class SintomasActualesEnumeration(Enum):
    DENTADURA_COMPLETA = "Dentadura completa",
    VECES_BAÑO = "¿Cuantas veces va al baño al dia?",
    CALIDAD_HECES = "Calidad de heces",
    ALTERACION_GASTROINTESTINAL = "Alteracion Gastrointestinal"

class AntecedentesClinicoAnormalesEnumeration(Enum):
    NOMBRE = "Laboratorios clinicos anormales "

class AntecedentesProblemasNutricionEnumeration(Enum):
    SUBIDA_PESO = "¿En que momento de su vida usted subio de peso?"
    ANOS_CAMBIO_PESO = "¿Hace cuantos años, tuvo su cambio de peso?"
    DIETAS_TRATAMIENTOS ="Dietas o tratamientos nutricios que ha realizado anteriormente"
    TRANSTARNOS_ALIMENTICIOS = "Trastornos alimenticios"

class ActividadFisicaEnumeration(Enum):
    ACTIVIDAD_FISICA = "Actividad Fisica"
    TIPO_EJERCICIO = "Ejercicio: "
    FECHA_INICIO = "¿Cuando inicio?"

class CronoHabitosEnumeration(Enum):
    HORA_DORMIR ="¿A que hora te duermes?"
    HORA_DESPERTAR ="¿A que hora despiertas?"
    DESCRIPCION_DESPERTARES_NOCHE = "¿Tiene despertares durante la noche?"
    CONDICIONES ="¿Cuáles son las condiciones en que duermes? Describa si duerme con o sin luz, si existe luz, esta es suficiente para ver las cosas, solo se observan siluetas, focos leds de aparatos, es capaz de ver su mano o duerme en absoluta o total obscuridad"
    RUIDO_DORMIR ="¿Existe algún ruido constante o frecuente mientras duerme?"
    HORAS_PROMEDIO ="Horas totales de sueño que en promedio duermes al día"
    DESCANSO_EXTRA ="Los días de descanso duermes más o te desvelas"
    SUEÑO_REPARADOR ="¿Consideras que tiene un sueño reparador? "
    POCA_LUZ_NATURAL ="¿Durante el día acostumbra a mantener la mayor cantidad de luz posible? o durante el día está el lugar de poca luz natural o artificial"
    LUCES_PRENDIDAS_NOCHE ="¿Mantiene las luces de la casa y de las habitaciones prendidas durante el anochecer? "
    HORA_LUCES_APAGADAS ="¿A qué hora apaga las luces de las habitaciones?"
    HORA_APAGADO_TOTAL ="¿A qué hora apagas todo cuando ya es hora de dormir? Tienes un foco, el celular, un led, música, tele, etc."
    COMER_NOCHE ="¿En alguna ocasión has levantado a comer de noche o madrugada? ¿O has cenado muy noche?"
    APNEA_SUEÑO ="¿Padecemos apnea del sueños?"

class IndicadoresDieteticosEnumeration(Enum):
    COMIDAS_DIA = "¿Cuántas comidas hace al día? "
    QUIEN_PREPARA_ALIMENTOS = "¿Quien prepara sus alimentos"
    CAMBIO_RADICAL = "¿Recientemente (de 6 meses a l fecha) ha experimentado algún cambio radical en su vida el cual haya influenciado alteración en su estado anímico o su estilo de vida?. ¿Poque? ¿Como?"
    APETITO = "Apetito"
    ESTRES = "Estres"
    HORA_MAS_HAMBRE = "¿A qué hora del día tienes más hambre? " 
    HORA_MENOS_HAMBRE = "¿A qué hora tienes menos hambre?"
    ALIMENTOS_PREFERIDOS ="Alimentos preferidos"
    ALIMENTOS_DISGUSTAN = "Alimentos que no le gustan"
    ALIMENTOS_MALESTAR_ALERGIA = "Alimentos que causan malestar o tenemos alergia"
    VARIACION_ANIMO = "Su estado de ánimo influye en sus consumos de alimentos. ¿Como?"
    PICOTEOS = "Usted tiene picoteos"
    SAL_EXTRA = "¿Agregas sal a la comida ya preparada?"
    TIPO_GRASA = "¿Que grasa utilizan en casa para preparar las comidas?"
    TRATAMIENTO_CONTROL_PESO ="¿Ha llevado un tratamiento para control de peso?",
    VECES_TRATAMIENTO ="¿Cuántas veces?"
    TIPO_DIETA = "¿Qué tipo de dieta? "
    HACE_CUANTO ="Hace cuanto"
    RAZON = "Por que razón"
    APEGO = "¿Qué tanto se apegó a ella?"
    RESULTADO_ESPERADO ="¿Obtuvo los resultados esperados?"
    MEDICAMENTO_BAJAR_PESO ="¿Ha utilizado medicamentos para bajar de peso?"
    FLUCTUACION_PESO ="¿Cómo ha fluctuado su peso a lo largo de su vida?"
    CIRUGIA_PESO = "¿Se ha sometido a alguna cirugía para perder peso?"
    CONSUMO_AGUA_SIMPLE ="Consumo regular de agua simple al día"

class Recordatorio24HorasEnumeration(Enum):
    DESPERTAR = "Despiertas: "
    DESAYUNO = "Desayuno: " 
    ALMUERZO = "Almuerzo: " 
    COMIDA = "Comida: "
    MERIENDA = "Merienda: "
    CENA = "Cena: "
    DORMIR = "Dormir: "

class FrecuenciaAlimentosEnumeration(Enum):
    LACTEOS = "Lacteos: "
    CARNES = "Carnes: "
    VERDURAS = "Verduras: "
    FRUTAS = "Frutas: "
    CEREALES = "Cereales: "
    GRASA = "Grasa: "
    AZUCARES = "Azucares: "
    LEGUMINOSAS = "Leguminosas: "
    OLEAGINOSAS = "Oleaginosas: "

class MotivacionEnumeration(Enum):
    PREGUNTA1 = "¿Este es un buen momento para empezar con el esfuerzo de bajar de peso?" 
    PREGUNTA2 = "¿Cuáles obstáculos considerarías que se te presentarían para llegar al éxito de tu meta?"
    PREGUNTA3 = "¿Qué ventaja, más allá de tu peso consideras te traería estos cambios en tu estilo de vida?"
    PREGUNTA4 = "¿Qué te ha funcionado en el pasado y que no?"
    PREGUNTA5 = "¿Qué sería lo más importante que obtendría al ir cambiando su estilo de vida y logrando sus objetivos?"

class MetasEnumeration(Enum):
    CORTO_PLAZO = "Metas a corto plazo"
    LARGO_PLAZO = "Metas a largo plazo"
    RED_APOYO = "Identificacion de red de apoyo "
    APOYO_FAMILIAR = "¿Considera que su familia esté dispuesta a apoyarlo en este tratamiento?"
    VENTAJAS_MODIFICACION = "Modificacion estilo de vida: Ventajas"
    DESVENTAJAS_MODIFICACION = "Modificacion estilo de vida: Desventajas"
