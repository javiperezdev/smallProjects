import random

def test_bases_de_datos():
    
    # Esta es la lista de preguntas, cada pregunta a su vez es un diccionario que contiene una lista de opciones. 
    # contiene la respuesta correcta y una explicación.
    
    preguntas = [
    {
        "pregunta": "Según FMBD (A. De Miguel), ¿qué característica NO es esencial en una base de datos?",
        "opciones": [
            "a) Redundancia controlada",
            "b) Almacenamiento en soporte volátil",
            "c) Independencia de datos respecto a aplicaciones",
            "d) Definición única almacenada con los datos"
        ],
        "respuesta_correcta": "b",
        "explicacion": "UT1bis.pdf especifica que los datos deben estar 'almacenados en soporte secundario (no volátil)'. El soporte volátil (como memoria RAM) no cumple este requisito fundamental."
    },
    {
        "pregunta": "¿Qué problema de los sistemas de archivos tradicionales se ilustra con el ejemplo de la transferencia bancaria fallida?",
        "opciones": [
            "a) Redundancia e inconsistencia",
            "b) Dificultad de acceso a los datos",
            "c) Falta de atomicidad",
            "d) Problemas de seguridad"
        ],
        "respuesta_correcta": "c",
        "explicacion": "UT1bis.pdf utiliza explícitamente el ejemplo: 'Si ocurre un fallo del sistema entre el PASO 1 y el PASO 2... INCONSISTENCIA DE DATOS' para demostrar la falta de atomicidad en operaciones críticas."
    },
    {
        "pregunta": "En la arquitectura ANSI/X3/SPARC, ¿qué nivel describe 'estructuras de datos complejas de bajo nivel'?",
        "opciones": [
            "a) Nivel de vistas",
            "b) Nivel lógico",
            "c) Nivel físico",
            "d) Nivel conceptual"
        ],
        "respuesta_correcta": "c",
        "explicacion": "UT1bis.pdf define el nivel físico como: 'Describe en detalle las estructuras de datos complejas de bajo nivel', mientras que el nivel lógico describe qué datos se almacenan y sus relaciones."
    },
    {
        "pregunta": "¿Qué modelo de datos se caracteriza por incluir 'métodos que definen su comportamiento' además de valores almacenados?",
        "opciones": [
            "a) Modelo entidad-relación",
            "b) Modelo relacional",
            "c) Modelo orientado a objetos",
            "d) Modelo de red"
        ],
        "respuesta_correcta": "c",
        "explicacion": "UT1bis.pdf establece: 'Modelo orientado a objetos: Un objeto contiene valores almacenados... Además y de forma adicional al E/R existen métodos en los objetos que definen su comportamiento'."
    },
    {
        "pregunta": "¿Qué propiedad ACID garantiza que 'los cambios deben ser consistentes y persistentes'?",
        "opciones": [
            "a) Atomicidad",
            "b) Consistencia",
            "c) Aislamiento",
            "d) Durabilidad"
        ],
        "respuesta_correcta": "d",
        "explicacion": "UT1bis.pdf define durabilidad como: 'Estado en el que se tiene que quedar la BD tras una operación atómica. Los cambios deben ser consistentes y persistentes (durabilidad)'."
    },
    {
        "pregunta": "Según UT1.pdf, ¿qué cualidad de la información NO se menciona como esencial?",
        "opciones": [
            "a) Precisión",
            "b) Oportunidad",
            "c) Redundancia",
            "d) Significatividad"
        ],
        "respuesta_correcta": "c",
        "explicacion": "UT1.pdf enumera como cualidades esenciales: 'Precisa, Oportuna, Completa, Significativa, Coherente e integra'. La redundancia es un problema a evitar, no una cualidad deseable."
    },
    {
        "pregunta": "¿Qué tipo de sistema de información se define como 'el que se diseña a conciencia para tratar la información de forma eficaz y eficiente'?",
        "opciones": [
            "a) Sistema de información informal",
            "b) Sistema de información formal",
            "c) Sistema de archivo tradicional",
            "d) Sistema de base de datos"
        ],
        "respuesta_correcta": "b",
        "explicacion": "UT1.pdf establece: 'Sistema de información formal u organizacional: El que se diseña a conciencia para tratar la información de forma eficaz y eficiente'."
    },
    {
        "pregunta": "En empresas grandes, ¿qué sistemas complejos se mencionan que se sitúan sobre las bases de datos?",
        "opciones": [
            "a) Solo sistemas de contabilidad",
            "b) ERP, CRM, SCM, BI, Big Data",
            "c) Sistemas operativos",
            "d) Hojas de cálculo compartidas"
        ],
        "respuesta_correcta": "b",
        "explicacion": "UT1.pdf indica explícitamente: 'Necesidad de sistemas informáticos más complejos que se sitúan sobre las base de datos: ERP, CRM, SCM, BI. BIG DATA'."
    },
    {
        "pregunta": "¿Qué función del DBA implica 'controlar las modificaciones físicas o del esquema interno'?",
        "opciones": [
            "a) Definición del esquema original",
            "b) Concesión de autorizaciones",
            "c) Modificación del esquema interno",
            "d) Especificación de reglas de integridad"
        ],
        "respuesta_correcta": "c",
        "explicacion": "UT1bis.pdf describe: 'Modificación del esquema interno de BD o de la organización física: El DBA deberá controlar las modificaciones físicas o del esquema interno que se pueden realizar'."
    },
    {
        "pregunta": "¿Qué tipo de usuario 'interactúa con el sistema mediante la invocación de programas de aplicación permanentes'?",
        "opciones": [
            "a) Usuarios sofisticados",
            "b) Programadores de aplicaciones",
            "c) Usuarios especializados",
            "d) Usuarios normales"
        ],
        "respuesta_correcta": "d",
        "explicacion": "UT1bis.pdf define usuarios normales como: 'Usuarios no sofisticados que interactúan con el sistema mediante la invocación de alguno de los programas de aplicación permanentes escrito previamente'."
    },
    {
        "pregunta": "Según Korth (FDBD), ¿qué es un Sistema Gestor de Base de Datos?",
        "opciones": [
            "a) Solo programas para gestionar archivos",
            "b) Colección de datos interrelacionados y programas para acceder a ellos",
            "c) Un sistema operativo mejorado",
            "d) Un conjunto de usuarios y aplicaciones"
        ],
        "respuesta_correcta": "b",
        "explicacion": "UT1bis.pdf cita textualmente a Korth: 'Sistema Gestor de Base de Datos (SGBD): Colección de datos interrelacionados entre sí y un conjunto de programas para acceder a dichos datos'."
    },
    {
        "pregunta": "¿Qué anomalía en accesos concurrentes se produce cuando dos procesos leen el mismo dato, lo modifican en memoria y escriben resultados inconsistentes?",
        "opciones": [
            "a) Redundancia de datos",
            "b) Pérdida de actualización",
            "c) Lectura no repetible",
            "d) Lectura fantasma"
        ],
        "respuesta_correcta": "b",
        "explicacion": "UT1bis.pdf describe este escenario: 'Al final en fich1 queda saldo = 900 eurs cuando debería quedar solo 700 eurs', ilustrando una pérdida de actualización por acceso concurrente no controlado."
    },
    {
        "pregunta": "¿Qué componente de un SGBD 'proporciona la interfaz entre los datos de bajo nivel y los programas de aplicación'?",
        "opciones": [
            "a) Procesador de consultas",
            "b) Gestor de almacenamiento",
            "c) Diccionario de datos",
            "d) Gestor de transacciones"
        ],
        "respuesta_correcta": "b",
        "explicacion": "UT1bis.pdf define: 'El gestor de almacenamiento del SGBD es un módulo de programa que proporciona la interfaz entre los datos de bajo nivel en la base de datos y los programas de aplicación y consultas'."
    },
    {
        "pregunta": "¿Qué tipo de lenguaje DML 'requiere que el usuario especifique qué datos se necesitan sin especificar cómo obtener esos datos'?",
        "opciones": [
            "a) DML procedimental",
            "b) DML no procedimental",
            "c) DDL",
            "d) SQL procedural"
        ],
        "respuesta_correcta": "b",
        "explicacion": "UT1bis.pdf establece: 'LMD NO PROCEDIMENTALES: Requieren que el usuario especifique qué datos se necesitan sin especificar cómo obtener esos datos'."
    },
    {
        "pregunta": "Según UT1.pdf, ¿qué problema de los sistemas de archivos tradicionales se produce cuando 'las distintas copias de la información duplicada no coinciden'?",
        "opciones": [
            "a) Redundancia",
            "b) Inconsistencia",
            "c) Aislamiento",
            "d) Falta de integridad"
        ],
        "respuesta_correcta": "b",
        "explicacion": "UT1bis.pdf define: 'Inconsistencia: Las distintas copias de la información duplicada no coinciden', como consecuencia directa del problema de redundancia."
    },
    {
        "pregunta": "¿Qué nivel de decisión empresarial corresponde a 'elaboración de planes y objetivos generales'?",
        "opciones": [
            "a) Nivel operacional",
            "b) Nivel táctico",
            "c) Nivel estratégico",
            "d) Nivel directivo"
        ],
        "respuesta_correcta": "c",
        "explicacion": "UT1.pdf clasifica: 'Nivel estratégico: Elaboración de planes. Objetivos generales', diferenciándolo del táctico (control de gestión) y operacional (tareas administrativas)."
    },
    {
        "pregunta": "¿Qué modelo de datos físicos se menciona específicamente en UT1bis.pdf?",
        "opciones": [
            "a) Modelo relacional",
            "b) Modelo de red",
            "c) Modelo de unificación",
            "d) Modelo entidad-relación"
        ],
        "respuesta_correcta": "c",
        "explicacion": "UT1bis.pdf indica: 'Existen pocos modelos de este tipo: Modelo de unificación, Modelo de memoria por marco', siendo estos los únicos modelos físicos mencionados explícitamente."
    },
    {
        "pregunta": "¿Qué ventaja de las bases de datos frente a ficheros se refiere a 'metadatos integrados con los datos'?",
        "opciones": [
            "a) Independencia de datos",
            "b) Mejor y más normalizada documentación",
            "c) Mayor eficiencia",
            "d) Reducción del espacio de almacenamiento"
        ],
        "respuesta_correcta": "b",
        "explicacion": "UT1.pdf enumera como ventaja: 'Mejor y más normalizada documentación de la información: metadatos integrados con los datos'."
    },
    {
        "pregunta": "¿Qué componente del procesamiento de consultas se encarga de 'transformar instrucciones que el gestor de almacenamiento entienda'?",
        "opciones": [
            "a) Compilador DML",
            "b) Intérprete DDL",
            "c) Motor de optimización y evaluación",
            "d) Precompilador de DML"
        ],
        "respuesta_correcta": "c",
        "explicacion": "UT1bis.pdf incluye en los componentes: 'Motor de optimización y evaluación de consultas', que se encarga de procesar las consultas para su ejecución eficiente."
    },
    {
        "pregunta": "Según UT1.pdf, ¿qué tipo de datos son 'datos que aportan información de carácter semántico sobre otros datos dándoles a estos cierto significado'?",
        "opciones": [
            "a) Microdatos",
            "b) Macrodatos",
            "c) Metadatos",
            "d) Datos estructurados"
        ],
        "respuesta_correcta": "c",
        "explicacion": "UT1.pdf define metadatos como: 'Datos que aportan información de carácter semántico sobre otros datos dándoles a estos cierto significado'."
        }
    ]

    print("---TEST BASES DE DATOS ---")
    print("Responde las siguientes preguntas (a, b, c o d):\n")
    
    aciertos = 0
    respuestas_usuario = []
    random.shuffle(preguntas)  # Para variar el orden de las preguntas.

    # Iteramos sobre las preguntas con un for loop.

    for i, p in enumerate(preguntas, 1): 
        print(f"Pregunta {i}: {p['pregunta']}")
        for opcion in p['opciones']:
            print(opcion)
        
        # Con el bucle while manejamos la entrada del usuario y nos aseguramos de que sea válida

        while True:
            respuesta = input("Tu respuesta: ").lower().strip()
            if respuesta in ['a', 'b', 'c', 'd']:
                break
            print("¡Respuesta no válida! Ingresa a, b, c o d")
        respuestas_usuario.append(respuesta)
        if respuesta == p['respuesta_correcta']:
            aciertos += 1 # Aumento contador de aciertos
            print("✅ Correcto\n")
        else:
            print(f"❌ Incorrecto. La respuesta correcta es: {p['respuesta_correcta']}\n")

            # Hacemos opcional el hecho de mostrar la explicación.

            ver_explicacion = input("¿Quieres ver la explicación de la respuesta correcta? (s/n): \n").lower().strip()
            if ver_explicacion == 's':
                print(f"Explicación: {p["explicacion"]}\n")
            elif ver_explicacion == 'n':
                print("Continuamos con el test.")
            else:
                print("Opción no válida, continuamos con las preguntas.")
    
    print("\n=== RESULTADOS ===")
    print(f"Aciertos: {aciertos}/{len(preguntas)}")
    print(f"Calificación: {aciertos/len(preguntas)*100:.1f}%")
    
    # Calificaciones mediante el contador de aciertos.
    if aciertos >= 35:
        nivel = "EXCELENTE"
    elif aciertos >= 30:
        nivel = "NOTABLE, ¿ES TU MÁXIMO?"
    elif aciertos >= 25:
        nivel = "BIEN, PUEDES HACERLO MEJOR"
    elif aciertos >= 20:
        nivel = "SUFICIENTE, ¿TE CONFORMAS?"
    else:
        nivel = "NECESITAS REPASAR A TOPE"
    
    print(f"Nivel de conocimiento: {nivel}")

test_bases_de_datos()