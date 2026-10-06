# Alcance inicial del MVP

## Propósito

Construir una API para que un despacho contable lleve control interno de los documentos que espera recibir de cada cliente durante un periodo mensual.

El objetivo es reducir el seguimiento manual disperso en correos, mensajes y carpetas, y permitir identificar rápidamente qué documentos ya fueron recibidos y cuáles siguen pendientes.

## Usuario principal

Personal administrativo o contable de un despacho que necesita dar seguimiento a la documentación mensual de varios clientes.

## Problema que resuelve

Un despacho puede atender varios clientes y cada cliente debe entregar distintos documentos cada mes.

Sin una lista centralizada, los documentos pueden mezclarse entre clientes, asociarse al periodo incorrecto o requerir seguimiento manual para saber qué falta.

## Alcance incluido

La primera versión permitirá:

- Registrar clientes.
- Registrar cuentas bancarias asociadas a un cliente.
- Definir los tipos de documentos esperados por cada cliente.
- Crear una checklist mensual de documentos esperados por cliente.
- Considerar un estado de cuenta por cada cuenta bancaria registrada.
- Consultar la checklist de un cliente para un periodo específico.
- Marcar una solicitud documental como `recibida`.
- Consultar solicitudes documentales `pendientes` y `recibidas`.

## Regla principal

Cada solicitud documental debe estar asociada a:

- Un cliente.
- Un periodo mensual.
- Un tipo de documento.
- Una cuenta bancaria, cuando aplique.
- Un estado de seguimiento.

## Estados iniciales

Para limitar el alcance, la primera versión manejará únicamente:

- `pendiente`: el documento se espera, pero aún no se ha registrado su recepción.
- `recibido`: el despacho registró que cuenta con el documento o evidencia correspondiente.

El sistema podrá identificar documentos faltantes al consultar las solicitudes que permanezcan en estado `pendiente`.

## Fuera de alcance

Esta versión no incluirá:

- Carga, almacenamiento o descarga de archivos.
- Lectura de XML, PDF, imágenes o archivos bancarios.
- Extracción automática de datos.
- Validación fiscal o contable de documentos.
- Estados `validado` o `rechazado`.
- Clasificación automática mediante IA.
- Conciliación bancaria.
- Cálculo de impuestos.
- Envío automático de recordatorios a clientes.
- Usuarios, autenticación, permisos o roles.
- Interfaz web o aplicación móvil.
- Integración con SAT, bancos, Odoo u otros sistemas externos.

## Supuestos iniciales

- El personal del despacho captura manualmente clientes, cuentas bancarias y tipos de documentos esperados.
- Un cliente puede tener cero, una o varias cuentas bancarias.
- Cada cliente puede requerir una lista distinta de documentos.
- Cada periodo corresponde a un mes y un año.
- Una solicitud marcada como `recibido` significa solamente que el despacho recibió evidencia documental; no significa que haya sido validada fiscal o contablemente.
- Las reglas detalladas de validación se definirán en una etapa posterior.

## Criterios de éxito del MVP

El MVP se considerará funcional si una persona puede:

1. Registrar al menos un cliente con dos cuentas bancarias.
2. Definir documentos esperados para ese cliente.
3. Generar la checklist de un periodo mensual.
4. Ver por separado los estados de cuenta requeridos para cada cuenta bancaria.
5. Marcar algunos elementos como `recibido`.
6. Consultar cuáles solicitudes permanecen `pendientes`.

## Decisiones pendientes

- Definir el catálogo inicial de tipos de documentos.
- Decidir si una checklist mensual se crea manualmente o se genera a partir de una plantilla.
- Definir los campos mínimos de una cuenta bancaria sin almacenar información sensible.
- Precisar los criterios para agregar posteriormente los estados `validado` y `rechazado`.
