# -*- coding: utf-8 -*-

from odoo import models, fields, api


class profesor(models.Model):
    _name = 'gestion_academica.profesor'
    _description = 'gestion_academica.profesor'

    name = fields.Char(string='Nombre', required=True)
    edad = fields.Integer(string='Edad')
    especialidad = fields.Char(string='Especialidad')
    materiacursogestion_ids = fields.One2many('gestion_academica.materia_curso_gestion', 'profesor_id', string='Materias, Cursos y Gestiones')

class Alumno(models.Model):
    _name = 'gestion_academica.alumno'
    _description = 'Alumno'

    name = fields.Char(string='Nombre', required=True)
    edad = fields.Integer(string='Edad')
    grado = fields.Char(string='Grado')
    curso_id = fields.Many2one('gestion_academica.curso', string='Curso')
    parentesco_ids = fields.One2many('gestion_academica.parentesco', 'alumno_id', string='Apoderados')
    inscripcion_id = fields.Many2one('gestion_academica.inscripcion', string='Inscripcion')
    nota_ids = fields.One2many('gestion_academica.nota', 'alumno_id', string='Notas')

class curso(models.Model):
    _name = 'gestion_academica.curso'
    _description = 'Curso'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    alumno_ids = fields.One2many('gestion_academica.alumno', 'curso_id', string='Alumnos')
    cursogestion_ids = fields.One2many('gestion_academica.curso_gestion', 'curso_id', string='Cursos y Gestiones')

class Apoderado(models.Model):
    _name = 'gestion_academica.apoderado'
    _description = 'Apoderado'

    name = fields.Char(string='Nombre', required=True)
    ci = fields.Char(string='Carnet de Identidad', required=True)
    genero = fields.Selection([
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ], string='Género', required=True)
    telefono = fields.Char(string='Teléfono')
    parentesco_ids = fields.One2many('gestion_academica.parentesco', 'apoderado_id', string='Alumnos')
    comunicado_id = fields.Many2one('gestion_academica.comunicado', string='Comunicado')

class parentesco(models.Model):
    _name = 'gestion_academica.parentesco'
    _description = 'Parentesco'

    descripcion = fields.Selection([
        ('padre', 'Padre'),
        ('madre', 'Madre'),
        ('tutor', 'Tutor'),
    ], string='Descripción')
    apoderado_id = fields.Many2one('gestion_academica.apoderado', string='Apoderado')
    alumno_id = fields.Many2one('gestion_academica.alumno', string='Alumno')

class gestion(models.Model):
    _name = 'gestion_academica.gestion'
    _description = 'Gestion'

    name = fields.Char(string='Nombre', required=True)
    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_final = fields.Date(string='Fecha Final')
    cursogestion_ids = fields.One2many('gestion_academica.curso_gestion', 'gestion_id', string='Cursos y Gestiones')
    
class cursogestion(models.Model):
    _name = 'gestion_academica.curso_gestion'
    _description = 'Curso y Gestion'

    curso_id = fields.Many2one('gestion_academica.curso', string='Curso')
    gestion_id = fields.Many2one('gestion_academica.gestion', string='Gestion')
    inscripcioncursogestion_ids = fields.One2many('gestion_academica.inscripcioncursogestion', 'cursogestion_id', string='Inscripciones, Cursos y Gestiones')
    materiacursogestion_ids = fields.One2many('gestion_academica.materia_curso_gestion', 'cursogestion_id', string='Materias, Cursos y Gestiones')

class materia(models.Model):
    _name = 'gestion_academica.materia'
    _description = 'Materia'

    name = fields.Char(string='Nombre', required=True)
    materiacursogestion_ids = fields.One2many('gestion_academica.materia_curso_gestion', 'materia_id', string='Materias, Cursos y Gestiones')
    
class materiacursogestion(models.Model):
    _name = 'gestion_academica.materia_curso_gestion'
    _description = 'Materia, Curso y Gestion'

    cursogestion_id = fields.Many2one('gestion_academica.cursogestion', string='Curso y Gestion')
    profesor_id = fields.Many2one('gestion_academica.profesor', string='Profesor')
    materia_id = fields.Many2one('gestion_academica.materia', string='Materia')
    nota_ids = fields.One2many('gestion_academica.nota', 'materiacursogestion_id', string='Notas')
    materiacursoparalelo_ids = fields.One2many('gestion_academica.materia_curso_paralelo', 'materiacursogestion_id', string='Materias, Cursos y Paralelos')
    
class paralelo(models.Model):
    _name = 'gestion_academica.paralelo'
    _description = 'Paralelo'

    descripcion = fields.Text(string='Descripción')
    materiacursoparalelo_ids = fields.One2many('gestion_academica.materia_curso_paralelo', 'paralelo_id', string='Materias, Cursos y Paralelos')
    
class materiacursoparalelo(models.Model):
    _name = 'gestion_academica.materia_curso_paralelo'
    _description = 'Materia, Curso y Paralelo'

    materiacursogestion_id = fields.Many2one('gestion_academica.materia_curso_gestion', string='Materia, Curso y Gestion')
    paralelo_id = fields.Many2one('gestion_academica.paralelo', string='Paralelo')
    horario_id = fields.Many2one('gestion_academica.horario', string='Horario')
    
class horario(models.Model):
    _name = 'gestion_academica.horario'
    _description = 'Horario'

    materia=fields.Selection([
        ('fisica', 'Fisica'),
        ('quimica', 'Quimica'),
        ('religion', 'Religion'),
        ('educacion fisica', 'Educaion Fisica'),
        ('psicologia', 'Psicologia'),
        ('ciencias sociales', 'Ciencias Sociales'),
        ('ciencias naturales', 'Ciencias Naturales'),
        ('musica', 'Musica'),
        ('artes plasticas', 'Artes Plasticas'),
        ('historia', 'Historia'),
        ('matematicas', 'Matematicas'),
        ('biologia', 'Biologia'),
    ], string='Materia', required=True)
    dia = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miércoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sábado', 'Sábado'),
        ('domingo', 'Domingo'),
    ], string='Día', required=True)
    hora_inicio = fields.Float(string='Hora de Inicio', required=True)
    hora_fin = fields.Float(string='Hora de Fin', required=True)
    materia_id = fields.Many2one('gestion_academica.materia', string='Materia')

class Inscripcion(models.Model):
    _name = 'gestion_academica.inscripcion'
    _description = 'Inscripcion'

    name = fields.Char(string='Nombre', required=True)
    fecha_inscripcion = fields.Date(string='Fecha de Inscripcion')
    alumno_ids = fields.One2many('gestion_academica.alumno', 'inscripcion_id', string='Alumnos')
    inscripcioncursogestion_ids = fields.One2many('gestion_academica.inscripcioncursogestion', 'inscripcion_id', string='Inscripciones, Cursos y Gestiones')

class Comunicado(models.Model):
    _name = 'gestion_academica.comunicado'
    _description = 'Comunicado'

    descripcion = fields.Text(string='Descripcion')
    apoderado_ids = fields.One2many('gestion_academica.apoderado', 'comunicado_id', string='Apoderados')

class Nota(models.Model):
    _name = 'gestion_academica.nota'
    _description = 'Nota'

    ponderacion = fields.Float(string='Ponderacion')
    alumno_id = fields.Many2one('gestion_academica.alumno', string='Alumno')
    materiacursogestion_id = fields.Many2one('gestion_academica.materia_curso_gestion', string='Materia, Curso y Gestion')
    bimestre_id = fields.Many2one('gestion_academica.bimestre', string='Bimestre')

class Bimestre(models.Model):
    _name = 'gestion_academica.bimestre'
    _description = 'Bimestre'

    descripcion = fields.Text(string='Descripcion')
    nota_ids = fields.One2many('gestion_academica.nota', 'bimestre_id', string='Notas')

class inscripcioncursogestion(models.Model):
    _name = 'gestion_academica.inscripcioncursogestion'
    _description = 'Inscripcion, Curso y Gestion'

    name = fields.Char(string='Nombre', required=True)
    paralelo = fields.Char(string='Paralelo')
    inscripcion_id = fields.Many2one('gestion_academica.inscripcion', string='Inscripcion')
    cursogestion_id = fields.Many2one('gestion_academica.curso_gestion', string='Curso y Gestion')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

