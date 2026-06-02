# 1.Account Creation
Account is created with personal gamil : https://app.snowflake.com/ciynlrp/ho16000/#/homepage <br>
User name : mahesh <br>
password  : Mahesh@8143738092 <br>

#### Snowflake :
Snowflake is a cloude based data  warehouse platform which separates data storage and compute resources to enable the independent scaling unlike traditional data warehouse and also it natively handles both the structured and non structured data and offers features like auto scaling and high concurency.

#### Snowflake Architecture :
Snowflake's architecture is a unique hybrid of traditional shared-disk and shared-nothing database technologies. It is built natively for the cloud and separates compute, storage, and cloud services into three independent layers. This design allows you to scale resources on-demand without disrupting operations.

##### 1.Storage layer : 
It is bottom layer in the architecture and if any data is loaded it will store data in the form of micro-partions (Snowflake  internal, compressed, and columnar format).

It sits on top of your preferred cloud provider's object storage (e.g., Amazon S3, Azure Blob Storage, or Google Cloud Storage).

The storage is entirely handled and optimized by Snowflake behind the scenes.
##### 2.Compute layer : 
It stays on top of the storage layer, All data computations will be done in this layer whith the compute Virtual Warehouse.Each virtual warehouse is completely independent.

Warehouses can be resized (scaled up) or spun up in parallel (multi-cluster scaling) instantly, and can be paused automatically when idle to save costs

##### 3.Cloud service layer : 
This is the "control plane" or brain of the platform, coordinating activities across all layers.It manages user authentication, access control, metadata, and security.It parses, compiles, and optimizes your SQL queries before sending them to the compute layer.It handles infrastructure management, concurrency, and automated statistics collection

