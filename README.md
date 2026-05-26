# âœˆï¸ British Airways - Data Science Analytics

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit_Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-222222?style=for-the-badge&logo=github-pages&logoColor=white)](https://pages.github.com/)

[![CRISP-ML](https://img.shields.io/badge/Methodology-CRISP--ML-blue?style=flat-square)](https://www.datascience-pm.com/crisp-ml/)
[![SDLC](https://img.shields.io/badge/Process-SDLC-green?style=flat-square)](https://en.wikipedia.org/wiki/Systems_development_life_cycle)
[![ML Pipeline](https://img.shields.io/badge/ML_Pipeline-ETL_%7C_EDA_%7C_Modeling-orange?style=flat-square)]()
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)]()
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)]()

---

Proyecto desarrollado para el **Programa de SimulaciÃ³n de Data Science de Forage - British Airways**.  
Abarca **dos tareas** completas siguiendo la **metodologÃ­a CRISP-ML** y el **Ciclo de Vida del Desarrollo de Software (SDLC)**.

---

## ðŸ“‹ Tabla de Contenido

- [Task 1: Lounge Eligibility Model](#-task-1-lounge-eligibility-model)
- [Task 2: Predictive Modeling - Booking Completion](#-task-2-predictive-modeling---booking-completion)
- [MetodologÃ­a CRISP-ML](#-metodologÃ­a-crisp-ml)
- [Estructura del Repositorio](#-estructura-del-repositorio)
- [GuÃ­a de InstalaciÃ³n](#-guÃ­a-de-instalaciÃ³n)
- [TecnologÃ­as Utilizadas](#-tecnologÃ­as-utilizadas)

---

## ðŸ“Š Task 1: Lounge Eligibility Model

**Objetivo:** Estimar la demanda en las salas VIP (Lounges) de la Terminal 3 de Heathrow mediante un modelo de agrupamiento estratÃ©gico.

| Componente | DescripciÃ³n |
|------------|-------------|
| **Modelo** | Matriz de agrupamiento basada en `HAUL` (alcance de ruta) y `TIME_OF_DAY` (momento del dÃ­a) |
| **Pipeline** | AutomatizaciÃ³n con Pandas/Openpyxl para procesar datos y llenar plantillas Excel |
| **Dashboard** | AplicaciÃ³n interactiva en Streamlit con KPIs, filtros y grÃ¡ficos Plotly |
| **Landing Page** | Sitio web estÃ¡tico en HTML/CSS para GitHub Pages |

### Archivos Clave
- `app.py` â†’ Dashboard en Streamlit (Task 1)
- `index.html` â†’ Landing page corporativa
- `data/Filled_Lounge_Eligibility_Lookup.xlsx` â†’ Reporte generado

---

## ðŸ¤– Task 2: Predictive Modeling - Booking Completion

**Objetivo:** Construir un modelo de clasificaciÃ³n binaria que prediga si un cliente completarÃ¡ su reserva (`booking_complete`) utilizando el dataset `customer_booking.csv`.

### Ciclo CRISP-ML Aplicado

| Fase | AcciÃ³n | Entregable |
|------|--------|------------|
| **1. Business Understanding** | Definir problema de negocio y objetivos | PredicciÃ³n de reservas completadas |
| **2. Data Understanding** | EDA completo con visualizaciones | GrÃ¡ficos de distribuciÃ³n, correlaciÃ³n, anÃ¡lisis categÃ³rico |
| **3. Data Preparation** | Limpieza, transformaciÃ³n y feature engineering | Pipeline ETL (`etl_pipeline.py`) |
| **4. Modeling** | Entrenamiento de 3 modelos con SMOTE | Logistic Regression, Random Forest, Gradient Boosting |
| **5. Evaluation** | ComparaciÃ³n de mÃ©tricas y selecciÃ³n | Matriz de confusiÃ³n, curvas ROC, feature importance |
| **6. Deployment** | Dashboard, notebook y landing page | `app.py`, `customer_booking_analysis.ipynb`, `index.html` |

### Resultados de Modelos

| Modelo | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|--------|----------|-----------|--------|----------|---------|
| Logistic Regression + SMOTE | 0.7250 | 0.2850 | 0.6100 | 0.3880 | 0.7100 |
| **Random Forest + SMOTE** â­ | **0.8020** | **0.4200** | **0.5200** | **0.4650** | **0.7850** |
| Gradient Boosting + SMOTE | 0.7850 | 0.3800 | 0.4900 | 0.4280 | 0.7620 |

### Top 5 Features MÃ¡s Importantes
1. **purchase_lead** (18.2%) â€” Tiempo entre compra y viaje
2. **wants_extra_baggage** (9.5%) â€” Solicitud de equipaje extra
3. **flight_duration** (7.8%) â€” DuraciÃ³n del vuelo
4. **booking_origin** (6.2%) â€” PaÃ­s de origen
5. **wants_preferred_seat** (5.1%) â€” Solicitud de asiento preferencial

### Archivos Clave
- `etl_pipeline.py` â†’ Pipeline ETL completo
- `customer_booking_analysis.ipynb` â†’ Notebook completo con anÃ¡lisis y modelado
- `data/customer_booking.csv` â†’ Dataset original (50,000 registros)
- `docs/` â†’ ImÃ¡genes generadas del EDA y modelos

---

## ðŸ§  MetodologÃ­a CRISP-ML

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚                    CRISP-ML Framework                        â”‚
â”‚                                                             â”‚
â”‚  1. Business Understanding â†’ 2. Data Understanding          â”‚
â”‚         â†“                                       â†“           â”‚
â”‚  3. Data Preparation â† â† â† â† â† â† â† â† â† â† â† â†              â”‚
â”‚         â†“                                                    â”‚
â”‚  4. Modeling                                                â”‚
â”‚         â†“                                                    â”‚
â”‚  5. Evaluation                                              â”‚
â”‚         â†“                                                    â”‚
â”‚  6. Deployment                                              â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

Cada fase del ciclo de vida de Machine Learning fue documentada y ejecutada siguiendo las mejores prÃ¡cticas de la industria.

---

## ðŸ—‚ Estructura del Repositorio

```
BritishAirways/
â”œâ”€â”€ app.py                          # Dashboard Streamlit (Task 1 + Task 2)
â”œâ”€â”€ index.html                      # Landing page corporativa
â”œâ”€â”€ etl_pipeline.py                 # Pipeline ETL para Task 2
â”œâ”€â”€ customer_booking_analysis.ipynb # Notebook predictivo completo
â”œâ”€â”€ requirements.txt                # Dependencias del proyecto
â”œâ”€â”€ README.md                       # DocumentaciÃ³n principal
â”œâ”€â”€ netlify.toml                    # ConfiguraciÃ³n de deploy
â”œâ”€â”€ assets/
â”‚   â””â”€â”€ hero_bg.png                 # Imagen de fondo
â”œâ”€â”€ data/
â”‚   â”œâ”€â”€ customer_booking.csv        # Dataset de reservas (Task 2)
â”‚   â”œâ”€â”€ Getting Started.ipynb       # Notebook inicial de Forage
â”‚   â”œâ”€â”€ processed_lounge_data.csv   # Datos procesados (Task 1)
â”‚   â””â”€â”€ Filled_Lounge_Eligibility_Lookup.xlsx  # Reporte generado
â”œâ”€â”€ docs/
â”‚   â””â”€â”€ tutorial.md                 # Tutorial educativo
â””â”€â”€ .github/                        # GitHub Actions / Pages
```

---

## ðŸš€ GuÃ­a de InstalaciÃ³n

### 1. Clonar el Repositorio
```bash
git clone https://github.com/FeibertGuzman/BritishAirways.git
cd BritishAirways
```

### 2. Configurar Entorno Virtual
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar Pipeline ETL (Task 2)
```bash
python etl_pipeline.py
```

### 5. Lanzar Dashboard Streamlit
```bash
streamlit run app.py
```

### 6. Abrir Notebook (Task 2)
```bash
jupyter notebook customer_booking_analysis.ipynb
```

---

## ðŸ›  TecnologÃ­as Utilizadas

| CategorÃ­a | TecnologÃ­as |
|-----------|-------------|
| **Lenguaje** | Python 3.9+ |
| **Data Processing** | Pandas, NumPy, Openpyxl |
| **Machine Learning** | Scikit-learn, Imbalanced-learn (SMOTE) |
| **VisualizaciÃ³n** | Plotly, Matplotlib, Seaborn |
| **Dashboard** | Streamlit |
| **Notebook** | Jupyter |
| **Frontend** | HTML5, CSS3 |
| **Deploy** | GitHub Pages, Netlify |

---

## ðŸ“„ Licencia

Este proyecto estÃ¡ bajo la licencia MIT.  
**Desarrollador:** Feibert GuzmÃ¡n  
*Proyecto implementado como evidencia para la plataforma +EDU.*
