while True:
    SEGUIDOR() #Corre el seguidor de línea
    while sa.distance() > 300: #Se encuentra con el objeto
       wait(10)
#Corrobora si la distancia a la que encontró el objeto sigue siendo la misma después de 10 milisegundos. Supongo que para mayor presición en el giro
    mi.run(-300)
    md.run(-300)
    wait(1000)
    mi.run(120)
    md.run(-120)
    wait(1000)
    #Hace marcha atrás 1 segundo y luego gira, siempre hacia atrás. Esta sería la parte en la que hace el giro y esquiva el obstáculo.