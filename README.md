# exabyte-esse

Exabyte Source of Schemas and Examples.
Contains schemas and examples for materials and simulations related data in JSON representation. 
Can be used as a node or python module on server-side.

## Installation

Python:

```bash
cd <this repo dir>
virtualenv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

To ensure latest functionality, run `pip install --upgrade https://github.com/timurbazhirov/json_include/archive/master.zip`.

Node:
```bash
npm install
```

## Usage

To produce json files with no inclusion statements (python):

```bash
python compile.py
```

`-m` flag will minify json files.

To produce json array with all dereferenced schemas (javascript):

```bash
npm install
npm run-script run
```

compiled schemas and examples can be found inside `lib` directory.

## Tests

Run from root directory of this repository:

```bash
npm test
```

## Debugging

To view all compiled schemas:

```bash
PRINT_SCHEMAS=1 ./node_modules/babel-cli/bin/babel-node.js src/index.js
```

## Notes

- Do not use circular references in the schemas but instead leave the type as object and add explanation to description.
