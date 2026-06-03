# Snowflake Objects 

#### Data base 

A database is a systematic, digitally stored collection of structured information or data. It is designed to allow data to be easily accessed, managed, modified, updated, controlled, and organized.

A Database is a Organized collection of structured information or data Stored electronically for easily access and Management typically  managed by database management system.

#### Schema 
A schema is a logical grouping of database objects (tables, views, etc.). Each schema belongs to a single database.

#### Tables 
A table in Snowflake is a fundamental database object that stores structured or semi-structured data in rows and columns. When you load data into a table, Snowflake automatically translates it into a highly compressed, optimized, columnar format and stores it in cloud storage.

There are mainly three types of tables in snowflake 

##### Temporary Tables 
- Table will create and  exist only for the duration of the current session.
- Time travel - Session duration  
- No fail-safe 
##### Transient table 
- Table will create and  exist till we drop.
- Time travel - 0-1 days  
- No fail-safe 
##### Permanent  table 
- Table will create and  exist till we drop.
- Time travel - 1-90 days (Enterprise)  (Standerd-0-1days  )
- Fail-safe   - 7 days (All)
 
#### Data Masking 
 
Snowflake Data Masking is a native column-level security feature that allows organizations to protect sensitive information like PII, PHI, or financial records by altering data in query results. The underlying data stored in your tables remains completely unchanged; the transformation happens entirely on-the-fly at query execution time based on the user's role and context.

#### Snowflake Stage 
A Snowflake stage is a secure holding area or intermediary storage location used to temporarily or permanently store data files before they are loaded into database tables or extracted to external systems. Stages simplify and optimize data ingestion, commonly used with the COPY INTO command.

Snowflake does support auto-ingestion for internal stages in specific situations.

By default, Snowpipe does not automatically trigger when files are placed in an internal stage. Historically, using an internal stage with Snowpipe meant you had to use the Snowpipe REST API to manually trigger the load after uploading your files.