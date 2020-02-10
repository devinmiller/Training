# Release Engineering

Release engineering is a relatively new and fast-growing discipline of software engineering that can be concisely described as building and delivering software.  Release engineers have a solid (if not expert) understanding of source code management, compilers, build configuration languages, automated build tools, package managers, and installers.

## The Role of a Release Engineer

>Release engineers define best practices for using our tools in order to make sure projects are released using consistent and repeatable methodologies.

## Philosophy

>Release engineering is guided by an engineering and service philosophy that’s expressed through four major principles, detailed in the following sections.

### Self-Service Model

In order to work at scale, teams must be self-sufficient.  The goal of release engineering is to develop best practices and tools that allow product teams to control and run their own release process.  

Releases should be truely automatic, only requiring an engineer if and when a problem arises.

### High Velocity

Rolling out new features to customers as quickly as possible results in fewer changes between versions.  This approach makes testing and troubleshooting easier.

### Hermetic Builds

Build tools should ensure consistency and repeatability.  Builds should be heretic, meaning they:

- Are insensitive to the libraries and other software installed on the build machine
- Depend on known versions of build tools, such as compilers, and dependencies, such as libraries
- Are self-contained and must not rely on services that are external to the build environment

### Enforcement of Policies and Procedures

Who can perform specific operations when releasing a project is determined by several layers of security.  Gate operations include:

- Approving source code changes—this operation is managed through configuration files scattered throughout the codebase
- Specifying the actions to be performed during the release process
- Creating a new release
- Approving the initial integration proposal (which is a request to perform a build at a specific revision number in the source code repository) and subsequent cherry picks
- Deploying a new release
- Making changes to a project’s build configuration

>By allowing SREs to understand what changes are included in a new release of a project, this report can expedite troubleshooting when there are problems with a release

## Continuous Build and Deployment

This is an example very specific to Google, and worth reading directly from the book.

## Conclusions

>When equipped with the right tools, proper automation, and well-defined policies, developers and SREs shouldn’t have to worry about releasing software. Releases can be as painless as simply pressing a button.

### Start Release Engineering at the Beginning

>Teams should budget for release engineering resources at the beginning of the product development cycle. It’s cheaper to put good practices and process in place early, rather than have to retrofit your system later.
