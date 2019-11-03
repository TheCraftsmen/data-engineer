create table if not exists Data_Movimientos_Totales (
	Fecha TIMESTAMP,
	Descripción_de_Cliente VARCHAR(255),
	Descripción_de_Proveedor VARCHAR(255), 
	Descripción_de_Producto VARCHAR(255),
	Descripcion_de_Marca VARCHAR(255),
	Cantidad INTEGER,
	Costo FLOAT,
	Venta FLOAT,
	Ganancia_Neta FLOAT
);