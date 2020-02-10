# The Evolution of Automation at Google

>Software-based automation is superior to manual operation in most circumstances, better than either option is a higher-level system design requiring neither of them—an autonomous system.

## The Value of Automation

>What exactly is the value of automation?

### Consistency

>For a start, any action performed by a human or humans hundreds of times won’t be performed the same way each time: even with the best will in the world, very few of us will ever be as consistent as a machine. This inevitable lack of consistency leads to mistakes, oversights, issues with data quality, and, yes, reliability problems. In this domain—the execution of well-scoped, known procedures the value of consistency is in many ways the primary value of automation.

### A Platform

>Automation doesn’t just provide consistency. Designed and done properly, automatic systems also provide a platform that can be extended, applied to more systems, or perhaps even spun out for profit.

Unlike human meat bags, an automation platform can:

- Provide a centralized location for mistakes
  - A bug fixed in the code will be fixed there once and forever
- Be extended to perform additional tasks
- Run continuously or with a high frequency
- Export metrics about its performance
- Discover unknown details about processes

### Faster Repairs

>There’s an additional benefit for systems where automation is used to resolve common faults in a system (a frequent situation for SRE-created automation). If automation runs regularly and successfully enough, the result is a reduced mean time to repair (MTTR) for those common faults.

### Faster Action

>In the infrastructural situations where SRE automation tends to be deployed, humans don’t usually react as fast as machines.  In most common cases...it makes no sense to effectively require a human to intermittently press a button called “Allow system to continue to run.”

### Time Saving

>It’s easy to overlook the fact that once you have encapsulated some task in automation, anyone can execute the task. Therefore, the time savings apply across anyone who would plausibly use the automation. Decoupling operator from operation is very powerful

## The Use Cases for Automation

While the term "automation" is very broad in how it is used, it generally refers to "meta-software", or, software that is meant to act on software.

There are numerous examples, to list a few:

- User account creation
- Cluster turnup and turndown for services
- Software or hardware installation preparation and decommissioning
- Rollouts of new software versions
- Runtime configuration changes
- A special case of runtime config changes: changes to your dependencies

### A Hierarchy of Automation Classes

>Although all of these automation steps are valuable, and indeed an automation platform is valuable in and of itself, in an ideal world, we wouldn’t need externalized automation. In fact, instead of having a system that has to have external glue logic, it would be even better to have a system that needs no glue logic at all, not just because internalization is more efficient (although such efficiency is useful), but because it has been designed to not need glue logic in the first place.

The evolution of software automation usually follows a path:

1. No automation
1. Externally maintained system-specific automation
1. Externally maintained generic automation
1. Internally maintained system-specific automation
1. Systems that don’t need any automation

>SRE hates manual operations, so we obviously try to create systems that don’t require them. However, sometimes manual operations are unavoidable.

## Automate Yourself Out of a Job: Automate ALL the Things!

This is an example very specific to Google, and worth reading directly from the book.

## Reliability Is the Fundamental Feature

>For effective troubleshooting, the details of internal operation that the introspection relies upon should also be exposed to the humans managing the overall system

The downside of highly effective automation is over time, as human operators have less direct contact with a system, they are less able to successfully operate it should automation fail.  The knowledge has been lost due to a lack of practice.  

This is the reality of automation, but the benefits still outweigh the drawbacks.

>Reliability is the fundamental feature, and autonomous, resilient behavior is one useful way to get that.

## Recommendations

>Automation provides more than just time saving, so it’s worth implementing in more cases than a simple time-expended versus time-saved calculation might suggest. But the approach with the highest leverage actually occurs in the design phase: shipping and iterating rapidly might allow you to implement functionality faster, yet rarely makes for a resilient system. Autonomous operation is difficult to convincingly retrofit to sufficiently large systems, but standard good practices in software engineering will help considerably: having decoupled subsystems, introducing APIs, minimizing side effects, and so on.
