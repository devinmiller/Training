# Service Level Objectives

>We use intuition, experience, and an understanding of what users want to define service level indicators (SLIs), objectives (SLOs), and agreements (SLAs). These measurements describe basic properties of metrics that matter, what values we want those metrics to have, and how we’ll react if we can’t provide the expected service. Ultimately, choosing appropriate metrics helps to drive the right action if something goes wrong, and also gives an SRE team confidence that a service is healthy.

## Service Level Terminology

The terms SLI, SLO, and SLA are worth careful defining for the sake of clarity.

### Indicators

>An SLI is a service level indicator—a carefully defined quantitative measure of some aspect of the level of service that is provided.

Typical metrics used for service indicators include:

- Request latency
  - How long it takes to return a response to a request
- Error rate
  - Often expressed as a fraction of all requests received
- System throughput
  - Typically measured in requests per second

>The measurements are often aggregated: i.e., raw data is collected over a measurement window and then turned into a rate, average, or percentile.

Another standard metric importent to SREs is availability, or the fraction of time a service is usable.  It is often defined in two ways:  

- Yield
  - The fraction of well-formed requests that succeed
- Durability
  - The likelihood that data will be retained over a long period of time
  - Important for data storage systems

As menntioned in previously, 100% availability is impossible.  Near 100% availability is often achievable, and high availability is usually expressed by the number of nines in the percentage (for example, 99.9% or three nines).

### Objectives

>An SLO is a service level objective: a target value or range of values for a service level that is measured by an SLI.  A natural structure for SLOs is thus **SLI ≤ target**, or **lower bound ≤ SLI ≤ upper bound**.

Choosing an appropriate SLO is complex, and often dictated by the users of a service rather than its designers.

>Choosing and publishing SLOs to users sets expectations about how a service will perform. This strategy can reduce unfounded complaints to service owners about, for example, the service being slow. Without an explicit SLO, users often develop their own beliefs about desired performance, which may be unrelated to the beliefs held by the people designing and operating the service.

### Agreements

>Finally, SLAs are service level agreements: an explicit or implicit contract with your users that includes consequences of meeting (or missing) the SLOs they contain. The consequences are most easily recognized when they are financial—a rebate or a penalty—but they can take other forms.

>SRE doesn’t typically get involved in constructing SLAs, because SLAs are closely tied to business and product decisions. SRE does, however, get involved in helping to avoid triggering the consequences of missed SLOs.

## Indicators in Practice

How do you identify metrics that are meaning ful to a service or system?

### What Do You and Your Users Care About?

Understanding what users want from a system will help determine the key indicators to use.  Choosing too many indicators can make it diffuicult to pay attention to indicators that matter, while choosing too few may leave important aspects of a system unexamined.

Services fall into the following broad categories in terms of the indicators they find important:

- User-facing serving systems
  - Availability - Could we respond to the request?
  - Latency - How long did it take to respond?
  - Throughput - How many requests could be handled?
- Storage systems
  - Latency - How long does it take to read or write data?
  - Availability - Can we access the data on demand?
  - Durability - Is the data still there when we need it?
- Big data systems
  - Throughput - How much data is being processed?
  - End-to-end latency - How long does it take the data to progress from ingestion to completion?
- All systems
  - Correctness - Was the right answer returned, the right data retrieved, the right analysis done?

### Collecting indicators

Most indicator metrics are gathered server side, either through dedicated monitoring systems or periodic log analysis.  However, systems should be instrumented with client-side collection where necessary, because not measuring behavior at the client can miss a range of problems that affect users but don’t affect server-side metrics

### Aggregation

>For simplicity and usability, we often aggregate raw measurements. This needs to be done carefully.
>
>Some metrics are seemingly straightforward, like the number of requests per second served, but even this apparently straightforward measurement implicitly aggregates data over the measurement window. Is the measurement obtained once a second, or by averaging requests over a minute? The latter may hide much higher instantaneous request rates in bursts that last for only a few seconds.
>
>Most metrics are better thought of as distributions rather than averages.
>
>Using percentiles for indicators allows you to consider the shape of the distribution and its differing attributes: a high-order percentile, such as the 99th or 99.9th, shows you a plausible worst-case value, while using the 50th percentile (also known as the median) emphasizes the typical case.

### Standardize Indicators

Standardize definitions for common SLIs.  This will save time and ensure consistency in understanding what an SLI means.  

## Objectives in Practice

Start by thinking about, or finding out, what user care about, not just what can be measured.

### Defining Objecives

>For maximum clarity, SLOs should specify how they’re measured and the conditions under which they’re valid.

Again, it is unrealistic and undesireable to expect that SLO will be met 100% of the time.  Such expectations can reduce the rate of innovation and deployment, require expensive, overly conservative solutions, or both.  It is better to allow an error budget.

The gap that exists when comparing the SLO violation rate against the error budget is used to decide when new releases can be rolled out.

### Choosing Targets

>Choosing targets (SLOs) is not a purely technical activity because of the product and business implications, which should be reflected in both the SLIs and SLOs (and maybe SLAs) that are selected

There are a few rules to keep in mind when discussing the risks and viability of targets:

#### Don’t pick a target based on current performance

If the current performance require a heroic effort to achieve it will continue to do so.  This can make it difficult to implement changes.

#### Keep it simple

Complicate SLIs are difficult to understand and can obscure changes to system performance.

#### Avoid absolutes

Only a sith deals in absolutes.

#### Have as few SLOs as possible

Choose just enough SLOs to provide good coverage of a system's attributes.

#### Perfection can wait

The SLO definitions and targets can always be refined over time as more is learned about a system's behavior.

>SLOs can—and should—be a major driver in prioritizing work for SREs and product developers, because they reflect what users care about

### Control Measures

>SLIs and SLOs are crucial elements in the control loops used to manage systems:
>
> 1. Monitor and measure the system’s SLIs.
> 1. Compare the SLIs to the SLOs, and decide whether or not action is needed.
> 1. If action is needed, figure out what needs to happen in order to meet the target.
> 1. Take that action.

### SLOs Set Expectations

User want to know what they can expect from a service, so they can determine if the service is appropriate for their particular use case.  Publishing SLOs sets expectations for system behaviors on which users will base their decision.

In order to set realistic expectations, consider the following:

#### Keep a safety margin

Maintain an SLO buffer by using a tighter SLO internally than externally.  This makes it possible to respond to problems before they become visible to users.

#### Don’t overachieve

Users will set expections based on the reality of what you offer, not on what you say you will supply.

>Understanding how well a system is meeting its expectations helps decide whether to invest in making the system faster, more available, and more resilient

## Agreements in Practice

>Crafting an SLA requires business and legal teams to pick appropriate consequences and penalties for a breach. SRE’s role is to help them understand the likelihood and difficulty of meeting the SLOs contained in the SLA.
