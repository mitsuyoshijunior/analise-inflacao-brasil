import extract
import transform
import queries

print("Pipeline iniciado")

extract.run()
transform.run()
queries.run()

print("Pipeline finalizado")