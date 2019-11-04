Parte 2

1a) Se puede utlizar aws glue etl jobs para importar la informacion desde s3 a redshift (permite mapear un json a una tabla redshift)
referencia: https://medium.com/@ly.lee/transform-and-import-a-json-file-into-amazon-redshift-with-aws-glue-3371006e03ca


Parte 3
a) Los crontab y Los deamons de linux

b)Con un contrab con un comando parecido al siguiente:
*/1 * * * * /home/run.sh > /home/runup.log 2>&1

La primera flecha indica que el stdout va a ir hacia el file .log y 
la segunda flecha indica que el stderr tambien va a ir a ese archivo .log

c) aws s3 cp SOURCE_DIR s3://DEST_BUCKET/ --recursive


d) s3 glacier parece una buena alternativa siempre y cuando lo datos 
no tengan que ser consultados exhaustivamente.