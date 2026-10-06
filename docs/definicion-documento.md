## Definición de documento

En este MVP, un documento representa una evidencia o conjunto de evidencias que el despacho espera recibir de un cliente para un periodo mensual.

Un documento no es todavía un archivo almacenado por el sistema. Es un registro de seguimiento dentro de una checklist.

Cada documento esperado debe tener como mínimo:

- Cliente al que pertenece.
- Periodo mensual al que corresponde.
- Tipo de documento.
- Estado de seguimiento: `pendiente` o `recibido`.
- Cuenta bancaria asociada, solo cuando el tipo sea `estado_de_cuenta_bancario`.
- Fecha en que el despacho registró la recepción, cuando aplique.
- Observación opcional.

Acciones permitidas en esta primera versión:

- Crear una solicitud documental.
- Consultar solicitudes por cliente y periodo.
- Consultar solicitudes por estado.
- Marcar una solicitud como `recibido`.
- Agregar o actualizar una observación.
