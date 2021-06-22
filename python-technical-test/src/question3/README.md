# REST API Architecture

You are tasked with designing, building and managing a global REST API that must be able to scale from 50 requests per second to bursts of 2,000 requests per second. Your team have built the API code and provided it to you. Your task is to build the platform that can serve the requests to the API.

The priority of requirements are listed as follows with the most important first.

1. Uptime/Reliability
2. Low Latency
3. Simplicity
4. Cost

In fewer than 8 paragraphs, describe how you would achieve this. Key things to think about are: Overall design, platform choices, any additional tools, management & maintenance.


#Solution:

I will use load balancing server(algorithm : Round Robin etc) and keep database server separate than the Apache server.
Database server traffic takes more load on the server due to which site may get slow.
Apache server configurations should be like 10TB HHD, 8GB RAM(each), Intel 12CPU processors.
And Keeping higher configuration for Database server than Apache server. MySQL handled 2,400 requests per second. 1 Mysql server with 1 slave will be enough. Slave is read only for statistics and reporting..

Performance benchmarking of the existing code can find inefficiencies in code using linting/debugging tools. Implement caching to avoid resource-hungry and slow computations and also using optimize query and do query caching and function caching.

Enabling persistent connections to database can avoid the overhead of re-establishing a connection to the database in each request.(Ex: max-connection-age = 5 hours)
Add version number in api to make it maintainable.

To enable quick and continues deployment i will create CD/CI pipeline from release branches.

Dockerizing the application may provide ease of installation and packaging application into a single bundle.
