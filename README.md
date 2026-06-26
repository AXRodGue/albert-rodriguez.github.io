📝 Acerca de mí

Soy QA Engineer Jr enfocado en el diseño y automatización de pruebas de software utilizando Python, Selenium WebDriver y Pytest. Mi enfoque combina la rigurosidad de las metodologías tradicionales de QA con la velocidad de la automatización moderna.

Me especializo en crear suites de Pruebas de Humo (Smoke Testing) para asegurar la estabilidad post-despliegue y en estructurar robustas suites de Pruebas de Regresión para garantizar que los nuevos cambios de código no rompan la lógica existente del negocio. Diseño mis escenarios aplicando técnicas clásicas como el Análisis de Valores Límites, optimizando la cobertura mediante pruebas parametrizadas y listas de comprobación inteligentes que aseguran una rigurosa validación de datos en la interfaz de usuario.

Mis habilidades clave:
🧪 Estrategia de QA: Diseño de casos de prueba, listas de comprobación (Checklists), análisis de valores límites.
🛠️ Automatización: Python, Selenium, Pytest (Fixtures, Parametrización y Marcadores).
🗄️ Bases de Datos: PostgreSQL (Consultas complejas, validación de integridad, scripts de limpieza).
🔄 Tipos de Pruebas: Smoke Testing, Pruebas de Regresión, Pruebas Funcionales de UI.
📊 Validación de Datos: Asersiones lógicas avanzadas, limpieza de cadenas y verificación de consistencia en UI.

📁 Mis Proyectos Recientes

Proyecto 1: Suite de Smoke Testing y Casos de Prueba para Autenticación
📌 Contexto y ProblemaEn un portal tecnológico SaaS, los despliegues frecuentes introducían errores que bloqueaban el acceso de los usuarios. Se requería una suite de Pruebas de Humo (Smoke Testing) rápida que validara que las funciones más críticas (Login y Recuperación de contraseña) estuvieran operativas tras cada actualización.

🛠️ Estrategia de QA e Impacto
Casos de Prueba y Checklist: Diseñé una lista de comprobación (Checklist) con los escenarios críticos antes de codificar.
Automatización Esencial: Creé scripts con Python y Selenium WebDriver usando pytest para verificar el flujo feliz (credenciales correctas) y el manejo de errores (credenciales incorrectas).
Validación de Datos: El script valida que los mensajes de error textuales de la interfaz coincidan exactamente con los requerimientos del negocio.
Impacto: Se redujo el tiempo de verificación post-despliegue de 15 minutos manuales a solo 12 segundos automatizados.

Proyecto 2: Pruebas de Valores Límites en Formulario de Registro
📌 Contexto y ProblemaUna plataforma web de tecnología restringía el registro a usuarios según su edad (mínimo 18 años, máximo 65 años). Existían reportes de que usuarios de 17 años lograban registrarse debido a una mala lógica en las validaciones del backend.

🛠️ Estrategia de QA e Impacto
Técnica de Diseño de Pruebas: Apliqué Análisis de Valores Límites (Boundary Value Testing) para identificar los puntos críticos exactos a probar.
Listas de Comprobación Parametrizadas: Utilicé la potencia de pytest.mark.parametrize para ejecutar una sola prueba matemática pasándole múltiples datos fronterizos (17, 18, 65, 66 años).
Validación de Datos: Selenium ingresa cada edad límite en el formulario y valida si la UI permite el registro o bloquea con un mensaje de alerta.
Impacto: Se detectó un bug crítico donde el límite superior (65 años) estaba bloqueando a personas que sí debían poder registrarse.

Proyecto 3: Suite de Pruebas de Regresión para Carrito de Compras.
📌 Contexto y ProblemaCada vez que el equipo de desarrollo añadía un nuevo método de pago o una actualización estética al módulo de e-commerce, funciones que ya servían (como agregar productos o calcular el total del carrito) dejaban de funcionar misteriosamente.

🛠️ Estrategia de QA e Impacto
Pruebas de Regresión: Diseñé una suite estable enfocada en re-verificar que las funcionalidades existentes no se hubieran roto con los nuevos cambios.
Validación Estricta de Datos: El script interactúa con la UI usando Selenium, añade un producto, extrae los textos de los precios y realiza una operación aritmética en Python para verificar que la suma sea correcta.
Uso de PyTest: Organización de los casos de prueba mediante marcadores (@pytest.mark.regression) para poder ejecutar toda la suite con un solo comando.
Impacto: Se automatizó la revisión de regresión eliminando la necesidad de simular compras manuales antes de cada entrega de código.
# albert-rodriguez.github.ioPortafolio QA

