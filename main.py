import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import account

huisstijl_kleur1 = "#EFEFE8"
huisstijl_kleur2 = "#375635"
huisstijl_kleur3 = "#449C41"
huisstijl_kleur4 = "#1B1B1B"

company = account.Account("DataReach")

# --- Instellingen voor de pagina ---
st.set_page_config(page_title="Dashboard", layout="wide")

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
        ➤ <b>Email:</b> <a href='mailto:DataReach@gmail.com' style='color: {huisstijl_kleur1}; text-decoration: none;'>datareach@gmail.com</a><br>
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
    st.title("Energy Dashboard - " + str(company.get_name()))

    num_rows = st.sidebar.slider("Aantal datapunten", 10, 500, 100)

    data = pd.DataFrame({
        "Datum": pd.date_range(start="2024-01-01", periods=num_rows, freq='D'),
        "Categorie": np.random.choice(["A", "B", "C", "D"], num_rows),
        "Waarde1": np.random.randint(10, 100, num_rows),
        "Waarde2": np.random.randint(100, 1000, num_rows)
    })

    # --- Lijn Diagram ---
    st.subheader("📈 Lijngrafiek van Waarde1 over de tijd")
    fig, ax = plt.subplots()
    ax.plot(data["Datum"], data["Waarde1"], marker='o', linestyle='-', color='b')
    ax.set_xlabel("Datum")
    ax.set_ylabel("Waarde1")
    st.pyplot(fig)

    # --- Staafdiagram met Plotly ---
    st.subheader("📊 Staafdiagram per Categorie")
    fig_bar = px.bar(data, x="Categorie", y="Waarde2", color="Categorie", title="Totale Waarde2 per Categorie")
    st.plotly_chart(fig_bar)

    # --- Scatterplot ---
    st.subheader("🔵 Scatterplot van Waarde1 vs Waarde2")
    fig_scatter = px.scatter(data, x="Waarde1", y="Waarde2", color="Categorie", title="Waarde1 vs Waarde2")
    st.plotly_chart(fig_scatter)

    # --- Data Tabel ---
    st.subheader("📋 Data Tabel")
    st.dataframe(data)


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


