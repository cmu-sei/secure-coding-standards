# Formatting and Style

## Headings

Use "Noncompliant Code Example" and "Compliant Solution." These can be followed by a lowercase code descriptor or an uppercase text element in parentheses. Any code should be in Courier and not initial capped (e.g., `calcPercentage` ).

Hyphenate Implementation-Specific Details.

## Citations in the text

Put square brackets around citations to set them off from the text.

Use a citation in the text when directly quoting or paraphrasing material from a source. If you're quoting from a specific page in a book, include the page number as in this example: \[Seacord 2013, p. 63\]. A page range would be \[Seacord 2013, pp. 172–5\].

Citations should not be used as nouns:

<table><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td class="highlight-red" data-highlight-colour="red"><strong>INCORRECT</strong></td><td class="highlight-red" data-highlight-colour="red">According to [Seacord 2013], . . .</td></tr><tr class="even"><td class="highlight-green" data-highlight-colour="green"><p><strong>CORRECT</strong> <strong><br />
</strong></p></td><td class="highlight-green" data-highlight-colour="green"><p>According to <em>Secure Coding in C and C++</em> , &lt;"quoted" or paraphrased material&gt; [Seacord 2013, p. 43].<br />
<em>or</em><br />
According to Robert Seacord, &lt;"quoted" or paraphrased material&gt;  [Seacord 2013, p. 43].</p></td></tr><tr class="odd"><td class="highlight-red" data-highlight-colour="red"><strong>INCORRECT</strong></td><td class="highlight-red" data-highlight-colour="red">[ISO/IEC 9899:2011] states. . . .</td></tr><tr class="even"><td class="highlight-green" data-highlight-colour="green"><strong>CORRECT</strong></td><td class="highlight-green" data-highlight-colour="green">The C Standard, subclause 7.2.1 [ISO/IEC 9899:2011], states. . . .</td></tr><tr class="odd"><td class="highlight-red" data-highlight-colour="red"><strong>INCORRECT</strong></td><td class="highlight-red" data-highlight-colour="red">See [Plum 2012] for details.</td></tr><tr class="even"><td class="highlight-green" data-highlight-colour="green"><strong>CORRECT</strong></td><td class="highlight-green" data-highlight-colour="green">See "C Finally Gets a New Standard" [Plum 2012] for details.</td></tr></tbody></table>

## Internal cross-references

Internal cross-references such as "(See [STR02-A. Sanitize data passed to complex subsystems](/sei-cert-c-coding-standard/recommendations/characters-and-strings-str/str02-c) for more information.)" are not citations. Do not put square brackets around them (except those used for creating the link). They should be in parentheses unless they're being used as nouns: "In \[STR02-A. Sanitize data passed to complex subsystems\], for example, . . ."

Use "see" alone, without "rule" or "guideline" after it.

## References in the Bibliography and Related Guidelines sections

Bibliography entries should consist of the same bracketed citation that appears in the text and, optionally, a chapter or a section title. The citation should be linked to a corresponding complete reference on the site-wide Bibliography page.

When multiple chapters, sections, guidelines, and so on, are cited from the same source, list them on separate lines but in the same cell. See the example for ISO/IEC TR 24772:2013 in the following table.

Including a section number and title, chapter number and title, and so on, is optional. Use the formats shown in the following table:

<table><colgroup><col style="width: 33%" /><col style="width: 33%" /><col style="width: 33%" /></colgroup><tbody><tr class="odd"><td colspan="3" class="highlight-green" data-highlight-colour="green"><strong>Bibliography Entries</strong></td></tr><tr class="even"><td><strong>Section of a book</strong></td><td>Spell out <em>Section</em> , use title caps</td><td>Section 2.8.3, "Section Title"</td></tr><tr class="odd"><td><strong>Chapter of a book</strong></td><td>Spell out <em>Chapter</em> , use title caps</td><td>Chapter x, "Chapter Title"</td></tr><tr class="even"><td><strong>C Standard</strong> [ <a href="https://www.securecoding.cert.org/confluence/display/seccode/AA.+Bibliography#AABibliography-ISOIEC9899-2011">ISO/IEC 9899:2011</a> ]</td><td>Use <em>Clause</em> for first level section<br />
Use <em>Subclause</em> for subsequent sections</td><td><p>Clause 7, "Clause Title"<br />
Subclause 7.21.6.1, "The <code>       fprintf      </code> Function"</p></td></tr><tr class="odd"><td><strong>C++ Standard</strong> [ <a href="/sei-cert-cpp-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO/IEC14882-2003">ISO/IEC 14882-2003</a> ]</td><td>Use <em>Clause</em> for first level section<br />
Use <em>Subclause</em> for subsequent sections</td><td>Clause 5, "Expressions<br />
Subclause 5.14, "Logical AND Operator"</td></tr><tr class="even"><td><strong>Java Language Specification</strong> [ <a href="/sei-cert-oracle-coding-standard-for-java/back-matter/rule-aa-references#RuleAA.References-JLS15">JLS 2015</a> ]</td><td>Use section symbol §, not the word <em>section€?<br />
</em> Hyperlink to the chapter or section cited</td><td><a href="http://docs.oracle.com/javase/specs/jls/se8/html/jls-16.html">Chapter 16, "Definite Assignment"</a> <a href="http://docs.oracle.com/javase/specs/jls/se8/html/jls-17.html#jls-17.4.3"><br />
§17.4.3, "Programs and Program Order"</a></td></tr><tr class="odd"><td><p><strong>Java Tutorials</strong> [ <a href="/sei-cert-oracle-coding-standard-for-java/back-matter/rule-aa-references#RuleAA.References-JavaTutorials">Java Tutorials</a> ]</p></td><td>Was [Tutorials 08]; update to Java Tutorials and include link in section title</td><td><a href="http://java.sun.com/j2se/1.4.2/docs/guide/lang/assert.html">Programming With Assertions</a></td></tr><tr class="even"><td><strong>Miscellaneous</strong></td><td><p>Rules, recommendations, questions, and similar lengthy items should be sentence case without quotation marks<br />
<br />
<br />
<br />
<br />
Gotchas, puzzles, and similar items with short titles should be title case and enclosed in quotation marks</p></td><td><p>AV Rule xx, Rule title in sentence case, no quotation<br />
marks<br />
Recommendation 12.5, Do not let destructors called<br />
during stack unwinding throw exceptions<br />
Question xx, Write out the question in sentence case,<br />
no quotation marks [or link to the question]<br />
Gotcha #xx, "Title of Gotcha"<br />
Item xx, "Title of Item"</p></td></tr><tr class="odd"><td colspan="3" class="highlight-green" data-highlight-colour="green"><strong>Related Guidelines Entries (note that these entries do not belong in the Bibliography section)</strong></td></tr><tr class="even"><td><p><a href="/sei-cert-c-coding-standard/">SEI CERT C Coding Standard</a></p></td><td rowspan="4"><p>Link to main page of source<br />
Link guideline to its page<br />
Make sure exact space title is used: for example, "SEI CERT C Coding Standard," not "The CERT C Secure Coding Standard"</p></td><td><a href="/sei-cert-c-coding-standard/recommendations/characters-and-strings-str/str02-c">STR02-C. Sanitize data passed to complex subsystems</a></td></tr><tr class="odd"><td><p><a href="/sei-cert-cpp-coding-standard/">SEI CERT C++ Coding Standard</a></p></td><td><p><a href="https://wiki.sei.cmu.edu/confluence/spaces/cplusplus/pages/88046726/VOID+STR02-CPP.+Sanitize+data+passed+to+complex+subsystems">VOID STR02-CPP. Sanitize data passed to complex subsystems</a></p></td></tr><tr class="even"><td><a href="/sei-cert-perl-coding-standard/">SEI CERT Perl Coding Standard</a></td><td><a href="/sei-cert-perl-coding-standard/rules/input-validation-and-data-sanitization-ids/ids33-pl">IDS33-PL. Sanitize untrusted data passed across a trust boundary</a></td></tr><tr class="odd"><td><a href="/sei-cert-oracle-coding-standard-for-java/">SEI CERT Oracle Coding Standard for Java</a></td><td><a href="/sei-cert-oracle-coding-standard-for-java/recommendations/miscellaneous-msc/msc51-j">MSC51-J. Do not place a semicolon immediately following an if, for, or while condition</a></td></tr><tr class="even"><td><a href="/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO-IECTS17961">ISO/IEC TS 17961</a></td><td>Sentence case; include identifier in square braces</td><td>Escaping of the address of an automatic object [addrescape]</td></tr><tr class="odd"><td><a href="/sei-cert-oracle-coding-standard-for-java/back-matter/rule-aa-references#RuleAA.References-ISO/IECTR24772-2013">ISO/IEC TR 24772:2013</a></td><td>Title case, three-letter identifier in square braces at end of title</td><td><p>Boundary Beginning Violation [XYX]<br />
Wrap-around Error [XYY]<br />
Unchecked Array Indexing [XYZ]</p></td></tr><tr class="even"><td><a href="http://cwe.mitre.org/">MITRE CWE</a></td><td>CWE number, name in title caps, no quotation marks<br />
Link CWE number but don't link title text</td><td><a href="http://cwe.mitre.org/data/definitions/192.html">CWE-192</a> , Integer Coercion Error</td></tr><tr class="odd"><td><a href="/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12">MISRA C:2012</a></td><td>USE RULE NUMBER ONLY: Do not use the rule text (for copyright reasons)</td><td>Rule 18.6 (required)</td></tr><tr class="even"><td><a href="http://www.oracle.com/technetwork/java/seccodeguide-139067.html">Secure Coding Guidelines for Java SE, Version 5.0</a></td><td>Replaces Secure Coding Guidelines for the Java Programming Language, version 3.0<br />
Guideline numbers changed in the new version and must be updated</td><td>Guideline 4-5 / EXTEND-5: Limit the extensibility of classes and methods</td></tr></tbody></table>

Do not put a period at the end of a reference listing.

If the source is an extensive online document that is already on the Bibliography page and you want to cite and link to a particular section, create the link on the section number and name (if you're including the latter). See the \[ [Summit 2005](https://www.securecoding.cert.org/confluence/display/seccode/AA.+Bibliography#AABibliography-Summit05) \] [Question 1.13](http://c-faq.com/decl/typedefvsdefine.html) , [Question 11.11](http://c-faq.com/ansi/typedefconst.html) entry in the bibliography of PRE03-C as an example.

## Using Courier (monospace) font for code

Use monospace font for keywords, variables, register names, and code. DO NOT USE when word is being used as an adjective. For example, say "the `volatile` keyword," but say "€œwhen the element is volatile."€? Do not use monospace for final, private, public, or static in text (e.g., "€œDeclare instance variables final"€?).

## Coding guidelines

### Comments

For comments in C, use the following form:

One-line comment:

`   /* Comment */  `

Multiline comment:

`   /*      * The comment starts on a new line after      * the slash-asterisk, and the ending      * asterisk-slash goes on a separate line      * after the last word of the comment. All of      * the asterisks should be aligned.      */     `

**One-line comments:** Capitalize the first word; do not add ending period even if comment is a complete sentence. Both of the following are correct in style:

`   /* This is a complete sentence */  `

`   /* Not a complete sentence */  `

If the first word of a comment is a code literal, lowercase is fine:

`   /* malloc destination string */  `

Vague comments such as `   /* etc. */  `,`   /* Do something */  `,`   /* Interesting stuff happens here */  ` , should be changed to `   /* ... */  `.`     `

**Multiline comments:** Capitalize the first word. Use ending punctuation in complete sentences:

`   /*      * Use assembly code to retrieve i  `

<div class="line number4 index3 alt1" style="margin-left: 30.0px;">

`   * implicitly from caller  `

</div>

<div class="line number5 index4 alt2" style="margin-left: 30.0px;">

`   * and transfer it to a less privileged file.      */  `

</div>

## Exceptions

Enumerate exceptions as EX1–EX *n* preceded by the rule tag. *Start numbering at 1, not 0.* For example:

**MET08-EX1:** Requirements of this rule may be violated provided that the incompatible types are never compared.

## Colons

### Lists

When introducing lists, colons should be used only at the end of a *complete sentence* . They bring the reader to a complete stop as much as a period does. So use a colon to introduce a list only if what precedes the colon is a complete sentence.

#### Noncompliant Colon Example (Lists)

::code-block{quality="bad"}
``` java
Guidelines identifiers consist of:
* A three-letter mnemonic
* A two-digit numeric value
* The letter "A" or "C"
```
::

#### Compliant Solution 1 (Lists)

::code-block{quality="good"}
``` java
Guidelines identifiers consist of
* A three-letter mnemonic
* A two-digit numeric value
* The letter "A" or "C"
```
::

#### Compliant Solution 2 (Lists)

::code-block{quality="good"}
``` java
Guidelines identifiers consist of three parts:
* A three-letter mnemonic
* A two-digit numeric value
* The letter "A" or "C"
```
::

### Quotations

The complete-sentence rule doesn't apply, however, when introducing a quotation. Just about anything goes. Except this:

#### Noncompliant Colon Example (Quotations)

::code-block{quality="bad"}
``` java
C11 says: [ISO/IEC 9899:2011]
```
::

#### Compliant Solution (Quotations)

::code-block{quality="good"}
``` java
C11 [ISO/IEC 9899:2011] says:
```
::

## Spelling and usage

<div class="WordSection1">

The C Standard and *Merriam-Webster's Collegiate Dictionary* , 11th edition, are helpful guides to style, particularly in deciding whether or not to hyphenate.  
(adj, adjective; adv, adverb; n, noun; pa, predicate adjective; v, verb)  
  

</div>

#### A

among, *not* amongst *  
anti* : close up unless noted here:  
anti-pattern  
application specific (pa); application-specific (adj)  
arbitrary-precision integer type  
arc injection attack  
array-like  
as-if infinitely ranged (AIR) integer model  
asynchronous-safe (adj, pa)  
autoboxing  
autoflush  
  

#### B

back end (n); back-end (adj)  
back pointer ( *not* backward pointer)  
backquotes ( \` )  
backslash  
backup (adj, n); back up (v)  
bareword  
bit-field (n, adj) (based on use in C Standard)  
blacklist (one word, no hyphen; adj, n, v)  
Boolean, not boolean (except in code)  
bounds-checking (adj, v)  
built in (pa), built-in (adj)  
bypass ( *not* by-pass)  
by-product  
bytecode  
byte order–related  
byte-ordering (adj)  
byte stream  
  

#### C

C Standard, but C standard library  
C++ Standard, but C++ standard library  
character handling (adj)  
cleanup (n, adj); clean up (v)  
cleartext  
client-side (adj)  
cloneable  
codebase  
command line (n); command-line (adj)  
compile time  
co-opt  
copy-initialize  
cross-platform  
cross-process (adj)  
  

#### D

data is singular (data *is* )  
dataflow  
data type  
deadlock-like  
deallocate  
declare volatile, *not* declare as volatile  
defense-in-depth (adj)  
denial of service (n); denial-of-service (adj)  
divide-by-zero error  
double-checked locking idiom  
double-linked (adj.), *not* doubly-linked  
doubleword ( *not* double word)  
`do-while` loop (n)  
dynamic locking (n, pa) dynamic-locking (adj)  
  

#### E

early-precedence logical operators  
e.g., (use in parentheses only, followed by a comma; *but prefer* “for example,”)  
email  
end-of-file (n)  
endpoints  
error-handling (adj)  
error-prone (adj); error prone (pa)  
error-recovery (adj)  
error-return behavior  
execute-around idiom  
  

#### F

42BSD system  
fail safe (pa)  
failsafe (adj)  
Fibonacci function  
file handle  
file name (not filename)  
file system ( *not* filesystem)  
fixed-code (adj)  
fixed-length (adj)  
floating point (n); floating-point (adj)  
for-each idiom  
forward and back pointers  
forward-looking (adj)  
forward slash  
functionlike (adj)  
  

#### G

garbage-collected (v)  
garbage-collection (adj)  
garbage-collection-ready  
garbage collector can be abbreviated GC in adjective form  
GCC compiler, not gcc  
getter and setter methods instead of get and set methods  
greatest-width (adj)  
  

#### H

happens-before (n, adj, v in discussions of JMM partial ordering)  
handoff  
hard code (v), *not* hardcode; *but* hard-coded (adj)  
hash table  
host name  
  

#### I

i.e., (use in parentheses only, followed by a comma; otherwise, use “that is,”)  
implementation-defined (a, pa) (always hyphenate)  
implementation-specific  
inbound (as in *incoming* )  
in-bounds (as in within the boundaries of)  
inlined (v)  
interclass  
intraclass  
I/O (not IO, except in page titles)  
  

#### J, K

JAR is always capitalized when referring to a JAR file (using regular font); jar is lowercase only when  
\* Referring to the `jar` utility (using monospace font)  
\* Used in the file name of a JAR file (e.g., foo.jar)

Java Collection Framework  
Java compiler  
*The Java Language Specification*  
Java Virtual Machine  
JavaBeans  
JDBC: Do not expand  
  

#### L

late-precedence logical operators  
left-shifting  
life cycle  
lifetime  
lockstep  
login (n, adj); log in (v)  
look-ahead (n)  
look-aside (adj)  
  

#### M

memorized  
memory management (n, adj)  
memory-mapped (adj)  
metacharacter  
method-chaining (adj)  
mix-and-match attack  
multi: *do not hyphenate unless noted here  
* multi-arg  
multibyte-encoded (adj)  
multiple-precision arithmetic  
multitranslation  
mutual-exclusion lock  
  

#### N

name space  
natural-language (adj)  
newline  
*non* : close up (noncompliant, nonunique, nonvolatile) except as noted:  
non-array  
non-atomic  
non- `const`  
non-debugging  
non-garbage-collected  
non-keyword  
non-null  
non-prototype-format (adj)  
non-reentrant  
non-reifiable  
non-safety-critical (adj; e.g., a non-safety-critical operation)  
non–safety critical (pa; e.g., the operation is non–safety critical) (use en dash)  
non-volatile-qualified (note that volatile is *not* set in code font)  
nonfinal  
nongeneric  
nonnative  
nonnegative  
nonpadding  
nonpublic  
nonunique  
nonzero  
no-operation (n)  
`NULL` (n) in “set to `NULL` ,” “returns `NULL` ,” etc.; otherwise, null (adj)  
null terminator  (n); null-terminate (v); null-terminated (a, pa)  
numeric value  
numerical analysis  
  

#### O

off-by-one (adj)  
out-of-range error (adj) (but an error is out of range *hyphenate as adj. only:* )  
overaligned  
  

#### P

package-private access  
pagelock  
path name (not pathname)  
path-dependent (adj)  
per-operation (adj)  
placement new operator (no monospace; C++ specific)  
plain-character-typed or plain-wide-character-typed expressions  
plain old function (no caps)  
platform-independent (adj, pa)  
platform-specific (adj, pa)  
point-and-click (adj)  
pointer intensive  
policymakers  
POSIX ( *not* Posix); no need for ™ symbol except in title *Portable Operating System Interface (POSIX®), Base Specifications, Issue 7*  
**NOTE:** Use *Portable Operating System Interface (POSIX®), Base Specifications, Issue 7* at first mention in a section; thereafter use  
POSIX or, when appropriate, POSIX standard  
post: close up (postcondition) unless noted here  
postinitialization  
pre: close up  
precondition  
preincremented  
preinitialized  
programmatically  
pseudocode  
pseudorandom  
  

#### Q, R

reallocate  
range-checking (n, adj, v)  
read-write lock  
reference-counted pointer  
remote-code-execution attack  
rethrown  
reverse engineer  
rightmost  
right-shifted  
round-to-nearest mode  
roundtrip  
runtime (n, adj)  
runtime-constraint (adj)

#### S

shared-memory (adj)  
shellcode ( *not* shell code)  
shortcut  
side effect (n)  
side-effect-free (adj)  
side-effect-infested (adj)  
sign-extended (pa); sign-extension (n)  
single-threaded (adj, pa)  
singleton, but Singleton pattern; `Singleton` class  
source code–checking (adj)  
spin-waiting  
a SQL ( *not* an SQL)  
StackGap (by OpenBSD)  
stack-smashing (adj)  
startup (n)  
straightforward, *not* straight forward  
string-handling (adj)  
`struct`  
*sub* : close up (subclause, subobject) except as noted: sub-subclause  
superclass  
superconstructor  
symlinked  
systemwide  
  

#### T

taint mode (a Perl feature—lowercase)  
thread management (n, adj)  
thread-role analysis  
thread-safe (adj, pa)  
thread safety (n)  
thread-starvation deadlock  
thread-scheduling interleaving  
timeshare; timeshared  
trade-off  
two’s complement (adj)  
type cast, type casting  
type-check (v); type checking (n)  
type-punning  
type-qualified (adj); type qualified (pa); type-qualify (v)  
type safety (n); type-safety (adj)  
  

#### U

UNIX, *not* Unix  
upcall  
user interface toolkit (no caps)  
user name

#### V

variable length array (VLA)  
virtual machine ( *not* Virtual Machine)  
volatile sets in running font except in cases such as  
`volatile` keyword  
declared `volatile`  
volatile-qualified (adj)  
volatile-read, synchronized-write technique  
  

#### W

wait/notify mechanism  
wakeup (n)  
warm-starting (v)  
website  
WebSphere  
whitelist, whitelisting (not white-list or white list)  
whitespace  
wide character (n, adj)  
  

#### X, Y, Z

XML external entity attack  
XML injection  
zero-fill (v)  
zeros

### Avoid wordiness

|                               |                                           |
|-------------------------------|-------------------------------------------|
| **INSTEAD OF**                | **PREFER**                                |
| a large number \[proportion\] | many                                      |
| adversary,  adversarial user  | attacker                                  |
| ahead of schedule             | early                                     |
| as a result of                | because of                                |
| as to whether                 | whether                                   |
| as yet                        | yet                                       |
| by the name of                | named                                     |
| carry out                     | perform,   conduct                        |
| could                         | can, esp. in Risk Assessment              |
| distinguish the difference    | distinguish                               |
| during that time              | while                                     |
| eliminate altogether          | eliminate                                 |
| every now and then            | now and then, occasionally                |
| fewer in number               | fewer                                     |
| filled to capacity            | filled                                    |
| general rule                  | rule                                      |
| give rise to                  | cause                                     |
| hence                         | for that reason                           |
| illustrates                   | shows                                     |
| in order to                   | to                                        |
| in order for                  | for                                       |
| in \[with\] regard to         | about,   regarding                        |
| in advance of                 | before                                    |
| in close proximity to         | near                                      |
| in terms of                   | in,   of, for                             |
| is able to                    | can                                       |
| last \[first\] of all         | last, first                               |
| near to                       | near                                      |
| needs to                      | must                                      |
| outside of                    | outside                                   |
| results in                    | causes                                    |
| since                         | because  (if expressing cause and effect) |
| take into consideration       | consider                                  |
| therefore                     | as a result, consequently                 |
| thus                          | consequently, as a result                 |
| uniformly consistent          | consistent, uniform                       |

## Common acronyms, initialisms, abbreviations

|         |                                                          |
|---------|----------------------------------------------------------|
| ACL     | access control list                                      |
| AES     | Advanced Encryption Standard                             |
| AIR     | as-if infinitely ranged                                  |
| API     | application programming interface                        |
| ARM     | Advanced RISC (Reduced Instruction Set Computer) Machine |
| ASLR    | address space layout   randomization                     |
| CA      | certification authority                                  |
| CAS     | compare and swap                                         |
| CIA     | confidentiality, integrity, and availability             |
| COFF    | common object file format                                |
| CRED    | C Range Error Detector                                   |
| CRLF    | carriage return and line feed                            |
| CRT     | C runtime                                                |
| CVS     | Concurrent Versions System                               |
| DAG     | directed acyclic graph                                   |
| DBMS    | database management system                               |
| DEP     | data execution prevention                                |
| DOM     | Document Object Model                                    |
| DoS     | denial-of-service                                        |
| DTD     | Document Type Definition                                 |
| EGID    | effective group ID                                       |
| EJB     | Enterprise JavaBeans                                     |
| EOF     | end-of-file                                              |
| EUID    | effective user ID                                        |
| FFRDC   | federally funded research and development center         |
| FIFO    | first in, first out                                      |
| FMECA   | failure mode, effects, and criticality analysis          |
| GID     | group ID                                                 |
| IA-32   | Intel architecture and 32-bit addressing                 |
| IDE     | interactive development environment                      |
| IPC     | interprocess communication                               |
| JAR     | Java Archive                                             |
| Java EE | Java Enterprise Edition                                  |
| Java ME | Java Micro Edition                                       |
| JCIP    | Java Concurrency in Practice                             |
| JDBC    | do not expand jdbc                                       |
| JIT     | just-in-time system                                      |
| JLS     | Java Language Specification                              |
| JMM     | Java Memory Model                                        |
| JMX     | Java Management Extension                                |
| JNI     | Java Native Interface                                    |
| JNLP    | Java Network Launching Protocol                          |
| JPDA    | Java Platform Debugger Architecture                      |
| JRE     | Java Runtime Environment                                 |
| JSP     | Java Server Pages                                        |
| JVM     | Java Virtual Machine                                     |
| JVMDI   | JVM Debug Interface                                      |
| JVMPI   | JVM Profiler Interface                                   |
| JVMTI   | JVM Tool Interface                                       |
| LCK     | Locking                                                  |
| LDAP    | Lightweight Directory Access Protocol                    |
| LDIF    | LDAP Data Interchange Format                             |
| LIFO    | last-in, first-out                                       |
| LL/SC   | load linked/store conditional                            |
| MDAC    | Microsoft Data Access Components                         |
| MTA     | mail transfer agent                                      |
| NIO     | new I/O                                                  |
| NTBS    | null-terminated byte string                              |
| NTFS    | New Technology File System                               |
| NTMBS   | null-terminated multibyte string                         |
| PE      | portable executable                                      |
| PEB     | process environment block                                |
| PKI     | public key infrastructure                                |
| POD     | plain old data                                           |
| POF     | plain old function                                       |
| POSIX   | Portable Operating System Interface for UNIX             |
| PRNG    | pseudorandom number generator                            |
| RAII    | resource acquisition is initialization                   |
| RCU     | read-copy-update                                         |
| RDS     | remote data services                                     |
| RGID    | real group ID                                            |
| RMI     | remote method invocation                                 |
| RTC     | real-time clock                                          |
| RUID    | real user ID                                             |
| SAX     | Simple API for XML                                       |
| SCALe   | Source Code Analysis Laboratory                          |
| SEH     | structured exception handling                            |
| SEI     | Software Engineering Institute                           |
| SIMD    | single instruction, multiple data                        |
| SMP     | symmetric multiprocessing                                |
| SPP     | Stack Smashing Protector                                 |
| SSCC    | Safe-Secure C/C++                                        |
| SSE     | Streaming SIMD Extensions                                |
| SSL     | Secure Sockets Layer                                     |
| SSL/TLS | Secure Sockets Layer/Transport Layer Security            |
| SSO     | short string optimization                                |
| STL     | standard template library                                |
| SVG     | Scalable Vector Graphics                                 |
| TEB     | thread environment block                                 |
| TLD     | tag library descriptor                                   |
| TOCTOU  | time-of-check, time-of-use                               |
| UNC     | universal naming convention                              |
| URI     | Uniform Resource Identifier                              |
| URL     | Uniform Resource Locator                                 |
| VLA     | variable length array                                    |
| VNA     | Visibility and Atomicity                                 |
| VPTR    | virtual pointer                                          |
| XML     | extensible markup language                               |
| XSI     | X/Open System Interface                                  |
| XSS     | cross-site scripting                                     |
| XXE     | XML external entity                                      |

## Miscellaneous

Use only one space between sentences.
