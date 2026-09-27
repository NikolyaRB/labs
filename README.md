# About this project

This is a simple CLI program on Python.

It can calculate expressions and convert units.

## How to use

Calculator:

```bash
python -m toolkit calc "2 + 3 * 4"
```

Converter:

```bash
python -m toolkit convert 100 --from cm --to m
```

Help:

```bash
python -m toolkit --help
```

## Converter

Supported units:

Length: `mm`, `cm`, `m`, `km`
Mass: `g`, `kg`
Temperature: `c`, `f`, `k`

Conversion data is stored in `conversions.json`.

## Calculator

Calculator supports `+`, `-`, `*`, `/`, integer and float numbers.
