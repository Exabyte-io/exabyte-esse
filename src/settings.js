import path from "path";
export const DEBUG = process.env['DEBUG'] || false;
export const NAMESPACE = "https://exabyte.io/schemas/";
// original directory with schema files
export const SCHEMAS_DIR = path.resolve(__dirname, "../schema");
// directory with compiled schema files
export const LIB_DIR = path.resolve(__dirname, "../lib");
// whether to omit "$schema" key, eg. to make MongoDB safe
export const OMIT_SCHEMA_KEY = true;
