"""
Nuño Europolitics Streamlit Dashboard Main Application.

This application provides the MVP functional dashboard for the Nuño Europolitics project.
Includes modules for Geopolitical Risk Analysis, Full-Cycle Intelligence,
Strategic Foresight, Community Policy Monitoring, and Technical Training.
"""

import sys
import asyncio
import pandas as pd
import streamlit as st
from loguru import logger
from sqlalchemy import text

# Configure loguru: Structured JSON via loguru. Console debug output enabled.
logger.remove()
logger.add(sys.stderr, level="DEBUG", serialize=True)

# Application Configuration
st.set_page_config(page_title="Nuño Europolitics Dashboard", layout="wide", page_icon="🌐")

async def fetch_geopolitical_risk_data() -> pd.DataFrame:
    """
    Simulates fetching geopolitical risk data asynchronously.
    
    Returns:
        pd.DataFrame: A simulated dataframe containing risk assessments.
    """
    logger.debug("Fetching geopolitcal risk data asynchronously.")
    await asyncio.sleep(1) # Simulate I/O delay
    data = {
        "Region": ["Eastern Europe", "Middle East", "Balkans", "North Africa"],
        "Risk Level": ["Critical", "High", "Medium", "High"],
        "Impact on Supply Chain (EU)": ["Severe", "Moderate", "Low", "Moderate"]
    }
    return pd.DataFrame(data)

def init_db():
    """
    Initializes SQLite database and creates the required tables if they don't exist.
    """
    conn = st.connection("europolitics", type="sql", url="sqlite:///europolitics.db")
    with conn.session as s:
        s.execute(text('''
            CREATE TABLE IF NOT EXISTS intelligence_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                source TEXT,
                validity_score INTEGER,
                content TEXT
            )
        '''))
        s.commit()
    logger.info("Database initialized successfully.")
    return conn

def main_dashboard():
    """Renders the main Streamlit dashboard."""
    st.title("🛡️ Nuño Europolitics - Strategic Intelligence")
    st.markdown("Plataforma de análisis de riesgo geopolítico y prospectiva estratégica.")
    
    conn = init_db()
    
    tabs = st.tabs([
        "Análisis Geopolítico", 
        "Inteligencia de Ciclo Completo", 
        "Prospectiva Estratégica", 
        "Monitorización UE", 
        "Capacitación Técnica"
    ])
    
    with tabs[0]:
        st.header("Análisis de Riesgo Geopolítico")
        st.write("Evaluación de tensiones regionales y su impacto directo en las cadenas de suministro.")
        # Execute async fetch
        risk_data = asyncio.run(fetch_geopolitical_risk_data())
        st.dataframe(risk_data, use_container_width=True)
        
    with tabs[1]:
        st.header("Inteligencia de Ciclo Completo")
        st.write("Ingreso y visualización de fuentes e informes de situación.")
        with st.form("add_report_form"):
            title = st.text_input("Título del Informe")
            source = st.text_input("Fuente/Agencia")
            validity = st.slider("Validación de Fiabilidad de Fuente (1-10)", 1, 10, 5)
            content = st.text_area("Cuerpo del Informe")
            submitted = st.form_submit_button("Guardar Informe")
            
            if submitted:
                with conn.session as s:
                    s.execute(text("INSERT INTO intelligence_reports (title, source, validity_score, content) VALUES (:t, :s, :v, :c)"), 
                              {"t": title, "s": source, "v": validity, "c": content})
                    s.commit()
                st.success("Informe de situación guardado correctamente en la base de datos local SQLite.")
                logger.info({"action": "report_saved", "title": title, "validity": validity})
        
        # Display existing reports summary
        st.subheader("Informes Recientes")
        reports = conn.query('SELECT * FROM intelligence_reports')
        st.dataframe(reports)
        
    with tabs[2]:
        st.header("Prospectiva Estratégica")
        st.write("Elaboración de escenarios futuros y 'cisnes negros'.")
        st.info("Módulo en desarrollo para mapeo probabilístico interactivo.")
        
    with tabs[3]:
        st.header("Monitorización de Políticas Comunitarias")
        st.write("Análisis del impacto regulatorio y político (Instituciones de la UE).")
        st.warning("Sin nuevas directivas operativas registradas en el último ciclo.")

    with tabs[4]:
        st.header("Capacitación Técnica")
        st.write("Formación especializada para equipos de seguridad y estrategia.")
        st.button("Acceso a Curso: Análisis Estructurado")

if __name__ == "__main__":
    main_dashboard()
