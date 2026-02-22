# 🌐 Nuño Europolitics - Strategic Intelligence Dashboard MVP

![Status](https://img.shields.io/badge/Status-MVP-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Database](https://img.shields.io/badge/Database-SQLite-lightgrey.svg)
![Security](https://img.shields.io/badge/Security-CONF23--STD--SDLC--004-critical.svg)

## 📌 Resumen del Proyecto

**Nuño Europolitics** es una plataforma de inteligencia estratégica diseñada para operar bajo el estándar de seguridad de ciclo de vida de desarrollo de software seguro de la compañía (`CONF23-STD-SDLC-004`). Permite a los analistas, directores y personal de seguridad evaluar el impacto geopolítico en las cadenas de suministro europeas, monitorear políticas comunitarias e ingresar informes en un registro local inmutable estructurado y clasificado, sin comprometer la seguridad operativa (OPSEC). Mediante el uso de bases de datos locales autoconstruidas (`SQLite`) y la I/O nativamente priorizada (`asyncio`), la aplicación actúa como un pilar ágil desconectado de terceras partes no confiables.

---

## 🏗️ Estado Actual del Proyecto (MVP)

Actualmente, el proyecto se encuentra en la etapa **MVP (Producto Mínimo Viable)** y es *plenamente funcional*. 
Las siguientes capacidades están desarrolladas y operativas:
- **✅ Análisis Geopolítico**: Renderización de datos de impacto en la cadena de suministro y evaluación de tensiones (I/O asíncrona).
- **✅ Inteligencia de Ciclo Completo**: Inserción segura de reportes desde el formulario de la propia plataforma, incluyendo fiabilidad de la fuente, con protección parametrizada (`loguru` activado en segundo plano).
- **✅ Capacitación y Exploración**: Bases UI y enrutamiento planteadas para los módulos de Políticas Comunitarias y el mapeo del impacto probable de Cisnes Negros.
- **✅ Infraestructura Autónoma**: Entorno sin dependencias instalado por el gestor de ciclo de vida (`build.cmd`).

*Para más detalles sobre las estimaciones para una versión de integración cloud (V2), puedes consultar el archivo `NuñoEuropolitics_ProductBacklog.md`.*

---

## 📚 Resumen de la Documentación Generada (ISO/IEC/IEEE 29148:2018)

Este desarrollo ha consolidado una base documental sólida y auditable conforme a las guías de ingeniería de sistemas formales:

| N.º / Docto. | Visión General y Propósito Principal |
|-------------|-----------------------|
| 📖 **DOC01 CONOPS** *(Concept of Operations)* | Resume la visión de liderazgo del proyecto. Muestra el flujo fundamental por el cual la herramienta servirá a los directores para el análisis sin descuidar el esquema táctico y seguro de cero-dependencia cloud en la V1. |
| 💼 **DOC02 BRS** *(Business Requirements)* | Documenta el problema fragmentado analítico actual y cómo la centralización MVP va alineada a metas de estabilidad en tierra europea para la dirección. |
| 👥 **DOC03 StRS** *(Stakeholder Req.)* | Perfila los roles de uso: *Analista de Inteligencia, Manager de Estrategia, y Líder de Capacitación*. Define las necesidades asiladas de cada usuario que impactara en la UX/UI de navegación. |
| ⚙️ **DOC04 SyRS** *(System Requirements)* | Establece los parámetros de despliegue, I/O asíncrono, librerías, entorno hardware e implementaciones requeridas por el marco (`CONF23-STD-SDLC-004`). |
| 💻 **DOC05 SRS** *(Software Requirements)* | Especificaciones de la arquitectura técnica SQL relacional de un solo nodo (tablas y parámetros), flujos subyacentes e iteración con Python `async`. |

### **Artefactos SCRUM & Agile:**
- `NuñoEuropolitics_ProductBacklog.md`: Muestra lo implementado en el **MVP** actual y los objetivos a seguir en el próximo desarrollo (REST APIs, Seguridad multi-rol y mapas dinámicos).
- `NuñoEuropolitics_DefinitionOfDone.md`: Documento de calidad de validación que se aseguró para declarar terminada la fase actual. Se revisan aquí requerimientos de logging e inicialización con cero toques (Zero-Touch).

---

## 🚀 Despliegue Automatizado (Zero-Touch Build)

El proyecto incluye un script de automatización (`build.cmd`) preparado para máquinas MS-DOS/Windows de forma local y segregada.

**Instrucciones de Despliegue (1 Minuto):**
1. Asegúrate de tener Python 3.x disponible en tus variables de entorno `PATH`.
2. Ejecuta en consola el instalador automatizado desde la carpeta raíz:
   ```cmd
   .\build.cmd
   ```
3. El script actuará con autonomía localizando el proceso de:
    - Compartimentación de entorno y activación virtual (`venv`).
    - Resolución de dependencias (`requirements.txt` vía `pip`).
    - Preparación del motor temporal y base de datos `SQLite` requerida en vivo.
    - Lanzamiento automático en el navegador por defecto (puerto `8501`).

---
*Diseñado por la iniciativa de Desarrollo Agente-Lógico bajo confidencialidad y requerimientos del grupo de SecDevOps de CONFIANZA23.*
