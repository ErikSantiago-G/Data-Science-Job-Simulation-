"""
etl_pipeline.py - ETL Pipeline para Task 2: Predictive Modeling
Metodologia: CRISP-ML (Cross-Industry Standard Process for Machine Learning)
=========================================================
Fases: Business Understanding -> Data Understanding -> Data Preparation -> Modeling -> Evaluation -> Deployment
"""

import pandas as pd
import numpy as np
import os
import warnings
warnings.filterwarnings('ignore')

RAW_DATA_PATH = 'data/customer_booking.csv'
PROCESSED_DATA_PATH = 'data/processed_booking_data.csv'
ENCODED_DATA_PATH = 'data/encoded_booking_data.csv'
REPORTS_DIR = 'docs'

os.makedirs(REPORTS_DIR, exist_ok=True)

# ============================================================
# FASE 1: BUSINESS UNDERSTANDING (Comprension del Negocio)
# ============================================================
print("=" * 70)
print("CRISP-ML FASE 1: BUSINESS UNDERSTANDING")
print("=" * 70)
print("Objetivo: Predecir si un cliente completara una reserva (booking_complete)")
print("Variable objetivo: booking_complete (0 = No completo, 1 = Completo)")
print("Problema: Clasificacion binaria")
print("Metricas objetivo: Precision, Recall, F1-Score, AUC-ROC")
print("")

# ============================================================
# FASE 2: DATA UNDERSTANDING (Comprension de los Datos)
# ============================================================
print("=" * 70)
print("CRISP-ML FASE 2: DATA UNDERSTANDING")
print("=" * 70)

df = pd.read_csv(RAW_DATA_PATH, encoding='ISO-8859-1')
print(f"Dimensiones del dataset: {df.shape}")
print(f"Columnas: {list(df.columns)}")
print(f"Tipos de datos:\n{df.dtypes}")

print(f"\nValores nulos por columna:\n{df.isnull().sum()}")
print(f"\nEstadisticas descriptivas:\n{df.describe()}")

target_dist = df['booking_complete'].value_counts(normalize=True)
print(f"\nDistribucion de variable objetivo:\n{target_dist}")
print(f"Clase 0 (No completo): {target_dist[0]*100:.2f}%")
print(f"Clase 1 (Completo): {target_dist[1]*100:.2f}%")
print(f"Desbalanceo detectado: {(target_dist[0]/target_dist[1]):.2f}x mas clase 0")
print("")

# ============================================================
# FASE 3: DATA PREPARATION (Preparacion de Datos)
# ============================================================
print("=" * 70)
print("CRISP-ML FASE 3: DATA PREPARATION")
print("=" * 70)

df_clean = df.copy()

# 3.1 Feature Engineering basico
df_clean['is_weekend'] = df_clean['flight_day'].isin(['Sat', 'Sun']).astype(int)

mapping = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 7}
df_clean['flight_day_num'] = df_clean['flight_day'].map(mapping)

df_clean['purchase_lead_binned'] = pd.cut(df_clean['purchase_lead'],
    bins=[-1, 7, 30, 90, 180, 1000],
    labels=['0-7d', '8-30d', '31-90d', '91-180d', '180d+'])

df_clean['length_of_stay_binned'] = pd.cut(df_clean['length_of_stay'],
    bins=[-1, 3, 7, 14, 30, 1000],
    labels=['0-3d', '4-7d', '8-14d', '15-30d', '30d+'])

df_clean['flight_hour_binned'] = pd.cut(df_clean['flight_hour'],
    bins=[-1, 5, 11, 17, 24],
    labels=['Madrugada', 'Manana', 'Tarde', 'Noche'])

df_clean['route_prefix'] = df_clean['route'].str[:3]

df_clean['total_services'] = (df_clean['wants_extra_baggage'] +
                               df_clean['wants_preferred_seat'] +
                               df_clean['wants_in_flight_meals'])

df_clean['has_premium_services'] = (df_clean['total_services'] >= 2).astype(int)

# 3.2 Manejo de outliers en purchase_lead
q99 = df_clean['purchase_lead'].quantile(0.99)
df_clean['purchase_lead_clipped'] = df_clean['purchase_lead'].clip(upper=q99)

# 3.3 One-hot encoding para variables categoricas
categorical_cols = ['sales_channel', 'trip_type', 'flight_day',
                    'purchase_lead_binned', 'length_of_stay_binned',
                    'flight_hour_binned']

df_encoded = pd.get_dummies(df_clean, columns=categorical_cols, drop_first=True)

# 3.4 Separar features y target
target_col = 'booking_complete'
feature_cols = [c for c in df_encoded.columns if c != target_col]

X = df_encoded[feature_cols]
y = df_encoded[target_col]

# 3.5 Guardar datos procesados
df_clean.to_csv(PROCESSED_DATA_PATH, index=False)
print(f"Datos procesados guardados en: {PROCESSED_DATA_PATH}")

df_encoded.to_csv(ENCODED_DATA_PATH, index=False)
print(f"Datos codificados guardados en: {ENCODED_DATA_PATH}")
print(f"Features finales: {len(feature_cols)}")
print(f"Shape procesado: {df_encoded.shape}")
print("")

# ============================================================
# RESUMEN DEL PIPELINE
# ============================================================
print("=" * 70)
print("ETL PIPELINE COMPLETADO EXITOSAMENTE")
print("=" * 70)
print(f"Registros originales: {len(df)}")
print(f"Registros procesados: {len(df_clean)}")
print(f"Features generadas: {len(feature_cols)}")
print(f"Variables categoricas codificadas: {len(categorical_cols)}")
print(f"Valores nulos despues de transformacion: {df_encoded.isnull().sum().sum()}")
print("\nSiguiente paso: Ejecutar customer_booking_analysis.ipynb para modelado predictivo")
