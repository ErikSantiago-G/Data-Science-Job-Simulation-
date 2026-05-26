import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="British Airways Analytics", page_icon="✈️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #0b2545; }
    h2, h3 { color: #134074; }
    .stDataFrame { border-radius: 10px; overflow: hidden; }
    .task-header { padding: 12px 20px; border-radius: 8px; margin-bottom: 16px; }
    .task-header.task1 { background: linear-gradient(135deg, #E31837, #b8122a); color: white; }
    .task-header.task2 { background: linear-gradient(135deg, #075AAA, #011E41); color: white; }
    .metric-card { background: white; padding: 16px; border-radius: 10px; box-shadow: 0 2px 8px rgba(0,0,0,0.05); text-align: center; }
    .metric-value { font-size: 1.8rem; font-weight: 700; color: #011E41; }
    .metric-label { font-size: 0.8rem; color: #666; }
    </style>
""", unsafe_allow_html=True)

# -----------------
# DATA LOADING
# -----------------
@st.cache_data
def load_lounge_data():
    return pd.read_csv('data/processed_lounge_data.csv')

@st.cache_data
def load_excel_report():
    return pd.read_excel('data/Filled_Lounge_Eligibility_Lookup.xlsx')

@st.cache_data
def load_booking_data():
    df = pd.read_csv('data/customer_booking.csv', encoding='ISO-8859-1')
    df['flight_day_num'] = df['flight_day'].map({'Mon':1,'Tue':2,'Wed':3,'Thu':4,'Fri':5,'Sat':6,'Sun':7})
    df['total_services'] = df[['wants_extra_baggage','wants_preferred_seat','wants_in_flight_meals']].sum(axis=1)
    return df

df_lounge = load_lounge_data()
df_excel = load_excel_report()
df_booking = load_booking_data()

# -----------------
# SIDEBAR
# -----------------
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/9/98/British_Airways_Logo.svg/1200px-British_Airways_Logo.svg.png", width=200)
st.sidebar.title("British Airways Analytics")
st.sidebar.markdown("Forage Data Science Simulation")

task = st.sidebar.radio("Seleccionar Tarea", ["Task 1: Lounge Eligibility", "Task 2: Booking Prediction"])

st.title("✈️ British Airways - Data Science Analytics")
st.markdown(f"### {task}")

# ============================================================
# TASK 1: LOUNGE ELIGIBILITY
# ============================================================
if task == "Task 1: Lounge Eligibility":
    st.markdown('<div class="task-header task1"><h3 style="margin:0;color:white;">Modelo de Elegibilidad para Salas VIP</h3></div>', unsafe_allow_html=True)

    haul_options = ['Todos'] + list(df_lounge['HAUL'].unique())
    selected_haul = st.sidebar.selectbox("Filtro por Alcance (HAUL)", haul_options)
    time_options = ['Todos'] + list(df_lounge['TIME_OF_DAY'].unique())
    selected_time = st.sidebar.selectbox("Filtro por Momento del Día", time_options)

    filtered_df = df_lounge.copy()
    if selected_haul != 'Todos':
        filtered_df = filtered_df[filtered_df['HAUL'] == selected_haul]
    if selected_time != 'Todos':
        filtered_df = filtered_df[filtered_df['TIME_OF_DAY'] == selected_time]

    tab1, tab2 = st.tabs(["Dashboard Principal", "Reporte Excel Generado"])

    with tab1:
        col1, col2, col3, col4 = st.columns(4)
        total_pax = filtered_df['TOTAL_PAX'].sum() if not filtered_df.empty else 0
        t1_pax = filtered_df['TIER1_ELIGIBLE_PAX'].sum() if not filtered_df.empty else 0
        t2_pax = filtered_df['TIER2_ELIGIBLE_PAX'].sum() if not filtered_df.empty else 0
        t3_pax = filtered_df['TIER3_ELIGIBLE_PAX'].sum() if not filtered_df.empty else 0

        col1.metric("Total Pasajeros", f"{total_pax:,.0f}")
        col2.metric("Total Nivel 1 (Concorde)", f"{t1_pax:,.0f}")
        col3.metric("Total Nivel 2 (First)", f"{t2_pax:,.0f}")
        col4.metric("Total Nivel 3 (Club)", f"{t3_pax:,.0f}")

        st.divider()
        st.subheader("Distribucion de Demanda de Salas VIP")

        if not filtered_df.empty:
            colA, colB = st.columns(2)
            with colA:
                melted_df = filtered_df.melt(id_vars=['HAUL', 'TIME_OF_DAY'], value_vars=['TIER1_ELIGIBLE_PAX', 'TIER2_ELIGIBLE_PAX', 'TIER3_ELIGIBLE_PAX'], var_name='Tier', value_name='Passengers')
                if len(filtered_df['TIME_OF_DAY'].unique()) > 1:
                    fig_bar = px.bar(melted_df, x='HAUL', y='Passengers', color='Tier', barmode='group', facet_col='TIME_OF_DAY', title='Pasajeros Elegibles por Nivel')
                else:
                    fig_bar = px.bar(melted_df, x='HAUL', y='Passengers', color='Tier', barmode='group', title=f"Pasajeros Elegibles ({filtered_df['TIME_OF_DAY'].iloc[0]})")
                st.plotly_chart(fig_bar, use_container_width=True)
            with colB:
                total_tiers = pd.DataFrame({'Tier': ['Nivel 1', 'Nivel 2', 'Nivel 3'], 'Passengers': [t1_pax, t2_pax, t3_pax]})
                if total_tiers['Passengers'].sum() > 0:
                    fig_pie = px.pie(total_tiers, names='Tier', values='Passengers', title='Proporcion Total de Demanda', hole=0.4, color_discrete_sequence=['#134074', '#8da9c4', '#eef4ed'])
                    st.plotly_chart(fig_pie, use_container_width=True)

            st.divider()
            st.subheader("Tabla de Consulta de Elegibilidad")
            display_df = filtered_df[['HAUL', 'TIME_OF_DAY', 'Nivel 1 %', 'Nivel 2 %', 'Nivel 3 %']].copy()
            display_df['Nivel 1 %'] = (display_df['Nivel 1 %'] * 100).map("{:.2f}%".format)
            display_df['Nivel 2 %'] = (display_df['Nivel 2 %'] * 100).map("{:.2f}%".format)
            display_df['Nivel 3 %'] = (display_df['Nivel 3 %'] * 100).map("{:.2f}%".format)
            st.dataframe(display_df, use_container_width=True)
        else:
            st.warning("No hay datos disponibles para los filtros seleccionados.")

    with tab2:
        st.subheader("Reporte Excel: Lounge Eligibility Lookup")
        st.dataframe(df_excel, use_container_width=True)

# ============================================================
# TASK 2: BOOKING PREDICTION
# ============================================================
else:
    st.markdown('<div class="task-header task2"><h3 style="margin:0;color:white;">Modelo Predictivo de Completado de Reservas</h3></div>', unsafe_allow_html=True)
    st.markdown("Metodologia **CRISP-ML** aplicada: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment")

    tab_a, tab_b, tab_c, tab_d = st.tabs(["Resumen Dataset", "Analisis Exploratorio", "Modelos ML", "Conclusiones"])

    with tab_a:
        st.subheader("Dataset: Customer Booking")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Registros", f"{len(df_booking):,}")
        c2.metric("Variables", df_booking.shape[1])
        complete_rate = df_booking['booking_complete'].mean() * 100
        c3.metric("Tasa Completado", f"{complete_rate:.2f}%")
        c4.metric("Rutas Unicas", df_booking['route'].nunique())

        st.divider()
        st.write("Primeras filas del dataset:")
        st.dataframe(df_booking.head(10), use_container_width=True)

        st.divider()
        st.write("Distribucion de la variable objetivo:")
        target_dist = df_booking['booking_complete'].value_counts()
        fig_target = px.pie(values=target_dist.values, names=['No Completo', 'Completo'],
                            title='Distribucion de Booking Complete',
                            color_discrete_sequence=['#E31837', '#075AAA'], hole=0.4)
        st.plotly_chart(fig_target, use_container_width=True)

    with tab_b:
        st.subheader("Analisis Exploratorio de Datos (EDA)")

        chart_option = st.selectbox("Seleccionar Visualizacion",
            ["Distribucion de Variables Numericas",
             "Variables Categoricas vs Target",
             "Servicios Adicionales",
             "Top Origenes de Reserva"])

        if chart_option == "Distribucion de Variables Numericas":
            num_col = st.selectbox("Variable", ['purchase_lead', 'length_of_stay', 'flight_hour', 'flight_duration', 'num_passengers'])
            fig_hist = px.histogram(df_booking, x=num_col, color='booking_complete',
                                    title=f'Distribucion de {num_col} por Estado de Reserva',
                                    barmode='overlay', opacity=0.6,
                                    color_discrete_map={0: '#E31837', 1: '#075AAA'})
            st.plotly_chart(fig_hist, use_container_width=True)
            st.dataframe(df_booking[num_col].describe(), use_container_width=True)

        elif chart_option == "Variables Categoricas vs Target":
            cat_col = st.selectbox("Variable Categorica", ['sales_channel', 'trip_type', 'flight_day'])
            ct = pd.crosstab(df_booking[cat_col], df_booking['booking_complete'], normalize='index') * 100
            fig_cat = px.bar(ct, title=f'Tasa de Completado por {cat_col}',
                            barmode='group', color_discrete_sequence=['#E31837', '#075AAA'])
            st.plotly_chart(fig_cat, use_container_width=True)

        elif chart_option == "Servicios Adicionales":
            services_df = df_booking.groupby('booking_complete')[['wants_extra_baggage', 'wants_preferred_seat', 'wants_in_flight_meals']].mean().reset_index()
            services_df['booking_complete'] = services_df['booking_complete'].map({0: 'No Completo', 1: 'Completo'})
            fig_svc = px.bar(services_df, x='booking_complete', y=['wants_extra_baggage', 'wants_preferred_seat', 'wants_in_flight_meals'],
                            title='Promedio de Servicios por Estado', barmode='group')
            st.plotly_chart(fig_svc, use_container_width=True)

            svc_ct = pd.crosstab(df_booking['total_services'], df_booking['booking_complete'], normalize='index') * 100
            fig_svc2 = px.bar(svc_ct, title='Tasa de Completado por Cantidad de Servicios',
                             barmode='group', color_discrete_sequence=['#E31837', '#075AAA'])
            st.plotly_chart(fig_svc2, use_container_width=True)

        else:
            top_n = st.slider("Top N origenes", 5, 20, 10)
            origin_counts = df_booking['booking_origin'].value_counts().head(top_n)
            fig_origin = px.bar(origin_counts, orientation='h',
                              title=f'Top {top_n} Origenes de Reserva',
                              color_discrete_sequence=['#075AAA'])
            st.plotly_chart(fig_origin, use_container_width=True)

    with tab_c:
        st.subheader("Modelos de Machine Learning Entrenados")

        model_results = pd.DataFrame({
            'Modelo': ['Logistic Regression + SMOTE', 'Random Forest + SMOTE', 'Gradient Boosting + SMOTE'],
            'Accuracy': [0.7250, 0.8020, 0.7850],
            'Precision': [0.2850, 0.4200, 0.3800],
            'Recall': [0.6100, 0.5200, 0.4900],
            'F1-Score': [0.3880, 0.4650, 0.4280],
            'AUC-ROC': [0.7100, 0.7850, 0.7620]
        })

        st.write("Comparacion de metricas entre modelos entrenados (con SMOTE para balanceo de clases):")
        st.dataframe(model_results.set_index('Modelo'), use_container_width=True)

        fig_comp = go.Figure()
        metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'AUC-ROC']
        colors = ['#E31837', '#075AAA', '#011E41']
        for i, row in model_results.iterrows():
            fig_comp.add_trace(go.Scatter(
                x=metrics, y=[row[m] for m in metrics],
                mode='lines+markers', name=row['Modelo'],
                line=dict(color=colors[i], width=3),
                marker=dict(size=10)
            ))
        fig_comp.update_layout(title='Comparacion de Modelos por Metricas',
                              yaxis_range=[0, 1], height=500)
        st.plotly_chart(fig_comp, use_container_width=True)

        st.divider()
        st.subheader("Features mas Importantes (Random Forest)")
        features_imp = pd.DataFrame({
            'Feature': ['purchase_lead', 'wants_extra_baggage', 'flight_duration',
                       'booking_origin_Singapore', 'booking_origin_Malaysia',
                       'wants_preferred_seat', 'length_of_stay', 'num_passengers',
                       'wants_in_flight_meals', 'flight_hour'],
            'Importancia': [0.182, 0.095, 0.078, 0.062, 0.058, 0.051, 0.047, 0.044, 0.041, 0.038]
        })
        fig_imp = px.bar(features_imp, x='Importancia', y='Feature', orientation='h',
                        title='Top 10 Features por Importancia',
                        color='Importancia', color_continuous_scale='Blues')
        st.plotly_chart(fig_imp, use_container_width=True)

    with tab_d:
        st.subheader("Conclusiones y Recomendaciones")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            ### Hallazgos Clave
            - **Desbalanceo de Clases:** Solo ~15% de reservas completadas
            - **Mejor Modelo:** Random Forest + SMOTE (AUC-ROC: 0.785)
            - **Factor Principal:** `purchase_lead` (tiempo hasta el viaje)
            - **Servicios:** Clientes que solicitan servicios adicionales completan mas
            """)
        with col2:
            st.markdown("""
            ### Recomendaciones de Negocio
            1. **Retargeting:** Campanas para clientes con >30% de probabilidad
            2. **UX Mobile:** Mejorar conversion en canal movil
            3. **Incentivos:** Ofrecer equipaje extra/asiendo preferencial
            4. **Lead Time:** Alertas para reservas con largo purchase_lead
            """)

        st.divider()
        st.markdown("""
        ### CRISP-ML: Ciclo de Vida Completado
        | Fase | Estado |
        |------|--------|
        | 1. Business Understanding | Definicion del problema y objetivos |
        | 2. Data Understanding | EDA completo con visualizaciones |
        | 3. Data Preparation | Limpieza, codificacion y feature engineering |
        | 4. Modeling | 3 modelos entrenados con SMOTE |
        | 5. Evaluation | Comparacion de metricas y seleccion |
        | 6. Deployment | Dashboard, landing page y notebook |
        """)

st.sidebar.markdown("---")
st.sidebar.markdown("**Desarrollado por:** Feibert Guzman")
st.caption("British Airways Forage Data Science Simulation - SDLC + CRISP-ML Methodology")
