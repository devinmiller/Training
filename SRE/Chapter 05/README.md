# Eliminating Toil

>In SRE, we want to spend time on long-term engineering project work instead of operational work. Because the term operational work may be misinterpreted, we use a specific word: toil.

## Toil Defined

>Toil is the kind of work tied to running a production service that tends to be manual, repetitive, automatable, tactical, devoid of enduring value, and that scales linearly as a service grows.

The more work matches one of more of the following descriptions, the more likes it is to be toil:

### Manual

>This includes work such as manually running a script that automates some task.

### Repetitive

>Toil is work you do over and over.

### Automatable

>If a machine could accomplish the task just as well as a human, or the need for the task could be designed away, that task is toil.

### Tacticle

>Toil is interrupt-driven and reactive, rather than strategy-driven and proactive.

### No enduring value

>If your service remains in the same state after you have finished a task, the task was probably toil.

### O(n) with service growth

>If the work involved in a task scales up linearly with service size, traffic volume, or user count, that task is probably toil.

## Why Less Toil Is Better

Less toil means more time for the _Engineering_ part of Software Reliability _Engineering_.  That means more time for work that will be spent on reducing future toil or adding service features.

### Calculating Toil

Methods for calculating toil can vary, but generally it should be capped to under 50% of an SRE's time.

>When individual SREs report excessive toil, it often indicates a need for managers to spread the toil load more evenly across the team and to encourage those SREs to find satisfying engineering projects.

## What Qualifies as Engineering?

>Engineering work is novel and intrinsically requires human judgment. It produces a permanent improvement in your service, and is guided by a strategy.

Typical SRE activities fall into the following categories:

### Software engineering

>Involves writing or modifying code, in addition to any associated design and documentation work.

### Systems engineering

>Involves configuring production systems, modifying configurations, or documenting systems in a way that produces lasting improvements from a one-time effort.

### Toil

>Work directly tied to running a service that is repetitive, manual, etc.

### Overhead

>Administrative work not tied directly to running a service.

## Is Toil Always Bad?

Toil isn't always bad, and some toil is often unavoidable in an engineering role.  Toil becomes toxic when it is experienced in large quantities.  There are several reasons why too much tool is bad:

### Carrer Stagnation

>Your career progress will slow down or grind to a halt if you spend too little time on projects.

### Low morale

>People have different limits for how much toil they can tolerate, but everyone has a limit.

As well, toil also hurts the entire SRE organization:

### Creates confusion

>Individuals or teams within SRE that engage in too much toil undermine the clarity of that communication and confuse people about our role.

### Slows progress

>Excessive toil makes a team less productive

### Sets precedent

>If you’re too willing to take on toil, your Dev counterparts will have incentives to load you down with even more toil, sometimes shifting operational tasks that should rightfully be performed by Devs to SRE.

### Promotes attrition

>If you build too much toil into your team’s procedures, you motivate the team’s best engineers to start looking elsewhere for a more rewarding job.

### Causes breach of faith

> New hires or transfers who joined SRE with the promise of project work will feel cheated, which is bad for morale.

## Conclusion

Invent more, toil less.
