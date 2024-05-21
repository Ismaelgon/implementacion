
from enum import Enum
from datetime import datetime
from typing import List

class Especialidad(Enum):
    CARDIOLOGIA = "Cardiología"
    DERMATOLOGIA = "Dermatología"
    PEDIATRIA = "Pediatría"

class Estado(Enum):
    PROGRAMADA = "Programada"
    REALIZADA = "Realizada"
    CANCELADA = "Cancelada"

class Persona:
    def __init__(self, nombre: str, identificacion: str, direccion: str):
        self.nombre = nombre
        self.identificacion = identificacion
        self.direccion = direccion

class Doctor(Persona):
    def __init__(self, nombre: str, identificacion: str, direccion: str, especialidad: Especialidad):
        super().__init__(nombre, identificacion, direccion)
        self.especialidad = especialidad

class Enfermero(Persona):
    def asistir_doc(self):
        print("Asistiendo al doctor")

class Cita:
    def __init__(self, fecha: datetime, hora: datetime, motivo: str, estado: Estado):
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.estado = estado

class GestionCitas:
    @staticmethod
    def programar_cita():
        print("Cita programada")

    @staticmethod
    def cancelar_cita():
        print("Cita cancelada")

    @staticmethod
    def realizar_cita():
        print("Cita realizada")

class Paciente(Persona):
    def __init__(self, nombre: str, identificacion: str, direccion: str, citas: List[Cita]):
        super().__init__(nombre, identificacion, direccion)
        self.citas = citas

class ExpedienteMedico:
    def __init__(self, diagnosticos: List[str], tratamientos: List[str], prescripciones: List[str]):
        self.diagnosticos = diagnosticos
        self.tratamientos = tratamientos
        self.prescripciones = prescripciones
