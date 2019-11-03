select Fecha, Descripción_de_Cliente, sum(ultimas_operaciones.ventas) as ventas from
(
	select Fecha, Descripción_de_Cliente, dmt.venta as ventas from 
		Data_Movimientos_Totales as dmt
	where Descripción_de_Cliente = '<:some_description>'
	where TRUNC(Fecha) <= TO_DATE('<:your_date>', 'YYYY-MM-DD')
	order by Fecha
	limit 7


) as ultimas_operaciones
group by Descripción_de_Cliente;