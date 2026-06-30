# Updating Automated Detection

This document is for developers who must update the "Automated Detection" sections in any of the guidelines. Typically, these developers support a static analysis tool, and they wish to add their tool to the table indicating its ability to enforce the guideline.

## Getting Started

At this point, we have one security policy: no changes shall be made to the main branch without a pull-request and at least one reviewer approves. As only the main branch is used for building the Secure Coding pages, this should prevent any malicious changes.  Anyone may branch or fork the repository, and anyone may create issues or pull requests.

You will need a Github account to make any changes, but creating one is free.

This means that to make any changes to the CERT standards, you must create a fork or branch of the project, make your changes, and submit a pull request.  There are several ways you can accomplish this. The simplest is to do everything on the Github website. Github provides several "web editors" that you can use without leaving your browser.  Or you can clone the repository to your own machine, make the changes, and push your commits.  The advantage of cloning the repo is that you can build your own local copy of the pages, and immediately validate any changes you make to them.

## Static Analysis Background

An understanding of the capabilities and limits of automated detection will help readers of this standard to better use the coding rules and guidelines.

There are three types of problems that static analysis can analyze for:

1.  syntactic;
2.  semantic; and
3.  depend on the intention of the programmer.

Automatic detection of syntactic problems can be 100% correct. Automatic detection methods for semantic problems can do well but cannot guarantee 100% detection because of the . Automated detection methods for problems that depend on the intention of the programmer cannot be 100% correct, and must depend on heuristics that attempt to intuit the intention of the programmer. For examples of automated detection of the third type of problem, see the paper [Automated Code Repair Based on Inferred Specifications](https://www.sei.cmu.edu/library/automated-code-repair-based-on-inferred-specifications/), that describes automated repairs for three types of bugs: integer overflows, missing array bounds checks, and missing authorization checks. Another example of automated detection of the third type of problem is that one static analysis tool provides an alert if in the analyzed codebase it detects that 4 of 5 times the code checks a particular function's return value to see if it is null, but in one case the return value isn't checked to see if it is null. In this way, it is inferring programmer intent from the other return value checks. A final example of automated detection inferring intent of the programmer is that one tool assumes a variable is sensitive if it is named "password" (and uses this inferred sensitivity for taint flow analyses).

By understanding the limits of automated detection for each coding rule in the standard, managers and developers can better use this standard.

Static analysis and automatic code repair tools are highly useful, but both have their limitations, and should be supplemented with additional secure coding lifecycle methods to increase security of the code. For some types of code flaws, automated static analysis still requires human inspection (a.k.a., auditors of the static analysis diagnostics) to determine if the automatically-generated warning is true or false. For other types of code flaws, automated analysis can correctly determine if the problem exists, and some tools also can automatically 'repair' (edit) the code to correct such problems. Some tools can edit code in a way that can be proven to not create new errors, even if the possible code flaw that was identified is not actually a true flaw (see paper  [Automated Code Repair Based on Inferred Specifications](https://www.sei.cmu.edu/library/automated-code-repair-based-on-inferred-specifications/).

Dynamic analysis (including fuzz testing, for instance using SEI's [Basic Fuzzing Framework](https://www.sei.cmu.edu/blog/cert-basic-fuzzing-framework/) fuzzing tool) can be automated, and can detect and verify some code flaws. Unit testing and regression testing can also be automated, and provide useful checks to a codebase.

For some code flaws, automated detection methods are too costly (take too much time, too much memory, or too much disk space) to be practical. Makers of automated detection tools (both proprietary code analysis tools and cost-free, open-source code analysis tools) must balance including the ability to check for a particular code flaw with the average user's cost, user's interest in finding that code flaw, and the false-positive rate of that particular code-flaw checker. Checkers that have high false-positive rates tend to displease tool users. For detailed discussion of the issues discussed in this paragraph, see the article [A Few Billion Lines of Code Later: Using Static Analysis to Find Bugs in the Real World](http://cacm.acm.org/magazines/2010/2/69354-a-few-billion-lines-of-code-later/fulltext) .

Widely-used automated code flaw detection tools often find somewhat-overlapping but quite different sets of code flaws, even just looking at automated static analysis tools (e.g., see SEI technical note, [Improving the Automated Detection and Analysis of Secure Coding Violations](http://resources.sei.cmu.edu/library/asset-view.cfm?assetID=295724) ).  Some code analysis frameworks use multiple analysis tools to analyze code for a wider variety of code flaws, however the number of code warnings (many of which are false positives) that must be manually inspected increases accordingly (for more information on this topic, see SEI blogpost [Prioritizing Alerts from Static Analysis to Find and Fix Code Flaws](https://insights.sei.cmu.edu/sei_blog/2016/06/prioritizing-alerts-from-static-analysis-to-find-and-fix-code-flaws.html) ).

Human code review is manual (not automated, although automation can help document findings and schedule reviews), but can detect some errors that widely-used automated static and dynamic analysis tools do not check for.

Software architecture also impacts a codebase's security, and some analyses of software architecture can be automated.

## Github Forking and Merging

We have published the following video about editing pages in Github:

[How to Update the SEI CERT Coding Standards in Github](https://www.youtube.com/watch?v=A11JgLKsoy0)

## Adding a Tool Page

First, you should create an empty page for the tool of interest under the "Analyzers" section of the backmatter, in each appropriate language space. It may be the case that a page already exists for the tool, in which case you can skip this step.  Below are links to the "Analyzers" sections for each space.

| Space   | Analyzers Page                                                                                                |
|---------+---------------------------------------------------------------------------------------------------------------|
| C       | [EE. Analyzers](/sei-cert-c-coding-standard/back-matter/ee-analyzers/)                                        |
| C++     | [CC. Analyzers](/sei-cert-cpp-coding-standard/back-matter/cc-analyzers/)                                      |
| Java    | [Rule or Rec. CC. Analyzers](/sei-cert-oracle-coding-standard-for-java/back-matter/rule-or-rec-cc-analyzers/) |
| Perl    | [BB. Analyzers](/sei-cert-perl-coding-standard/back-matter/bb-analyzers/)                                     |
| Android | [BB. Analyzers](android-secure-coding-standard/back-matter/bb-analyzers)                                      |

The page should be titled with the name of the analysis tool.  Eventually, the page will be automatically populated with the information that you provide on individual rule/rec pages, but for now, you should populate this page manually with the information about your tool.

Additionally, a "version" page should be created alongside the tool page.  This page is titled *ToolName_V* , should be populated with the version number of the tool. For example, [GCC_V](/sei-cert-c-coding-standard/back-matter/ee-analyzers/gcc_v) documents the version of the GCC compiler. You are responsible for entering the version information into this page.

## Editing Automated Detection Tables

Each rule/rec page has an *Automated Detection* (AD) section, describing which tools can detect violations of the rule/rec. This section contains a table. Each row of the table contains information for a specific version of a tool. A row in the AD table has the following format.

| Tool                         | Version                 | Checker        | Description           |
|------------------------------+-------------------------+----------------+-----------------------|
|                              |                         | Checker Name 1 | Checker Description 1 |
| Hyperlinked name of the tool | The version of the tool | Checker Name 2 | Checker Description 2 |
|                              |                         | Checker Name 3 | Checker Description 3 |
|                              |                         | ...            | ...                   |

Eventually each tool page will be updated with the aggregated data from these individual tables. This aggregation process is automatic. In order for the process to pick up your changes, you should adhere to certain guidelines when entering data into the AD tables.

1.  The **Tool** column should contain the name of the tool, hyperlinked to the corresponding tool page.
    1.  The easiest way to populate this field is with the Link macro in Confluence. Simply insert a Link macro and point it towards the appropriate tool page.
2.  The **Version** column contains the version of the tool to which this information pertains.  
    1.  The easiest way to populate this field is with the "Include Page" macro in Confluence. You should include the version page associated with the tool into this cell.
3.  Each checker name should be provided on a separate line in the **Checker** column.
4.  Each checker description should be provided on a separate line in the **Description** column, adjacent to the associated checker.
