# Overview of Amazon Web Services

Amazon Web Services offers a broad set of global cloud-based products
including compute, storage, databases, analytics, networking, mobile,
developer tools, management tools, IoT, security, and enterprise applications:
on-demand, available in seconds, with pay-as-you-go pricing

## What is Cloud Computing

Cloud computing provides a simple way to access servers, storage, databases
and a broad set of application services over the Internet. A cloud services
platform, such as Amazon Web Services, owns and maintains the network 
connected hardware required for these application services, while you provision
and use what you need via a web application.

## Six Advantage of Cloud Computing

1. Trade capital expense for variable expense
1. Benefit from massive economies of scale
1. Stop guessing capacity
1. Increase speed and agility
1. Stop spending money running and maintaining data centers
1. Go global in minutes

## Types of Cloud Computing

Understanding the differences between Infrastructure as a Service, Platform as
a Service, and Software as a Service, as well as what deployment strategies
you can use, can help you decide what set of services is right for your needs.

### Cloud Computing Models

<details>

<summary>Infrastructure as a Service (IaaS)</summary>

> Think EC2.
>
> Infrastructure as a service (IaaS) is an instant computing infrastructure,
> provisioned and managed over the internet

</details>

<details>

<summary>Platform as a Service (IaaS)</summary>

> Think Elastic Beanstalk or Lightsail.  
>
> Platform as a service (PaaS) is a complete development and deployment
> environment in the cloud, with resources that enable you to deliver
> everything from simple cloud-based apps to sophisticated, cloud-enabled
> enterprise applications.

</details>

<details>

<summary>Software as a Service (SaaS)</summary>

> Think Gmail.  
>
> Software as a service (SaaS) allows users to connect to and use
> cloud-based apps over the Internet.

</details>

### Cloud Computing Deployment Models

<details>

<summary>Cloud</summary>

> A cloud-based application is fully deployed in the cloud and all parts of
> the application run in the cloud.

</details>

<details>

<summary>Hybrid</summary>

> A hybrid deployment is a way to connect infrastructure and applications
> between cloud-based resources and existing resources that are not located
> in the cloud.

</details>

<details>

<summary>On-Premises</summary>

> The deployment of resources on-premises, using virtualization and resource
> management tools, is sometimes called the “private cloud.”

</details>

## Global Infrastructure

The AWS Cloud infrastructure is built around AWS Regions and Availability
Zones.

<details>

<summary>AWS Region</summary>

> A physical location in the world with multiple (at least two) Availability > Zones.

</details>

<details>

<summary>AWS Availability Zone</summary>

> One or more discrete data centers, each with redundant power, networking,
> and connectivity housed in separate facilities

</details>

## Security and Compliance

### Security

The AWS Cloud enables a shared responsibility model.

![Shared Responsibility Model](images/Shared_Responsibility_Model.jpg)

Below are examples of controls that are managed by AWS, AWS Customers and/or both.

<details>

<summary>Inherited Controls</summary>

> Controls which a customer fully inherits from AWS.
>
> - Physical and Environmental controls

</details>

<details>

<summary>Shared Controls</summary>

> Controls which apply to both the infrastructure layer and customer layers.
>
> - Patch Management
> - Configuration Management
> - Awareness & Training

</details>

<details>

<summary>Customer Specific</summary>

> Controls which are solely the responsibility of the customer
>
> - Service and Communications Protection or Zone Security

</details>

#### Security Resources

- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)

### Compliance

AWS Cloud Compliance enables you to understand the robust controls in place
at AWS to maintain security and data protection in the cloud.

AWS Artifact is the central resource for compliance-related information. It
provides on-demand access to security and compliance reports and select online
agreements. Reports available in AWS Artifact include our Service Organization
Control (SOC) reports, Payment Card Industry (PCI) reports, and certifications
from accreditation bodies across geographies and compliance verticals that
validate the implementation and operating effectiveness of AWS security
controls.

## Amazon Web Services Cloud Platform

There are three ways to access AWS services -

1. Management Console
1. Command Line Interface (CLI)
1. Software Development Kits (SDKs)

### Analytics

<details>

<summary>Athena</summary>

> Run SQL queries against data stored in S3 without the need for complex 
> extract, transform, and load (ETL) jobs to prepare the data for analysis.

</details>

<details>

<summary>Elastic Map Reduce (EMR)</summary>

> A big data platform for processing vast amounts of data in the cloud using 
> popular open source tools.

</details>

<details>

<summary>CloudSearch</summary>

> A fully managed service for adding simple and cost effective search 
> solutions to websites or applications.

</details>

<details>

<summary>Elasticsearch Service</summary>

> A service to deploy, operate and manage Elasticsearch to provide search, 
> analyses, and visualization of data in real-time.

</details>

<details>

<summary>Kinesis</summary>

> A service for collecting, processing, and analyzing real-time, streaming> data.

</details>

<details>

<summary>Redshift</summary>

> A fast, scalable data warehouse for analyzing data.

</details>

<details>

<summary>QuickSight</summary>

> A business intelligence (BI) service.

</details>

<details>

<summary>Data Pipeline</summary>

> A web service for moving data between different cloud sources and 
> on-premise sources at specified intervals.

</details>

<details>

<summary>Glue</summary>

> A fully managed extract, load, and transform (ETL) service to prepare and 
> load data for analytics.

</details>

<details>

<summary>Lake Formation</summary>

> A service to help with setting up a secure data lake.

</details>

### Application Integration

<details>

<summary>Step Functions</summary>

> Allows multiple services to be combined into serverless workflows.

</details>

<details>

<summary>Simple Queue Service (SQS)</summary>

> A fully managed message queuing service.
>
> SQS offers two types of message queues:
>
> 1. Standard queues
> 1. First In First Out (FIFO) queues

</details>

<details>

<summary>Simple Notification Service (SNS)</summary>

> A Fully managed pu/sub messaging service.

</details>

<details>

<summary>Simple Workflow (SWF)</summary>

> A service to help build, run, and scale background jobs that have sequential 
> or parallel steps.

</details>

### Cost Management

<details>

<summary>Cost Explorer</summary>

> Used to visualize, understand, and manage costs and usage over time.

</details>

<details>

<summary>Budgets</summary>

> Used for the following:
>
> - Set custom budgets that alert when costs or usage exceed budgeted amount.
> - Set Reserved Instance (RI) utilization targets that alert when utilization 
> drops below defined threshold.

</details>

<details>

<summary>Cost & Usage Report</summary>

> A single location for accessing comprehensive information about cost and
> usage.  Lists usage for each service category used by an account and its
> IAM users, as well as any tags activated for cost allocation purposes.

</details>

### Compute

<details>

<summary>Elastic Cloud Compute (EC2)</summary>

Think virtual machines in the cloud.

A service that provides secure, resizable computer capacity in the cloud.

#### Instance Types

- On-Demand
  > Pay for compute capacity by the hour with no long-term commitments
- Reserved Instances
  > Offer significant cost saving over On-Demand for a 1 or 3 year commitment
  >
  > Choose between three payment options:
  >
  > 1. All Upfront
  > 1. Partial Upfront
  > 1. No Upfront
  >
  > Reserved Instance Types:
  >
  > - Convertible
  >   - Capability to change the attributes of the RI as long as the exchange
  >     results in the creation of RIs of equal or greater value.
  >   - Change Availability Zone, instance size (for Linux OS), networking type
  >   - Change instance families, operating system, tenancy, and payment option
  > - Scheduled
  >   - Are available to launch within the reserved time windows.
  >   - Allows matching capacity reservation to a predictable recurring
  >     schedule that only requires a fraction of a day, a week, or a month.
  >
- Spot
  > Allow for bidding on spare or unused EC2 compute capacity for a
  > significant discount.
- Dedicated Host
  > A physical server with EC2 instance capacity fully dedicated to a single
  > customer's use.
  >
  > Supports use of existing per-socket, per-core, or per-VM software licenses.

</details>

<details>

<summary>EC2 Auto Scaling</summary>

> Maintains application availability by automatically adding or removing EC2
> instances according to defined conditions.

</details>

<details>

<summary>Elastic Container Registry (ECR)</summary>

> A fully managed Docker container registry.

</details>

<details>

<summary>Elastic Container Service (ECS)</summary>

> A container orchestration service that supports docker containers.

</details>

<details>

<summary>Elastic Container Service for Kubernetes (EKS)</summary>

> A service to deploy, manage, and scale containerized applications on AWS
> using Kubernetes.

</details>

<details>

<summary>Lightsail</summary>

> An easy way to launch and manage a virtual private server, includes a
> virtual machine, SSD storage, data transfer, DNS management, and a static IP
> address.

</details>

<details>

<summary>Batch</summary>

> Enables developers, scientists, and engineers to easily and efficiently run
> hundreds of thousands of batch computing jobs.

</details>

<details>

<summary>Elastic Beanstalk</summary>

> A service for deploying and scaling web applications and services.  

</details>

<details>

<summary>Lambda</summary>

> Serverless functions.

</details>

### Customer Engagement

<details>

<summary>Connect</summary>

> A self-service, cloud-based contact center service.

</details>

<details>

<summary>Simple Email Service (SES)</summary>

> An email sending service designed to with marketing, transactional, or
> notification emails.

</details>

### Database

<details>

<summary>Aurora</summary>

> A fast, scalable MySQL and PostgreSQL compatible relational database engine.

</details>

<details>

<summary>Relational Database Service (RDS)</summary>

> A service for setting up, operating, and scaling relational database
> services in the cloud.

</details>

<details>

<summary>DynamoDB</summary>

> A NoSQL document database.

</details>

<details>

<summary>Elasticache</summary>

> A service for deploying, operating, and scaling an in-memory cache.
>
> Supports two in-memory caching engines:
>
> - Redis
> - Memcached

</details>

<details>

<summary>Neptune</summary>

> A fully managed graph database service.

</details>

### Desktop and App Streaming

<details>

<summary>Workspaces</summary>

> A fully managed, secure cloud desktop service.

</details>

<details>

<summary>AppStream 2.0</summary>

> A fully managed application streaming service.

</details>

### Developer Tools

<details>

<summary>CodeCommit</summary>

> A fully managed source control service that hosts secure git-based
> repositories.

</details>

<details>

<summary>CodeBuild</summary>

> A a fully managed build service that compiles source code,
> runs tests, and produces software packages that are ready to deploy

</details>

<details>

<summary>CodeDeploy</summary>

> A service that automates code deployments to any instance, including EC2
> instances and instances on premises.

</details>

<details>

<summary>CodePipeline</summary>

> A fully managed continuous delivery service for automating the build, test
> and deploy phases of a release every time there is a code change.

</details>

<details>

<summary>CodeStar</summary>

> A unified interface to manage software development activities in one place.

</details>

<details>

<summary>Cloud9</summary>

> A cloud-based integrated development environment (IDE).

</details>

<details>

<summary>X-Ray</summary>

> A service to help  analyze and debug distributed applications in
> production or under development.

</details>

### Machine Learning

<details>

<summary>SageMaker</summary>

> A fully managed platform to build, train, and deploy machine learning models.

</details>

<details>

<summary>Comprehend</summary>

> A natural language processing (NLP) service that uses machine learning to
> find insights and relationships in text.

</details>

<details>

<summary>Lex</summary>

> A service for building conversational interfaces into applications using
> voice and text.

</details>

<details>

<summary>Polly</summary>

> A that turns text into speech.

</details>

<details>

<summary>Rekognition</summary>

> A service for adding image recognition to applications.

</details>

### Management and Governance

<details>

<summary>CloudWatch</summary>

> A service that collects monitoring and operational data in the form of logs
> metrics, and events to provide a unified view of resources.
>
> Can be used to set alarms, visual logs and metrics, troubleshoot issues, or
> take automated actions.

</details>

<details>

<summary>Auto Scaling</summary>

> Monitors applications and automatically adjusts capacity to maintain steady,
> predictable performance at the lowest possible cost.

</details>

<details>

<summary>Control Tower</summary>

> Automates the set-up of a baseline environment, or landing zone, that is a
> secure, well-architected multi-account AWS environment.

</details>

<details>

<summary>Systems Manager</summary>

> Provides a unified interface for grouping resources, monitoring and
> troubleshooting resource groups, as well as taking action on resource groups.

</details>

<details>

<summary>CloudFormation</summary>

> Provides a means for programmatically provisioning resources by defining
> configuration in JSON or YAML files.

</details>

<details>

<summary>CloudTrail</summary>

> A service for recording and auditing AWS API calls from an account.

</details>

<details>

<summary>Config</summary>

> A service for assessing, auditing, and evaluating the configurations of
> resources.

</details>

<details>

<summary>OpsWorks</summary>

> A configuration management service using Chef and Puppet.

</details>

<details>

<summary>Service Catalog</summary>

> Allows organization to create and manage catalogs of services that are
> approved for use on AWS.

</details>

<details>

<summary>Trusted Advisor</summary>

> An online resource to help reduce cost, increase performance, and
> improve security by optimizing the AWS environment.

</details>

<details>

<summary>Personal Health Dashboard</summary>

> Provides alerts and remediation guidance when AWS is experiencing events
> that might impact availability or performance.

</details>

<details>

<summary>Managed Services</summary>

> Operates AWS on behalf of the customer, providing a secure and compliant AWS
> Landing Zone, a proven enterprise operating model, on-going cost
> optimization, and day-to-day infrastructure management.

</details>

<details>

<summary>Well-Architected Tool</summary>

> A free tools that helps review the current state of workloads and compares
> them to the latest architectural best practices.

</details>

### Migration and Transfer

<details>

<summary>Migration Hub</summary>

> Provides a single location to track the progress of application migrations.

</details>

<details>

<summary>Application Discovery Service</summary>

> Helps enterprise customers plan migration projects by gathering information
> about their on-premises data centers.

</details>

<details>

<summary>Database Migration Service (DMS)</summary>

> A service that helps migrate on-premises databases to AWs.

</details>

<details>

<summary>Server Migration Service (SMS)</summary>

> A service that helps migrate on-premises workloads to AWS.

</details>

<details>

<summary>Snowball</summary>

> A petabyte-scale data transport solution that uses secure appliances to
> transfer large amounts of data into and out of AWS.

</details>

<details>

<summary>Snowball Edge</summary>

> A data migration and edge computing device.

</details>

<details>

<summary>Snowmobile</summary>

> An exabyte-scale data transfer service used to move extremely large amounts
> of data to AWS

</details>

<details>

<summary>DataSync</summary>

> A data transfer service used to automate moving data between on-premises
> storage and S# or Elastic File System (EFS),

</details>

### Mobile

<details>

<summary>Cognito</summary>

> A service to add user sign-up, sign-in, and access control to web and mobile
> applications.

</details>

### Networking and Content Delivery

<details>

<summary>Virtual Private Cloud</summary>

> A virtual network that serves as an isolated section of the AWS Cloud for
> launching resources.

</details>

<details>

<summary>CloudFront</summary>

> A content delivery network (CDN) for delivering data globally with low
> latency.

</details>

<details>

<summary>Route 53</summary>

> A domain name system (DNS) used to connect user requests to infrastructure.

</details>

<details>

<summary>PrivateLink</summary>

> Provides private connectivity between VPCs, AWS services, and on-premises
> applications.

</details>

<details>

<summary>Direct Connect</summary>

> Establishes a private, dedicated network connection from on-premises to AWs.

</details>

<details>

<summary>Global Accelerator</summary>

> A networking service that improves the availability and performance of the
> applications that offered to global users.

</details>

<details>

<summary>API Gateway</summary>

> A service for creating, publishing, maintaining, monitoring, and securing
> APIs.

</details>

<details>

<summary>Transit Gateway</summary>

> A service that enables customers to connect their Virtual Private Clouds
> (VPCs) and their on-premises networks to a single gateway.

</details>

<details>

<summary>Elastic Load Balancing</summary>

> Distributes incoming application traffic across multiple targets, such as EC2
> instances, containers, and IP addresses.
>
> There are three types of load balancers:
>
> - Application Load Balancer
>   - Best suited for load balancing of HTTP and HTTPS traffic
> - Network Load Balancer
>   - Best suited for load balancing of TCP traffic where extreme performance
>     is required
> - Classic Load Balancer
>   - Intended for applications that were built within the EC2-Classic network

</details>
