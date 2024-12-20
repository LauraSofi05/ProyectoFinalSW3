#Servicio Docente
from Model.teacher import Teacher
from Model.connection import db

class TeacherService:

    @staticmethod
    def create_teacher(data):
        print(f"Datos recibidos en el servicio: {data}")
        # Validacion de los datos requeridos
        if not data.get('teTypeIdentification') or not data.get('teIdentification') \
            or not data.get('teTypeTeacher') or not data.get('teName')\
            or not data.get('teLastName') or not data.get('teLastTitle')\
            or not data.get('teEmail'):

            return None, "Todos los campos son requeridos"
        
        # Crear un nuevo docente
        new_teacher = Teacher(
                teTypeIdentification=data['teTypeIdentification'],
                teIdentification=data['teIdentification'],
                teTypeTeacher=data['teTypeTeacher'],
                teName=data['teName'],
                teLastName=data['teLastName'],
                teLastTitle=data['teLastTitle'],
                teEmail=data['teEmail'],
                teState=['Activo']
            )
        
        try:
            db.session.add(new_teacher)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return None, f"Error al crear el profesor: {str(e)}"

        return new_teacher, None
    
    @staticmethod
    def get_all_teacher():
        #*Obtiene todos los docentes
        try:
            # Consultar todos los docentes 
            # Consultar solo los campos requeridos
            teachers = db.session.query(Teacher).all()

            if not teachers:
                return [], "No se encontraron docentes."
            # Convertir las tuplas resultantes en una lista de diccionarios
            teachers_dict = [tea.to_dict() for tea in teachers]
        
            print(teachers_dict)  # Esto imprimirá el contenido de los diccionarios
            
            return teachers_dict, None  # Devolver los resultados como lista de diccionarios
        except Exception as e:
            # En caso de error, devolver el mensaje de error
            return [], f"Error al obtener los docentes: {str(e)}"
        
    @staticmethod
    def search_by_identificationTeacher(teIdentification):
        try:
            #Busca un docente por su identificación
            teacher = Teacher.query.filter_by(teIdentification=teIdentification).first()
            if teacher:
                return teacher, None
            return None, "Docente no encontrado"
        except Exception as e:
            return None, f"Error al buscar al docente {str(e)}"
        
    @staticmethod
    def search_by_typeTeacher(teTypeTeacher):
        try:
            #Buscar todos los docentes por el tipo de docente
            teachers = Teacher.query.filter_by(teTypeTeacher=teTypeTeacher).all()
            if teachers:
                return teachers, None
            return None, "No se encontraron docentes con el tipo especificado"
        except Exception as e:
            return None, f"Error al buscar al docente {str(e)}"