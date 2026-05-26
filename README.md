# British Airways - Data Science Analytics

Proyecto desarrollado para el programa de simulacion de Data Science de Forage - British Airways.
Abarca dos tareas completas siguiendo la metodologia CRISP-ML y el ciclo de vida del desarrollo de software (SDLC).

## Tecnologias

Python, Pandas, Scikit-Learn, Streamlit, Plotly, Jupyter, HTML5, GitHub Pages

## Task 1: Lounge Eligibility Model

Estimar la demanda en las salas VIP (Lounges) de la Terminal 3 de Heathrow mediante un modelo de agrupamiento estrategico basado en HAUL (alcance de ruta) y TIME_OF_DAY (momento del dia).

**Archivos clave:**
- `app.py` - Dashboard en Streamlit (Task 1)
- `index.html` - Landing page corporativa
- `data/Filled_Lounge_Eligibility_Lookup.xlsx` - Reporte generado

## Task 2: Predictive Modeling - Booking Completion

Construir un modelo de clasificacion binaria que prediga si un cliente completara su reserva (booking_complete) utilizando el dataset customer_booking.csv (50,000 registros, 14 columnas).

### Metodologia CRISP-ML

| Fase | Descripcion |
|------|-------------|
| 1. Business Understanding | Definir problema de negocio y objetivos |
| 2. Data Understanding | EDA completo con visualizaciones |
| 3. Data Preparation | Limpieza, transformacion y feature engineering |
| 4. Modeling | Entrenamiento de 3 modelos con SMOTE |
| 5. Evaluation | Comparacion de metricas y seleccion |
| 6. Deployment | Dashboard, notebook y landing page |

### Resultados de Modelos

| Modelo | Accuracy | Precision | Recall | F1-Score | AUC-ROC |
|--------|----------|-----------|--------|----------|---------|
| Logistic Regression + SMOTE | 0.7250 | 0.2850 | 0.6100 | 0.3880 | 0.7100 |
| Random Forest + SMOTE | 0.8020 | 0.4200 | 0.5200 | 0.4650 | 0.7850 |
| Gradient Boosting + SMOTE | 0.7850 | 0.3800 | 0.4900 | 0.4280 | 0.7620 |

### Archivos clave Task 2

- `etl_pipeline.py` - Pipeline ETL completo
- `customer_booking_analysis.ipynb` - Notebook predictivo completo
- `generate_report.py` - Genera imagenes EDA
- `generate_pptx.py` - Genera presentacion PowerPoint
- `docs/reporte_integral.html` - Reporte completo navegable
- `docs/British_Airways_Task2_Predictive_Modeling.pptx` - Presentacion

## Estructura del repositorio

```
BritishAirways/
├── app.py
├── index.html
├── etl_pipeline.py
├── customer_booking_analysis.ipynb
├── generate_report.py
├── generate_pptx.py
├── requirements.txt
├── data/
│   ├── customer_booking.csv
│   └── Filled_Lounge_Eligibility_Lookup.xlsx
├── docs/
│   ├── reporte_integral.html
│   ├── British_Airways_Task2_Predictive_Modeling.pptx
│   └── *.png (12 imagenes)
└── assets/
    └── hero_bg.png
```

## Instalacion y uso

```bash
git clone https://github.com/ErikSantiago-G/Data-Science-Job-Simulation-.git
cd Data-Science-Job-Simulation-

python -m venv .venv
.venv\Scripts\activate     # Windows

pip install -r requirements.txt

python etl_pipeline.py     # ETL
python generate_report.py  # Imagenes
python generate_pptx.py    # PowerPoint
streamlit run app.py       # Dashboard
jupyter notebook customer_booking_analysis.ipynb  # Notebook
```

**Desarrollador:** Erik Santiago Garcia Gonzalez
