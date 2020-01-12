# Embracing Risk

Past a certain point, increasing reliability is worse for a service and its users rather than better.  There are several costs for extreme reliability:

- Limits how fast new features can be developed
- Limits how quickly products can be delivered to users
- Dramatically increases the cost of new products and features
  - Reduces the numbers of features a team can afford to offer

As mentioned previously, users don't typically notice the difference between between high availability and extreme availability, mostly because the user experience is dominated by less reliable components, such as their network or device.

>With this in mind, rather than simply maximizing uptime, Site Reliability Engineering seeks to balance the risk of unavailability with the goals of rapid innovation and efficient service operations, so that users’ overall happiness—with features, service, and performance—is optimized.

## Managing Risk

Experience shows that cost does not increase linearly as reliability increments.  An incremental improvement in reliability may cost 100x more than the previous increment.  This is a result of two factors:

### The cost of redundant machine/compute resources

>The cost associated with redundant equipment that, for example, allows us to take systems offline for routine or unforeseen maintenance, or provides space for us to store parity code blocks that provide a minimum data durability guarantee.

### The opportunity cost

>The cost borne by an organization when it allocates engineering resources to build systems or features that diminish risk instead of features that are directly visible to or usable by end users. These engineers no longer work on new features and products for end users

In SRE, managing service reliability is largely about managing risk.  Risk is a continuum on which equal importance is given to figuring out how to engineer greater reliability and identifying the appropriate level of tolerance for the services that are run.  A service should reliable enough, but no more reliable than it needs to be.  Exceeding an availability target would waste opportunities to add features to the system, clean up technical debt, or reduce its operational costs.

## Measuring Service Risk

>For most services, the most straightforward way of representing risk tolerance is in terms of the acceptable level of unplanned downtime. Unplanned downtime is captured by the desired level of service availability, usually expressed in terms of the number of "nines" we would like to provide: 99.9%, 99.99%, or 99.999% availability.

For serving systems, this metric is traditionally calculated based on the proportion of system downtime.

### Time-based availability

![time-based availability](time-availability.png)

For non-serving system (e.g., batch, pipeline, storage, and transactional systems) or distributed systems, availability is defined in terms of request success rate.

### Aggregate availability

![aggregate-based availability](aggregate-availability.png)

>In a typical application, not all requests are equal: failing a new user sign-up request is different from failing a request polling for new email in the background. In many cases, however, availability calculated as the request success rate over all requests is a reasonable approximation of unplanned downtime, as viewed from the end-user perspective.

## Risk Tolerance of Services

>To identify the risk tolerance of a service, SREs must work with the product owners to turn a set of business goals into explicit objectives to which we can engineer.
>
>While consumer services often have clear product owners, it is unusual for infrastructure services (e.g., storage systems or a general-purpose HTTP caching layer) to have a similar structure of product ownership.

### Identifying the Risk Tolerance of Consumer Services

A product team, if one exists, is usually the best resource to discuss reliability requirements for a service.  In the absence of a product team, the responsibility falls on the engineers building the system.

The following factors should be considered when assessing risk tolerance of services:

- What level of availability is required?
- Do different types of failures have different effects on the service?
- How can we use the service cost to help locate a service on the risk continuum?
- What other service metrics are important to take into account?

#### Target level of availability

The target level of availability for a service depends on the function it provides and how the service is positioned in the marketplace.  Consider the following issues:

- What level of service will the users expect?
- Does this service tie directly to revenue (either our revenue, or our customers’ revenue)?
- Is this a paid service, or is it free?
- If there are competitors in the marketplace, what level of service do those competitors provide?
- Is this service targeted at consumers, or at enterprises?

#### Types of failures

>The expected shape of failures for a given service is another important consideration. How resilient is our business to service downtime? Which is worse for the service: a constant low rate of failures, or an occasional full-site outage? Both types of failure may result in the same absolute number of errors, but may have vastly different impacts on the business.

#### Cost

Cost is a key factor in determining the target availability for a service.  Can request successes and failures be directly translated into revenue gained or lost?  Ask the following questions to determine the availability target for each service:

- If we were to build and operate these systems at one more nine of availability, what would our incremental increase in revenue be?
- Does this additional revenue offset the cost of reaching that level of reliability?

#### Other service metrics

>Examining the risk tolerance of services in relation to metrics besides availability is often fruitful. Understanding which metrics are important and which metrics aren’t important provides us with degrees of freedom when attempting to take thoughtful risks.

### Identifying the Risk Tolerance of Infrastructure Services

>The requirements for building and running infrastructure components differ from the requirements for consumer products in a number of ways. A fundamental difference is that, by definition, infrastructure components have multiple clients, often with varying needs.

#### Target level of availability

Determining the availability target for infrastructure services can involve examining differing needs between users of the same service.  For example, a team needing low latency and high reliability versus another team more concerned with throughput than latency, both using the same service.  Risk tolerance between the two is distinct.

#### Types of failures

Much like the target level of availability, what might be considered a success or failure can differ between two users, each of whom has different expectations of the service.

#### Cost

>One way to satisfy these competing constraints in a cost-effective manner is to partition the infrastructure and offer it at multiple independent levels of service.
>
>The key strategy with regards to infrastructure is to deliver services with explicitly delineated levels of service, thus enabling the clients to make the right risk and cost trade-offs when building their systems. With explicitly delineated levels of service, the infrastructure providers can effectively externalize the difference in the cost it takes to provide service at a given level to clients. Exposing cost in this way motivates the clients to choose the level of service with the lowest cost that still meets their needs.

## Motivation for Error Budgets

As mentioned previously, tensions can often arise between product development and SRE teams , given they are evaluated on different metrics.

>Product development performance is largely evaluated on product velocity, which creates an incentive to push new code as quickly as possible. Meanwhile, SRE performance is evaluated based upon reliability of a service, which implies an incentive to push back against a high rate of change.

The following are a few typical tensions that arise between the teams:

### Software fault tolerance

>How hardened do we make the software to unexpected events? Too little, and we have a brittle, unusable product. Too much, and we have a product no one wants to use (but that runs very stably).

### Testing

>Again, not enough testing and you have embarrassing outages, privacy data leaks, or a number of other press-worthy events. Too much testing, and you might lose your market.

### Push frequency

>Every push is risky. How much should we work on reducing that risk, versus doing other work?

### Canary duration and size

>It’s a best practice to test a new release on some small subset of a typical workload, a practice often called canarying. How long do we wait, and how big is the canary?

The more data-based a decision can be, the better.  The goal is to define objective metrics, agreed upon by both sides, that can be used to guide the negotiations in a reproducible way.

## Forming Your Error Budget

>In order to base these decisions on objective data, the two teams jointly define a quarterly error budget based on the service’s service level objective, or SLO. The error budget provides a clear, objective metric that determines how unreliable the service is allowed to be within a single quarter. This metric removes the politics from negotiations between the SREs and the product developers when deciding how much risk to allow.

The practice is then as follows:

- Product Management defines an SLO, which sets an expectation of how much uptime the service should have per quarter.
- The actual uptime is measured by a neutral third party: our monitoring system.
- The difference between these two numbers is the "budget" of how much "unreliability" is remaining for the quarter.
- As long as the uptime measured is above the SLO—in other words, as long as there is error budget remaining—new releases can be pushed.

## Benefits

>The main benefit of an error budget is that it provides a common incentive that allows both product development and SRE to focus on finding the right balance between innovation and reliability.
>
>The budget also helps to highlight some of the costs of overly high reliability targets, in terms of both inflexibility and slow innovation. If the team is having trouble launching new features, they may elect to loosen the SLO (thus increasing the error budget) in order to increase innovation.

# Key Insights

> - Managing service reliability is largely about managing risk, and managing risk can be costly.
> - 100% is probably never the right reliability target: not only is it impossible to achieve, it’s typically more reliability than a service’s users want or notice. Match the profile of the service to the risk the business is willing to take.
> - An error budget aligns incentives and emphasizes joint ownership between SRE and product development. Error budgets make it easier to decide the rate of releases and to effectively defuse discussions about outages with stakeholders, and allows multiple teams to reach the same conclusion about production risk without rancor.