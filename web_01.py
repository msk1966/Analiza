# file: app.py
import streamlit as st
import matplotlib.pyplot as plt

# --- Konfiguracija lozinke ---
PASSWORD = "tajna123"

# --- Unos lozinke ---
st.title("📊 Privatna Analiza")
password_input = st.text_input("Unesi lozinku za pristup:", type="password")

if password_input != PASSWORD:
    st.warning("⛔ Neispravna lozinka ili pristup nije odobren.")
    st.stop()

# --- Ako je lozinka točna ---
st.success("✅ Uspješna autentikacija!")
st.header("Rezultati analize")

# --- Prikaz teksta ---
st.write("Ovdje se prikazuje neki rezultat analize u tekstualnom obliku.")

# --- Prikaz grafikona ---
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]

fig, ax = plt.subplots()
ax.plot(x, y, marker='o')
ax.set_title("Kvadratna funkcija")
ax.set_xlabel("X")
ax.set_ylabel("Y = X^2")

st.pyplot(fig)
