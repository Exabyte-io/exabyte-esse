# ESSE

Exabyte Source of Schemas and Examples (ESSE) contains data formats and associated examples specifically designed for digital materials science [1](#links).

## Installation

ESSE can be used as a Node.js or Python package on the server side. Please note that schemas and examples are unavailable on the client side (JS).

### Python

ESSE can be install as a Python package either via PyPi or the repository as below.

#### PyPi

```bash
pip install esse
```

#### Repository

```bash
virtualenv .venv
source .venv/bin/activate
pip install -e PATH_TO_ESSE_REPOSITORY
```

### Node

ESSE can be installed as a Node.js package either via NPM or the repository as below.

#### NPM

```bash
npm install esse-js
```

#### Repository

Add `"esse-js": "file:PATH_TO_ESSE_REPOSITORY"` to `package.json`.

## Usage

ESSE contains separate but equivalent interfaces for Python and Javascript.
The package provides `ESSE` class that can be initialized and used as below.

### Python

```python
from esse import ESSE

es = ESSE()
schema = es.get_schema_by_id("material")
```

### Node

```javascript
import {ESSE} from "esse-js";

const es = new ESSE();
const schema = es.getSchemaById("material");
```

## Structure

ESSE contains 3 main directories, [schema](schema), [example](example) and [src](src) outlined below.

### Schema

The schema directory contains the schemas specifying the rules to structure data. A set of core schemas, outlined below, are defined to facilitate the schema modularity.

#### Primitive

[Primitive](schema/core/primitive) directory contains a set of custom primitives that extends default standard primitive types allowed by schema, such as String and Number.
Primitives are solely defined by the default primitives and can not be re-constructed from each other.

#### Abstract

[Abstract](schema/core/abstract) directory contains unit-less schemas that are constructed from default and custom primitives.

#### Reusable

[Reusable](schema/core/reusable) directory contains the schemas that are widely used in other schemas to avoid duplication, constructed from the abstract and primitive schemas.

#### Reference

[Reference](schema/core/reference) directory contains the schemas defining the rules to structure the references to data sources.

### Example

This directory contains the examples formed according to the schemas and implements the same directory structure as the schema directory.

### src

This directory contains Python and Javascript interfaces implementing the functionality to access and validate schemas and examples.

## Tests

Execute the following command from the root directory of this repository to run the tests. The script will run both Javascript and Python tests in which examples are validated against the corresponding schemas.

```bash
sh run-tests.sh
```

## Contribution

This repository is an [open-source](LICENSE.md) work-in-progress and we welcome contributions. We suggest forking this repository and introducing the adjustments there, the changes in the fork can further be considered for merging into this repository as it is commonly done on Github [#links](2).

## Best Practices

- Use unique IDs for schemas. One can run `sh refactor.sh` to automatically set the IDs and reformat examples.

- Do not use circular references in the schemas, instead leave the type as object and add explanation to description.

## Links

1: [Data-centric online ecosystem for digital materials science](https://arxiv.org/pdf/1902.10838.pdf)

2: [GitHub Standard Fork & Pull Request Workflow](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
