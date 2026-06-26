# 📋 Lista de Comprobación y Casos de Prueba: Módulo de Autenticación

**Proyecto:** Suite de Smoke Testing para Login  
**Rol:** QA Engineer Jr  
**Tipo de Prueba:** Pruebas de Humo (Smoke Testing) / Funcional Caja Negra  

---

## 🔍 Lista de Comprobación (Checklist) Enfoque Rápido
- [ ] Verificar acceso inicial a la URL de Login.
- [ ] Validar comportamiento con credenciales válidas (Flujo Feliz).
- [ ] Validar comportamiento con credenciales inválidas (Manejo de Errores).
- [ ] Validar presencia de elementos clave de la interfaz de usuario (Campos y Botón).

---

## 📄 Diseño de Casos de Prueba Detallados

### Caso de Prueba 1: Login Exitoso (Smoke Test)
*   **ID:** CP-001
*   **Descripción:** Validar que un usuario registrado pueda iniciar sesión correctamente usando credenciales válidas.
*   **Precondiciones:** El usuario debe estar previamente registrado en el sistema.
*   **Pasos de Ejecución:**
    1. Navegar a la URL: `https://ejemplo-tech.com`
    2. Ingresar `usuario_qa` en el campo "Username".
    3. Ingresar `Password123!` en el campo "Password".
    4. Hacer clic en el botón "Iniciar Sesión".
*   **Resultado Esperado:** El usuario es redirigido correctamente a la página del Dashboard (`/dashboard`).
*   **Estado Automatizado:** ✅ Sí (`test_smoke_login.py -> test_smoke_login_exitoso`)

### Caso de Prueba 2: Intento de Login con Credenciales Inválidas
*   **ID:** CP-002
*   **Descripción:** Validar que el sistema bloquee el acceso y muestre un mensaje claro si las credenciales son erróneas.
*   **Precondiciones:** Ninguna.
*   **Pasos de Ejecución:**
    1. Navegar a la URL: `https://ejemplo-tech.com`
    2. Ingresar `usuario_falso` en el campo "Username".
    3. Ingresar `WrongPass` en el campo "Password".
    4. Hacer clic en el botón "Iniciar Sesión".
*   **Resultado Esperado:** El sistema permanece en la página de login y muestra el mensaje en pantalla: *"Credenciales incorrectas. Intente de nuevo."*
*   **Estado Automatizado:** ✅ Sí (`test_smoke_login.py -> test_login_invalido_muestra_error`)
