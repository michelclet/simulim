import streamlit as st
from immo_functions import simulation_resultat
from immo_functions import mensualite_resultat
from immo_functions import interet_resultat
from immo_functions import capital_resultat
from immo_functions import capacite_resultat

st.title("Ma capacité d'emprunt")

taux = st.number_input("Taux d'emprunt [%]", value=4.00)
duree = st.number_input("Durée du prêt (années) [€]", value=25)
apport = st.number_input("Apport personnel [€]", value=60000)
revenus = st.number_input("Revenus mensuels (net avant impôts) [€]", value=2500)
endettement = st.number_input("Taux d'endettement (max 35%) [%]", value=33)
assurance = 50
credit = 0

output = capacite_resultat(taux, duree, apport, assurance, revenus, credit, endettement)
st.text("Prix du bien " + str(output['bien']) + " €")
st.text("Mensualités " + str(output['mensualite']) + " €")
st.text("Frais de notaire " + str(output['notaire']) + " €")
st.text("Frais de dossier " + str(output['dossier']) + " €")
st.text("Frais de garantie " + str(output['garantie']) + " €")
st.text("Montant du prêt " + str(output['pret']) + " €")
st.text("Coût des intérêts du prêt " + str(output['interets']) + " €")
