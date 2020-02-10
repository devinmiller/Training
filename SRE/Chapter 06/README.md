# Monitoring Distributed Systems

>This chapter offers guidelines for what issues should interrupt a human via a page, and how to deal with issues that aren’t serious enough to trigger a page.

## Definitions

There is not a universal vocabullary for discussing all topics on monitor, but a few common interpretations are listed here.

### Monitoring

>Collecting, processing, aggregating, and displaying real-time quantitative data about a system, such as query counts and types, error counts and types, processing times, and server lifetimes.

### White-box monitoring

>Monitoring based on metrics exposed by the internals of the system.

### Black-box monitoring

>Testing externally visible behavior as a user would see it.

### Dashboard

>An application (usually web-based) that provides a summary view of a service’s core metrics.

### Alert

>A notification intended to be read by a human and that is pushed to a system such as a bug or ticket queue, an email alias, or a pager.

### Root cause

>A defect in a software or human system that, if repaired, instills confidence that this event won’t happen again in the same way.

### Node and machine

>Used interchangeably to indicate a single instance of a running kernel in either a physical server, virtual machine, or container.

### Push

>Any change to a service’s running software or its configuration.

## Why Monitor?

The reasons to monitor a system include:

- Analyzing long-term trends
- Comparing over time or experiment groups
- Alerting
- Building dashboards
- Conducting ad hoc retrospective analysis (i.e., debugging)
- Supplying raw input into business analytics
- Facilitating analysis of security breaches

>Monitoring and alerting enables a system to tell us when it’s broken, or perhaps to tell us what’s about to break.

## Setting Reasonable Expectations for Monitoring

Monitoring can be complex and require significant effort in and of itself.

- Trend toward simpler and faster monitoring systems
  - Aim for better tools for post hoc analysis
- Avoid "magic" systems that try to learn thresholds or automatically detect causality
  - Rules that detect unexpected changes in end-user request rates are one counterexample
- Capacity planning and traffic prediction can tolerate more fragility
- Observations over a very long time with a low sampling rate can tolerate more fragility
  - Occasional missed samples won’t hide a long-running trend

## Symptoms Versus Causes

>Your monitoring system should address two questions: what’s broken, and why?
>
>The "what’s broken" indicates the symptom; the "why" indicates a (possibly intermediate) cause.

## Black-Box Versus White-Box

The simplest way to think about block-box versus whitebox monitoring, is that black-box monitoring is symptom-oriented and represents active problems.  On the other hand, white-box monitoring, which relies on the ability to inspect the innards of the system, allows detection of imminent problems, failures masked by retries, and so forth.

## The Four Golden Signals

>The four golden signals of monitoring are latency, traffic, errors, and saturation. If you can only measure four metrics of your user-facing system, focus on these four.

### Latency

>The time it takes to service a request. It’s important to distinguish between the latency of successful requests and the latency of failed requests

### Traffic 

>A measure of how much demand is being placed on your system, measured in a high-level system-specific metric.

### Errors

>The rate of requests that fail, either explicitly (e.g., HTTP 500s), implicitly (for example, an HTTP 200 success response, but coupled with the wrong content), or by policy (for example, "If you committed to one-second response times, any request over one second is an error").

### Saturation

>How "full" your service is. A measure of your system fraction, emphasizing the resources that are most constrained (e.g., in a memory-constrained system, show memory; in an I/O-constrained system, show I/O).

>If you measure all four golden signals and page a human when one signal is problematic (or, in the case of saturation, nearly problematic), your service will be at least decently covered by monitoring.

## Worrying About Your Tail (or, Instrumentation and Performance)

>When building a monitoring system from scratch, it’s tempting to design a system based upon the mean of some quantity: the mean latency, the mean CPU usage of your nodes, or the mean fullness of your databases. The danger presented by the latter two cases is obvious: CPUs and databases can easily be utilized in a very imbalanced way. The same holds for latency. 
>
>The simplest way to differentiate between a slow average and a very slow "tail" of requests is to collect request counts bucketed by latencies (suitable for rendering a histogram), rather than actual latencies: how many requests did I serve that took between 0 ms and 10 ms, between 10 ms and 30 ms, between 30 ms and 100 ms, between 100 ms and 300 ms, and so on?

## Choosing an Appropriate Resolution for Measurements

The level of granularity being for measurement should make sense for the system.  For example:

- Observing CPU load over the time span of a minute won’t reveal even quite long-lived spikes that drive high tail latencies.
- On the other hand, for a web service targeting no more than 9 hours aggregate downtime per year (99.9% annual uptime), probing for a 200 (success) status more than once or twice a minute is probably unnecessarily frequent.
- Similarly, checking hard drive fullness for a service targeting 99.9% availability more than once every 1–2 minutes is probably unnecessary.

## As Simple as Possible, No Simpler

A monitoring system should be designed towards simplicity.  Keep the following in mind when choosing what to monitor:

- The rules that catch real incidents most often should be as simple, predictable, and reliable as possible.
- Data collection, aggregation, and alerting configuration that is rarely exercised (e.g., less than once a quarter for some SRE teams) should be up for removal.
- Signals that are collected, but not exposed in any prebaked dashboard nor used by any alert, are candidates for removal.

## Tying These Principles Together

Asking the follwoing questions when creating rules for monitoring and alerting can help avoid false positives and pager burnout:

- Does this rule detect an otherwise undetected condition that is urgent, actionable, and actively or imminently user-visible?
- Will I ever be able to ignore this alert, knowing it’s benign? When and why will I be able to ignore this alert, and how can I avoid this scenario?
- Does this alert definitely indicate that users are being negatively affected? Are there detectable cases in which users aren’t being negatively impacted, such as drained traffic or test deployments, that should be filtered out?
- Can I take action in response to this alert? Is that action urgent, or could it wait until morning? Could the action be safely automated? Will that action be a long-term fix, or just a short-term workaround?
- Are other people getting paged for this issue, therefore rendering at least one of the pages unnecessary?

## Conclusion

>A healthy monitoring and alerting pipeline is simple and easy to reason about. It focuses primarily on symptoms for paging, reserving cause-oriented heuristics to serve as aids to debugging problems. Monitoring symptoms is easier the further "up" your stack you monitor, though monitoring saturation and performance of subsystems such as databases often must be performed directly on the subsystem itself. Email alerts are of very limited value and tend to easily become overrun with noise; instead, you should favor a dashboard that monitors all ongoing subcritical problems for the sort of information that typically ends up in email alerts. A dashboard might also be paired with a log, in order to analyze historical correlations.
