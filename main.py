import random

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from sympy.printing.pretty.pretty_symbology import line_width
from sympy.printing.tree import print_node

import account
import openpyxl

fig_width = 2.5
fig_height = 1.2
line_width = 0.5
marker_size = 1.5
label_size = 5
tick_size = 4

huisstijl_kleur1 = "#EFEFE8"
huisstijl_kleur2 = "#375635"
huisstijl_kleur3 = "#449C41"
huisstijl_kleur4 = "#1B1B1B"

company = account.Account("DataReach")

# --- Instellingen voor de pagina ---
st.set_page_config(page_title="Dashboard", layout="wide")




# HOW TO RUN THIS STREAMLIT APP:
# -> TERMINAL:

# python -m streamlit run main.py




# --- Titel en Intro ---
#st.write("Dit dashboard toont willekeurige data in verschillende grafieken.")

# --- Genereren van Willekeurige Data ---
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.sidebar.header("NAVIGATION")

st.sidebar.markdown(f"""
    <style>
        div.stButton > button {{
            width: 100%;
            text-align: left;
            padding-left: 5px;
            display: flex;
            justify-content: flex-start;
            color: {huisstijl_kleur1} !important;
            background-color: {huisstijl_kleur2} !important;
            border: none;
        }}
        /* TO FIX TEXT TO THE BOTTOM */
        .sidebar-footer {{
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%
            padding: 10px;
            color: {huisstijl_kleur1}
            background-color: {huisstijl_kleur2};
            text-align: left;
            font-size: 14px;
        }}
    </style>
    <div class="sidebar-footer">
        <p><b>CONTACT US:</b><br>
        ➤ <b>LinkedIn:</b> <a href='https://www.linkedin.com/company/datareachbv/about/' target='_blank' style='color: {huisstijl_kleur1}; text-decoration: none;'>DataReach</a><br>
        ➤ <b>Email:</b> <a href='mailto:datareachbv@gmail.com' style='color: {huisstijl_kleur1}; text-decoration: none;'>datareachbv@gmail.com</a><br>
        © 2025 DataReach</p>
    </div>
    """, unsafe_allow_html=True)
if st.sidebar.button("🏠 HOME"):
    st.session_state.page = "Home"
if st.sidebar.button("📊 DASHBOARD"):
    st.session_state.page = "Dashboard"
if st.sidebar.button("\U00002754 SUPPORT"):
    st.session_state.page = "Support"

if st.session_state.page == "Home":
    st.title("About Us")
    st.write("Welcome to the Home Page! 🏠")

elif st.session_state.page == "Dashboard":
    upload_file = pd.read_excel(io="D:\\User\\Mateo\\Unif\\S6\\56-The_Company\\DataReach_Dashboard\\fictieve_data.xlsx", engine="openpyxl",usecols="A:H",nrows=35)
    verbruik1 = upload_file["component 1 - industrial motor"]
    harmonische1 = upload_file["harmonische 1"]
    verbruik2 = upload_file["component2 - HVAC"]
    harmonische2 = upload_file["harmonische 2"]
    verbruik3 = upload_file["component 3 - water pump"]
    harmonische3 = upload_file["harmonische 3"]
    verbruik4 = upload_file["component 4 - compressor"]
    harmonische4 = upload_file["harmonische 4"]
    time = range(1,35)
    Hz = range(0,1200,100)

    #df = pd.read_excel(uploaded_file, engine="openpyxl")
    st.title("Energy Dashboard - " + str(company.get_name()))
    for title1, data1, title2, data2 in [
        ("Consumption-Industrial motor 1", verbruik1, "Harmonic wave-Industrial motor 1", harmonische1),
        ("Consumption-HVAC unit 1", verbruik2, "Harmonic wave-HVAC unit 1", harmonische2),
        ("Consumption-water pump 1", verbruik3, "Harmonic wave-water pump 1", harmonische3),
        ("Consumption-compressor 1", verbruik4, "Harmonic wave-compressor 1", harmonische4),
    ]:
        col1, col2 = st.columns(2)  # Create a new row with two columns

        with col1:
            st.subheader(title1)
            st.markdown("<div style='padding-top: 55px;'></div>", unsafe_allow_html=True)
            fig, ax = plt.subplots(figsize=(fig_width,fig_height))
            fig.patch.set_facecolor(huisstijl_kleur1)
            ax.set_facecolor(huisstijl_kleur1)
            ax.plot(time, data1, marker='o', linestyle='-', color='b', linewidth=line_width, markersize=marker_size)
            ax.set_xlabel("time[min]",fontsize=label_size)
            ax.set_ylabel("Consumption[kW]",fontsize=label_size)
            ax.tick_params(axis="both", labelsize=tick_size)
            st.pyplot(fig)

        with col2:
            st.subheader(title2)
            data_edited = []
            for data in data2:
                if (str(data) != "nan"):
                    data_edited.append(data)

            df_bar = pd.DataFrame({
                "Frequentie [Hz]": Hz,
                "Amplitude": data_edited
            })

            # --- Staafdiagram met Plotly ---
            fig_bar = px.bar(df_bar, x="Frequentie [Hz]", y="Amplitude"  )
            fig_bar.update_layout(
                height=350,
                plot_bgcolor=huisstijl_kleur1,
                paper_bgcolor=huisstijl_kleur1
            )
            st.plotly_chart(fig_bar)

    # # --- Lijn Diagram ---
    # st.subheader("📈 Lijngrafiek van Waarde1 over de tijd")
    # fig, ax = plt.subplots()
    # ax.plot(data["Datum"], data["Waarde1"], marker='o', linestyle='-', color='b')
    # ax.set_xlabel("Datum")
    # ax.set_ylabel("Waarde1")
    # st.pyplot(fig)
    #
    # # --- Staafdiagram met Plotly ---
    # st.subheader("📊 Staafdiagram per Categorie")
    # fig_bar = px.bar(data, x="Categorie", y="Waarde2", color="Categorie", title="Totale Waarde2 per Categorie")
    # st.plotly_chart(fig_bar)
    #
    # # --- Scatterplot ---
    # st.subheader("🔵 Scatterplot van Waarde1 vs Waarde2")
    # fig_scatter = px.scatter(data, x="Waarde1", y="Waarde2", color="Categorie", title="Waarde1 vs Waarde2")
    # st.plotly_chart(fig_scatter)
    #
    # # --- Data Tabel ---
    # st.subheader("📋 Data Tabel")
    # st.dataframe(data)


elif st.session_state.page == "Support":
    st.title("Support")
    st.write("Welcome to the Support Page! \U00002754")


st.markdown(f"""
    <style>
        /* Change Main Panel Background */
        [data-testid="stAppViewContainer"] {{
            background-color: {huisstijl_kleur1} !important;
        }}
        
        /* Change Sidebar Background */
        [data-testid="stSidebar"] {{
            background-color: {huisstijl_kleur2} !important;
        }}
        
        /* Change Sidebar Header Color */
        [data-testid="stSidebar"] {{
            color: {huisstijl_kleur1} !important;
        }}
    </style>
    """, unsafe_allow_html=True)


