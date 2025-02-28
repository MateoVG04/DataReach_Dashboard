import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import account

company = Account("company_A")

# --- Instellingen voor de pagina ---
st.set_page_config(page_title="Dashboard - "+str(company.get_name()), layout="wide")

# --- Titel en Intro ---
st.title("📊 Interactief Dashboard met Streamlit")
st.write("Dit dashboard toont willekeurige data in verschillende grafieken.")

# --- Genereren van Willekeurige Data ---
st.sidebar.header("Instellingen")
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
