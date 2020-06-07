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

- <details>
    <summary>Infrastructure as a Service (IaaS)</summary>
    <br />

    Think EC2.

    Infrastructure as a service (IaaS) is an instant computing infrastructure,
    provisioned and managed over the internet

</details>

- <details>
    <summary>Platform as a Service (IaaS)</summary>
    <br />

    Think Elastic Beanstalk or Lightsail.  

    Platform as a service (PaaS) is a complete development and deployment
    environment in the cloud, with resources that enable you to deliver
    everything from simple cloud-based apps to sophisticated, cloud-enabled
    enterprise applications.

</details>

- <details>
    <summary>Software as a Service (SaaS)</summary>
    <br />

    Think Gmail.  

    Software as a service (SaaS) allows users to connect to and use
    cloud-based apps over the Internet.

</details>

### Cloud Computing Deployment Models

- <details>
    <summary>Cloud</summary>
    <br />

    A cloud-based application is fully deployed in the cloud and all parts of
    the application run in the cloud.

</details>

- <details>
    <summary>Hybrid</summary>
    <br />

    A hybrid deployment is a way to connect infrastructure and applications
    between cloud-based resources and existing resources that are not located
    in the cloud.

</details>

- <details>
    <summary>On-Premises</summary>
    <br />

    The deployment of resources on-premises, using virtualization and resource
    management tools, is sometimes called the “private cloud.”

</details>

## Global Infrastructure

The AWS Cloud infrastructure is built around AWS Regions and Availability
Zones.

- <details>
    <summary>AWS Region</summary>
    <br />

    A physical location in the world with multiple (at least two) Availability Zones.

</details>

- <details>
    <summary>AWS Availability Zone</summary>
    <br />

    One or more discrete data centers, each with redundant power, networking,
    and connectivity housed in separate facilities

</details>

## Security and Compliance

### Security

The AWS Cloud enables a shared responsibility model.

![Shared Responsibility Model](images/Shared_Responsibility_Model.jpg)

Below are examples of controls that are managed by AWS, AWS Customers and/or both.

<details>
    <summary>Inherited Controls</summary>
    <br />

Controls which a customer fully inherits from AWS.

- Physical and Environmental controls

</details>

<details>
    <summary>Shared Controls</summary>
    <br />

    Controls which apply to both the infrastructure layer and customer layers.

    - Patch Management
    - Configuration Management
    - Awareness & Training

</details>

<details>
    <summary>Customer Specific</summary>
    <br />

    Controls which are solely the responsibility of the customer

    - Service and Communications Protection or Zone Security

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
    <br />

    Run SQL queries against data stored in S3 without the need for complex 
    extract, transform, and load (ETL) jobs to prepare the data for analysis.

</details>

<details>
    <summary>Elastic Map Reduce (EMR)</summary>
    <br />

    A big data platform for processing vast amounts of data in the cloud using 
    popular open source tools.

</details>

<details>
    <summary>CloudSearch</summary>
    <br />

    A fully managed service for adding simple and cost effective search 
    solutions to websites or applications.

</details>

<details>
    <summary>Elasticsearch Service</summary>
    <br />

    A service to deploy, operate and manage Elasticsearch to provide search, 
    analyses, and visualization of data in real-time.

</details>

<details>
    <summary>Kinesis</summary>
    <br />

    A service for collecting, processing, and analyzing real-time, streaming data.

</details>

<details>
    <summary>Redshift</summary>
    <br />

    A fast, scalable data warehouse for analyzing data.

</details>

<details>
    <summary>QuickSight</summary>
    <br />

    A business intelligence (BI) service.

</details>

<details>
    <summary>Data Pipeline</summary>
    <br />

    A web service for moving data between different cloud sources and 
    on-premise sources at specified intervals.

</details>

<details>
    <summary>Glue</summary>
    <br />

    A fully managed extract, load, and transform (ETL) service to prepare and 
    load data for analytics.

</details>

<details>
    <summary>Lake Formation</summary>
    <br />

    A service to help with setting up a secure data lake.

</details>


