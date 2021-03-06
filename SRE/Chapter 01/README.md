# Software Reliability Engineering

Almost all of these notes were taken directly from Google's book, [_the book_](https://landing.google.com/sre/sre-book/toc/index.html), about software reliability engineering.  This is the important information that stands out in my mind from reading the book.

## The Sysadmin Approach to Service Management

>This systems administrator, or sysadmin, approach involves assembling existing software components and deploying them to work together to produce a service. Sysadmins are then tasked with running the service and responding to events and updates as they occur. As the system grows in complexity and traffic volume, generating a corresponding increase in events and updates, the sysadmin team grows to absorb the additional work. Because the sysadmin role requires a markedly different skill set than that required of a product’s developers, developers and sysadmins are divided into discrete teams: "development" and "operations" or "ops."

### Advantages

- This approach is relatively easy to implement
  - Familiar industry paradigm with many examples
- Relevant talent pool is widely available
- A wide array of pre-existing tools, software components, and integration companies are available
  - Novice teams do not need to reinvent te wheel and design a system from scratch

### Disadvantages

- Direct Costs
  - Manual intervention for change management and event handling becomes expensive as the service grows
  - Size of the team necessarily scales with the load generated by the system
- Indirect Costs
  - Can be subtle, but often more expensive that the direct costs
  - Costs arise from the fact that the two teams are quite different in background, skill set, and incentives
    - Use different vocabulary to describe situations
    - Carry different assumptions about both risk and possibilities for technical solutions
    - Have different assumptions about the target level of product stability

### Result

>The split between the groups can easily become one of not just incentives, but also communication, goals, and eventually, trust and respect. This outcome is a pathology.
>
>Traditional operations teams and their counterparts in product development thus often end up in conflict, most visibly over how quickly software can be released to production. At their core, the development teams want to launch new features and see them adopted by users. At their core, the ops teams want to make sure the service doesn’t break while they are holding the pager. Because most outages are caused by some kind of change—a new configuration, a new feature launch, or a new type of user traffic—the two teams’ goals are fundamentally in tension.

## Google’s Approach to Service Management: Site Reliability Engineering

>Conflict isn’t an inevitable part of offering a software service. Google has chosen to run our systems with a different approach: our Site Reliability Engineering teams focus on hiring software engineers to run our products and to create systems to accomplish the work that would otherwise be performed, often manually, by sysadmins.

Site Reliability Engineering is what happens when you ask a software engineer to design an operations team.  A primary building block of this approach to service management is the composition of the SRE team, which can be broken down into two main categories:

- 50-60% are standard software engineers
- 40-50% are close to software engineer qualifications, but also possess technical skills rare among software engineers
  - For Example, UNIX system internals and networking expertise

Common to all SREs should be the belief in and aptitude for developing software systems to solve complex problems.  The end result will be a team of people who:

1. Will quickly become bored by performing tasks by hand
1. Have the skill set necessary to write software to replace previously manual work

>Therefore, SRE is fundamentally doing work that has historically been done by an operations team, but using engineers with software expertise, and banking on the fact that these engineers are inherently both predisposed to, and have the ability to, design and implement automation with software to replace human labor.
>
>By design, it is crucial that SRE teams are focused on engineering. Without constant engineering, operations load increases and teams will need more people just to keep pace with the workload. Eventually, a traditional ops-focused group scales linearly with service size: if the products supported by the service succeed, the operational load will grow with traffic. That means hiring more people to do the same tasks over and over again.

This approach to running large-scale systems has many advantages:

- SRE teams are characterized by rapid innovations and a large acceptance of change
- SRE teams are relatively inexpensive
  - Supporting the same service with an ops-oriented team would require a significantly larger number of people
  - The number of SREs needed to run, maintain, and improve a system scales sublinearly with the size of the system
- Circumvents the dysfunction of the dev/ops split
- Improves product development teams
  - Easy transfers between product development and SRE teams cross-train the entire group
  - Improve skills of developers who otherwise may have difficulty learning how to build distributed system

## Tenets of SRE

> In general, an SRE team is responsible for the availability, latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning of their service(s).

### Ensuring a Durable Focus on Engineering

- Operational work for SREs should be capped at 50% of their time
  - Remaining time should be spent using coding skills on project work
- SREs should receive a maximum of two events per 8-12 hour on-call shift
- Postmortems should be written for all significant incidents incidents
  - Done regardless of whether or not a page was received
  - Postmortems that did not trigger a page can indicate monitoring gaps
  - Utilize a blame-free postmortem culture
    - Goal of exposing faults and applying engineering to fix, rather than avoiding or minimizing

### Pursuing Maximum Change Velocity Without Violating a Service’s SLO

The SRE and product development teams enjoy a productive working relationship through eliminating conflict in their respective goals.  This conflict is between the pace of innovation, driven by the product development team, and product stability, desired by the SRE team.  In SRE, this conflict is resolved through the use of an error budget.

The concept of an error budget stems from the observation that 100% is the wrong reliability target for basically any system.  This is because most users will not notice the difference between 100% available versus 99.99% available.  The user receives no benefit from the enormous effort require to add the last .01% availability.

Determining the correct reliability target for a system depends on the following considerations:

- What level of availability will the users be happy with, given how they use the product?
- What alternatives are available to users who are dissatisfied with the product’s availability?
- What happens to users’ usage of the product at different availability levels?

The business or product must establish the system's availability target.  Once done, the error budget is one minus the availability target.  So a system that is 99.99% available is .01% unavailable.  The permitted .01% unavailability is considered the system's error budget.

>So how do we want to spend the error budget? The development team wants to launch features and attract new users. Ideally, we would spend all of our error budget taking risks with things we launch in order to launch them quickly. This basic premise describes the whole model of error budgets. As soon as SRE activities are conceptualized in this framework, freeing up the error budget through tactics such as phased rollouts and 1% experiments can optimize for quicker launches.

The goal is no longer zero outages, rather, SREs and product developers spend the error budget getting maximum feature velocity.  An outage is no longer a bad thing, but an expected part of the process of innovation.  It is an occurrence to be managed rather than feared. 

### Monitoring

>Monitoring is one of the primary means by which service owners keep track of a system’s health and availability. As such, monitoring strategy should be constructed thoughtfully.
>
>Monitoring should never require a human to interpret any part of the alerting domain. Instead, software should do the interpreting, and humans should be notified only when they need to take action.

There are three kinds of valid monitoring output:

#### Alerts

> Signify that a human needs to take action immediately in response to something that is either happening or about to happen, in order to improve the situation.

#### Tickets

>Signify that a human needs to take action, but not immediately. The system cannot automatically handle the situation, but if a human takes action in a few days, no damage will result.

#### Logging

>No one needs to look at this information, but it is recorded for diagnostic or forensic purposes. The expectation is that no one reads logs unless something else prompts them to do so.

### Emergency Response

>Reliability is a function of mean time to failure (MTTF) and mean time to repair (MTTR). The most relevant metric in evaluating the effectiveness of emergency response is how quickly the response team can bring the system back to health—that is, the MTTR.

Humans add latency.  A system that can avoid emergencies that require human intervention will have higher availability than a system that requires hands-on intervention.  When humans are necessary, thinking through and recording best practices ahead of time in a playbook produces improvement in MTTR over the strategy of winging it.  While no playbook is a substitute for an engineer able to think on the fly, clear and thorough troubleshooting steps are valuable when responding to high-stakes or time0sensitive issues.

### Change Management

Roughly 70% of outages are due to changes in a live system. Best practices in this domain use automation to accomplish the following:

- Implementing progressive rollouts
- Quickly and accurately detecting problems
- Rolling back changes safely when problems arise

These practices minimize the number of users and operations exposed to bad changes.Removing humans from the loop avoids the normal problems of fatigue, familiarity/contempt, and and inattention to highly repetitive tasks.  As a result, both release velocity and safety increase.

### Demand Forecasting and Capacity Planning

>Demand forecasting and capacity planning can be viewed as ensuring that there is sufficient capacity and redundancy to serve projected future demand with the required availability.

Capacity planning should take the following into consideration:

- Organic growth
  - stems from the natural product adoption and usage by customers
- Inorganic growth
  - Results from events like feature launches, marketing campaigns, or other business-driven change

Several steps are mandatory in capacity planning:

- An accurate organic demand forecast, which extends beyond the lead time required for acquiring capacity
- An accurate incorporation of inorganic demand sources into the demand forecast
- Regular load testing of the system to correlate raw capacity(servers, disks, and so on) to service capacity

>Because capacity is critical to availability, it naturally follows that the SRE team must be in charge of capacity planning, which means they also must be in charge of provisioning.

### Provisioning

Provisioning is a combination of both change management and capacity planning.  

- Provisioning must be conducted quickly and only when necessary, as capacity is expensive
- Provisioning must be done correctly, or capacity doesn't work when needed

Provisioning is a risky operation and must be treated with an extra degree of caution.  It often involves:

- Spinning up a new instance or location
- Making significant modification to existing systems
  - For example - configuration files, load balancers, networking
- Validating that the new capacity performs and delivers correct results

### Efficiency and Performance

>Because SRE ultimately controls provisioning, it must also be involved in any work on utilization, as utilization is a function of how a given service works and how it is provisioned. It follows that paying close attention to the provisioning strategy for a service, and therefore its utilization, provides a very, very big lever on the service’s total costs.
>
>Resource use is a function of demand (load), capacity, and software efficiency. SREs predict demand, provision capacity, and can modify the software. These three factors are a large part (though not the entirety) of a service’s efficiency.
>
>SREs provision to meet a capacity target at a specific response speed, and thus are keenly interested in a service’s performance. SREs and product developers will (and should) monitor and modify a service to improve its performance, thus adding capacity and improving efficiency
