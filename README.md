# Asistente Documental para Despachos Contables

Proyecto de aprendizaje para construir un flujo profesional de desarrollo asistido por IA.

El sistema busca ayudar a un despacho contable a dar seguimiento a los documentos que debe recibir de cada cliente en cada periodo mensual, evitando pérdidas, cruces de información y seguimiento manual disperso.

## Problema

Un despacho contable atiende a varios clientes y, cada mes, debe solicitar y organizar documentos como:

- Estados de cuenta bancarios.
- Facturas.
- Comprobantes de pago.
- Otros documentos requeridos para el proceso contable.

Cuando esos documentos se gestionan mediante mensajes, correos o carpetas sin una checklist clara, es fácil no saber qué falta, a qué cliente pertenece un archivo o a qué periodo corresponde.

## Objetivo del MVP

Crear una API sencilla que permita administrar una checklist de documentos esperados por cliente y por periodo mensual.

La primera versión permitirá:

- Registrar clientes.
- Registrar cuentas bancarias asociadas a cada cliente.
- Definir documentos esperados para un cliente.
- Crear y consultar una checklist mensual de documentos.
- Registrar que un documento fue recibido.
- Consultar documentos pendientes o recibidos por cliente y periodo.

## Alcance inicial

El proyecto se enfoca únicamente en el seguimiento interno de recepción documental.

No incluirá todavía:

- Carga o almacenamiento real de archivos.
- Lectura automática de XML, PDF o imágenes.
- Validación fiscal de CFDI.
- Clasificación automática con inteligencia artificial.
- Conciliación bancaria.
- Cálculo de impuestos.
- Autenticación de usuarios.
- Interfaz web.

## Tecnologías previstas

- Python
- FastAPI
- SQLite
- SQLModel o SQLAlchemy
- pytest
- Git y GitHub
- GitHub Actions
- VS Code

## Estructura prevista

```text
asistente-documental-despacho/
├── docs/             # Requisitos, decisiones y notas de aprendizaje
├── app/              # Código de la aplicación
├── tests/            # Pruebas automatizadas
├── README.md
└── .gitignore
```

> La estructura podrá cambiar conforme avance el proyecto y se tomen decisiones técnicas documentadas.

## Estado del proyecto

En preparación. Actualmente se está definiendo el alcance, configurando el repositorio y estableciendo el flujo de trabajo.

## Objetivo de aprendizaje

Este proyecto forma parte del Mes 1 de una ruta de aprendizaje sobre desarrollo asistido por IA. El objetivo es practicar:

- Definición y control de alcance.
- Git, GitHub, ramas, commits y pull requests.
- Diseño a partir de requisitos y criterios de aceptación.
- Generación y revisión responsable de código con asistentes de IA.
- Pruebas automatizadas.
- Integración continua con GitHub Actions.

## Próximos pasos

1. Crear la documentación inicial del alcance.
2. Configurar el entorno de Python.
3. Crear el esqueleto de la API con FastAPI.
4. Diseñar el modelo de datos inicial.
5. Implementar pruebas automatizadas.
6. Configurar integración continua.
