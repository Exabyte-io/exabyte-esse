# Exabyte Source of Schemas and Examples (ESSE)

ESSE contains schemas and examples for materials and simulations related data in JSON representation outlined in [this manuscript]().

## Installation

ESSE can be used as a Node or Python package on the server side.
Pleas note that schemas and examples are not available on the client.

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
pip install -e PATH_TO_ESSE_REPOSITIRY
```

### Node

ESSE can be install as a Node package either via NPM or the repository as below.

#### NPM

```bash
npm install exabyte-esse
```

#### Repository

Add `"exabyte-esse": "file:PATH_TO_ESSE_REPOSITIRY"` to `package.json`.

## Usage

ESSE contains separate but equivalent interfaces for Python and Node.
The package provides `ESSE` class that can be initialized and used as below.

### Python

```python
from esse import ESSE

es = ESSE()
schema = es.get_schema_by_id("material")
```

### Node

```javascript
import {ESSE} from "exabyte-esse";

const es = new ESSE();
const schema = es.getSchemaById("material");
```

## Structure

ESSE contains 3 main directories, [schema](schema), [example](example) and [src](src) outlined below.

### Schema

The schema directory contains the schemas specifying the rules to structure materials-related data.
In order to apply object-oriented design principals, a set of basic schemas are defined to facilitate the schema modularity.

#### Primitive

[Primitive](schema/core/primitive) directory contains a set of custom primitives that extends default standard primitive types allowed by schema, such as String and Number.
Primitives are solely defined by the default primitives and can not be re-constructed from each other.

#### Abstract

[Abstract](schema/core/abstract) directory contains unit-less schemas that are constructed from default and custom primitives.

#### Reusable

[Reusable](schema/core/reusable) directory contains the schemas that are widely used in other schemas to avoid duplication, constructed from the abstract and primitive schemas.

### Example

This directory contains the examples formed according to the schemas and implements the same directory structure as the schema directory.

### Src

This directory contains Python and Node interfaces implementing the functionality to access and validate schemas and examples.

## Tests

Run the following command from the root directory of this repository to run the tests.
The script will run both Node and Python tests in which examples are validated against their schemas.

```bash
sh run-tests.sh
```

## Contribution

This is an open-source repository and we welcome contributions for other test cases.
We suggest forking this repository and introducing the adjustments there.
The changes in the fork can further be considered for merging into this repository as it is commonly used on Github.
This process is explained in more details [here](https://gist.github.com/Chaser324/ce0505fbed06b947d962).

## Best Practices

- Use unique IDs for schemas. One can run `sh refactor.sh` to automatically set the IDs and reformat examples.

- Do not use circular references in the schemas, instead leave the type as object and add explanation to description.
