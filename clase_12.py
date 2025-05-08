import wooldridge as wd
wase = wd.data("wage1")
wase.info()
datos = wase[["wage","educ","exper","female"]]
datos
datos["female"]=datos["female"].map({0: "Hombre", 1:"Mujer"})
datos
datos = datos.rename(columns={"female":"genero"})
datos.to_csv("wooldridge.csv", index=False)