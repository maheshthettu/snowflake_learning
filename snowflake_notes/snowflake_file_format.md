### Snowflake File Format

A snowflake file format is a named database object in snowflake which cntains complete information about the data file like type of file(csv,json),formatted options and compression method.

In snowflake File format generally used to simplify the process of loading and unlaoding.
These are the format types which snowflake allows :
- CSV Format
- JSON
- Avro
- ORC
- Parquet
- XML


##### CSV Format

The files which are having CSV files 

```sql
CREATE OR REPLACE FILE FORMAT csv_format
TYPE = CSV
COMPRESSION = AUTO
FIELD_DELIMITER = ','
RECORD_DELIMITER = '\n'
SKIP_HEADER = 1
FIELD_OPTIONALLY_ENCLOSED_BY = '"'
TRIM_SPACE = TRUE
ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE
ESCAPE = NONE
ESCAPE_UNENCLOSED_FIELD = NONE
NULL_IF = ('NULL', 'null', '')
EMPTY_FIELD_AS_NULL = TRUE
BINARY_FORMAT = HEX
DATE_FORMAT = AUTO
TIME_FORMAT = AUTO
TIMESTAMP_FORMAT = AUTO
REPLACE_INVALID_CHARACTERS = TRUE
SKIP_BYTE_ORDER_MARK = TRUE;
```

##### JSON

```sql
CREATE OR REPLACE FILE FORMAT json_format
TYPE = JSON
COMPRESSION = AUTO
STRIP_OUTER_ARRAY = FALSE
STRIP_NULL_VALUES = FALSE
IGNORE_UTF8_ERRORS = FALSE;
```
##### PARQUET

```sql 
CREATE OR REPLACE FILE FORMAT parquet_format
TYPE = PARQUET
COMPRESSION = AUTO
SNAPPY_COMPRESSION = TRUE
BINARY_AS_TEXT = FALSE
TRIM_SPACE = FALSE;
```

##### AVRO

```sql 
CREATE OR REPLACE FILE FORMAT avro_format
TYPE = AVRO
COMPRESSION = AUTO
TRIM_SPACE = FALSE;
```

##### ORC
```sql
CREATE OR REPLACE FILE FORMAT orc_format
TYPE = ORC
COMPRESSION = AUTO;
```

##### XML
```sql
CREATE OR REPLACE FILE FORMAT xml_format
TYPE = XML
COMPRESSION = AUTO
STRIP_OUTER_ELEMENT = FALSE
DISABLE_SNOWFLAKE_DATA = FALSE
IGNORE_UTF8_ERRORS = FALSE;
```