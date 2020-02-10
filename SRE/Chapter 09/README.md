# Simplicity

>In fact, a good summary of the SRE approach to managing systems is: "At the end of the day, our job is to keep agility and stability in balance in the system."

## System Stability Versus Agility

The majority of production systems should have a balanced mix of stability and agility.  SREs should create procedures, practices, and tools for more reliable software, while ensuring this work has a minimal impact on developer agility.

>Building reliability into development allows developers to focus their attention on what we really do care about—the functionality and performance of their software and systems.

## The Virtue of Boring

Software should be boring, not spontaneous and interesting.

It is important to understand the difference between essential complixity and accidental complexity.

- Essential complexity is the complexity inherent in a given situation that cannot be removed from a problem definition
- accidental complexity is more fluid and can be resolved with engineering effort

In an effort to minimize accidental complexity, the SRE team should:

- Push back when accidental complexity is introduced into the systems for which they are responsible
- Constantly strive to eliminate complexity in systems they onboard and for which they assume operational responsibility

## I Won’t Give Up My Code!

Don't form emotional attatchments to code and don't be afraid to purge dead code.  Source control makes it easy to reverse any changes.

>SRE promotes practices that make it more likely that all code has an essential purpose, such as scrutinizing code to make sure that it actually drives business goals, routinely removing dead code, and building bloat detection into all levels of testing.

## The "Negative Lines of Code" Metric

Avoid software bloat.  Consider carefully before adding new features to a project.  Each line of code changed or added contains the potential for introducing new defects or bugs.

## Minimal APIs

>Writing clear, minimal APIs is an essential aspect of managing simplicity in a software system. The fewer methods and arguments we provide to consumers of the API, the easier that API will be to understand, and the more effort we can devote to making those methods as good as they can possibly be.

## Modularity

>The ability to make changes to parts of the system in isolation is essential to creating a supportable system. Specifically, loose coupling between binaries, or between binaries and configuration, is a simplicity pattern that simultaneously promotes developer agility and system stability.

## Release Simplicity

>Simple releases are generally better than complicated releases. It is much easier to measure and understand the impact of a single change rather than a batch of changes released simultaneously.

## A Simple Conclusion

>This chapter has repeated one theme over and over: software simplicity is a prerequisite to reliability. We are not being lazy when we consider how we might simplify each step of a given task.