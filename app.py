import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df = pd.read_csv("wooldridge.csv")
st.title("Salario con base a género, experiencia y educacióm")
tab1, tab2 = st.tabs(["Análisis Univariado","Análisis Bivariado"])

with tab1:
    fig, ax = plt.subplots(1,4, figsize = (10,4))
    ax[0].hist(df["wage"])
    ax[0].set_title("SALARIO")
    ax[1].hist(df["educ"])
    ax[1].set_title("EDUCACIÓN")
    ax[2].hist(df["exper"])
    ax[2].set_title("EXPERIENCIA")
    conteo = df["genero"].value_counts()
    ax[3].bar(conteo.index, conteo.values)
    ax[3].set_title("GÉNERO")
    fig.tight_layout()
    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(1,3, figsize = (10,4))
    sns.boxplot(x = "genero", y = "wage", data=df, ax=ax[0])
    ax[0].set_xlabel("Género")
    ax[0].set_ylabel("Salario")
    ax[0].set_title("SALARIO - GENERO")
    sns.scatterplot(x = "educ", y = "wage", data=df, ax=ax[1])
    ax[1].set_xlabel("Educación")
    ax[1].set_ylabel("Salario")
    ax[1].set_title("SALARIO - EDUCACIÓN")
    sns.scatterplot(x = "exper", y = "wage", data=df, ax=ax[2])
    ax[2].set_xlabel("Experiencia")
    ax[2].set_ylabel("Salario")
    ax[2].set_title("SALARIO - EXPERIENCIA")
    fig.tight_layout()
    st.pyplot(fig)
