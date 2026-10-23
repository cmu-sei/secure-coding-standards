# Codex conversation

## User

The file:
content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/

has two tables. The first column of the first table has hyperlinks (in Markdown format) in place of each CERT rule, which link to the rule's appropriate page.  The first column of the second table has CERT rules but no links. Please add links to all the rules in the second table.

## Assistant

I’ll inspect the two tables, mirror the established link format from the first table, and update only the second table’s rule column.

## Activity

    $ rg --files content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines && rg -n '^\|' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines
    ✓ • 6ms

## Activity

    $ sed -n '1,240p' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
    # MISRA C:2025
    
    This page was automatically generated and should not be edited.
    
    | CERT Rule                                                                                               | Related Guidelines                                                                                                                                      |
    |---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [STR34-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str34-c)                         | [CWE-704](https://cwe.mitre.org/data/definitions/704.html) , Incorrect Type Conversion or Cast                                                           |
    | [MSC41-C](/sei-cert-c-coding-standard/rules/miscellaneous-msc/msc41-c)                                  | [CWE-259](https://cwe.mitre.org/data/definitions/259.html) , Use of Hard-Coded Password                                                                  |
    
    | CERT Rule                                                                                               | Related Guidelines                                                                                                                                      |
    |---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
    | API00-C | Dir 4.11                                                          |
    | ARR01-C | Rule 12.5                                                         |
    | ARR30-C | Rule 1.3, 18.1, 21.17, 21.18                                      |
    | ARR32-C | Rule 18.8                                                         |
    | ARR36-C | Rule 18.2, 18.3                                                   |
    | ARR37-C | Rule 18.1, 18.4                                                   |
    | ARR38-C | Rule 1.3, 21.6, 21.17, 21.18                                      |
    | ARR39-C | Rule 1.3, 18.4                                                    |
    | CON30-C | Dir 4.12, Rule 22.1, 22.13                                        |
    | CON31-C | Rule 22.15, 22.16                                                 |
    | CON32-C | Dir 5.1                                                           |
    | CON33-C | Dir 5.1, Rule 9.7, 21.8, 21.19, 21.24                             |
    | CON34-C | Dir 4.12, Rule 18.6, 18.9, 22.13, 22.15                           |
    | CON35-C | Dir 5.2                                                           |
    | CON36-C | Dir 4.13, 5.1                                                     |
    | CON37-C | Rule 21.5                                                         |
    | CON39-C | Rule 22.11                                                        |
    | CON40-C | Rule 13.2                                                         |
    | CON43-C | Dir 5.1                                                           |
    | DCL01-C | Rule 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9                            |
    | DCL02-C | Dir 4.5, Rule 5.1, 5.2                                            |
    | DCL16-C | Rule 7.3                                                          |
    | DCL30-C | Rule 1.3, 18.6                                                    |
    | DCL31-C | Rule 8.1, 17.3                                                    |
    | DCL36-C | Rule 8.2, 8.4, 8.8, 17.3                                          |
    | DCL37-C | Rule 1.3, 5.10, 20.15, 21.1, 21.2                                 |
    | DCL38-C | Rule 1.1, 1.3, 21.3                                               |
    | DCL40-C | Rule 1.3, 5.1, 5.2, 8.3, 8.4, 8.5                                 |
    | DCL41-C | Rule 16.1                                                         |
    | ENV30-C | Rule 21.10, 21.19                                                 |
    | ENV31-C | Rule 1.3                                                          |
    | ENV32-C | Rule 21.4, 21.8                                                   |
    | ENV33-C | Rule 21.21                                                        |
    | ENV34-C | Rule 21.20                                                        |
    | ERR04-C | Rule 21.8                                                         |
    | ERR30-C | Rule 22.8, 22.9, 22.10                                            |
    | ERR32-C | Rule 21.5                                                         |
    | ERR33-C | Dir 4.7                                                           |
    | ERR34-C | Dir 4.7, Rule 21.7                                                |
    | EXP00-C | Rule 12.1                                                         |
    | EXP02-C | Rule 13.5                                                         |
    | EXP12-C | Rule 17.5                                                         |
    | EXP19-C | Rule 15.6                                                         |
    | EXP30-C | Rule 1.3, 13.2                                                    |
    | EXP32-C | Rule 1.3, 11.8                                                    |
    | EXP33-C | Dir 4.1, Rule 1.3, 9.1                                            |
    | EXP34-C | Dir 4.1, Rule 1.3                                                 |
    | EXP35-C | Rule 18.9                                                         |
    | EXP36-C | Rule 1.3, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6                      |
    | EXP37-C | Rule 8.2, 17.3                                                    |
    | EXP39-C | Rule 1.3, 11.1, 11.2, 11.3, 11.7                                  |
    | EXP40-C | Rule 1.3, 7.4, 11.8                                               |
    | EXP42-C | Rule 21.16                                                        |
    | EXP43-C | Rule 1.3, 8.14                                                    |
    | EXP44-C | Rule 13.6, 18.10, 23.2, 23.7                                      |
    | EXP45-C | Rule 13.4, Rule 14.4                                              |
    | EXP46-C | Rule 10.1                                                         |
    | FIO32-C | Rule 21.6                                                         |
    | FIO34-C | Rule 22.7                                                         |
    | FIO37-C | Rule 21.6                                                         |
    | FIO38-C | Rule 22.5                                                         |
    | FIO39-C | Dir 4.13, Rule 21.6, 22.4                                         |
    | FIO40-C | Rule 21.6                                                         |
    | FIO41-C | Rule 21.6                                                         |
    | FIO42-C | Rule 22.1                                                         |
    | FIO44-C | Rule 21.6                                                         |
    | FIO45-C | Dir 5.1                                                           |
    | FIO46-C | Rule 22.6                                                         |
    | FIO47-C | Rule 21.6                                                         |
    | FLP30-C | Rule 14.1                                                         |
    | FLP32-C | Dir 4.11, Rule 21.12                                              |
    | FLP34-C | Rule 10.3, 10.4, 10.5, 10.8                                       |
    | FLP36-C | Dir 1.1, Rule 1.3, 10.3, 10.4, 10.5, 10.8                         |
    | FLP37-C | Rule 21.16                                                        |
    | FLP38-C | Rule 21.11, 21.22, 21.23                                          |
    | INT30-C | Rule 12.4                                                         |
    | INT31-C | Rule 10.1, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 21.6, 21.13, 21.18 |
    | INT32-C | Dir 4.1, Rule 1.3                                                 |
    | INT33-C | Dir 4.1, Rule 1.3                                                 |
    | INT34-C | Rule 10.1, 12.2                                                   |
    | INT35-C | Dir 4.1, Rule 1.3                                                 |
    | INT36-C | Dir 1.1, Rule 11.1, 11.2, 11.4, 11.6, 11.7                        |
    | MEM30-C | Dir 4.12, Rule 1.3, 21.3, 22.2                                    |
    | MEM31-C | Rule 22.1                                                         |
    | MEM33-C | Rule 18.7                                                         |
    | MEM34-C | Rule 22.2                                                         |
    | MEM35-C | Dir 4.1, 4.12, Rule 1.3, 21.3                                     |
    | MEM36-C | Rule 21.3                                                         |
    | MSC00-C | Dir 2.1                                                           |
    | MSC01-C | Rule 15.7 16.4                                                    |
    | MSC04-C | Rule 3.1, 3.2                                                     |
    | MSC07-C | Dir 4.4, Rule 2.2                                                 |
    | MSC12-C | Rule 2.1                                                          |
    | MSC13-C | Rule 2.7, 2.8                                                     |
    | MSC15-C | Rule 1.3                                                          |
    | MSC17-C | Rule 16.3                                                         |
    | MSC24-C | Rule 1.5                                                          |
    | MSC30-C | Rule 21.24                                                        |
    | MSC32-C | Rule 21.24                                                        |
    | MSC33-C | Rule 21.10                                                        |
    | MSC37-C | Rule 17.4                                                         |
    | MSC38-C | Rule 1.1, 1.3                                                     |
    | MSC39-C | Rule 17.1                                                         |
    | MSC40-C | Rule 1.1                                                          |
    | POS53-C | Rule 22.19                                                        |
    | PRE06-C | Dir 4.10                                                          |
    | PRE12-C | Rule 20.7                                                         |
    | PRE30-C | Rule 1.3                                                          |
    | PRE31-C | Rule 13.2                                                         |
    | PRE32-C | Rule 1.3, 20.6                                                    |
    | SIG30-C | Rule 21.5                                                         |
    | SIG31-C | Rule 21.5                                                         |
    | SIG34-C | Rule 21.5                                                         |
    | SIG35-C | Rule 21.5                                                         |
    | STR05-C | Rule 7.4                                                          |
    | STR30-C | Rule 7.4                                                          |
    | STR31-C | Dir 4.1, Rule 1.3, 18.1, 21.6, 21.17, 21.18                       |
    | STR32-C | Rule 21.16                                                        |
    | STR34-C | Rule 10.1, 10.3, 10.4                                             |
    | STR37-C | Rule 21.13                                                        |
    | STR38-C | Rule 1.3, 10.3                                                    |
    ✓ • 0ms

## Activity

    $ find content/4.sei-cert-c-coding-standard -maxdepth 3 -type d -path '*/rules/*' | sort && rg -n '^\| (API|ARR|CON|DCL|ENV|ERR|EXP|FIO|FLP|INT|MEM|MSC|POS|PRE|SIG|STR)[0-9]{2}-C \|' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
    12:| API00-C | Dir 4.11                                                          |
    13:| ARR01-C | Rule 12.5                                                         |
    14:| ARR30-C | Rule 1.3, 18.1, 21.17, 21.18                                      |
    15:| ARR32-C | Rule 18.8                                                         |
    16:| ARR36-C | Rule 18.2, 18.3                                                   |
    17:| ARR37-C | Rule 18.1, 18.4                                                   |
    18:| ARR38-C | Rule 1.3, 21.6, 21.17, 21.18                                      |
    19:| ARR39-C | Rule 1.3, 18.4                                                    |
    20:| CON30-C | Dir 4.12, Rule 22.1, 22.13                                        |
    21:| CON31-C | Rule 22.15, 22.16                                                 |
    22:| CON32-C | Dir 5.1                                                           |
    23:| CON33-C | Dir 5.1, Rule 9.7, 21.8, 21.19, 21.24                             |
    24:| CON34-C | Dir 4.12, Rule 18.6, 18.9, 22.13, 22.15                           |
    25:| CON35-C | Dir 5.2                                                           |
    26:| CON36-C | Dir 4.13, 5.1                                                     |
    27:| CON37-C | Rule 21.5                                                         |
    28:| CON39-C | Rule 22.11                                                        |
    29:| CON40-C | Rule 13.2                                                         |
    30:| CON43-C | Dir 5.1                                                           |
    31:| DCL01-C | Rule 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9                            |
    32:| DCL02-C | Dir 4.5, Rule 5.1, 5.2                                            |
    33:| DCL16-C | Rule 7.3                                                          |
    34:| DCL30-C | Rule 1.3, 18.6                                                    |
    35:| DCL31-C | Rule 8.1, 17.3                                                    |
    36:| DCL36-C | Rule 8.2, 8.4, 8.8, 17.3                                          |
    37:| DCL37-C | Rule 1.3, 5.10, 20.15, 21.1, 21.2                                 |
    38:| DCL38-C | Rule 1.1, 1.3, 21.3                                               |
    39:| DCL40-C | Rule 1.3, 5.1, 5.2, 8.3, 8.4, 8.5                                 |
    40:| DCL41-C | Rule 16.1                                                         |
    41:| ENV30-C | Rule 21.10, 21.19                                                 |
    42:| ENV31-C | Rule 1.3                                                          |
    43:| ENV32-C | Rule 21.4, 21.8                                                   |
    44:| ENV33-C | Rule 21.21                                                        |
    45:| ENV34-C | Rule 21.20                                                        |
    46:| ERR04-C | Rule 21.8                                                         |
    47:| ERR30-C | Rule 22.8, 22.9, 22.10                                            |
    48:| ERR32-C | Rule 21.5                                                         |
    49:| ERR33-C | Dir 4.7                                                           |
    50:| ERR34-C | Dir 4.7, Rule 21.7                                                |
    51:| EXP00-C | Rule 12.1                                                         |
    52:| EXP02-C | Rule 13.5                                                         |
    53:| EXP12-C | Rule 17.5                                                         |
    54:| EXP19-C | Rule 15.6                                                         |
    55:| EXP30-C | Rule 1.3, 13.2                                                    |
    56:| EXP32-C | Rule 1.3, 11.8                                                    |
    57:| EXP33-C | Dir 4.1, Rule 1.3, 9.1                                            |
    58:| EXP34-C | Dir 4.1, Rule 1.3                                                 |
    59:| EXP35-C | Rule 18.9                                                         |
    60:| EXP36-C | Rule 1.3, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6                      |
    61:| EXP37-C | Rule 8.2, 17.3                                                    |
    62:| EXP39-C | Rule 1.3, 11.1, 11.2, 11.3, 11.7                                  |
    63:| EXP40-C | Rule 1.3, 7.4, 11.8                                               |
    64:| EXP42-C | Rule 21.16                                                        |
    65:| EXP43-C | Rule 1.3, 8.14                                                    |
    66:| EXP44-C | Rule 13.6, 18.10, 23.2, 23.7                                      |
    67:| EXP45-C | Rule 13.4, Rule 14.4                                              |
    68:| EXP46-C | Rule 10.1                                                         |
    69:| FIO32-C | Rule 21.6                                                         |
    70:| FIO34-C | Rule 22.7                                                         |
    71:| FIO37-C | Rule 21.6                                                         |
    72:| FIO38-C | Rule 22.5                                                         |
    73:| FIO39-C | Dir 4.13, Rule 21.6, 22.4                                         |
    74:| FIO40-C | Rule 21.6                                                         |
    75:| FIO41-C | Rule 21.6                                                         |
    76:| FIO42-C | Rule 22.1                                                         |
    77:| FIO44-C | Rule 21.6                                                         |
    78:| FIO45-C | Dir 5.1                                                           |
    79:| FIO46-C | Rule 22.6                                                         |
    80:| FIO47-C | Rule 21.6                                                         |
    81:| FLP30-C | Rule 14.1                                                         |
    82:| FLP32-C | Dir 4.11, Rule 21.12                                              |
    83:| FLP34-C | Rule 10.3, 10.4, 10.5, 10.8                                       |
    84:| FLP36-C | Dir 1.1, Rule 1.3, 10.3, 10.4, 10.5, 10.8                         |
    85:| FLP37-C | Rule 21.16                                                        |
    86:| FLP38-C | Rule 21.11, 21.22, 21.23                                          |
    87:| INT30-C | Rule 12.4                                                         |
    88:| INT31-C | Rule 10.1, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 21.6, 21.13, 21.18 |
    89:| INT32-C | Dir 4.1, Rule 1.3                                                 |
    90:| INT33-C | Dir 4.1, Rule 1.3                                                 |
    91:| INT34-C | Rule 10.1, 12.2                                                   |
    92:| INT35-C | Dir 4.1, Rule 1.3                                                 |
    93:| INT36-C | Dir 1.1, Rule 11.1, 11.2, 11.4, 11.6, 11.7                        |
    94:| MEM30-C | Dir 4.12, Rule 1.3, 21.3, 22.2                                    |
    95:| MEM31-C | Rule 22.1                                                         |
    96:| MEM33-C | Rule 18.7                                                         |
    97:| MEM34-C | Rule 22.2                                                         |
    98:| MEM35-C | Dir 4.1, 4.12, Rule 1.3, 21.3                                     |
    99:| MEM36-C | Rule 21.3                                                         |
    100:| MSC00-C | Dir 2.1                                                           |
    101:| MSC01-C | Rule 15.7 16.4                                                    |
    102:| MSC04-C | Rule 3.1, 3.2                                                     |
    103:| MSC07-C | Dir 4.4, Rule 2.2                                                 |
    104:| MSC12-C | Rule 2.1                                                          |
    105:| MSC13-C | Rule 2.7, 2.8                                                     |
    106:| MSC15-C | Rule 1.3                                                          |
    107:| MSC17-C | Rule 16.3                                                         |
    108:| MSC24-C | Rule 1.5                                                          |
    109:| MSC30-C | Rule 21.24                                                        |
    110:| MSC32-C | Rule 21.24                                                        |
    111:| MSC33-C | Rule 21.10                                                        |
    112:| MSC37-C | Rule 17.4                                                         |
    113:| MSC38-C | Rule 1.1, 1.3                                                     |
    114:| MSC39-C | Rule 17.1                                                         |
    115:| MSC40-C | Rule 1.1                                                          |
    116:| POS53-C | Rule 22.19                                                        |
    117:| PRE06-C | Dir 4.10                                                          |
    118:| PRE12-C | Rule 20.7                                                         |
    119:| PRE30-C | Rule 1.3                                                          |
    120:| PRE31-C | Rule 13.2                                                         |
    121:| PRE32-C | Rule 1.3, 20.6                                                    |
    122:| SIG30-C | Rule 21.5                                                         |
    123:| SIG31-C | Rule 21.5                                                         |
    124:| SIG34-C | Rule 21.5                                                         |
    125:| SIG35-C | Rule 21.5                                                         |
    126:| STR05-C | Rule 7.4                                                          |
    127:| STR30-C | Rule 7.4                                                          |
    128:| STR31-C | Dir 4.1, Rule 1.3, 18.1, 21.6, 21.17, 21.18                       |
    129:| STR32-C | Rule 21.16                                                        |
    130:| STR34-C | Rule 10.1, 10.3, 10.4                                             |
    131:| STR37-C | Rule 21.13                                                        |
    132:| STR38-C | Rule 1.3, 10.3                                                    |
    ✓ • 1.19s

## Activity

    $ rg -n '\[API00-C\]|\[CON30-C\]|\[POS53-C\]|\[PRE06-C\]' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines content/4.sei-cert-c-coding-standard | head -80
    content/4.sei-cert-c-coding-standard/04.back-matter/8.gg-risk-assessments.md:20:| [CON30-C](/sei-cert-c-coding-standard/rules/concurrency-con/con30-c) | Medium | Unlikely | No | No | <span style="color: #27ae60;">**P2**</span> | <span style="color: #27ae60;">**L3**</span> |
    content/4.sei-cert-c-coding-standard/04.back-matter/8.gg-risk-assessments.md:120:| [POS53-C](/sei-cert-c-coding-standard/rules/posix-pos/pos53-c) | Medium | Probable | Yes | No | <span style="color: #f1c40f;">**P8**</span> | <span style="color: #f1c40f;">**L2**</span> |
    content/4.sei-cert-c-coding-standard/04.back-matter/8.gg-risk-assessments.md:141:| [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c) | Medium | Unlikely | No | No | **P2** | **L3** |
    content/4.sei-cert-c-coding-standard/04.back-matter/8.gg-risk-assessments.md:296:| [PRE06-C](/sei-cert-c-coding-standard/recommendations/preprocessor-pre/pre06-c) | Low | Unlikely | Yes | Yes | **P3** | **L3** |
    content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/12.mitre-cwe-211.md:122:| [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c) | [CWE-20](https://cwe.mitre.org/data/definitions/20.html) , Insufficient input validation                                                                                               |
    content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/11.mitre-cwe.md:10:| [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c)   | [CWE-476](https://cwe.mitre.org/data/definitions/476.html)                                                                                                |
    content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/12.mitre-cwe-211.md:122:| [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c) | [CWE-20](https://cwe.mitre.org/data/definitions/20.html) , Insufficient input validation                                                                                               |
    content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/11.mitre-cwe.md:10:| [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c)   | [CWE-476](https://cwe.mitre.org/data/definitions/476.html)                                                                                                |
    ✓ • 168ms

## Assistant

I found the intended file: `10.misra-c-2025.md`. Its second table has 121 unlinked entries, including both rules and recommendations, so I’m resolving each destination from the repository’s existing canonical CERT links before applying the mechanical update.

## Activity

    $ perl -e '
        my ($target, $source) = @ARGV;
        my (%urls, %conflicts, %needed);
        open my $s, "<", $source or die "$source: $!\n";
        while (<$s>) {
          while (/\[([A-Z]{3}\d{2}-C)\]\((\/sei-cert-c-coding-standard\/(?:rules|recommendations)\/[^)]+)\)/g) {
            $conflicts{$1}{$2} = 1;
            $urls{$1} = $2;
          }
        }
        open my $t, "<", $target or die "$target: $!\n";
        while (<$t>) { $needed{$1} = 1 if /^\| ([A-Z]{3}\d{2}-C) \|/; }
        my @missing = grep { !exists $urls{$_} } sort keys %needed;
        my @ambiguous = grep { scalar(keys %{$conflicts{$_}}) != 1 } sort keys %needed;
        print "needed=" . scalar(keys %needed) . " mapped=" . (scalar(keys %needed) - scalar(@missing)) . "\n";
        print "missing: @missing\n" if @missing;
        for my $code (@ambiguous) { print "ambiguous $code: " . join(", ", sort keys %{$conflicts{$code}}) . "\n"; }
        ' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md content/4.sei-cert-c-coding-standard/04.back-matter/8.gg-risk-assessments.md
    needed=121 mapped=121
    ✓ • 0ms

## Activity

    $ perl -i -pe '
        BEGIN {
          my $source = "content/4.sei-cert-c-coding-standard/04.back-matter/8.gg-risk-assessments.md";
          open my $s, "<", $source or die "$source: $!\n";
          while (<$s>) {
            while (/\[([A-Z]{3}\d{2}-C)\]\((\/sei-cert-c-coding-standard\/(?:rules|recommendations)\/[^)]+)\)/g) {
              $urls{$1} = $2;
            }
          }
        }
        if (/^\| ([A-Z]{3}\d{2}-C) \|/) {
          my $code = $1;
          die "Missing URL for $code\n" unless exists $urls{$code};
          s/^\| \Q$code\E \|/| [$code]($urls{$code}) |/;
        }
        ' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
        
        git diff --check -- content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
        git diff --stat -- content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
        git diff -- content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
    ✓ • 0ms

## Activity

    $ sed -n '8,20p' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md && git status --short -- content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
    | [MSC41-C](/sei-cert-c-coding-standard/rules/miscellaneous-msc/msc41-c)                                  | [CWE-259](https://cwe.mitre.org/data/definitions/259.html) , Use of Hard-Coded Password                                                                  |
    
    | CERT Rule                                                                                               | Related Guidelines                                                                                                                                      |
    |---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c) | Dir 4.11                                                          |
    | [ARR01-C](/sei-cert-c-coding-standard/recommendations/arrays-arr/arr01-c) | Rule 12.5                                                         |
    | [ARR30-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr30-c) | Rule 1.3, 18.1, 21.17, 21.18                                      |
    | [ARR32-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr32-c) | Rule 18.8                                                         |
    | [ARR36-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr36-c) | Rule 18.2, 18.3                                                   |
    | [ARR37-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr37-c) | Rule 18.1, 18.4                                                   |
    | [ARR38-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr38-c) | Rule 1.3, 21.6, 21.17, 21.18                                      |
    | [ARR39-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr39-c) | Rule 1.3, 18.4                                                    |
    | [CON30-C](/sei-cert-c-coding-standard/rules/concurrency-con/con30-c) | Dir 4.12, Rule 22.1, 22.13                                        |
    ?? content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
    ✓ • 0ms

## Activity

    $ awk 'BEGIN{table=0} /^\| CERT Rule/{table++} table==2 && /^\| \[/{split($0,a," | "); cell=a[1]; sub(/^\| /,"",cell); if(length(cell)>max){max=length(cell); line=NR; value=cell}} END{print "max_first_cell_length=" max " line=" line; print value}' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
        rg -n '^\| [A-Z]{3}[0-9]{2}-C \|' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md || true
        rg -n '^\| \[[A-Z]{3}[0-9]{2}-C\]\(/sei-cert-c-coding-standard/(rules|recommendations)/[^)]+\) \|' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md | wc -l
        find content/4.sei-cert-c-coding-standard -type f -name '*.md' | wc -l
    max_first_cell_length=1 line=12
    |
    121
    429
    ✓ • 0ms

## Activity

    $ perl -ne '
        if (/^\| (\[[A-Z]{3}\d{2}-C\]\([^)]+\)) \|/) {
          my $n=length($1); if($n>$max){$max=$n;$line=$.;$value=$1}
        }
        END { print "max=$max line=$line\n$value\n" }
        ' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
        perl -ne 'if ($. == 10 || $. == 11) { /^\|([^|]+)\|/; print $. . ":" . length($1) . ":$1\n" }' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
    max=101 line=12
    [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c)
    10:105: CERT Rule
    11:105:---------------------------------------------------------------------------------------------------------
    ✓ • 0ms

## Activity

    $ perl -i -pe '
        if (/^\| (\[[A-Z]{3}\d{2}-C\]\([^)]+\)) \|/) {
          my $cell = $1;
          s/^\| \Q$cell\E \|/sprintf("| %-104s|", $cell)/e;
        }
        ' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
        sed -n '8,20p' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
        sed -n '124,134p' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
    | [MSC41-C](/sei-cert-c-coding-standard/rules/miscellaneous-msc/msc41-c)                                  | [CWE-259](https://cwe.mitre.org/data/definitions/259.html) , Use of Hard-Coded Password                                                                  |
    
    | CERT Rule                                                                                               | Related Guidelines                                                                                                                                      |
    |---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c)   | Dir 4.11                                                          |
    | [ARR01-C](/sei-cert-c-coding-standard/recommendations/arrays-arr/arr01-c)                               | Rule 12.5                                                         |
    | [ARR30-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr30-c)                                         | Rule 1.3, 18.1, 21.17, 21.18                                      |
    | [ARR32-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr32-c)                                         | Rule 18.8                                                         |
    | [ARR36-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr36-c)                                         | Rule 18.2, 18.3                                                   |
    | [ARR37-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr37-c)                                         | Rule 18.1, 18.4                                                   |
    | [ARR38-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr38-c)                                         | Rule 1.3, 21.6, 21.17, 21.18                                      |
    | [ARR39-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr39-c)                                         | Rule 1.3, 18.4                                                    |
    | [CON30-C](/sei-cert-c-coding-standard/rules/concurrency-con/con30-c)                                    | Dir 4.12, Rule 22.1, 22.13                                        |
    | [SIG34-C](/sei-cert-c-coding-standard/rules/signals-sig/sig34-c)                                        | Rule 21.5                                                         |
    | [SIG35-C](/sei-cert-c-coding-standard/rules/signals-sig/sig35-c)                                        | Rule 21.5                                                         |
    | [STR05-C](/sei-cert-c-coding-standard/recommendations/characters-and-strings-str/str05-c)               | Rule 7.4                                                          |
    | [STR30-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str30-c)                         | Rule 7.4                                                          |
    | [STR31-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str31-c)                         | Dir 4.1, Rule 1.3, 18.1, 21.6, 21.17, 21.18                       |
    | [STR32-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str32-c)                         | Rule 21.16                                                        |
    | [STR34-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str34-c)                         | Rule 10.1, 10.3, 10.4                                             |
    | [STR37-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str37-c)                         | Rule 21.13                                                        |
    | [STR38-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str38-c)                         | Rule 1.3, 10.3                                                    |
    ✓ • 0ms

## Activity

    $ find content/4.sei-cert-c-coding-standard -type f -name '*api00-c*' -o -name '*arr01-c*' -o -name '*con30-c*' | sort | head -30
        perl -e '
        my ($target, $source) = @ARGV;
        my %canonical;
        open my $s, "<", $source or die "$source: $!\n";
        while (<$s>) {
          while (/\[([A-Z]{3}\d{2}-C)\]\((\/sei-cert-c-coding-standard\/(?:rules|recommendations)\/[^)]+)\)/g) {
            $canonical{$1} = $2;
          }
        }
        open my $t, "<", $target or die "$target: $!\n";
        my ($table, $rows, $bad, $mismatch) = (0, 0, 0, 0);
        while (<$t>) {
          $table++ if /^\| CERT Rule/;
          next unless $table == 2 && /^\|/;
          next if /^\|(?:-| CERT Rule)/;
          $rows++;
          if (!/^\| \[([A-Z]{3}\d{2}-C)\]\(([^)]+)\)\s+\|/) { print "malformed line $.: $_"; $bad++; next; }
          my ($code, $url) = ($1, $2);
          if (!exists $canonical{$code} || $canonical{$code} ne $url) { print "noncanonical line $.: $code -> $url\n"; $mismatch++; }
        }
        print "second-table rows=$rows malformed=$bad noncanonical=$mismatch\n";
        exit(($bad || $mismatch || $rows != 121) ? 1 : 0);
        ' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md content/4.sei-cert-c-coding-standard/04.back-matter/8.gg-risk-assessments.md
    content/4.sei-cert-c-coding-standard/03.rules/05.concurrency-con/02.con30-c.md
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/3.arr01-c.md
    second-table rows=121 malformed=0 noncanonical=0
    ✓ • 0ms

## Activity

    $ rg --files -g 'AGENTS.md' -g '!node_modules' -g '!vendor' /host 2>/dev/null | sort
    ✓ • 2.44s

## Assistant

Added links to all 121 CERT entries in the second table of [10.misra-c-2025.md](/host/content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md:12).

Validated that every link matches the repository’s canonical rule or recommendation URL.

## User

Thanks, that seems to have worked perfectly.

My next task is to take the table at
content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
and update each CERT C rule and recommendation with this info.

In particular, for each guideline/row in the table, I need to add a row in that guideline's Automated Detection table.
The leftmost cell in the row should have the following link:

[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)

All remaining cells should have the same content in the guideline's table as they do in the original tab.e.

I don't want you to actually do this work. What I want instead is for you to create a Python script that can do this work.
You can put this script in to the file:
scripts/distribute_guideline_table.py
I will try the script and provide feedback.

## Assistant

I’ll inspect the source table, the guideline page layout, and any existing distribution scripts so the new script preserves each Automated Detection table’s exact column structure and remains safe to rerun.

## Activity

    $ rg --files scripts content/4.sei-cert-c-coding-standard | sed -n '1,240p'
        rg -n -i '^#{1,6} automated detection|Automated Detection' content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations | head -80
        rg -n 'distribut|guideline table|Related Guidelines' scripts 2>/dev/null | head -100
    ✓ • 8ms

## Activity

    $ sed -n '1,240p' scripts/README.md
        sed -n '1,260p' scripts/manage_links.py
        for f in \
         content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md \
         content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/2.arr30-c.md \
         content/4.sei-cert-c-coding-standard/03.rules/05.concurrency-con/02.con30-c.md \
         content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/13.fio46-c.md; do
          rg -n -A18 -B2 '^## Automated Detection' "$f"
        done
    # Scripts
    
    This directory contains helpful scripts which are used to maintain the secure coding standards.
    
    NOTE: All bash snippets in this file assume your current directory is the root of the secure coding standards repository.
    
    ## Setup
    
    For the python-based scripts, you will need to have the packages listed in `requirements.txt`.
    
    A good way to do this is via a venv to keep the requirements for these scripts separate from your system or other projects.
    
    ```bash
    # Use venv to setup a virtual environment. Do this only once
    python -m venv venv
    
    # Source the venv into your shell. You must do this each time.
    source venv/bin/activate
    
    # Install the required packages. You only need to do this after changes to requirements.txt.
    pip install -r scripts/requirements.txt
    ```
    
    ## manage_links.py
    
    The subcommands in this script can be used to manage links found in the standards. For up to date information, check the help:
    
    ```bash
    python scripts/manage_links.py --help
    ```
    
    ### find-urls
    
    This subcommand finds files which contain at least one of the urls provided via the command line.
    
    ### find-urls-from-file
    
    This subcommand finds files which contain at least one of the urls found on the lines of a given file.
    
    ### check-links
    
    This subcommand traverses the standards and then uses the python requests library to attempt a HEAD request on the url. It then categorizes the response as `alive`, `redirect`, `dead`, or `error`.
    
    Intermediate and final results are cached in `./checked_links.json`.
    
    NOTE: Some external websites use bot protection that makes pages return 403 when accessed via requests. Thus, "dead" links with code 403 need to be checked manually in a browser. Also zscaler interferes with some external websites (notably gnu), so it is best to run the script off of zscaler.
    
    ### rules-to-recommendations
    
    This subcommand traverses the standards and identifies links from rules to recommendations.
    
    ### summary
    
    This subcommand traverses the standards and emits the list of links found on each page.
    
    #!/usr/bin/env python3
    """
    Extract links from markdown files in content/ and construct a map
    between files and all links they contain (both HTML and markdown style).
    
    EXAMPLE:  python3 ./scripts/extract_links.py find-urls /sei-cert-c-coding-standard/recommendations/integers-int/int01-c
      prints all files that reference CERT recommendation INT01-C
    """
    
    import re
    import json
    import concurrent.futures
    from pathlib import Path
    from typing import Dict, List
    from tqdm import tqdm
    import requests
    
    
    def extract_markdown_links(content: str) -> List[str]:
        """Extract markdown-style links: [text](url).
        """
        links = []
    
        # Inline links: [text](url) or [text](<url>)
        inline_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        for match in re.finditer(inline_pattern, content):
            url = match.group(2).strip()
            # Clean up angle brackets if present
            url = url.strip('<>')
            if url:
                links.append(url)
    
        return links
    
    
    def extract_html_links(content: str) -> List[str]:
        """Extract HTML-style links: <a href="url"> or <a href='url'>."""
        links = []
    
        # Anchor tags with href attribute
        # Match both single and double quotes, handle multi-line
        href_pattern = r'<a[^>]*\s+href\s*=\s*["\']([^"\']+)["\'][^>]*>'
    
        for match in re.finditer(href_pattern, content, re.IGNORECASE):
            url = match.group(1).strip()
            if url:
                links.append(url)
    
        return links
    
    
    def extract_links(content: str) -> List[str]:
        """Extract all links from markdown content (both markdown and HTML style)."""
        all_links = []
    
        # Extract markdown links
        markdown_links = extract_markdown_links(content)
        all_links.extend(markdown_links)
    
        # Extract HTML links
        html_links = extract_html_links(content)
        all_links.extend(html_links)
    
        return all_links
    
    
    def is_relative_url(url: str) -> bool:
        """Check if a URL is relative (starts with / or doesn't have a protocol)."""
        return not (url.startswith('http://') or
                    url.startswith('https://') or
                    url.startswith('mailto:') or
                    url.startswith('tel:') or
                    url.startswith('#'))
    
    
    def process_markdown_files(paths: List[str]) -> Dict[str, List[str]]:
    
        """Process all markdown files in content directory and extract links.
    
        Args:
            content_dir: Path to the content directory
    
        Returns:
            Dictionary mapping markdown file paths to lists of links found in them
        """
    
        # Find all md files associated with the paths
        md_files = []
        for path in map(Path, paths):
            if not path.exists():
                raise ValueError(f"Path does not exist: {path}")
    
            if path.is_dir():
                # Find all markdown files
                md_files.extend(path.glob('**/*.md'))
            elif path.is_file() and path.suffix == '.md':
                md_files.append(path)
            else:
                raise ValueError(f"Invalid path: {path}")
    
        # Extract all links for the md files.
        result = {}
        for md_file in md_files:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
    
            links = extract_links(content)
    
            file_key = str(md_file)
            result[file_key] = links
    
        return result
    
    
    def find_files_with_urls(link_map: Dict[str, List[str]], urls: List[str]) -> Dict[str, List[str]]:
        """Find all files that reference any of the provided URLs.
    
        Args:
            link_map: Dictionary mapping file paths to lists of links
            urls: List of URLs to search for
    
        Returns:
            Dictionary mapping file paths to lists of matching URLs found in them
        """
        results = {}
    
        for file_path, links in link_map.items():
            matching_urls = [url for url in urls if url in links]
            if matching_urls:
                results[file_path] = list(sorted(matching_urls))
    
        return results
    
    
    def check_links_main(link_map: Dict[str, List[str]], output_format: str, checkpoint_file: str = 'checked_links.json'):
        """Check if absolute URLs are alive or dead using parallel requests and tqdm progress bar."""
        url_to_files = {}
        for file_path, links in link_map.items():
            for url in links:
                if url.startswith('http://') or url.startswith('https://'):
                    if url not in url_to_files:
                        url_to_files[url] = []
                    url_to_files[url].append(file_path)
    
        if not url_to_files:
            print("No absolute URLs found to check.")
            return
    
        # Load checkpoint
        old_checked_data = {}
        checked_data = {}
        try:
            with open(checkpoint_file, 'r', encoding='utf-8') as f:
                old_checked_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
    
        urls_to_check = []
        for url in url_to_files:
            if url in old_checked_data:
                checked_data[url] = old_checked_data[url]
            else:
                urls_to_check.append(url)
    
        print(f"Total unique URLs found: {len(url_to_files)}")
        if urls_to_check:
            print(f"Already checked: {len(url_to_files) - len(urls_to_check)}")
            print(f"To check: {len(urls_to_check)}")
        else:
            print("All URLs have already been checked.")
    
        def worker(url):
            try:
                try:
                    response = requests.head(url, timeout=10, allow_redirects=False)
                    if response.status_code == 405:
                        response = requests.get(url, timeout=10, allow_redirects=False)
                except requests.RequestException:
                    response = requests.get(url, timeout=10, allow_redirects=False)
    
                if 400 <= response.status_code < 600:
                    return url, {"status": "dead", "code": response.status_code}
                elif 300 <= response.status_code < 400:
                    return url, {"status": "redirect", "code": response.status_code, "dest": response.headers.get('Location')}
                else:
                    return url, {"status": "alive", "code": response.status_code}
            except Exception as e:
                return url, {"status": "error", "error": str(e)}
    
        # Parallel execution
        if urls_to_check:
            i = 0
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                futures = {executor.submit(worker, url): url for url in urls_to_check}
                for future in tqdm(concurrent.futures.as_completed(futures), total=len(urls_to_check), desc="Checking URLs"):
                    url, result = future.result()
                    checked_data[url] = result
                    # Save checkpoint periodically (every 10 URLs or so to reduce I/O, or just every time for safety)
                    # For simplicity and safety against interruption, we save every time.
                    if i % 100 == 99:
                        with open(checkpoint_file, 'w', encoding='utf-8') as f:
                            json.dump(checked_data, f, indent=2)
                    i += 1
    
        with open(checkpoint_file, 'w', encoding='utf-8') as f:
            json.dump(checked_data, f, indent=2)
    
        if output_format == 'json':
            print(json.dumps(checked_data, indent=4))
        else:
            dead_urls = []
            alive_urls = []
            redirect_urls = []
            error_urls = []
    
            for url, info in checked_data.items():
                if info["status"] == "dead":
                    dead_urls.append((url, info["code"]))
                elif info["status"] == "alive":
                    alive_urls.append(url)
                elif info["status"] == "redirect":
                    redirect_urls.append((url, info["dest"]))
                elif info["status"] == "error":
                    error_urls.append((url, info["error"]))
    
            print(f"\nSummary:")
            print(f"  Alive: {len(alive_urls)}")
            print(f"  Redirect: {len(redirect_urls)}")
            print(f"  Dead: {len(dead_urls)}")
            print(f"  Errors: {len(error_urls)}")
    
            if redirect_urls:
                print("\nRedirect URLs:")
                for url, dest in redirect_urls:
                    print(f"- {url} (moved to {dest})")
                    for file_path in url_to_files.get(url, []):
                        print(f"    - {file_path}")
    
            if dead_urls:
                print("\nDead URLs:")
                for url, code in dead_urls:
                    print(f"- {url} (Status: {code})")
                    for file_path in url_to_files.get(url, []):
                        print(f"    - {file_path}")
    
            if error_urls:
                print("\nError URLs (could not connect):")
                for url, err in error_urls:
                    print(f"- {url} (Error: {err})")
                    for file_path in url_to_files.get(url, []):
                        print(f"    - {file_path}")
    
    def find_rules_referencing_recommendations(link_map: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """Find all files under rules/ that reference files under recommendations/.
    
        Handles both direct path matching and numbered directory patterns like:
        - 3.rules/ referencing 4.recommendations/
        - rules/ referencing recommendations/
        - Any number prefix for rules or recommendations directories
    
    90-| API00-C | Medium | Unlikely | No | No | <span style="color: #27ae60;">**P2**</span> | <span style="color: #27ae60;">**L3**</span> |
    91-
    92:## Automated Detection
    93-
    94-| Tool      | Version  | Checker | Description |
    95-|-----------|----------|---------|-------------|
    96-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> |  | Supported |
    97-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/codesonar">CodeSonar</a> | <div class="content-wrapper">27.0</div> | **LANG.STRUCT.UPD** | Unchecked parameter dereference |
    98-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/parasoft">Parasoft C/C++test</a> | <div class="content-wrapper">2026.1</div> | **CERT_C-API00-a** | The validity of parameters must be checked inside each function |
    99-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/pc-lint-plus">PC-lint Plus</a> | <div class="content-wrapper">1.4</div> | **413, 613, 668** | Partially supported: reports use of null pointers including function parameters which are assumed to have the potential to be null |
    100-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/pvs-studio">PVS-Studio</a> | <div class="content-wrapper">8.01</div> | **<a href="https://pvs-studio.com/en/docs/warnings/v781/">V781</a> , <a href="https://pvs-studio.com/en/docs/warnings/v1111/">V1111</a>** |  |
    101-
    102-
    103-## Related Vulnerabilities
    104-
    105-Search for [vulnerabilities](/sei-cert-c-coding-standard/back-matter/bb-definitions#BB.Definitions-vulnerabilty) resulting from the violation of this rule on the [CERT website](https://www.kb.cert.org/vuls/search/?q=MSC08-C) .
    106-
    107-## Related Guidelines
    108-
    109-[Key here](/sei-cert-c-coding-standard/front-matter/introduction/how-this-coding-standard-is-organized#HowthisCodingStandardisOrganized-RelatedGuidelines) (explains table format and definitions)
    110-
    389-| ARR30-C | High | Likely | No | No | <span style="color: #f1c40f;">**P9**</span> | <span style="color: #f1c40f;">**L2**</span> |
    390-
    391:## Automated Detection
    392-
    393-| Tool      | Version  | Checker | Description |
    394-|-----------|----------|---------|-------------|
    395-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> | **array-index-range** <br /> **array-index-range-constant** <br /> **null-dereferencing** <br /> **pointered-deallocation** <br /> **return-reference-local** <br /> **csa-stack-address-escape** (C++) | Partially checked <br /> Can detect all accesses to invalid pointers as well as array index out-of-bounds accesses and prove their absence. <br /> This rule is only partially checked as invalid but unused pointers may not be reported. |
    396-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/axivion-suite">Axivion Suite</a> | <div class="content-wrapper">7.12.0</div> | **CertC-ARR30** | Can detect out-of-bound access to array / buffer |
    397-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/codee">Codee</a> | <div class="content-wrapper">2025.4.9</div> | **PWR014** <br /> **PWD004** <br /> **PWD005** <br /> **PWD006** <br /> **PWD008** | Out-of-dimension-bounds matrix access <br /> Out-of-memory-bounds array access <br /> Array range copied to or from the GPU does not cover the used range <br /> Missing deep copy of non-contiguous data to the GPU <br /> Unprotected multithreading recurrence due to out-of-dimension-bounds array access |
    398-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/codesonar">CodeSonar</a> | <div class="content-wrapper">27.0</div> | **LANG.MEM.BO** <br />  **LANG.MEM.BU** <br />  **LANG.MEM.TBA**  <br /> **LANG.MEM.TO** <br /> **LANG.MEM.TULANG.STRUCT.PARITH** <br />  **LANG.STRUCT.PBB** <br /> **LANG.STRUCT.PPE** <br />  **BADFUNC.BO.*** | Buffer overrun <br /> Buffer underrun <br /> Tainted buffer access <br /> Type overrun <br /> Type underrun <br /> Pointer Arithmetic <br /> Pointer before beginning of object <br /> Pointer past end of object <br /> A collection of warning classes that report uses of library functions prone to internal buffer overflows. |
    399-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/rose">Compass/ROSE</a> |  |  | Could be configured to catch violations of this rule. The way to catch the noncompliant code example is to first hunt for example code that follows this pattern:<pre><code>for (LPWSTR pwszTemp = pwszPath + 2; *pwszTemp != L&#39;\\&#39;; *pwszTemp++;)</code></pre>In particular, the iteration variable is a pointer, it gets incremented, and the loop condition does not set an upper bound on the pointer. Once this case is handled, ROSE can handle cases like the real noncompliant code example, which is effectively the same semantics, just different syntax |
    400-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/coverity">Coverity</a> | <div class="content-wrapper">2017.07</div> | **OVERRUN** <br /> **NEGATIVE_RETURNS** <br /> **ARRAY_VS_SINGLETON** <br /> **BUFFER_SIZE** | Can detect the access of memory past the end of a memory buffer/array <br /> Can detect when the loop bound may become negative <br /> Can detect the out-of-bound read/write to array allocated statically or dynamically <br /> Can detect buffer overflows |
    401-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/cppcheck">Cppcheck</a> | <div class="content-wrapper">2.15</div> | **arrayIndexOutOfBounds, outOfBounds, negativeIndex, arrayIndexThenCheck, arrayIndexOutOfBoundsCond,  possibleBufferAccessOutOfBounds** |  |
    402-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/cppcheck-premium">Cppcheck Premium</a> | <div class="content-wrapper">24.11.0</div> | **arrayIndexOutOfBounds, outOfBounds, negativeIndex, arrayIndexThenCheck, arrayIndexOutOfBoundsCond,  possibleBufferAccessOutOfBounds** <br /> **premium-cert-arr30-c** |  |
    403-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/helix-qac">Helix QAC</a> | <div class="content-wrapper">2025.2</div> | **C2840** <br /> **DF2820, DF2821, DF2822, DF2823, DF2840, DF2841, DF2842, DF2843, DF2930, DF2931, DF2932, DF2933, DF2935, DF2936, DF2937, DF2938, DF2950, DF2951, DF2952, DF2953** |  |
    404-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/klocwork">Klocwork</a> | <div class="content-wrapper">2025.2</div> | **ABV.ANY_SIZE_ARRAY** <br /> **ABV.GENERAL** <br /> **ABV.GENERAL.MULTIDIMENSION** <br /> **ABV.NON_ARRAY** <br /> **ABV.STACK** <br /> **ABV.TAINTED** <br /> **ABV.UNICODE.BOUND_MAP** <br /> **ABV.UNICODE.FAILED_MAP** <br /> **ABV.UNICODE.NNTS_MAP** <br /> **ABV.UNICODE.SELF_MAP** <br /> **ABV.UNKNOWN_SIZE** <br /> **NNTS.MIGHT** <br /> **NNTS.MUST** <br /> **NNTS.TAINTED** <br /> **NPD.FUNC.CALL.MIGHT** <br /> **SV.TAINTED.INDEX_ACCESS** <br /> **SV.TAINTED.LOOP_BOUND** |  |
    405-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/ldra">LDRA tool suite</a> | <div class="content-wrapper">10.6.0</div> | **45 S, 141 D, 47 S, 476 S, 489 S, 692 S, 64 X, 66 X, 68 X, 69 X, 70 X, 71 X, 79 X** | Statically implemented |
    406-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/parasoft">Parasoft C/C++test</a> | <div class="content-wrapper">2026.1</div> | **CERT_C-ARR30-a** | Avoid accessing arrays out of bounds |
    407-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/parasoft">Parasoft Insure++</a> |  |  | Runtime analysis |
    408-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/pc-lint-plus">PC-lint Plus</a> | <div class="content-wrapper">1.4</div> | **413, 415, 416, 613, 661, 662, 676** | Fully supported |
    409-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/polyspace-bug-finder">Polyspace Bug Finder</a> | <div class="content-wrapper">R2025b</div> | <a href="https://www.mathworks.com/help/bugfinder/ref/certcrulearr30c.html">CERT C: Rule ARR30-C</a> | Checks for:<ul><li>Array access out of bounds</li><li>Pointer access out of bounds</li><li>Array access with tainted index</li><li>Use of tainted pointer</li><li>Pointer dereference with tainted offset</li></ul>Rule partially covered. |
    172-| CON30-C | Medium | Unlikely | No | No | <span style="color: #27ae60;">**P2**</span> | <span style="color: #27ae60;">**L3**</span> |
    173-
    174:## Automated Detection
    175-
    176-
    177-| Tool      | Version  | Checker | Description |
    178-|-----------|----------|---------|-------------|
    179-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> | | Supported, but no explicit checker |
    180-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/axivion-suite">Axivion Suite</a> | <div class="content-wrapper">7.12.0</div> | **CertC-CON30** |  |
    181-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/codesonar">CodeSonar</a> | <div class="content-wrapper">27.0</div> | **ALLOC.LEAK** | Leak |
    182-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/coverity">Coverity</a> | <div class="content-wrapper">2017.07</div> | **ALLOC_FREE_MISMATCH** | Partially implemented, correct implementation is more involved |
    183-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/cppcheck-premium">Cppcheck Premium</a> | <div class="content-wrapper">24.11.0</div> | **premium-cert-con30-c** | |
    184-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/helix-qac">Helix QAC</a> | <div class="content-wrapper">2025.2</div> | **C1780, C1781, C1782, C1783, C1784** | |
    185-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/parasoft">Parasoft C/C++test</a> | <div class="content-wrapper">2026.1</div> | **CERT_C-CON30-a** | Ensure resources are freed |
    186-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/polyspace-bug-finder">Polyspace Bug Finder</a> | <div class="content-wrapper">R2025b</div> | [CERT C: Rule CON30-C](https://www.mathworks.com/help/bugfinder/ref/certcrulecon30c.html) | Checks for thread-specific memory leak (rule fully covered) |
    187-
    188-
    189-## Related Vulnerabilities
    190-
    191-Search for [vulnerabilities](/sei-cert-c-coding-standard/back-matter/bb-definitions#BB.Definitions-vulnerability) resulting from the violation of this rule on the [CERT website](https://www.kb.cert.org/vuls/search/?q=CON30-C) .
    192-
    59-| FIO46-C | Medium | Unlikely | No | No | <span style="color: #27ae60;">**P2**</span> | <span style="color: #27ae60;">**L3**</span> |
    60-
    61:## Automated Detection
    62-
    63-| Tool      | Version  | Checker | Description |
    64-|-----------|----------|---------|-------------|
    65-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> |  | Supported |
    66-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/codesonar">CodeSonar</a> | <div class="content-wrapper">27.0</div> | **IO.UAC** | Use after close |
    67-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/rose">Compass/ROSE</a> |  |  |  |
    68-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/coverity">Coverity</a> | <div class="content-wrapper">2017.07</div> | **USE_AFTER_FREE** | Implemented |
    69-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/helix-qac">Helix QAC</a> | <div class="content-wrapper">2025.2</div> | **DF2696, DF2697, DF2698** |  |
    70-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/klocwork">Klocwork</a> | <div class="content-wrapper">2025.2</div> | **SV.INCORRECT_RESOURCE_HANDLING.URH** |  |
    71-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/ldra">LDRA tool suite</a> | <div class="content-wrapper">10.6.0</div> | **48 D** | Statically implemented |
    72-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/parasoft">Parasoft C/C++test</a> | <div class="content-wrapper">2026.1</div> | **CERT_C-FIO46-a** | Do not use resources that have been freed |
    73-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/pc-lint-plus">PC-lint Plus</a> | <div class="content-wrapper">1.4</div> | **2471** | Fully supported |
    74-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/polyspace-bug-finder">Polyspace Bug Finder</a> | <div class="content-wrapper">R2025b</div> | <a href="https://www.mathworks.com/help/bugfinder/ref/certcrulefio46c.html">CERT C: Rule FIO46-C</a> | Checks for use of previously closed resource (rule partially covered) |
    75-| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/sonarqube-ccpp-plugin">SonarQube C/C++ Plugin</a> | <div class="content-wrapper">3.11</div> | **<a href="https://www.sonarsource.com/products/codeanalyzers/sonarcfamilyforcpp/rules-c.html#RSPEC-3588">S3588</a>** |  |
    76-
    77-
    78-## Related Vulnerabilities
    79-
    ✓ • 0ms

## Activity

    $ rg -n 'MISRA C:(2012|2023|2025)|AA\.Bibliography-MISRA' content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations | head -120
        rg -n 'MISRA C:(2012|2023|2025)|AA\.Bibliography-MISRA' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines | head -120
    content/4.sei-cert-c-coding-standard/08.recommendations/15.miscellaneous-msc/23.msc09-c.md:166:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Directive 1.1 (required) <br> Rule 4.1 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/21.dcl20-c.md:150:| [MISRA C:2012](https://www.securecoding.cert.org/confluence/display/seccode/AA.+Bibliography#AA.Bibliography-MISRA12) | Rule 8.2 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/09.expressions-exp/16.exp19-c.md:169:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 15.6 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/05.api03-c.md:94:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 21.3 (required) | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/05.api03-c.md:95:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Directive 4.12 (required) | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/13.memory-management-mem/07.mem05-c.md:155:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 17.2 (required)                                                                                                                                                                          |
    content/4.sei-cert-c-coding-standard/08.recommendations/09.expressions-exp/05.exp05-c.md:167:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 11.8 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/12.integers-int/11.int12-c.md:90:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule  10.1 (required)                                                                                                                                                                                                                                                                                          |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/04.dcl02-c.md:106:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Directive 4.5 (advisory)                                                                                                                                                                                            |
    content/4.sei-cert-c-coding-standard/08.recommendations/12.integers-int/13.int14-c.md:159:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 6.1 (required) <br> Rule 6.2 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/06.api04-c.md:84:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 21.3 (required) | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/06.api04-c.md:85:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Directive 4.12 (required) | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/08.error-handling-err/2.err00-c.md:65:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 17.1 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/09.expressions-exp/13.exp14-c.md:79:| [MISRA-C](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA04) | Rule 10.5                                                                                                                                                                                                                                                                                       |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/15.dcl13-c.md:162:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 8.13 (advisory)                                                                                                                                                                                                                                                                                                                      |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/20.dcl19-c.md:144:| [MISRA C:2012](https://www.securecoding.cert.org/confluence/display/seccode/AA.+Bibliography#AA.Bibliography-MISRA12) | Rule 8.9 (advisory)                                                                                                                                                                                                                     |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/03.dcl01-c.md:175:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 5.3 (required)                                                                                                                                                                                                               |
    content/4.sei-cert-c-coding-standard/08.recommendations/15.miscellaneous-msc/17.msc20-c.md:191:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO/MISRA12) | Rule 16.2 (required)                                                                                                                                                                                                                                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/09.expressions-exp/09.exp10-c.md:138:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 13.5 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/13.dcl11-c.md:138:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 17.1 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/09.expressions-exp/10.exp11-c.md:167:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Directive 1.1 (required)                                                                                                                                                                                                                                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/24.dcl23-c.md:99:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> |  | Supported indirectly via MISRA C:2012 Rules 5.1 , 5.2, 5.3 , 5.4 and 5.5. |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/24.dcl23-c.md:108:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/rulechecker">RuleChecker</a> | <div class="content-wrapper">25.10</div> |  | Supported indirectly via MISRA C:2012 Rules 5.1 , 5.2, 5.3 , 5.4 and 5.5. |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/24.dcl23-c.md:121:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 5.1 (required) <br> Rule 5.2 (required) <br> Rule 5.3 (required) <br> Rule 5.4 (required) <br> Rule 5.5 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/14.dcl12-c.md:96:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Directive 4.8 (advisory) |
    content/4.sei-cert-c-coding-standard/08.recommendations/12.integers-int/04.int02-c.md:255:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 10.1 (required) <br> Rule 10.3 (required) <br> Rule 10.4 (required) <br> Rule 10.6 (required) <br> Rule 10.7 (required) <br> Rule 10.8 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/09.dcl07-c.md:164:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 8.2 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/12.dcl10-c.md:123:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 17.1 (required)                                                                                           |
    content/4.sei-cert-c-coding-standard/08.recommendations/09.expressions-exp/02.exp00-c.md:105:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 12.1 (advisory)                                                                                                                                                                                                |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/16.dcl15-c.md:107:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 8.7 (advisory) <br> Rule 8.8 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/09.expressions-exp/07.exp08-c.md:176:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 18.1 (required) <br> Rule 18.2 (required) <br> Rule 18.3 (required) <br> Rule 18.4 (advisory) |
    content/4.sei-cert-c-coding-standard/08.recommendations/15.miscellaneous-msc/21.msc24-c.md:209:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 21.3 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/15.miscellaneous-msc/10.msc12-c.md:359:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 2.2 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/19.dcl18-c.md:70:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 7.1 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/17.dcl16-c.md:70:| [MISRA C:2012](https://www.securecoding.cert.org/confluence/display/seccode/AA.+Bibliography#AA.Bibliography-MISRA12) | Rule 7.3 (required)                                                                                                                         |
    content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/23.dcl22-c.md:104:| [MISRA C:2012](https://www.securecoding.cert.org/confluence/display/seccode/AA.+Bibliography#AA.Bibliography-MISRA12)       | Rule 2.2 (required)                                                                                                                                                                                                                     |
    content/4.sei-cert-c-coding-standard/08.recommendations/12.integers-int/09.int09-c.md:125:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 8.12 (required)                                                                                                                                                                                                         |
    content/4.sei-cert-c-coding-standard/08.recommendations/15.miscellaneous-msc/04.msc04-c.md:143:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 1.2 (advisory) <br> Rule 3.1 (required) <br> Directive 4.4 (advisory) |
    content/4.sei-cert-c-coding-standard/08.recommendations/15.miscellaneous-msc/07.msc07-c.md:183:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 2.1 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/12.integers-int/07.int07-c.md:62:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> |  | Supported indirectly via MISRA C:2012 rules 10.1, 10.3 and 10.4. |
    content/4.sei-cert-c-coding-standard/08.recommendations/12.integers-int/07.int07-c.md:74:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/rulechecker">RuleChecker</a> | <div class="content-wrapper">25.10</div> |  | Supported indirectly via MISRA C:2012 rules 10.1, 10.3 and 10.4. |
    content/4.sei-cert-c-coding-standard/08.recommendations/12.integers-int/07.int07-c.md:88:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 10.1 (required) <br> Rule 10.3 (required) <br> Rule 10.4 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/17.preprocessor-pre/07.pre06-c.md:73:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Directive 4.10 (required)                                                                                                                                                                                      |
    content/4.sei-cert-c-coding-standard/08.recommendations/17.preprocessor-pre/02.pre00-c.md:261:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Directive 4.9 (advisory)                                                                                                                                                 |
    content/4.sei-cert-c-coding-standard/08.recommendations/17.preprocessor-pre/08.pre07-c.md:115:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 4.2 (advisory)                                                                                                                                                                                  |
    content/4.sei-cert-c-coding-standard/08.recommendations/17.preprocessor-pre/03.pre01-c.md:110:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 20.7 (required) |
    content/4.sei-cert-c-coding-standard/03.rules/04.characters-and-strings-str/5.str34-c.md:189:| [MISRA-C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA04) | Rule 10.1 (required)<br>Rule 10.2 (required)<br>Rule 10.3 (required)<br>Rule 10.4 (required) |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/4.arr02-c.md:118:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 8.11 (advisory)                                                                                                                                                                                                                         | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/4.arr02-c.md:119:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 9.5 (required)                                                                                                                                                                                                                          | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/04.characters-and-strings-str/03.str01-c.md:17:Dynamic allocation is often disallowed in safety-critical systems. For example, the MISRA standard requires that "dynamic heap memory allocation shall not be used" \[ [MISRA 2004](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA04) \]. Some safety-critical systems can take advantage of dynamic memory allocation during initialization but not during operations. For example, avionics software may dynamically allocate memory while initializing the aircraft but not during flight.
    content/4.sei-cert-c-coding-standard/08.recommendations/04.characters-and-strings-str/03.str01-c.md:41:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Directive 4.12 (required) |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/3.arr32-c.md:162:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> | **variable-array-length** | Supported, absence of variable length arrays can be enforced using MISRA C:2023 Rule 18.8. |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/3.arr32-c.md:174:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/rulechecker">RuleChecker</a> | <div class="content-wrapper">25.10</div> | **variable-array-length** | Supported, absence of variable length arrays can be enforced using MISRA C:2023 Rule 18.8. |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/02.exp30-c.md:271:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 13.2 (required)                                                                                                                                                            | CERT cross-reference in [MISRA C:2012 – Addendum 3](https://www.misra.org.uk/Publications/tabid/57/Default.aspx#label-c3-add3) |
    content/4.sei-cert-c-coding-standard/08.recommendations/04.characters-and-strings-str/06.str04-c.md:95:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 10.1 (required) <br> Rule 10.2 (required) <br> Rule 10.3 (required) <br> Rule 10.4 (required) |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/12.exp43-c.md:323:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> | **restrict** | Supported indirectly via MISRA C:2012 Rule 8.14. |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/12.exp43-c.md:335:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/rulechecker">RuleChecker</a> | <div class="content-wrapper">25.10</div> | **restrict** | Supported indirectly via MISRA C:2012 Rule 8.14. |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/12.exp43-c.md:336:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/sonarqube-ccpp-plugin">SonarQube C/C++ Plugin</a> | <div class="content-wrapper">3.11</div> | **<a href="https://www.sonarsource.com/products/codeanalyzers/sonarcfamilyforcpp/rules-c.html#RSPEC-1836">S1836</a>** | Implements <a href="/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12">MISRA C:2012</a> Rule 8.14 to flag uses of <code>restrict</code> |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/12.exp43-c.md:349:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 8.14 (required) <sup>1</sup>                                                                             | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/04.characters-and-strings-str/10.str10-c.md:11:According to [MISRA 2008](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA08) , concatenation of wide and narrow string literals leads to [undefined behavior](/sei-cert-c-coding-standard/back-matter/bb-definitions#BB.Definitions-undefinedbehavior) . This was once considered implicitly undefined behavior until C90 \[ [ISO/IEC 9899:1990](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO-IEC9899-1990) \]. However, C99 defined this behavior \[ [ISO/IEC 9899:1999](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO-IEC9899-1999) \], and C11 further explains in subclause 6.4.5, paragraph 5 \[ [ISO/IEC 9899:2011](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO-IEC9899-2011) \]:
    content/4.sei-cert-c-coding-standard/08.recommendations/04.characters-and-strings-str/10.str10-c.md:82:| [MISRA C++:2008](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA08) | Rule 2-13-5 |
    content/4.sei-cert-c-coding-standard/08.recommendations/04.characters-and-strings-str/02.str00-c.md:67:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> |  | Supported indirectly via MISRA C:2004 rule 6.1 and MISRA C:2012 rule 10.1. |
    content/4.sei-cert-c-coding-standard/08.recommendations/04.characters-and-strings-str/02.str00-c.md:72:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/rulechecker">RuleChecker</a> | <div class="content-wrapper">25.10</div> |  | Supported indirectly via MISRA C:2004 rule 6.1 and MISRA C:2012 rule 10.1. |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/07.exp36-c.md:258:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 11.1 (required)                                                                                                                                                                                 | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/07.exp36-c.md:259:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 11.2 (required)                                                                                                                                                                                 | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/07.exp36-c.md:260:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 11.5 (advisory)                                                                                                                                                                                 | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/07.exp36-c.md:261:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 11.7 (required)                                                                                                                                                                                 | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/2.flp30-c.md:133:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Directive 1.1 (required)                                                                                                                                                      | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/2.flp30-c.md:134:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 14.1 (required)                                                                                                                                                          | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/04.characters-and-strings-str/09.str09-c.md:64:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> | | Supported indirectly via MISRA C:2012 rule 10.1. |
    content/4.sei-cert-c-coding-standard/08.recommendations/04.characters-and-strings-str/09.str09-c.md:70:| <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/rulechecker">RuleChecker</a> | <div class="content-wrapper">25.10</div> | | Supported indirectly via MISRA C:2012 rule 10.1. |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/03.exp32-c.md:120:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 11.8 (required)                                                                                                                          | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/2.arr30-c.md:435:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 18.1 (required)                                                                                                                | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/08.exp37-c.md:261:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 8.2 (required)                                                                                                                                                  | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/08.exp37-c.md:262:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 17.3 (mandatory)                                                                                                                                                | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/7.arr39-c.md:215:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 18.1 (required)                                                                                                                  | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/7.arr39-c.md:216:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 18.2 (required)                                                                                                                  | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/7.arr39-c.md:217:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 18.3 (required)                                                                                                                  | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/7.arr39-c.md:218:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 18.4 (advisory)                                                                                                                  | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/2.mem30-c.md:273:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 18.6 (required)                                                                                                                         | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/04.dcl36-c.md:142:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 8.2 (required)   | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/04.dcl36-c.md:143:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 8.4 (required)   | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/04.dcl36-c.md:144:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 8.8 (required)   | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/04.dcl36-c.md:145:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 17.3 (mandatory) | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/08.dcl40-c.md:259:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)            | Rule 8.4 (required)                                                     | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/02.dcl30-c.md:211:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 18.6 (required)                                                                                                        | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/05.dcl37-c.md:328:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)            | Rule 21.1 (required)                                                                                                                           | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/05.dcl37-c.md:329:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)            | Rule 21.2 (required)                                                                                                                           | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/09.dcl41-c.md:121:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 16.1 (required) | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/03.dcl31-c.md:194:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 8.1 (required)                                                                                                                                                  | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/3.int31-c.md:374:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 10.1 (required)                                                                                                                                                                                    | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/3.int31-c.md:375:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 10.3 (required)                                                                                                                                                                                    | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/3.int31-c.md:376:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 10.4 (required)                                                                                                                                                                                    | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/3.int31-c.md:377:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 10.6 (required)                                                                                                                                                                                    | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/3.int31-c.md:378:| [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 10.7 (required)                                                                                                                                                                                    | Prior to 2018-01-12: CERT: Unspecified Relationship |
    content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/01.index.md:15:-   [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/ff-related-guidelines/2012)
    content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/01.index.md:19:-   [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/ff-related-guidelines/misra-c-2025)
    content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md:1:# MISRA C:2025
    ✓ • 0ms

## Assistant

The destination tables have four analyzer columns, while the source MISRA table has two columns. I’m preserving the source row exactly as requested—replacing only its first cell with the MISRA bibliography link—so the script copies every remaining source cell verbatim. I’ll also make it idempotent, preflight all targets before writing, and include a dry-run mode.

## Activity

    $ stat -c '%a %n' scripts/manage_links.py scripts/update-package-lock.sh
        sed -n '130,190p' content/4.sei-cert-c-coding-standard/08.recommendations/06.declarations-and-initialization-dcl/03.dcl01-c.md
        sed -n '250,285p' content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/02.exp30-c.md
        sed -n '1,150p' content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
    755 scripts/manage_links.py
    755 scripts/update-package-lock.sh
      int tmp = 100;
      int a = 10, b = 20;
      SWAP(int, a, b); /* Hidden redeclaration of tmp is acceptable */
      SWAP(int, tmp, b); /* NONCOMPLIANT: Hidden redeclaration of tmp clashes with argument */
    }
    ```
    ::
    
    ## Risk Assessment
    
    Reusing a variable name in a subscope can lead to unintentionally referencing an incorrect variable.
    
    | Recommendation | Severity | Likelihood | Detectable | Repairable | Priority | Level |
    | --- | --- | --- | --- | --- | --- | --- |
    | DCL01-C | Low | Unlikely | Yes | Yes | <span style="color: #27ae60;">**P3**</span> | <span style="color: #27ae60;">**L3**</span> |
    
    ## Automated Detection
    
    | Tool      | Version  | Checker | Description |
    |-----------|----------|---------|-------------|
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/astree">Astrée</a> | <div class="content-wrapper">25.10</div> | **identifier-hidden** | Fully checked |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/axivion-suite">Axivion Suite</a> | <div class="content-wrapper">7.12.0</div> | **CertC-DCL01** |  |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/codesonar">CodeSonar</a> | <div class="content-wrapper">27.0</div> | **LANG.ID.ND.NEST** | Non-distinct identifiers: nested scope |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/rose">Compass/ROSE</a> |  |  |  |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/eclair">ECLAIR</a> | <div class="content-wrapper">1.2</div> | **CC2.DCL01** | Fully implemented |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/helix-qac">Helix QAC</a> | <div class="content-wrapper">2025.2</div> | **C0795, C0796, C2547, C3334** |  |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/klocwork">Klocwork</a> | <div class="content-wrapper">2025.2</div> | **MISRA.VAR.HIDDEN** |  |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/ldra">LDRA tool suite</a> | <div class="content-wrapper">10.6.0</div> | **131 S** | Fully implemented |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/parasoft">Parasoft C/C++test</a> | <div class="content-wrapper">2026.1</div> | **CERT_C-DCL01-a** <br /> **CERT_C-DCL01-b** | Identifier declared in a local or function prototype scope shall not hide an identifier declared in a global or namespace scope<br /> Identifiers declared in an inner local scope should not hide identifiers declared in an outer local scope |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/pc-lint-plus">PC-lint Plus</a> | <div class="content-wrapper">1.4</div> | **578** | Fully supported |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/polyspace-bug-finder">Polyspace Bug Finder</a> | <div class="content-wrapper">R2025b</div> | <a href="https://www.mathworks.com/help/bugfinder/ref/certcrec.dcl01c.html">CERT C: Rec. DCL01-C</a> | Checks for variable shadowing (rule fully covered) |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/pvs-studio">PVS-Studio</a> | <div class="content-wrapper">8.01</div> | <a href="https://pvs-studio.com/en/docs/warnings/v561/">**V561**</a> , <a href="https://pvs-studio.com/en/docs/warnings/v688/">**V688**</a> , <a href="https://pvs-studio.com/en/docs/warnings/v703/">**V703**</a> , **<a href="https://pvs-studio.com/en/docs/warnings/v711/">V711</a>** , **<a href="https://pvs-studio.com/en/docs/warnings/v2015/">V2015</a>** |  |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/rulechecker">RuleChecker</a> | <div class="content-wrapper">25.10</div> | **identifier-hidden** | Fully checked |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/security-reviewer-static-reviewer">Security Reviewer - Static Reviewer</a> | <div class="content-wrapper">6.02</div> | **C126** <br /> **C127** | Fully Implemented |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/splint">Splint</a> | <div class="content-wrapper">3.1.1</div> |  |  |
    
    
    ## Related Vulnerabilities
    
    Search for vulnerabilities resulting from the violation of this rule on the [CERT website](https://www.kb.cert.org/vuls/search/?q=DCL01-C) .
    
    ## Related Guidelines
    
    |                                                                                                 |                                                                                                                                                                                                                                   |
    |-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12) | Rule 5.3 (required)                                                                                                                                                                                                               |
    
    
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/security-reviewer-static-reviewer">Security Reviewer - Static Reviewer</a> | <div class="content-wrapper">6.02</div> | **C50** | Fully implemented |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/splint">Splint</a> | <div class="content-wrapper">3.1.1</div> |  |  |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/sonarqube-ccpp-plugin">SonarQube C/C++ Plugin</a> | <div class="content-wrapper">3.11</div> | **<a href="https://www.sonarsource.com/products/codeanalyzers/sonarcfamilyforcpp/rules-c.html#RSPEC-881">IncAndDecMixedWithOtherOperators</a>** |  |
    | <a href="/sei-cert-c-coding-standard/back-matter/ee-analyzers/trustinsoft-analyzer">TrustInSoft Analyzer</a> | <div class="content-wrapper">1.38</div> | **separated** | Exhaustively verified (see <a href="https://taas.trust-in-soft.com/tsnippet/t/17da0bf9">one compliant and one non-compliant example</a> ). |
    
    
    ## Related Vulnerabilities
    
    Search for [vulnerabilities](/sei-cert-c-coding-standard/back-matter/bb-definitions#BB.Definitions-vulnerability) resulting from the violation of this rule on the [CERT website](https://www.kb.cert.org/vuls/search/?q=EXP30-C) .
    
    ## Related Guidelines
    
    [Key here](/sei-cert-c-coding-standard/front-matter/introduction/how-this-coding-standard-is-organized#HowthisCodingStandardisOrganized-RelatedGuidelines) (explains table format and definitions)
    
    |                                                                                                                      |                                                                                                                                                                                 |                                                                                                                                |
    |----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
    | Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                   | Relationship                                                                                                                   |
    | [CERT C](/sei-cert-cpp-coding-standard/)                                                                             | [EXP50-CPP. Do not depend on the order of evaluation for side effects](/sei-cert-cpp-coding-standard/rules/expressions-exp/exp50-cpp)                                           | Prior to 2018-01-12: CERT: Unspecified Relationship                                                                            |
    | [CERT Oracle Secure Coding Standard for Java](/sei-cert-oracle-coding-standard-for-java/)                            | [EXP05-J. Do not follow a write by a subsequent write or read of the same object within an expression](/sei-cert-oracle-coding-standard-for-java/rules/expressions-exp/exp05-j) | Prior to 2018-01-12: CERT: Unspecified Relationship                                                                            |
    | [ISO/IEC TR 24772:2013](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO-IECTR24772-2013) | Operator Precedence/Order of Evaluation \[JCW\]                                                                                                                                 | Prior to 2018-01-12: CERT: Unspecified Relationship                                                                            |
    | [ISO/IEC TR 24772:2013](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO-IECTR24772-2013) | Side-effects and Order of Evaluation \[SAM\]                                                                                                                                    | Prior to 2018-01-12: CERT: Unspecified Relationship                                                                            |
    | [MISRA C:2012](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA12)                      | Rule 13.2 (required)                                                                                                                                                            | CERT cross-reference in [MISRA C:2012 – Addendum 3](https://www.misra.org.uk/Publications/tabid/57/Default.aspx#label-c3-add3) |
    | [CWE 2.11](https://cwe.mitre.org/)                                                                                    | [CWE-758](https://cwe.mitre.org/data/definitions/758.html)                                                                                                                        | 2017-07-07: CERT: Rule subset of CWE                                                                                           |
    
    ## CERT-CWE Mapping Notes
    
    [Key here](/sei-cert-c-coding-standard/front-matter/introduction/how-this-coding-standard-is-organized#HowthisCodingStandardisOrganized-CERT-CWEMappingNotes) for mapping notes
    
    ### CWE-758 and EXP30-C
    
    Independent( INT34-C, INT36-C, MEM30-C, MSC37-C, FLP32-C, EXP33-C, EXP30-C, ERR34-C, ARR32-C)
    
    CWE-758 = Union( EXP30-C, list) where list =
    
    
    
    # MISRA C:2025
    
    This page was automatically generated and should not be edited.
    
    | CERT Rule                                                                                               | Related Guidelines                                                                                                                                      |
    |---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
    | [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c)   | Dir 4.11                                                          |
    | [ARR01-C](/sei-cert-c-coding-standard/recommendations/arrays-arr/arr01-c)                               | Rule 12.5                                                         |
    | [ARR30-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr30-c)                                         | Rule 1.3, 18.1, 21.17, 21.18                                      |
    | [ARR32-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr32-c)                                         | Rule 18.8                                                         |
    | [ARR36-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr36-c)                                         | Rule 18.2, 18.3                                                   |
    | [ARR37-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr37-c)                                         | Rule 18.1, 18.4                                                   |
    | [ARR38-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr38-c)                                         | Rule 1.3, 21.6, 21.17, 21.18                                      |
    | [ARR39-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr39-c)                                         | Rule 1.3, 18.4                                                    |
    | [CON30-C](/sei-cert-c-coding-standard/rules/concurrency-con/con30-c)                                    | Dir 4.12, Rule 22.1, 22.13                                        |
    | [CON31-C](/sei-cert-c-coding-standard/rules/concurrency-con/con31-c)                                    | Rule 22.15, 22.16                                                 |
    | [CON32-C](/sei-cert-c-coding-standard/rules/concurrency-con/con32-c)                                    | Dir 5.1                                                           |
    | [CON33-C](/sei-cert-c-coding-standard/rules/concurrency-con/con33-c)                                    | Dir 5.1, Rule 9.7, 21.8, 21.19, 21.24                             |
    | [CON34-C](/sei-cert-c-coding-standard/rules/concurrency-con/con34-c)                                    | Dir 4.12, Rule 18.6, 18.9, 22.13, 22.15                           |
    | [CON35-C](/sei-cert-c-coding-standard/rules/concurrency-con/con35-c)                                    | Dir 5.2                                                           |
    | [CON36-C](/sei-cert-c-coding-standard/rules/concurrency-con/con36-c)                                    | Dir 4.13, 5.1                                                     |
    | [CON37-C](/sei-cert-c-coding-standard/rules/concurrency-con/con37-c)                                    | Rule 21.5                                                         |
    | [CON39-C](/sei-cert-c-coding-standard/rules/concurrency-con/con39-c)                                    | Rule 22.11                                                        |
    | [CON40-C](/sei-cert-c-coding-standard/rules/concurrency-con/con40-c)                                    | Rule 13.2                                                         |
    | [CON43-C](/sei-cert-c-coding-standard/rules/concurrency-con/con43-c)                                    | Dir 5.1                                                           |
    | [DCL01-C](/sei-cert-c-coding-standard/recommendations/declarations-and-initialization-dcl/dcl01-c)      | Rule 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9                            |
    | [DCL02-C](/sei-cert-c-coding-standard/recommendations/declarations-and-initialization-dcl/dcl02-c)      | Dir 4.5, Rule 5.1, 5.2                                            |
    | [DCL16-C](/sei-cert-c-coding-standard/recommendations/declarations-and-initialization-dcl/dcl16-c)      | Rule 7.3                                                          |
    | [DCL30-C](/sei-cert-c-coding-standard/rules/declarations-and-initialization-dcl/dcl30-c)                | Rule 1.3, 18.6                                                    |
    | [DCL31-C](/sei-cert-c-coding-standard/rules/declarations-and-initialization-dcl/dcl31-c)                | Rule 8.1, 17.3                                                    |
    | [DCL36-C](/sei-cert-c-coding-standard/rules/declarations-and-initialization-dcl/dcl36-c)                | Rule 8.2, 8.4, 8.8, 17.3                                          |
    | [DCL37-C](/sei-cert-c-coding-standard/rules/declarations-and-initialization-dcl/dcl37-c)                | Rule 1.3, 5.10, 20.15, 21.1, 21.2                                 |
    | [DCL38-C](/sei-cert-c-coding-standard/rules/declarations-and-initialization-dcl/dcl38-c)                | Rule 1.1, 1.3, 21.3                                               |
    | [DCL40-C](/sei-cert-c-coding-standard/rules/declarations-and-initialization-dcl/dcl40-c)                | Rule 1.3, 5.1, 5.2, 8.3, 8.4, 8.5                                 |
    | [DCL41-C](/sei-cert-c-coding-standard/rules/declarations-and-initialization-dcl/dcl41-c)                | Rule 16.1                                                         |
    | [ENV30-C](/sei-cert-c-coding-standard/rules/environment-env/env30-c)                                    | Rule 21.10, 21.19                                                 |
    | [ENV31-C](/sei-cert-c-coding-standard/rules/environment-env/env31-c)                                    | Rule 1.3                                                          |
    | [ENV32-C](/sei-cert-c-coding-standard/rules/environment-env/env32-c)                                    | Rule 21.4, 21.8                                                   |
    | [ENV33-C](/sei-cert-c-coding-standard/rules/environment-env/env33-c)                                    | Rule 21.21                                                        |
    | [ENV34-C](/sei-cert-c-coding-standard/rules/environment-env/env34-c)                                    | Rule 21.20                                                        |
    | [ERR04-C](/sei-cert-c-coding-standard/recommendations/error-handling-err/err04-c)                       | Rule 21.8                                                         |
    | [ERR30-C](/sei-cert-c-coding-standard/rules/error-handling-err/err30-c)                                 | Rule 22.8, 22.9, 22.10                                            |
    | [ERR32-C](/sei-cert-c-coding-standard/rules/error-handling-err/err32-c)                                 | Rule 21.5                                                         |
    | [ERR33-C](/sei-cert-c-coding-standard/rules/error-handling-err/err33-c)                                 | Dir 4.7                                                           |
    | [ERR34-C](/sei-cert-c-coding-standard/rules/error-handling-err/err34-c)                                 | Dir 4.7, Rule 21.7                                                |
    | [EXP00-C](/sei-cert-c-coding-standard/recommendations/expressions-exp/exp00-c)                          | Rule 12.1                                                         |
    | [EXP02-C](/sei-cert-c-coding-standard/recommendations/expressions-exp/exp02-c)                          | Rule 13.5                                                         |
    | [EXP12-C](/sei-cert-c-coding-standard/recommendations/expressions-exp/exp12-c)                          | Rule 17.5                                                         |
    | [EXP19-C](/sei-cert-c-coding-standard/recommendations/expressions-exp/exp19-c)                          | Rule 15.6                                                         |
    | [EXP30-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp30-c)                                    | Rule 1.3, 13.2                                                    |
    | [EXP32-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp32-c)                                    | Rule 1.3, 11.8                                                    |
    | [EXP33-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp33-c)                                    | Dir 4.1, Rule 1.3, 9.1                                            |
    | [EXP34-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp34-c)                                    | Dir 4.1, Rule 1.3                                                 |
    | [EXP35-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp35-c)                                    | Rule 18.9                                                         |
    | [EXP36-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp36-c)                                    | Rule 1.3, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6                      |
    | [EXP37-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp37-c)                                    | Rule 8.2, 17.3                                                    |
    | [EXP39-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp39-c)                                    | Rule 1.3, 11.1, 11.2, 11.3, 11.7                                  |
    | [EXP40-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp40-c)                                    | Rule 1.3, 7.4, 11.8                                               |
    | [EXP42-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp42-c)                                    | Rule 21.16                                                        |
    | [EXP43-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp43-c)                                    | Rule 1.3, 8.14                                                    |
    | [EXP44-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp44-c)                                    | Rule 13.6, 18.10, 23.2, 23.7                                      |
    | [EXP45-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp45-c)                                    | Rule 13.4, Rule 14.4                                              |
    | [EXP46-C](/sei-cert-c-coding-standard/rules/expressions-exp/exp46-c)                                    | Rule 10.1                                                         |
    | [FIO32-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio32-c)                                   | Rule 21.6                                                         |
    | [FIO34-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio34-c)                                   | Rule 22.7                                                         |
    | [FIO37-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio37-c)                                   | Rule 21.6                                                         |
    | [FIO38-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio38-c)                                   | Rule 22.5                                                         |
    | [FIO39-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio39-c)                                   | Dir 4.13, Rule 21.6, 22.4                                         |
    | [FIO40-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio40-c)                                   | Rule 21.6                                                         |
    | [FIO41-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio41-c)                                   | Rule 21.6                                                         |
    | [FIO42-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio42-c)                                   | Rule 22.1                                                         |
    | [FIO44-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio44-c)                                   | Rule 21.6                                                         |
    | [FIO45-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio45-c)                                   | Dir 5.1                                                           |
    | [FIO46-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio46-c)                                   | Rule 22.6                                                         |
    | [FIO47-C](/sei-cert-c-coding-standard/rules/input-output-fio/fio47-c)                                   | Rule 21.6                                                         |
    | [FLP30-C](/sei-cert-c-coding-standard/rules/floating-point-flp/flp30-c)                                 | Rule 14.1                                                         |
    | [FLP32-C](/sei-cert-c-coding-standard/rules/floating-point-flp/flp32-c)                                 | Dir 4.11, Rule 21.12                                              |
    | [FLP34-C](/sei-cert-c-coding-standard/rules/floating-point-flp/flp34-c)                                 | Rule 10.3, 10.4, 10.5, 10.8                                       |
    | [FLP36-C](/sei-cert-c-coding-standard/rules/floating-point-flp/flp36-c)                                 | Dir 1.1, Rule 1.3, 10.3, 10.4, 10.5, 10.8                         |
    | [FLP37-C](/sei-cert-c-coding-standard/rules/floating-point-flp/flp37-c)                                 | Rule 21.16                                                        |
    | [FLP38-C](/sei-cert-c-coding-standard/rules/floating-point-flp/flp38-c)                                 | Rule 21.11, 21.22, 21.23                                          |
    | [INT30-C](/sei-cert-c-coding-standard/rules/integers-int/int30-c)                                       | Rule 12.4                                                         |
    | [INT31-C](/sei-cert-c-coding-standard/rules/integers-int/int31-c)                                       | Rule 10.1, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 21.6, 21.13, 21.18 |
    | [INT32-C](/sei-cert-c-coding-standard/rules/integers-int/int32-c)                                       | Dir 4.1, Rule 1.3                                                 |
    | [INT33-C](/sei-cert-c-coding-standard/rules/integers-int/int33-c)                                       | Dir 4.1, Rule 1.3                                                 |
    | [INT34-C](/sei-cert-c-coding-standard/rules/integers-int/int34-c)                                       | Rule 10.1, 12.2                                                   |
    | [INT35-C](/sei-cert-c-coding-standard/rules/integers-int/int35-c)                                       | Dir 4.1, Rule 1.3                                                 |
    | [INT36-C](/sei-cert-c-coding-standard/rules/integers-int/int36-c)                                       | Dir 1.1, Rule 11.1, 11.2, 11.4, 11.6, 11.7                        |
    | [MEM30-C](/sei-cert-c-coding-standard/rules/memory-management-mem/mem30-c)                              | Dir 4.12, Rule 1.3, 21.3, 22.2                                    |
    | [MEM31-C](/sei-cert-c-coding-standard/rules/memory-management-mem/mem31-c)                              | Rule 22.1                                                         |
    | [MEM33-C](/sei-cert-c-coding-standard/rules/memory-management-mem/mem33-c)                              | Rule 18.7                                                         |
    | [MEM34-C](/sei-cert-c-coding-standard/rules/memory-management-mem/mem34-c)                              | Rule 22.2                                                         |
    | [MEM35-C](/sei-cert-c-coding-standard/rules/memory-management-mem/mem35-c)                              | Dir 4.1, 4.12, Rule 1.3, 21.3                                     |
    | [MEM36-C](/sei-cert-c-coding-standard/rules/memory-management-mem/mem36-c)                              | Rule 21.3                                                         |
    | [MSC00-C](/sei-cert-c-coding-standard/recommendations/miscellaneous-msc/msc00-c)                        | Dir 2.1                                                           |
    | [MSC01-C](/sei-cert-c-coding-standard/recommendations/miscellaneous-msc/msc01-c)                        | Rule 15.7 16.4                                                    |
    | [MSC04-C](/sei-cert-c-coding-standard/recommendations/miscellaneous-msc/msc04-c)                        | Rule 3.1, 3.2                                                     |
    | [MSC07-C](/sei-cert-c-coding-standard/recommendations/miscellaneous-msc/msc07-c)                        | Dir 4.4, Rule 2.2                                                 |
    | [MSC12-C](/sei-cert-c-coding-standard/recommendations/miscellaneous-msc/msc12-c)                        | Rule 2.1                                                          |
    | [MSC13-C](/sei-cert-c-coding-standard/recommendations/miscellaneous-msc/msc13-c)                        | Rule 2.7, 2.8                                                     |
    | [MSC15-C](/sei-cert-c-coding-standard/recommendations/miscellaneous-msc/msc15-c)                        | Rule 1.3                                                          |
    | [MSC17-C](/sei-cert-c-coding-standard/recommendations/miscellaneous-msc/msc17-c)                        | Rule 16.3                                                         |
    | [MSC24-C](/sei-cert-c-coding-standard/recommendations/miscellaneous-msc/msc24-c)                        | Rule 1.5                                                          |
    | [MSC30-C](/sei-cert-c-coding-standard/rules/miscellaneous-msc/msc30-c)                                  | Rule 21.24                                                        |
    | [MSC32-C](/sei-cert-c-coding-standard/rules/miscellaneous-msc/msc32-c)                                  | Rule 21.24                                                        |
    | [MSC33-C](/sei-cert-c-coding-standard/rules/miscellaneous-msc/msc33-c)                                  | Rule 21.10                                                        |
    | [MSC37-C](/sei-cert-c-coding-standard/rules/miscellaneous-msc/msc37-c)                                  | Rule 17.4                                                         |
    | [MSC38-C](/sei-cert-c-coding-standard/rules/miscellaneous-msc/msc38-c)                                  | Rule 1.1, 1.3                                                     |
    | [MSC39-C](/sei-cert-c-coding-standard/rules/miscellaneous-msc/msc39-c)                                  | Rule 17.1                                                         |
    | [MSC40-C](/sei-cert-c-coding-standard/rules/miscellaneous-msc/msc40-c)                                  | Rule 1.1                                                          |
    | [POS53-C](/sei-cert-c-coding-standard/rules/posix-pos/pos53-c)                                          | Rule 22.19                                                        |
    | [PRE06-C](/sei-cert-c-coding-standard/recommendations/preprocessor-pre/pre06-c)                         | Dir 4.10                                                          |
    | [PRE12-C](/sei-cert-c-coding-standard/recommendations/preprocessor-pre/pre12-c)                         | Rule 20.7                                                         |
    | [PRE30-C](/sei-cert-c-coding-standard/rules/preprocessor-pre/pre30-c)                                   | Rule 1.3                                                          |
    | [PRE31-C](/sei-cert-c-coding-standard/rules/preprocessor-pre/pre31-c)                                   | Rule 13.2                                                         |
    | [PRE32-C](/sei-cert-c-coding-standard/rules/preprocessor-pre/pre32-c)                                   | Rule 1.3, 20.6                                                    |
    | [SIG30-C](/sei-cert-c-coding-standard/rules/signals-sig/sig30-c)                                        | Rule 21.5                                                         |
    | [SIG31-C](/sei-cert-c-coding-standard/rules/signals-sig/sig31-c)                                        | Rule 21.5                                                         |
    | [SIG34-C](/sei-cert-c-coding-standard/rules/signals-sig/sig34-c)                                        | Rule 21.5                                                         |
    | [SIG35-C](/sei-cert-c-coding-standard/rules/signals-sig/sig35-c)                                        | Rule 21.5                                                         |
    | [STR05-C](/sei-cert-c-coding-standard/recommendations/characters-and-strings-str/str05-c)               | Rule 7.4                                                          |
    | [STR30-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str30-c)                         | Rule 7.4                                                          |
    | [STR31-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str31-c)                         | Dir 4.1, Rule 1.3, 18.1, 21.6, 21.17, 21.18                       |
    | [STR32-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str32-c)                         | Rule 21.16                                                        |
    | [STR34-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str34-c)                         | Rule 10.1, 10.3, 10.4                                             |
    | [STR37-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str37-c)                         | Rule 21.13                                                        |
    | [STR38-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str38-c)                         | Rule 1.3, 10.3                                                    |
    ✓ • 0ms

## Activity

    $ git status --short -- scripts content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md | sed -n '1,120p'
        rg -n '^## Automated Detection\s*$' content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations | wc -l
        rg -n '^\| \[MISRA C:2025\]\(/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA\.Bibliography-MISRA25\)' content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations | wc -l
    294
    0
    ✓ • 91ms

## Activity

    file changes: Completed · 1 changes
    Add: /host/scripts/distribute_guideline_table.py
    #!/usr/bin/env python3
    """Distribute a related-guidelines table to guideline pages.
    
    For each row in the MISRA C:2025 table, this script finds the linked CERT C
    rule or recommendation and adds a row to its Automated Detection table.  The
    new row replaces the source row's first cell with ``MISRA_LINK`` and preserves
    all remaining source cells.
    
    Run from anywhere in the repository:
    
        python3 scripts/distribute_guideline_table.py --dry-run
        python3 scripts/distribute_guideline_table.py
    
    The script preflights every source row and destination before writing any
    files.  It is safe to rerun: an existing MISRA C:2025 row is left alone when
    it is current and updated in place when its contents differ.
    """
    
    from __future__ import annotations
    
    import argparse
    import os
    import re
    import sys
    import tempfile
    from dataclasses import dataclass
    from pathlib import Path
    from typing import Dict, List, Optional, Sequence, Tuple
    
    
    MISRA_LINK = (
        "[MISRA C:2025]"
        "(/sei-cert-c-coding-standard/back-matter/"
        "aa-bibliography#AA.Bibliography-MISRA25)"
    )
    
    REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
    DEFAULT_SOURCE = REPOSITORY_ROOT / (
        "content/4.sei-cert-c-coding-standard/04.back-matter/"
        "7.ff-related-guidelines/10.misra-c-2025.md"
    )
    DEFAULT_STANDARD_ROOT = (
        REPOSITORY_ROOT / "content/4.sei-cert-c-coding-standard"
    )
    
    GUIDELINE_LINK_RE = re.compile(
        r"^\[(?P<code>[A-Z]{3}\d{2}-C)\]"
        r"\((?P<url>/sei-cert-c-coding-standard/"
        r"(?P<kind>rules|recommendations)/"
        r"(?P<category>[a-z0-9-]+)/(?P<slug>[a-z]{3}\d{2}-c))\)$"
    )
    GUIDELINE_FILE_RE = re.compile(r"^\d+\.(?P<slug>[a-z]{3}\d{2}-c)\.md$")
    HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)\s*$")
    SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
    
    
    class DistributionError(Exception):
        """Raised when input cannot be distributed without ambiguity."""
    
    
    @dataclass(frozen=True)
    class SourceRow:
        code: str
        kind: str
        category: str
        slug: str
        cells: Tuple[str, ...]
    
        @property
        def destination_cells(self) -> Tuple[str, ...]:
            return (MISRA_LINK, *self.cells[1:])
    
    
    @dataclass(frozen=True)
    class MarkdownTable:
        header_index: int
        separator_index: int
        first_data_index: int
        end_index: int
        header_cells: Tuple[str, ...]
    
    
    @dataclass(frozen=True)
    class PlannedChange:
        path: Path
        original: str
        updated: str
        action: str
    
    
    def parse_markdown_row(line: str) -> Optional[Tuple[str, ...]]:
        """Return trimmed cells from a pipe-delimited Markdown row.
    
        Pipes escaped with a backslash remain part of the cell content.
        """
    
        stripped = line.rstrip("\r\n").strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            return None
    
        body = stripped[1:-1]
        cells: List[str] = []
        current: List[str] = []
        backslash_run = 0
    
        for character in body:
            if character == "|" and backslash_run % 2 == 0:
                cells.append("".join(current).strip())
                current = []
            else:
                current.append(character)
    
            if character == "\\":
                backslash_run += 1
            else:
                backslash_run = 0
    
        cells.append("".join(current).strip())
        return tuple(cells)
    
    
    def is_separator_row(cells: Optional[Tuple[str, ...]]) -> bool:
        return bool(cells) and all(SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)
    
    
    def find_markdown_tables(
        lines: Sequence[str], start: int = 0, end: Optional[int] = None
    ) -> List[MarkdownTable]:
        """Find conventional Markdown tables between two line indexes."""
    
        if end is None:
            end = len(lines)
    
        tables: List[MarkdownTable] = []
        index = start
        while index + 1 < end:
            header = parse_markdown_row(lines[index])
            separator = parse_markdown_row(lines[index + 1])
            if header is None or not is_separator_row(separator):
                index += 1
                continue
    
            if len(header) != len(separator):
                index += 1
                continue
    
            table_end = index + 2
            while table_end < end and parse_markdown_row(lines[table_end]) is not None:
                table_end += 1
    
            tables.append(
                MarkdownTable(
                    header_index=index,
                    separator_index=index + 1,
                    first_data_index=index + 2,
                    end_index=table_end,
                    header_cells=header,
                )
            )
            index = table_end
    
        return tables
    
    
    def read_utf8(path: Path) -> str:
        try:
            return path.read_bytes().decode("utf-8")
        except FileNotFoundError as error:
            raise DistributionError(f"File does not exist: {path}") from error
        except UnicodeDecodeError as error:
            raise DistributionError(f"File is not valid UTF-8: {path}") from error
    
    
    def parse_source_rows(source: Path) -> List[SourceRow]:
        text = read_utf8(source)
        lines = text.splitlines(keepends=True)
        matching_tables = [
            table
            for table in find_markdown_tables(lines)
            if table.header_cells[:2] == ("CERT Rule", "Related Guidelines")
        ]
    
        if len(matching_tables) != 1:
            raise DistributionError(
                f"Expected exactly one 'CERT Rule | Related Guidelines' table in "
                f"{source}, found {len(matching_tables)}"
            )
    
        table = matching_tables[0]
        rows: List[SourceRow] = []
        seen_codes: Dict[str, int] = {}
    
        for line_index in range(table.first_data_index, table.end_index):
            cells = parse_markdown_row(lines[line_index])
            if cells is None or len(cells) < 2:
                raise DistributionError(
                    f"Malformed source row at {source}:{line_index + 1}"
                )
    
            match = GUIDELINE_LINK_RE.fullmatch(cells[0])
            if match is None:
                raise DistributionError(
                    f"The first cell at {source}:{line_index + 1} is not a supported "
                    "CERT C rule or recommendation link"
                )
    
            code = match.group("code")
            slug = match.group("slug")
            if code.lower() != slug:
                raise DistributionError(
                    f"Link text and destination disagree at {source}:{line_index + 1}: "
                    f"{code} versus {slug}"
                )
            if code in seen_codes:
                raise DistributionError(
                    f"Duplicate {code} rows at {source}:{seen_codes[code]} and "
                    f"{source}:{line_index + 1}"
                )
    
            seen_codes[code] = line_index + 1
            rows.append(
                SourceRow(
                    code=code,
                    kind=match.group("kind"),
                    category=match.group("category"),
                    slug=slug,
                    cells=cells,
                )
            )
    
        if not rows:
            raise DistributionError(f"The source table in {source} has no data rows")
    
        return rows
    
    
    def unnumbered_name(path: Path) -> str:
        """Remove a leading numeric ordering prefix from a file or directory name."""
    
        return re.sub(r"^\d+\.", "", path.name)
    
    
    def build_guideline_index(standard_root: Path) -> Dict[Tuple[str, str], Path]:
        """Map (rules/recommendations, URL slug) to local Markdown files."""
    
        index: Dict[Tuple[str, str], Path] = {}
        roots = {
            "rules": standard_root / "03.rules",
            "recommendations": standard_root / "08.recommendations",
        }
    
        for kind, root in roots.items():
            if not root.is_dir():
                raise DistributionError(f"Guideline directory does not exist: {root}")
    
            for path in root.rglob("*.md"):
                match = GUIDELINE_FILE_RE.fullmatch(path.name)
                if match is None:
                    continue
    
                key = (kind, match.group("slug"))
                previous = index.get(key)
                if previous is not None:
                    raise DistributionError(
                        f"Multiple files represent {kind}/{key[1]}: {previous} and {path}"
                    )
                index[key] = path
    
        return index
    
    
    def find_section_bounds(lines: Sequence[str], title: str, path: Path) -> Tuple[int, int]:
        matches: List[Tuple[int, int]] = []
    
        for index, line in enumerate(lines):
            match = HEADING_RE.fullmatch(line.rstrip("\r\n"))
            if match is not None and match.group("title").strip() == title:
                matches.append((index, len(match.group("marks"))))
    
        if len(matches) != 1:
            raise DistributionError(
                f"Expected exactly one '{title}' section in {path}, found {len(matches)}"
            )
    
        section_start, heading_level = matches[0]
        section_end = len(lines)
        for index in range(section_start + 1, len(lines)):
            match = HEADING_RE.fullmatch(lines[index].rstrip("\r\n"))
            if match is not None and len(match.group("marks")) <= heading_level:
                section_end = index
                break
    
        return section_start + 1, section_end
    
    
    def format_markdown_row(cells: Sequence[str], newline: str) -> str:
        return "| " + " | ".join(cells) + " |" + newline
    
    
    def newline_for(text: str) -> str:
        if "\r\n" in text:
            return "\r\n"
        return "\n"
    
    
    def plan_destination_update(path: Path, row: SourceRow) -> Optional[PlannedChange]:
        original = read_utf8(path)
        lines = original.splitlines(keepends=True)
        section_start, section_end = find_section_bounds(
            lines, "Automated Detection", path
        )
        tables = [
            table
            for table in find_markdown_tables(lines, section_start, section_end)
            if table.header_cells and table.header_cells[0] == "Tool"
        ]
    
        if len(tables) != 1:
            raise DistributionError(
                f"Expected exactly one Automated Detection table beginning with 'Tool' "
                f"in {path}, found {len(tables)}"
            )
    
        table = tables[0]
        desired_cells = row.destination_cells
        matching_indexes: List[int] = []
    
        for line_index in range(table.first_data_index, table.end_index):
            cells = parse_markdown_row(lines[line_index])
            if cells is not None and cells and cells[0] == MISRA_LINK:
                matching_indexes.append(line_index)
    
        if len(matching_indexes) > 1:
            line_numbers = ", ".join(str(index + 1) for index in matching_indexes)
            raise DistributionError(
                f"Multiple MISRA C:2025 rows in {path} at lines {line_numbers}"
            )
    
        newline = newline_for(original)
        desired_line = format_markdown_row(desired_cells, newline)
    
        if matching_indexes:
            line_index = matching_indexes[0]
            existing_cells = parse_markdown_row(lines[line_index])
            if existing_cells == desired_cells:
                return None
            lines[line_index] = desired_line
            action = "updated"
        else:
            lines.insert(table.end_index, desired_line)
            action = "inserted"
    
        return PlannedChange(
            path=path,
            original=original,
            updated="".join(lines),
            action=action,
        )
    
    
    def plan_changes(
        source: Path, standard_root: Path
    ) -> Tuple[List[SourceRow], List[PlannedChange]]:
        """Validate every row and destination, then return the complete write plan."""
    
        rows = parse_source_rows(source)
        guideline_index = build_guideline_index(standard_root)
        changes: List[PlannedChange] = []
    
        for row in rows:
            key = (row.kind, row.slug)
            destination = guideline_index.get(key)
            if destination is None:
                raise DistributionError(
                    f"No local file found for {row.code} ({row.kind}/{row.slug})"
                )
    
            actual_category = unnumbered_name(destination.parent)
            if actual_category != row.category:
                raise DistributionError(
                    f"Category mismatch for {row.code}: source link uses {row.category}, "
                    f"but {destination} is in {actual_category}"
                )
    
            change = plan_destination_update(destination, row)
            if change is not None:
                changes.append(change)
    
        return rows, changes
    
    
    def write_atomic(change: PlannedChange) -> None:
        """Atomically replace one file while preserving its permission bits."""
    
        mode = change.path.stat().st_mode
        temporary_name: Optional[str] = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="wb", prefix=f".{change.path.name}.", dir=change.path.parent,
                delete=False
            ) as temporary:
                temporary_name = temporary.name
                temporary.write(change.updated.encode("utf-8"))
                temporary.flush()
                os.fsync(temporary.fileno())
    
            os.chmod(temporary_name, mode)
            os.replace(temporary_name, change.path)
            temporary_name = None
        finally:
            if temporary_name is not None:
                try:
                    os.unlink(temporary_name)
                except FileNotFoundError:
                    pass
    
    
    def path_argument(value: str) -> Path:
        return Path(value).expanduser().resolve()
    
    
    def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description=(
                "Copy rows from the MISRA C:2025 related-guidelines table into "
                "the linked guidelines' Automated Detection tables."
            )
        )
        parser.add_argument(
            "--source",
            type=path_argument,
            default=DEFAULT_SOURCE,
            help=f"source Markdown file (default: {DEFAULT_SOURCE})",
        )
        parser.add_argument(
            "--standard-root",
            type=path_argument,
            default=DEFAULT_STANDARD_ROOT,
            help=f"CERT C content root (default: {DEFAULT_STANDARD_ROOT})",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="validate and report changes without writing files",
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="list every file that would be or was changed",
        )
        return parser.parse_args(argv)
    
    
    def main(argv: Optional[Sequence[str]] = None) -> int:
        arguments = parse_arguments(argv)
    
        try:
            rows, changes = plan_changes(arguments.source, arguments.standard_root)
        except (DistributionError, OSError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 1
    
        inserted = sum(change.action == "inserted" for change in changes)
        updated = sum(change.action == "updated" for change in changes)
        unchanged = len(rows) - len(changes)
    
        if arguments.verbose:
            for change in changes:
                try:
                    display_path = change.path.relative_to(REPOSITORY_ROOT)
                except ValueError:
                    display_path = change.path
                print(f"{change.action}: {display_path}")
    
        if arguments.dry_run:
            print(
                f"Dry run: {len(changes)} file(s) would change "
                f"({inserted} inserted, {updated} updated); {unchanged} already current."
            )
            return 0
    
        try:
            for change in changes:
                write_atomic(change)
        except OSError as error:
            print(f"error while writing {change.path}: {error}", file=sys.stderr)
            return 1
    
        print(
            f"Processed {len(rows)} guideline row(s): {inserted} inserted, "
            f"{updated} updated, {unchanged} already current."
        )
        return 0
    
    
    if __name__ == "__main__":
        raise SystemExit(main())

## Activity

    $ chmod 755 scripts/distribute_guideline_table.py
        python3 scripts/distribute_guideline_table.py --dry-run
        python3 -m py_compile scripts/distribute_guideline_table.py
        scripts/distribute_guideline_table.py --help | sed -n '1,160p'
        git diff --check -- scripts/distribute_guideline_table.py
        git diff --stat -- scripts/distribute_guideline_table.py
    Dry run: 121 file(s) would change (121 inserted, 0 updated); 0 already current.
    usage: distribute_guideline_table.py [-h] [--source SOURCE]
                                         [--standard-root STANDARD_ROOT]
                                         [--dry-run] [--verbose]
    
    Copy rows from the MISRA C:2025 related-guidelines table into the linked
    guidelines' Automated Detection tables.
    
    options:
      -h, --help            show this help message and exit
      --source SOURCE       source Markdown file (default: /host/content/4.sei-
                            cert-c-coding-standard/04.back-matter/7.ff-related-
                            guidelines/10.misra-c-2025.md)
      --standard-root STANDARD_ROOT
                            CERT C content root (default: /host/content/4.sei-
                            cert-c-coding-standard)
      --dry-run             validate and report changes without writing files
      --verbose             list every file that would be or was changed
    ✓ • 300ms

## Assistant

The script now preflights all 121 source rows successfully without touching any guideline files. I’m doing a final review of rerun behavior and failure handling, including a sandboxed copy test so the real content remains unchanged.

## Activity

    $ git status --short -- scripts
        find scripts -maxdepth 2 -type f -path '*/__pycache__/*' -print
        nl -ba scripts/distribute_guideline_table.py | sed -n '1,420p'
    ?? scripts/__pycache__/
    ?? scripts/distribute_guideline_table.py
    scripts/__pycache__/distribute_guideline_table.cpython-310.pyc
         1    #!/usr/bin/env python3
         2    """Distribute a related-guidelines table to guideline pages.
         3
         4    For each row in the MISRA C:2025 table, this script finds the linked CERT C
         5    rule or recommendation and adds a row to its Automated Detection table.  The
         6    new row replaces the source row's first cell with ``MISRA_LINK`` and preserves
         7    all remaining source cells.
         8
         9    Run from anywhere in the repository:
        10
        11        python3 scripts/distribute_guideline_table.py --dry-run
        12        python3 scripts/distribute_guideline_table.py
        13
        14    The script preflights every source row and destination before writing any
        15    files.  It is safe to rerun: an existing MISRA C:2025 row is left alone when
        16    it is current and updated in place when its contents differ.
        17    """
        18
        19    from __future__ import annotations
        20
        21    import argparse
        22    import os
        23    import re
        24    import sys
        25    import tempfile
        26    from dataclasses import dataclass
        27    from pathlib import Path
        28    from typing import Dict, List, Optional, Sequence, Tuple
        29
        30
        31    MISRA_LINK = (
        32        "[MISRA C:2025]"
        33        "(/sei-cert-c-coding-standard/back-matter/"
        34        "aa-bibliography#AA.Bibliography-MISRA25)"
        35    )
        36
        37    REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
        38    DEFAULT_SOURCE = REPOSITORY_ROOT / (
        39        "content/4.sei-cert-c-coding-standard/04.back-matter/"
        40        "7.ff-related-guidelines/10.misra-c-2025.md"
        41    )
        42    DEFAULT_STANDARD_ROOT = (
        43        REPOSITORY_ROOT / "content/4.sei-cert-c-coding-standard"
        44    )
        45
        46    GUIDELINE_LINK_RE = re.compile(
        47        r"^\[(?P<code>[A-Z]{3}\d{2}-C)\]"
        48        r"\((?P<url>/sei-cert-c-coding-standard/"
        49        r"(?P<kind>rules|recommendations)/"
        50        r"(?P<category>[a-z0-9-]+)/(?P<slug>[a-z]{3}\d{2}-c))\)$"
        51    )
        52    GUIDELINE_FILE_RE = re.compile(r"^\d+\.(?P<slug>[a-z]{3}\d{2}-c)\.md$")
        53    HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)\s*$")
        54    SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
        55
        56
        57    class DistributionError(Exception):
        58        """Raised when input cannot be distributed without ambiguity."""
        59
        60
        61    @dataclass(frozen=True)
        62    class SourceRow:
        63        code: str
        64        kind: str
        65        category: str
        66        slug: str
        67        cells: Tuple[str, ...]
        68
        69        @property
        70        def destination_cells(self) -> Tuple[str, ...]:
        71            return (MISRA_LINK, *self.cells[1:])
        72
        73
        74    @dataclass(frozen=True)
        75    class MarkdownTable:
        76        header_index: int
        77        separator_index: int
        78        first_data_index: int
        79        end_index: int
        80        header_cells: Tuple[str, ...]
        81
        82
        83    @dataclass(frozen=True)
        84    class PlannedChange:
        85        path: Path
        86        original: str
        87        updated: str
        88        action: str
        89
        90
        91    def parse_markdown_row(line: str) -> Optional[Tuple[str, ...]]:
        92        """Return trimmed cells from a pipe-delimited Markdown row.
        93
        94        Pipes escaped with a backslash remain part of the cell content.
        95        """
        96
        97        stripped = line.rstrip("\r\n").strip()
        98        if not (stripped.startswith("|") and stripped.endswith("|")):
        99            return None
       100
       101        body = stripped[1:-1]
       102        cells: List[str] = []
       103        current: List[str] = []
       104        backslash_run = 0
       105
       106        for character in body:
       107            if character == "|" and backslash_run % 2 == 0:
       108                cells.append("".join(current).strip())
       109                current = []
       110            else:
       111                current.append(character)
       112
       113            if character == "\\":
       114                backslash_run += 1
       115            else:
       116                backslash_run = 0
       117
       118        cells.append("".join(current).strip())
       119        return tuple(cells)
       120
       121
       122    def is_separator_row(cells: Optional[Tuple[str, ...]]) -> bool:
       123        return bool(cells) and all(SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)
       124
       125
       126    def find_markdown_tables(
       127        lines: Sequence[str], start: int = 0, end: Optional[int] = None
       128    ) -> List[MarkdownTable]:
       129        """Find conventional Markdown tables between two line indexes."""
       130
       131        if end is None:
       132            end = len(lines)
       133
       134        tables: List[MarkdownTable] = []
       135        index = start
       136        while index + 1 < end:
       137            header = parse_markdown_row(lines[index])
       138            separator = parse_markdown_row(lines[index + 1])
       139            if header is None or not is_separator_row(separator):
       140                index += 1
       141                continue
       142
       143            if len(header) != len(separator):
       144                index += 1
       145                continue
       146
       147            table_end = index + 2
       148            while table_end < end and parse_markdown_row(lines[table_end]) is not None:
       149                table_end += 1
       150
       151            tables.append(
       152                MarkdownTable(
       153                    header_index=index,
       154                    separator_index=index + 1,
       155                    first_data_index=index + 2,
       156                    end_index=table_end,
       157                    header_cells=header,
       158                )
       159            )
       160            index = table_end
       161
       162        return tables
       163
       164
       165    def read_utf8(path: Path) -> str:
       166        try:
       167            return path.read_bytes().decode("utf-8")
       168        except FileNotFoundError as error:
       169            raise DistributionError(f"File does not exist: {path}") from error
       170        except UnicodeDecodeError as error:
       171            raise DistributionError(f"File is not valid UTF-8: {path}") from error
       172
       173
       174    def parse_source_rows(source: Path) -> List[SourceRow]:
       175        text = read_utf8(source)
       176        lines = text.splitlines(keepends=True)
       177        matching_tables = [
       178            table
       179            for table in find_markdown_tables(lines)
       180            if table.header_cells[:2] == ("CERT Rule", "Related Guidelines")
       181        ]
       182
       183        if len(matching_tables) != 1:
       184            raise DistributionError(
       185                f"Expected exactly one 'CERT Rule | Related Guidelines' table in "
       186                f"{source}, found {len(matching_tables)}"
       187            )
       188
       189        table = matching_tables[0]
       190        rows: List[SourceRow] = []
       191        seen_codes: Dict[str, int] = {}
       192
       193        for line_index in range(table.first_data_index, table.end_index):
       194            cells = parse_markdown_row(lines[line_index])
       195            if cells is None or len(cells) < 2:
       196                raise DistributionError(
       197                    f"Malformed source row at {source}:{line_index + 1}"
       198                )
       199
       200            match = GUIDELINE_LINK_RE.fullmatch(cells[0])
       201            if match is None:
       202                raise DistributionError(
       203                    f"The first cell at {source}:{line_index + 1} is not a supported "
       204                    "CERT C rule or recommendation link"
       205                )
       206
       207            code = match.group("code")
       208            slug = match.group("slug")
       209            if code.lower() != slug:
       210                raise DistributionError(
       211                    f"Link text and destination disagree at {source}:{line_index + 1}: "
       212                    f"{code} versus {slug}"
       213                )
       214            if code in seen_codes:
       215                raise DistributionError(
       216                    f"Duplicate {code} rows at {source}:{seen_codes[code]} and "
       217                    f"{source}:{line_index + 1}"
       218                )
       219
       220            seen_codes[code] = line_index + 1
       221            rows.append(
       222                SourceRow(
       223                    code=code,
       224                    kind=match.group("kind"),
       225                    category=match.group("category"),
       226                    slug=slug,
       227                    cells=cells,
       228                )
       229            )
       230
       231        if not rows:
       232            raise DistributionError(f"The source table in {source} has no data rows")
       233
       234        return rows
       235
       236
       237    def unnumbered_name(path: Path) -> str:
       238        """Remove a leading numeric ordering prefix from a file or directory name."""
       239
       240        return re.sub(r"^\d+\.", "", path.name)
       241
       242
       243    def build_guideline_index(standard_root: Path) -> Dict[Tuple[str, str], Path]:
       244        """Map (rules/recommendations, URL slug) to local Markdown files."""
       245
       246        index: Dict[Tuple[str, str], Path] = {}
       247        roots = {
       248            "rules": standard_root / "03.rules",
       249            "recommendations": standard_root / "08.recommendations",
       250        }
       251
       252        for kind, root in roots.items():
       253            if not root.is_dir():
       254                raise DistributionError(f"Guideline directory does not exist: {root}")
       255
       256            for path in root.rglob("*.md"):
       257                match = GUIDELINE_FILE_RE.fullmatch(path.name)
       258                if match is None:
       259                    continue
       260
       261                key = (kind, match.group("slug"))
       262                previous = index.get(key)
       263                if previous is not None:
       264                    raise DistributionError(
       265                        f"Multiple files represent {kind}/{key[1]}: {previous} and {path}"
       266                    )
       267                index[key] = path
       268
       269        return index
       270
       271
       272    def find_section_bounds(lines: Sequence[str], title: str, path: Path) -> Tuple[int, int]:
       273        matches: List[Tuple[int, int]] = []
       274
       275        for index, line in enumerate(lines):
       276            match = HEADING_RE.fullmatch(line.rstrip("\r\n"))
       277            if match is not None and match.group("title").strip() == title:
       278                matches.append((index, len(match.group("marks"))))
       279
       280        if len(matches) != 1:
       281            raise DistributionError(
       282                f"Expected exactly one '{title}' section in {path}, found {len(matches)}"
       283            )
       284
       285        section_start, heading_level = matches[0]
       286        section_end = len(lines)
       287        for index in range(section_start + 1, len(lines)):
       288            match = HEADING_RE.fullmatch(lines[index].rstrip("\r\n"))
       289            if match is not None and len(match.group("marks")) <= heading_level:
       290                section_end = index
       291                break
       292
       293        return section_start + 1, section_end
       294
       295
       296    def format_markdown_row(cells: Sequence[str], newline: str) -> str:
       297        return "| " + " | ".join(cells) + " |" + newline
       298
       299
       300    def newline_for(text: str) -> str:
       301        if "\r\n" in text:
       302            return "\r\n"
       303        return "\n"
       304
       305
       306    def plan_destination_update(path: Path, row: SourceRow) -> Optional[PlannedChange]:
       307        original = read_utf8(path)
       308        lines = original.splitlines(keepends=True)
       309        section_start, section_end = find_section_bounds(
       310            lines, "Automated Detection", path
       311        )
       312        tables = [
       313            table
       314            for table in find_markdown_tables(lines, section_start, section_end)
       315            if table.header_cells and table.header_cells[0] == "Tool"
       316        ]
       317
       318        if len(tables) != 1:
       319            raise DistributionError(
       320                f"Expected exactly one Automated Detection table beginning with 'Tool' "
       321                f"in {path}, found {len(tables)}"
       322            )
       323
       324        table = tables[0]
       325        desired_cells = row.destination_cells
       326        matching_indexes: List[int] = []
       327
       328        for line_index in range(table.first_data_index, table.end_index):
       329            cells = parse_markdown_row(lines[line_index])
       330            if cells is not None and cells and cells[0] == MISRA_LINK:
       331                matching_indexes.append(line_index)
       332
       333        if len(matching_indexes) > 1:
       334            line_numbers = ", ".join(str(index + 1) for index in matching_indexes)
       335            raise DistributionError(
       336                f"Multiple MISRA C:2025 rows in {path} at lines {line_numbers}"
       337            )
       338
       339        newline = newline_for(original)
       340        desired_line = format_markdown_row(desired_cells, newline)
       341
       342        if matching_indexes:
       343            line_index = matching_indexes[0]
       344            existing_cells = parse_markdown_row(lines[line_index])
       345            if existing_cells == desired_cells:
       346                return None
       347            lines[line_index] = desired_line
       348            action = "updated"
       349        else:
       350            lines.insert(table.end_index, desired_line)
       351            action = "inserted"
       352
       353        return PlannedChange(
       354            path=path,
       355            original=original,
       356            updated="".join(lines),
       357            action=action,
       358        )
       359
       360
       361    def plan_changes(
       362        source: Path, standard_root: Path
       363    ) -> Tuple[List[SourceRow], List[PlannedChange]]:
       364        """Validate every row and destination, then return the complete write plan."""
       365
       366        rows = parse_source_rows(source)
       367        guideline_index = build_guideline_index(standard_root)
       368        changes: List[PlannedChange] = []
       369
       370        for row in rows:
       371            key = (row.kind, row.slug)
       372            destination = guideline_index.get(key)
       373            if destination is None:
       374                raise DistributionError(
       375                    f"No local file found for {row.code} ({row.kind}/{row.slug})"
       376                )
       377
       378            actual_category = unnumbered_name(destination.parent)
       379            if actual_category != row.category:
       380                raise DistributionError(
       381                    f"Category mismatch for {row.code}: source link uses {row.category}, "
       382                    f"but {destination} is in {actual_category}"
       383                )
       384
       385            change = plan_destination_update(destination, row)
       386            if change is not None:
       387                changes.append(change)
       388
       389        return rows, changes
       390
       391
       392    def write_atomic(change: PlannedChange) -> None:
       393        """Atomically replace one file while preserving its permission bits."""
       394
       395        mode = change.path.stat().st_mode
       396        temporary_name: Optional[str] = None
       397        try:
       398            with tempfile.NamedTemporaryFile(
       399                mode="wb", prefix=f".{change.path.name}.", dir=change.path.parent,
       400                delete=False
       401            ) as temporary:
       402                temporary_name = temporary.name
       403                temporary.write(change.updated.encode("utf-8"))
       404                temporary.flush()
       405                os.fsync(temporary.fileno())
       406
       407            os.chmod(temporary_name, mode)
       408            os.replace(temporary_name, change.path)
       409            temporary_name = None
       410        finally:
       411            if temporary_name is not None:
       412                try:
       413                    os.unlink(temporary_name)
       414                except FileNotFoundError:
       415                    pass
       416
       417
       418    def path_argument(value: str) -> Path:
       419        return Path(value).expanduser().resolve()
       420
    ✓ • 0ms

## Activity

    $ test_root=$(mktemp -d /tmp/distribute-guideline-table.XXXXXX)
        cp -a content/4.sei-cert-c-coding-standard "$test_root/standard"
        python3 scripts/distribute_guideline_table.py --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --standard-root "$test_root/standard"
        python3 scripts/distribute_guideline_table.py --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --standard-root "$test_root/standard" --dry-run
        rg -l '^\| \[MISRA C:2025\]\(/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA\.Bibliography-MISRA25\) \|' "$test_root/standard/03.rules" "$test_root/standard/08.recommendations" | wc -l
        rg -n '^\| \[MISRA C:2025\]' "$test_root/standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md"
        rg -n '^\| \[MISRA C:2025\]' "$test_root/standard/03.rules/12.integers-int/3.int31-c.md"
        printenv test_root 2>/dev/null || true
        printf '%s\n' "$test_root"
    Processed 121 guideline row(s): 121 inserted, 0 updated, 0 already current.
    Dry run: 0 file(s) would change (0 inserted, 0 updated); 121 already current.
    121
    101:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Dir 4.11 |
    353:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 10.1, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 21.6, 21.13, 21.18 |
    /tmp/distribute-guideline-table.6wwTLl
    ✓ • 689ms

## Activity

    $ rm -r /tmp/distribute-guideline-table.6wwTLl
        rm scripts/__pycache__/distribute_guideline_table.cpython-310.pyc
        rmdir scripts/__pycache__
        git status --short -- scripts content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations
    ?? scripts/distribute_guideline_table.py
    ✓ • 212ms

## Activity

    $ nl -ba scripts/distribute_guideline_table.py | sed -n '390,560p'
        git diff --no-index -- /dev/null scripts/distribute_guideline_table.py | sed -n '1,620p'
       390
       391
       392    def write_atomic(change: PlannedChange) -> None:
       393        """Atomically replace one file while preserving its permission bits."""
       394
       395        mode = change.path.stat().st_mode
       396        temporary_name: Optional[str] = None
       397        try:
       398            with tempfile.NamedTemporaryFile(
       399                mode="wb", prefix=f".{change.path.name}.", dir=change.path.parent,
       400                delete=False
       401            ) as temporary:
       402                temporary_name = temporary.name
       403                temporary.write(change.updated.encode("utf-8"))
       404                temporary.flush()
       405                os.fsync(temporary.fileno())
       406
       407            os.chmod(temporary_name, mode)
       408            os.replace(temporary_name, change.path)
       409            temporary_name = None
       410        finally:
       411            if temporary_name is not None:
       412                try:
       413                    os.unlink(temporary_name)
       414                except FileNotFoundError:
       415                    pass
       416
       417
       418    def path_argument(value: str) -> Path:
       419        return Path(value).expanduser().resolve()
       420
       421
       422    def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
       423        parser = argparse.ArgumentParser(
       424            description=(
       425                "Copy rows from the MISRA C:2025 related-guidelines table into "
       426                "the linked guidelines' Automated Detection tables."
       427            )
       428        )
       429        parser.add_argument(
       430            "--source",
       431            type=path_argument,
       432            default=DEFAULT_SOURCE,
       433            help=f"source Markdown file (default: {DEFAULT_SOURCE})",
       434        )
       435        parser.add_argument(
       436            "--standard-root",
       437            type=path_argument,
       438            default=DEFAULT_STANDARD_ROOT,
       439            help=f"CERT C content root (default: {DEFAULT_STANDARD_ROOT})",
       440        )
       441        parser.add_argument(
       442            "--dry-run",
       443            action="store_true",
       444            help="validate and report changes without writing files",
       445        )
       446        parser.add_argument(
       447            "--verbose",
       448            action="store_true",
       449            help="list every file that would be or was changed",
       450        )
       451        return parser.parse_args(argv)
       452
       453
       454    def main(argv: Optional[Sequence[str]] = None) -> int:
       455        arguments = parse_arguments(argv)
       456
       457        try:
       458            rows, changes = plan_changes(arguments.source, arguments.standard_root)
       459        except (DistributionError, OSError) as error:
       460            print(f"error: {error}", file=sys.stderr)
       461            return 1
       462
       463        inserted = sum(change.action == "inserted" for change in changes)
       464        updated = sum(change.action == "updated" for change in changes)
       465        unchanged = len(rows) - len(changes)
       466
       467        if arguments.verbose:
       468            for change in changes:
       469                try:
       470                    display_path = change.path.relative_to(REPOSITORY_ROOT)
       471                except ValueError:
       472                    display_path = change.path
       473                print(f"{change.action}: {display_path}")
       474
       475        if arguments.dry_run:
       476            print(
       477                f"Dry run: {len(changes)} file(s) would change "
       478                f"({inserted} inserted, {updated} updated); {unchanged} already current."
       479            )
       480            return 0
       481
       482        try:
       483            for change in changes:
       484                write_atomic(change)
       485        except OSError as error:
       486            print(f"error while writing {change.path}: {error}", file=sys.stderr)
       487            return 1
       488
       489        print(
       490            f"Processed {len(rows)} guideline row(s): {inserted} inserted, "
       491            f"{updated} updated, {unchanged} already current."
       492        )
       493        return 0
       494
       495
       496    if __name__ == "__main__":
       497        raise SystemExit(main())
    diff --git a/scripts/distribute_guideline_table.py b/scripts/distribute_guideline_table.py
    new file mode 100755
    index 00000000..8d8f067f
    --- /dev/null
    +++ b/scripts/distribute_guideline_table.py
    @@ -0,0 +1,497 @@
    +#!/usr/bin/env python3
    +"""Distribute a related-guidelines table to guideline pages.
    +
    +For each row in the MISRA C:2025 table, this script finds the linked CERT C
    +rule or recommendation and adds a row to its Automated Detection table.  The
    +new row replaces the source row's first cell with ``MISRA_LINK`` and preserves
    +all remaining source cells.
    +
    +Run from anywhere in the repository:
    +
    +    python3 scripts/distribute_guideline_table.py --dry-run
    +    python3 scripts/distribute_guideline_table.py
    +
    +The script preflights every source row and destination before writing any
    +files.  It is safe to rerun: an existing MISRA C:2025 row is left alone when
    +it is current and updated in place when its contents differ.
    +"""
    +
    +from __future__ import annotations
    +
    +import argparse
    +import os
    +import re
    +import sys
    +import tempfile
    +from dataclasses import dataclass
    +from pathlib import Path
    +from typing import Dict, List, Optional, Sequence, Tuple
    +
    +
    +MISRA_LINK = (
    +    "[MISRA C:2025]"
    +    "(/sei-cert-c-coding-standard/back-matter/"
    +    "aa-bibliography#AA.Bibliography-MISRA25)"
    +)
    +
    +REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
    +DEFAULT_SOURCE = REPOSITORY_ROOT / (
    +    "content/4.sei-cert-c-coding-standard/04.back-matter/"
    +    "7.ff-related-guidelines/10.misra-c-2025.md"
    +)
    +DEFAULT_STANDARD_ROOT = (
    +    REPOSITORY_ROOT / "content/4.sei-cert-c-coding-standard"
    +)
    +
    +GUIDELINE_LINK_RE = re.compile(
    +    r"^\[(?P<code>[A-Z]{3}\d{2}-C)\]"
    +    r"\((?P<url>/sei-cert-c-coding-standard/"
    +    r"(?P<kind>rules|recommendations)/"
    +    r"(?P<category>[a-z0-9-]+)/(?P<slug>[a-z]{3}\d{2}-c))\)$"
    +)
    +GUIDELINE_FILE_RE = re.compile(r"^\d+\.(?P<slug>[a-z]{3}\d{2}-c)\.md$")
    +HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)\s*$")
    +SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
    +
    +
    +class DistributionError(Exception):
    +    """Raised when input cannot be distributed without ambiguity."""
    +
    +
    +@dataclass(frozen=True)
    +class SourceRow:
    +    code: str
    +    kind: str
    +    category: str
    +    slug: str
    +    cells: Tuple[str, ...]
    +
    +    @property
    +    def destination_cells(self) -> Tuple[str, ...]:
    +        return (MISRA_LINK, *self.cells[1:])
    +
    +
    +@dataclass(frozen=True)
    +class MarkdownTable:
    +    header_index: int
    +    separator_index: int
    +    first_data_index: int
    +    end_index: int
    +    header_cells: Tuple[str, ...]
    +
    +
    +@dataclass(frozen=True)
    +class PlannedChange:
    +    path: Path
    +    original: str
    +    updated: str
    +    action: str
    +
    +
    +def parse_markdown_row(line: str) -> Optional[Tuple[str, ...]]:
    +    """Return trimmed cells from a pipe-delimited Markdown row.
    +
    +    Pipes escaped with a backslash remain part of the cell content.
    +    """
    +
    +    stripped = line.rstrip("\r\n").strip()
    +    if not (stripped.startswith("|") and stripped.endswith("|")):
    +        return None
    +
    +    body = stripped[1:-1]
    +    cells: List[str] = []
    +    current: List[str] = []
    +    backslash_run = 0
    +
    +    for character in body:
    +        if character == "|" and backslash_run % 2 == 0:
    +            cells.append("".join(current).strip())
    +            current = []
    +        else:
    +            current.append(character)
    +
    +        if character == "\\":
    +            backslash_run += 1
    +        else:
    +            backslash_run = 0
    +
    +    cells.append("".join(current).strip())
    +    return tuple(cells)
    +
    +
    +def is_separator_row(cells: Optional[Tuple[str, ...]]) -> bool:
    +    return bool(cells) and all(SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)
    +
    +
    +def find_markdown_tables(
    +    lines: Sequence[str], start: int = 0, end: Optional[int] = None
    +) -> List[MarkdownTable]:
    +    """Find conventional Markdown tables between two line indexes."""
    +
    +    if end is None:
    +        end = len(lines)
    +
    +    tables: List[MarkdownTable] = []
    +    index = start
    +    while index + 1 < end:
    +        header = parse_markdown_row(lines[index])
    +        separator = parse_markdown_row(lines[index + 1])
    +        if header is None or not is_separator_row(separator):
    +            index += 1
    +            continue
    +
    +        if len(header) != len(separator):
    +            index += 1
    +            continue
    +
    +        table_end = index + 2
    +        while table_end < end and parse_markdown_row(lines[table_end]) is not None:
    +            table_end += 1
    +
    +        tables.append(
    +            MarkdownTable(
    +                header_index=index,
    +                separator_index=index + 1,
    +                first_data_index=index + 2,
    +                end_index=table_end,
    +                header_cells=header,
    +            )
    +        )
    +        index = table_end
    +
    +    return tables
    +
    +
    +def read_utf8(path: Path) -> str:
    +    try:
    +        return path.read_bytes().decode("utf-8")
    +    except FileNotFoundError as error:
    +        raise DistributionError(f"File does not exist: {path}") from error
    +    except UnicodeDecodeError as error:
    +        raise DistributionError(f"File is not valid UTF-8: {path}") from error
    +
    +
    +def parse_source_rows(source: Path) -> List[SourceRow]:
    +    text = read_utf8(source)
    +    lines = text.splitlines(keepends=True)
    +    matching_tables = [
    +        table
    +        for table in find_markdown_tables(lines)
    +        if table.header_cells[:2] == ("CERT Rule", "Related Guidelines")
    +    ]
    +
    +    if len(matching_tables) != 1:
    +        raise DistributionError(
    +            f"Expected exactly one 'CERT Rule | Related Guidelines' table in "
    +            f"{source}, found {len(matching_tables)}"
    +        )
    +
    +    table = matching_tables[0]
    +    rows: List[SourceRow] = []
    +    seen_codes: Dict[str, int] = {}
    +
    +    for line_index in range(table.first_data_index, table.end_index):
    +        cells = parse_markdown_row(lines[line_index])
    +        if cells is None or len(cells) < 2:
    +            raise DistributionError(
    +                f"Malformed source row at {source}:{line_index + 1}"
    +            )
    +
    +        match = GUIDELINE_LINK_RE.fullmatch(cells[0])
    +        if match is None:
    +            raise DistributionError(
    +                f"The first cell at {source}:{line_index + 1} is not a supported "
    +                "CERT C rule or recommendation link"
    +            )
    +
    +        code = match.group("code")
    +        slug = match.group("slug")
    +        if code.lower() != slug:
    +            raise DistributionError(
    +                f"Link text and destination disagree at {source}:{line_index + 1}: "
    +                f"{code} versus {slug}"
    +            )
    +        if code in seen_codes:
    +            raise DistributionError(
    +                f"Duplicate {code} rows at {source}:{seen_codes[code]} and "
    +                f"{source}:{line_index + 1}"
    +            )
    +
    +        seen_codes[code] = line_index + 1
    +        rows.append(
    +            SourceRow(
    +                code=code,
    +                kind=match.group("kind"),
    +                category=match.group("category"),
    +                slug=slug,
    +                cells=cells,
    +            )
    +        )
    +
    +    if not rows:
    +        raise DistributionError(f"The source table in {source} has no data rows")
    +
    +    return rows
    +
    +
    +def unnumbered_name(path: Path) -> str:
    +    """Remove a leading numeric ordering prefix from a file or directory name."""
    +
    +    return re.sub(r"^\d+\.", "", path.name)
    +
    +
    +def build_guideline_index(standard_root: Path) -> Dict[Tuple[str, str], Path]:
    +    """Map (rules/recommendations, URL slug) to local Markdown files."""
    +
    +    index: Dict[Tuple[str, str], Path] = {}
    +    roots = {
    +        "rules": standard_root / "03.rules",
    +        "recommendations": standard_root / "08.recommendations",
    +    }
    +
    +    for kind, root in roots.items():
    +        if not root.is_dir():
    +            raise DistributionError(f"Guideline directory does not exist: {root}")
    +
    +        for path in root.rglob("*.md"):
    +            match = GUIDELINE_FILE_RE.fullmatch(path.name)
    +            if match is None:
    +                continue
    +
    +            key = (kind, match.group("slug"))
    +            previous = index.get(key)
    +            if previous is not None:
    +                raise DistributionError(
    +                    f"Multiple files represent {kind}/{key[1]}: {previous} and {path}"
    +                )
    +            index[key] = path
    +
    +    return index
    +
    +
    +def find_section_bounds(lines: Sequence[str], title: str, path: Path) -> Tuple[int, int]:
    +    matches: List[Tuple[int, int]] = []
    +
    +    for index, line in enumerate(lines):
    +        match = HEADING_RE.fullmatch(line.rstrip("\r\n"))
    +        if match is not None and match.group("title").strip() == title:
    +            matches.append((index, len(match.group("marks"))))
    +
    +    if len(matches) != 1:
    +        raise DistributionError(
    +            f"Expected exactly one '{title}' section in {path}, found {len(matches)}"
    +        )
    +
    +    section_start, heading_level = matches[0]
    +    section_end = len(lines)
    +    for index in range(section_start + 1, len(lines)):
    +        match = HEADING_RE.fullmatch(lines[index].rstrip("\r\n"))
    +        if match is not None and len(match.group("marks")) <= heading_level:
    +            section_end = index
    +            break
    +
    +    return section_start + 1, section_end
    +
    +
    +def format_markdown_row(cells: Sequence[str], newline: str) -> str:
    +    return "| " + " | ".join(cells) + " |" + newline
    +
    +
    +def newline_for(text: str) -> str:
    +    if "\r\n" in text:
    +        return "\r\n"
    +    return "\n"
    +
    +
    +def plan_destination_update(path: Path, row: SourceRow) -> Optional[PlannedChange]:
    +    original = read_utf8(path)
    +    lines = original.splitlines(keepends=True)
    +    section_start, section_end = find_section_bounds(
    +        lines, "Automated Detection", path
    +    )
    +    tables = [
    +        table
    +        for table in find_markdown_tables(lines, section_start, section_end)
    +        if table.header_cells and table.header_cells[0] == "Tool"
    +    ]
    +
    +    if len(tables) != 1:
    +        raise DistributionError(
    +            f"Expected exactly one Automated Detection table beginning with 'Tool' "
    +            f"in {path}, found {len(tables)}"
    +        )
    +
    +    table = tables[0]
    +    desired_cells = row.destination_cells
    +    matching_indexes: List[int] = []
    +
    +    for line_index in range(table.first_data_index, table.end_index):
    +        cells = parse_markdown_row(lines[line_index])
    +        if cells is not None and cells and cells[0] == MISRA_LINK:
    +            matching_indexes.append(line_index)
    +
    +    if len(matching_indexes) > 1:
    +        line_numbers = ", ".join(str(index + 1) for index in matching_indexes)
    +        raise DistributionError(
    +            f"Multiple MISRA C:2025 rows in {path} at lines {line_numbers}"
    +        )
    +
    +    newline = newline_for(original)
    +    desired_line = format_markdown_row(desired_cells, newline)
    +
    +    if matching_indexes:
    +        line_index = matching_indexes[0]
    +        existing_cells = parse_markdown_row(lines[line_index])
    +        if existing_cells == desired_cells:
    +            return None
    +        lines[line_index] = desired_line
    +        action = "updated"
    +    else:
    +        lines.insert(table.end_index, desired_line)
    +        action = "inserted"
    +
    +    return PlannedChange(
    +        path=path,
    +        original=original,
    +        updated="".join(lines),
    +        action=action,
    +    )
    +
    +
    +def plan_changes(
    +    source: Path, standard_root: Path
    +) -> Tuple[List[SourceRow], List[PlannedChange]]:
    +    """Validate every row and destination, then return the complete write plan."""
    +
    +    rows = parse_source_rows(source)
    +    guideline_index = build_guideline_index(standard_root)
    +    changes: List[PlannedChange] = []
    +
    +    for row in rows:
    +        key = (row.kind, row.slug)
    +        destination = guideline_index.get(key)
    +        if destination is None:
    +            raise DistributionError(
    +                f"No local file found for {row.code} ({row.kind}/{row.slug})"
    +            )
    +
    +        actual_category = unnumbered_name(destination.parent)
    +        if actual_category != row.category:
    +            raise DistributionError(
    +                f"Category mismatch for {row.code}: source link uses {row.category}, "
    +                f"but {destination} is in {actual_category}"
    +            )
    +
    +        change = plan_destination_update(destination, row)
    +        if change is not None:
    +            changes.append(change)
    +
    +    return rows, changes
    +
    +
    +def write_atomic(change: PlannedChange) -> None:
    +    """Atomically replace one file while preserving its permission bits."""
    +
    +    mode = change.path.stat().st_mode
    +    temporary_name: Optional[str] = None
    +    try:
    +        with tempfile.NamedTemporaryFile(
    +            mode="wb", prefix=f".{change.path.name}.", dir=change.path.parent,
    +            delete=False
    +        ) as temporary:
    +            temporary_name = temporary.name
    +            temporary.write(change.updated.encode("utf-8"))
    +            temporary.flush()
    +            os.fsync(temporary.fileno())
    +
    +        os.chmod(temporary_name, mode)
    +        os.replace(temporary_name, change.path)
    +        temporary_name = None
    +    finally:
    +        if temporary_name is not None:
    +            try:
    +                os.unlink(temporary_name)
    +            except FileNotFoundError:
    +                pass
    +
    +
    +def path_argument(value: str) -> Path:
    +    return Path(value).expanduser().resolve()
    +
    +
    +def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    +    parser = argparse.ArgumentParser(
    +        description=(
    +            "Copy rows from the MISRA C:2025 related-guidelines table into "
    +            "the linked guidelines' Automated Detection tables."
    +        )
    +    )
    +    parser.add_argument(
    +        "--source",
    +        type=path_argument,
    +        default=DEFAULT_SOURCE,
    +        help=f"source Markdown file (default: {DEFAULT_SOURCE})",
    +    )
    +    parser.add_argument(
    +        "--standard-root",
    +        type=path_argument,
    +        default=DEFAULT_STANDARD_ROOT,
    +        help=f"CERT C content root (default: {DEFAULT_STANDARD_ROOT})",
    +    )
    +    parser.add_argument(
    +        "--dry-run",
    +        action="store_true",
    +        help="validate and report changes without writing files",
    +    )
    +    parser.add_argument(
    +        "--verbose",
    +        action="store_true",
    +        help="list every file that would be or was changed",
    +    )
    +    return parser.parse_args(argv)
    +
    +
    +def main(argv: Optional[Sequence[str]] = None) -> int:
    +    arguments = parse_arguments(argv)
    +
    +    try:
    +        rows, changes = plan_changes(arguments.source, arguments.standard_root)
    +    except (DistributionError, OSError) as error:
    +        print(f"error: {error}", file=sys.stderr)
    +        return 1
    +
    +    inserted = sum(change.action == "inserted" for change in changes)
    +    updated = sum(change.action == "updated" for change in changes)
    +    unchanged = len(rows) - len(changes)
    +
    +    if arguments.verbose:
    +        for change in changes:
    +            try:
    +                display_path = change.path.relative_to(REPOSITORY_ROOT)
    +            except ValueError:
    +                display_path = change.path
    +            print(f"{change.action}: {display_path}")
    +
    +    if arguments.dry_run:
    +        print(
    +            f"Dry run: {len(changes)} file(s) would change "
    +            f"({inserted} inserted, {updated} updated); {unchanged} already current."
    +        )
    +        return 0
    +
    +    try:
    +        for change in changes:
    +            write_atomic(change)
    +    except OSError as error:
    +        print(f"error while writing {change.path}: {error}", file=sys.stderr)
    +        return 1
    +
    +    print(
    +        f"Processed {len(rows)} guideline row(s): {inserted} inserted, "
    +        f"{updated} updated, {unchanged} already current."
    +    )
    +    return 0
    +
    +
    +if __name__ == "__main__":
    +    raise SystemExit(main())
    ✓ • 0ms

## Activity

    $ python3 -B scripts/distribute_guideline_table.py --dry-run
        rg -n '[[:blank:]]+$' scripts/distribute_guideline_table.py || true
        git status --short -- scripts/distribute_guideline_table.py content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations
    Dry run: 121 file(s) would change (121 inserted, 0 updated); 0 already current.
    ?? scripts/distribute_guideline_table.py
    ✓ • 329ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /host/scripts/distribute_guideline_table.py
    @@ -23,2 +23,3 @@
     import re
    +import stat
     import sys
    @@ -394,3 +395,3 @@
     
    -    mode = change.path.stat().st_mode
    +    mode = stat.S_IMODE(change.path.stat().st_mode)
         temporary_name: Optional[str] = None

## Activity

    $ python3 -B scripts/distribute_guideline_table.py --dry-run
        git status --short -- scripts/distribute_guideline_table.py content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations
        stat -c '%a %n' scripts/distribute_guideline_table.py
    Dry run: 121 file(s) would change (121 inserted, 0 updated); 0 already current.
    ?? scripts/distribute_guideline_table.py
    755 scripts/distribute_guideline_table.py
    ✓ • 219ms

## Assistant

Created [distribute_guideline_table.py](/host/scripts/distribute_guideline_table.py).

It:

- Preflights all destinations before writing.
- Preserves every source cell except the replaced first cell.
- Is idempotent on repeated runs.
- Supports `--dry-run` and `--verbose`.
- Makes atomic file updates.

Validation found all 121 target guidelines:

```bash
python3 scripts/distribute_guideline_table.py --dry-run
```

No guideline files were modified during testing. Run without `--dry-run` to apply the changes.

## User

OK. I do need the following to be arguments to the program:
 * The MISRA_LINK (cell that goes in distributed tables)
 * The original MISRA table (which is now DEFAULT_SOURCE)

Also, if in any guideline, row with the MISRA_LINK already exists, then remove it before adding the new row.

## Assistant

I’ll make both values required command-line options, thread the supplied link through the distribution logic, and change replacement behavior to remove every existing row whose first cell matches that link before appending one fresh row at the end of the table.

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /host/scripts/distribute_guideline_table.py
    @@ -3,6 +3,6 @@
     
    -For each row in the MISRA C:2025 table, this script finds the linked CERT C
    +For each row in a related-guidelines table, this script finds the linked CERT C
     rule or recommendation and adds a row to its Automated Detection table.  The
    -new row replaces the source row's first cell with ``MISRA_LINK`` and preserves
    -all remaining source cells.
    +new row replaces the source row's first cell with a caller-supplied link and
    +preserves all remaining source cells.
     
    @@ -10,8 +10,10 @@
     
    -    python3 scripts/distribute_guideline_table.py --dry-run
    -    python3 scripts/distribute_guideline_table.py
    +    python3 scripts/distribute_guideline_table.py \
    +        --misra-link '[MISRA C:2025](...)' \
    +        --source path/to/table.md \
    +        --dry-run
     
     The script preflights every source row and destination before writing any
    -files.  It is safe to rerun: an existing MISRA C:2025 row is left alone when
    -it is current and updated in place when its contents differ.
    +files.  It is safe to rerun: existing rows beginning with the supplied link
    +are removed before one fresh row is appended.
     """
    @@ -31,13 +33,3 @@
     
    -MISRA_LINK = (
    -    "[MISRA C:2025]"
    -    "(/sei-cert-c-coding-standard/back-matter/"
    -    "aa-bibliography#AA.Bibliography-MISRA25)"
    -)
    -
     REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
    -DEFAULT_SOURCE = REPOSITORY_ROOT / (
    -    "content/4.sei-cert-c-coding-standard/04.back-matter/"
    -    "7.ff-related-guidelines/10.misra-c-2025.md"
    -)
     DEFAULT_STANDARD_ROOT = (
    @@ -69,5 +61,4 @@
     
    -    @property
    -    def destination_cells(self) -> Tuple[str, ...]:
    -        return (MISRA_LINK, *self.cells[1:])
    +    def destination_cells(self, distributed_link: str) -> Tuple[str, ...]:
    +        return (distributed_link, *self.cells[1:])
     

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /host/scripts/distribute_guideline_table.py
    @@ -297,3 +297,5 @@
     
    -def plan_destination_update(path: Path, row: SourceRow) -> Optional[PlannedChange]:
    +def plan_destination_update(
    +    path: Path, row: SourceRow, distributed_link: str
    +) -> Optional[PlannedChange]:
         original = read_utf8(path)
    @@ -316,3 +318,3 @@
         table = tables[0]
    -    desired_cells = row.destination_cells
    +    desired_cells = row.destination_cells(distributed_link)
         matching_indexes: List[int] = []
    @@ -321,24 +323,20 @@
             cells = parse_markdown_row(lines[line_index])
    -        if cells is not None and cells and cells[0] == MISRA_LINK:
    +        if cells is not None and cells and cells[0] == distributed_link:
                 matching_indexes.append(line_index)
     
    -    if len(matching_indexes) > 1:
    -        line_numbers = ", ".join(str(index + 1) for index in matching_indexes)
    -        raise DistributionError(
    -            f"Multiple MISRA C:2025 rows in {path} at lines {line_numbers}"
    -        )
    -
         newline = newline_for(original)
         desired_line = format_markdown_row(desired_cells, newline)
    +    matching_index_set = set(matching_indexes)
     
         if matching_indexes:
    -        line_index = matching_indexes[0]
    -        existing_cells = parse_markdown_row(lines[line_index])
    -        if existing_cells == desired_cells:
    -            return None
    -        lines[line_index] = desired_line
    -        action = "updated"
    -    else:
    -        lines.insert(table.end_index, desired_line)
    -        action = "inserted"
    +        lines = [
    +            line for line_index, line in enumerate(lines)
    +            if line_index not in matching_index_set
    +        ]
    +
    +    insertion_index = table.end_index - len(matching_indexes)
    +    lines.insert(insertion_index, desired_line)
    +    updated = "".join(lines)
    +    if updated == original:
    +        return None
     
    @@ -347,4 +345,4 @@
             original=original,
    -        updated="".join(lines),
    -        action=action,
    +        updated=updated,
    +        action="updated" if matching_indexes else "inserted",
         )
    @@ -353,3 +351,3 @@
     def plan_changes(
    -    source: Path, standard_root: Path
    +    source: Path, standard_root: Path, distributed_link: str
     ) -> Tuple[List[SourceRow], List[PlannedChange]]:
    @@ -376,3 +374,3 @@
     
    -        change = plan_destination_update(destination, row)
    +        change = plan_destination_update(destination, row, distributed_link)
             if change is not None:

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /host/scripts/distribute_guideline_table.py
    @@ -411,2 +411,17 @@
     
    +def cell_argument(value: str) -> str:
    +    """Validate a command-line value that will become one Markdown cell."""
    +
    +    cell = value.strip()
    +    if not cell:
    +        raise argparse.ArgumentTypeError("must not be empty")
    +    if "\n" in cell or "\r" in cell:
    +        raise argparse.ArgumentTypeError("must not contain a newline")
    +    if len(parse_markdown_row(f"| {cell} |") or ()) != 1:
    +        raise argparse.ArgumentTypeError(
    +            "must not contain an unescaped pipe character"
    +        )
    +    return cell
    +
    +
     def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    @@ -414,3 +429,3 @@
             description=(
    -            "Copy rows from the MISRA C:2025 related-guidelines table into "
    +            "Copy rows from a related-guidelines table into "
                 "the linked guidelines' Automated Detection tables."
    @@ -419,6 +434,12 @@
         parser.add_argument(
    +        "--misra-link",
    +        required=True,
    +        type=cell_argument,
    +        help="Markdown cell to place first in every distributed row",
    +    )
    +    parser.add_argument(
             "--source",
    +        required=True,
             type=path_argument,
    -        default=DEFAULT_SOURCE,
    -        help=f"source Markdown file (default: {DEFAULT_SOURCE})",
    +        help="Markdown file containing the source related-guidelines table",
         )
    @@ -447,3 +468,5 @@
         try:
    -        rows, changes = plan_changes(arguments.source, arguments.standard_root)
    +        rows, changes = plan_changes(
    +            arguments.source, arguments.standard_root, arguments.misra_link
    +        )
         except (DistributionError, OSError) as error:

## Activity

    $ python3 -B scripts/distribute_guideline_table.py --help
        python3 -B scripts/distribute_guideline_table.py --misra-link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --dry-run
    Dry run: 121 file(s) would change (121 inserted, 0 updated); 0 already current.
    ✓ • 508ms

## Assistant

The CLI now requires `--misra-link` and `--source`. The replacement logic removes all matching rows and then appends one canonical row, while still producing no file change when a rerun would result in identical content. I’m testing both normal reruns and duplicate-row cleanup in a temporary copy.

## Activity

    $ test_root=$(mktemp -d /tmp/distribute-guideline-table.XXXXXX)
        cp -a content/4.sei-cert-c-coding-standard "$test_root/standard"
        python3 -B scripts/distribute_guideline_table.py --misra-link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --standard-root "$test_root/standard"
        python3 -B scripts/distribute_guideline_table.py --misra-link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --standard-root "$test_root/standard" --dry-run
        rg -l '^\| \[MISRA C:2025\]\(/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA\.Bibliography-MISRA25\) \|' "$test_root/standard/03.rules" "$test_root/standard/08.recommendations" | wc -l
        printf '%s\n' "$test_root"
    Processed 121 guideline row(s): 121 inserted, 0 updated, 0 already current.
    Dry run: 0 file(s) would change (0 inserted, 0 updated); 121 already current.
    121
    /tmp/distribute-guideline-table.OEYmNd
    ✓ • 2.08s

## Activity

    $ target=/tmp/distribute-guideline-table.OEYmNd/standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md
        perl -i -pe 'if (!$duplicated && /^\| \[MISRA C:2025\]/) { print $_; $duplicated = 1; }' "$target"
        rg -c '^\| \[MISRA C:2025\]' "$target"
        python3 -B scripts/distribute_guideline_table.py --misra-link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --standard-root /tmp/distribute-guideline-table.OEYmNd/standard --dry-run
        python3 -B scripts/distribute_guideline_table.py --misra-link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --standard-root /tmp/distribute-guideline-table.OEYmNd/standard
        rg -c '^\| \[MISRA C:2025\]' "$target"
    Dry run: 1 file(s) would change (0 inserted, 1 updated); 120 already current.
    Processed 121 guideline row(s): 0 inserted, 1 updated, 120 already current.
    1
    ✓ • 445ms

## Activity

    $ rm -r /tmp/distribute-guideline-table.OEYmNd
        python3 -B scripts/distribute_guideline_table.py --misra-link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --dry-run
        rg -n 'MISRA_LINK|DEFAULT_SOURCE|MISRA C:2025 row|MISRA C:2025 table' scripts/distribute_guideline_table.py || true
        rg -n '[[:blank:]]+$' scripts/distribute_guideline_table.py || true
        git status --short -- scripts/distribute_guideline_table.py content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations
    Dry run: 121 file(s) would change (121 inserted, 0 updated); 0 already current.
    AM scripts/distribute_guideline_table.py
    ✓ • 621ms

## Activity

    $ git diff --check -- scripts/distribute_guideline_table.py
        git diff --cached --check -- scripts/distribute_guideline_table.py
        git diff --stat -- scripts/distribute_guideline_table.py
        git diff --cached --stat -- scripts/distribute_guideline_table.py
        git diff -- scripts/distribute_guideline_table.py | sed -n '1,280p'
     scripts/distribute_guideline_table.py | 104 +++++++++++++++++++---------------
     1 file changed, 58 insertions(+), 46 deletions(-)
     scripts/distribute_guideline_table.py | 498 ++++++++++++++++++++++++++++++++++
     1 file changed, 498 insertions(+)
    diff --git a/scripts/distribute_guideline_table.py b/scripts/distribute_guideline_table.py
    index cc73d7d4..d05474a2 100755
    --- a/scripts/distribute_guideline_table.py
    +++ b/scripts/distribute_guideline_table.py
    @@ -1,19 +1,21 @@
     #!/usr/bin/env python3
     """Distribute a related-guidelines table to guideline pages.
    
    -For each row in the MISRA C:2025 table, this script finds the linked CERT C
    +For each row in a related-guidelines table, this script finds the linked CERT C
     rule or recommendation and adds a row to its Automated Detection table.  The
    -new row replaces the source row's first cell with ``MISRA_LINK`` and preserves
    -all remaining source cells.
    +new row replaces the source row's first cell with a caller-supplied link and
    +preserves all remaining source cells.
    
     Run from anywhere in the repository:
    
    -    python3 scripts/distribute_guideline_table.py --dry-run
    -    python3 scripts/distribute_guideline_table.py
    +    python3 scripts/distribute_guideline_table.py \
    +        --misra-link '[MISRA C:2025](...)' \
    +        --source path/to/table.md \
    +        --dry-run
    
     The script preflights every source row and destination before writing any
    -files.  It is safe to rerun: an existing MISRA C:2025 row is left alone when
    -it is current and updated in place when its contents differ.
    +files.  It is safe to rerun: existing rows beginning with the supplied link
    +are removed before one fresh row is appended.
     """
    
     from __future__ import annotations
    @@ -29,17 +31,7 @@ from pathlib import Path
     from typing import Dict, List, Optional, Sequence, Tuple
    
    
    -MISRA_LINK = (
    -    "[MISRA C:2025]"
    -    "(/sei-cert-c-coding-standard/back-matter/"
    -    "aa-bibliography#AA.Bibliography-MISRA25)"
    -)
    -
     REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
    -DEFAULT_SOURCE = REPOSITORY_ROOT / (
    -    "content/4.sei-cert-c-coding-standard/04.back-matter/"
    -    "7.ff-related-guidelines/10.misra-c-2025.md"
    -)
     DEFAULT_STANDARD_ROOT = (
         REPOSITORY_ROOT / "content/4.sei-cert-c-coding-standard"
     )
    @@ -67,9 +59,8 @@ class SourceRow:
         slug: str
         cells: Tuple[str, ...]
    
    -    @property
    -    def destination_cells(self) -> Tuple[str, ...]:
    -        return (MISRA_LINK, *self.cells[1:])
    +    def destination_cells(self, distributed_link: str) -> Tuple[str, ...]:
    +        return (distributed_link, *self.cells[1:])
    
    
     @dataclass(frozen=True)
    @@ -304,7 +295,9 @@ def newline_for(text: str) -> str:
         return "\n"
    
    
    -def plan_destination_update(path: Path, row: SourceRow) -> Optional[PlannedChange]:
    +def plan_destination_update(
    +    path: Path, row: SourceRow, distributed_link: str
    +) -> Optional[PlannedChange]:
         original = read_utf8(path)
         lines = original.splitlines(keepends=True)
         section_start, section_end = find_section_bounds(
    @@ -323,44 +316,40 @@ def plan_destination_update(path: Path, row: SourceRow) -> Optional[PlannedChang
             )
    
         table = tables[0]
    -    desired_cells = row.destination_cells
    +    desired_cells = row.destination_cells(distributed_link)
         matching_indexes: List[int] = []
    
         for line_index in range(table.first_data_index, table.end_index):
             cells = parse_markdown_row(lines[line_index])
    -        if cells is not None and cells and cells[0] == MISRA_LINK:
    +        if cells is not None and cells and cells[0] == distributed_link:
                 matching_indexes.append(line_index)
    
    -    if len(matching_indexes) > 1:
    -        line_numbers = ", ".join(str(index + 1) for index in matching_indexes)
    -        raise DistributionError(
    -            f"Multiple MISRA C:2025 rows in {path} at lines {line_numbers}"
    -        )
    -
         newline = newline_for(original)
         desired_line = format_markdown_row(desired_cells, newline)
    +    matching_index_set = set(matching_indexes)
    
         if matching_indexes:
    -        line_index = matching_indexes[0]
    -        existing_cells = parse_markdown_row(lines[line_index])
    -        if existing_cells == desired_cells:
    -            return None
    -        lines[line_index] = desired_line
    -        action = "updated"
    -    else:
    -        lines.insert(table.end_index, desired_line)
    -        action = "inserted"
    +        lines = [
    +            line for line_index, line in enumerate(lines)
    +            if line_index not in matching_index_set
    +        ]
    +
    +    insertion_index = table.end_index - len(matching_indexes)
    +    lines.insert(insertion_index, desired_line)
    +    updated = "".join(lines)
    +    if updated == original:
    +        return None
    
         return PlannedChange(
             path=path,
             original=original,
    -        updated="".join(lines),
    -        action=action,
    +        updated=updated,
    +        action="updated" if matching_indexes else "inserted",
         )
    
    
     def plan_changes(
    -    source: Path, standard_root: Path
    +    source: Path, standard_root: Path, distributed_link: str
     ) -> Tuple[List[SourceRow], List[PlannedChange]]:
         """Validate every row and destination, then return the complete write plan."""
    
    @@ -383,7 +372,7 @@ def plan_changes(
                     f"but {destination} is in {actual_category}"
                 )
    
    -        change = plan_destination_update(destination, row)
    +        change = plan_destination_update(destination, row, distributed_link)
             if change is not None:
                 changes.append(change)
    
    @@ -420,18 +409,39 @@ def path_argument(value: str) -> Path:
         return Path(value).expanduser().resolve()
    
    
    +def cell_argument(value: str) -> str:
    +    """Validate a command-line value that will become one Markdown cell."""
    +
    +    cell = value.strip()
    +    if not cell:
    +        raise argparse.ArgumentTypeError("must not be empty")
    +    if "\n" in cell or "\r" in cell:
    +        raise argparse.ArgumentTypeError("must not contain a newline")
    +    if len(parse_markdown_row(f"| {cell} |") or ()) != 1:
    +        raise argparse.ArgumentTypeError(
    +            "must not contain an unescaped pipe character"
    +        )
    +    return cell
    +
    +
     def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
         parser = argparse.ArgumentParser(
             description=(
    -            "Copy rows from the MISRA C:2025 related-guidelines table into "
    +            "Copy rows from a related-guidelines table into "
                 "the linked guidelines' Automated Detection tables."
             )
         )
    +    parser.add_argument(
    +        "--misra-link",
    +        required=True,
    +        type=cell_argument,
    +        help="Markdown cell to place first in every distributed row",
    +    )
         parser.add_argument(
             "--source",
    +        required=True,
             type=path_argument,
    -        default=DEFAULT_SOURCE,
    -        help=f"source Markdown file (default: {DEFAULT_SOURCE})",
    +        help="Markdown file containing the source related-guidelines table",
         )
         parser.add_argument(
             "--standard-root",
    @@ -456,7 +466,9 @@ def main(argv: Optional[Sequence[str]] = None) -> int:
         arguments = parse_arguments(argv)
    
         try:
    -        rows, changes = plan_changes(arguments.source, arguments.standard_root)
    +        rows, changes = plan_changes(
    +            arguments.source, arguments.standard_root, arguments.misra_link
    +        )
         except (DistributionError, OSError) as error:
             print(f"error: {error}", file=sys.stderr)
             return 1
    ✓ • 0ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /host/scripts/distribute_guideline_table.py
    @@ -321,4 +321,4 @@
     
    -    for line_index in range(table.first_data_index, table.end_index):
    -        cells = parse_markdown_row(lines[line_index])
    +    for line_index, line in enumerate(lines):
    +        cells = parse_markdown_row(line)
             if cells is not None and cells and cells[0] == distributed_link:
    @@ -336,3 +336,6 @@
     
    -    insertion_index = table.end_index - len(matching_indexes)
    +    removed_before_insertion = sum(
    +        line_index < table.end_index for line_index in matching_indexes
    +    )
    +    insertion_index = table.end_index - removed_before_insertion
         lines.insert(insertion_index, desired_line)

## Activity

    $ test_root=$(mktemp -d /tmp/distribute-guideline-table.XXXXXX)
        cp -a content/4.sei-cert-c-coding-standard "$test_root/standard"
        link='[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)'
        source_file=content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
        python3 -B scripts/distribute_guideline_table.py --misra-link "$link" --source "$source_file" --standard-root "$test_root/standard"
        target="$test_root/standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md"
        perl -i -pe 'if (!$added && /^\| \[MISRA C:2012\]/) { print "| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | stale |\n"; $added = 1; }' "$target"
        rg -c '^\| \[MISRA C:2025\]' "$target"
        python3 -B scripts/distribute_guideline_table.py --misra-link "$link" --source "$source_file" --standard-root "$test_root/standard" --dry-run
        python3 -B scripts/distribute_guideline_table.py --misra-link "$link" --source "$source_file" --standard-root "$test_root/standard"
        rg -n '^\| \[MISRA C:2025\]' "$target"
        printf '%s\n' "$test_root"
    Processed 121 guideline row(s): 121 inserted, 0 updated, 0 already current.
    1
    Dry run: 0 file(s) would change (0 inserted, 0 updated); 121 already current.
    Processed 121 guideline row(s): 0 inserted, 0 updated, 121 already current.
    101:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Dir 4.11 |
    /tmp/distribute-guideline-table.XBK1FW
    ✓ • 1.03s

## Activity

    $ link='[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)'
        source_file=content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md
        target=/tmp/distribute-guideline-table.XBK1FW/standard/08.recommendations/06.declarations-and-initialization-dcl/03.dcl01-c.md
        perl -i -pe 'if (!$added && /^\| \[MISRA C:2012\]/) { print "| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | stale |\n"; $added = 1; }' "$target"
        rg -c '^\| \[MISRA C:2025\]' "$target"
        python3 -B scripts/distribute_guideline_table.py --misra-link "$link" --source "$source_file" --standard-root /tmp/distribute-guideline-table.XBK1FW/standard --dry-run
        python3 -B scripts/distribute_guideline_table.py --misra-link "$link" --source "$source_file" --standard-root /tmp/distribute-guideline-table.XBK1FW/standard
        rg -n '^\| \[MISRA C:2025\]' "$target"
    Dry run: 1 file(s) would change (0 inserted, 1 updated); 120 already current.
    Processed 121 guideline row(s): 0 inserted, 1 updated, 120 already current.
    165:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9 |
    ✓ • 352ms

## Activity

    $ rm -r /tmp/distribute-guideline-table.XBK1FW
        python3 -B scripts/distribute_guideline_table.py --misra-link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --dry-run
        rg -n '[[:blank:]]+$' scripts/distribute_guideline_table.py || true
        git diff --check -- scripts/distribute_guideline_table.py
        git status --short -- scripts/distribute_guideline_table.py content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations
    Dry run: 121 file(s) would change (121 inserted, 0 updated); 0 already current.
    AM scripts/distribute_guideline_table.py
    ✓ • 422ms

## Assistant

Updated [distribute_guideline_table.py](/host/scripts/distribute_guideline_table.py).

Both values are now required arguments:

```bash
python3 scripts/distribute_guideline_table.py \
  --misra-link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' \
  --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md \
  --dry-run
```

Before adding a row, the script now removes every existing row in that guideline whose first cell exactly matches `--misra-link`. Duplicate and rerun behavior was tested in a temporary copy; no guideline files were changed.

## User

Please make a few more changes: In particular, the Python script should not mention MISRA...unless it wants to provide a sample argument.  Likewise, it should not mention CERT C. If you need that, it can also become a required argument.  I do want to run this on other tables eventually.

## Assistant

I’ll generalize the script’s names, help text, parsing, and destination lookup so it no longer embeds MISRA or CERT C assumptions. I’ll retain those only in the usage example, as requested.

## Activity

    $ rg -n -i 'misra|cert|guideline|rules|recommendations|standard' scripts/distribute_guideline_table.py
        sed -n '1,540p' scripts/distribute_guideline_table.py
    2:"""Distribute a related-guidelines table to guideline pages.
    4:For each row in a related-guidelines table, this script finds the linked CERT C
    11:    python3 scripts/distribute_guideline_table.py \
    12:        --misra-link '[MISRA C:2025](...)' \
    35:DEFAULT_STANDARD_ROOT = (
    36:    REPOSITORY_ROOT / "content/4.sei-cert-c-coding-standard"
    39:GUIDELINE_LINK_RE = re.compile(
    41:    r"\((?P<url>/sei-cert-c-coding-standard/"
    42:    r"(?P<kind>rules|recommendations)/"
    45:GUIDELINE_FILE_RE = re.compile(r"^\d+\.(?P<slug>[a-z]{3}\d{2}-c)\.md$")
    172:        if table.header_cells[:2] == ("CERT Rule", "Related Guidelines")
    177:            f"Expected exactly one 'CERT Rule | Related Guidelines' table in "
    192:        match = GUIDELINE_LINK_RE.fullmatch(cells[0])
    196:                "CERT C rule or recommendation link"
    235:def build_guideline_index(standard_root: Path) -> Dict[Tuple[str, str], Path]:
    236:    """Map (rules/recommendations, URL slug) to local Markdown files."""
    240:        "rules": standard_root / "03.rules",
    241:        "recommendations": standard_root / "08.recommendations",
    246:            raise DistributionError(f"Guideline directory does not exist: {root}")
    249:            match = GUIDELINE_FILE_RE.fullmatch(path.name)
    355:    source: Path, standard_root: Path, distributed_link: str
    360:    guideline_index = build_guideline_index(standard_root)
    365:        destination = guideline_index.get(key)
    433:            "Copy rows from a related-guidelines table into "
    434:            "the linked guidelines' Automated Detection tables."
    438:        "--misra-link",
    447:        help="Markdown file containing the source related-guidelines table",
    450:        "--standard-root",
    452:        default=DEFAULT_STANDARD_ROOT,
    453:        help=f"CERT C content root (default: {DEFAULT_STANDARD_ROOT})",
    473:            arguments.source, arguments.standard_root, arguments.misra_link
    506:        f"Processed {len(rows)} guideline row(s): {inserted} inserted, "
    #!/usr/bin/env python3
    """Distribute a related-guidelines table to guideline pages.
    
    For each row in a related-guidelines table, this script finds the linked CERT C
    rule or recommendation and adds a row to its Automated Detection table.  The
    new row replaces the source row's first cell with a caller-supplied link and
    preserves all remaining source cells.
    
    Run from anywhere in the repository:
    
        python3 scripts/distribute_guideline_table.py \
            --misra-link '[MISRA C:2025](...)' \
            --source path/to/table.md \
            --dry-run
    
    The script preflights every source row and destination before writing any
    files.  It is safe to rerun: existing rows beginning with the supplied link
    are removed before one fresh row is appended.
    """
    
    from __future__ import annotations
    
    import argparse
    import os
    import re
    import stat
    import sys
    import tempfile
    from dataclasses import dataclass
    from pathlib import Path
    from typing import Dict, List, Optional, Sequence, Tuple
    
    
    REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
    DEFAULT_STANDARD_ROOT = (
        REPOSITORY_ROOT / "content/4.sei-cert-c-coding-standard"
    )
    
    GUIDELINE_LINK_RE = re.compile(
        r"^\[(?P<code>[A-Z]{3}\d{2}-C)\]"
        r"\((?P<url>/sei-cert-c-coding-standard/"
        r"(?P<kind>rules|recommendations)/"
        r"(?P<category>[a-z0-9-]+)/(?P<slug>[a-z]{3}\d{2}-c))\)$"
    )
    GUIDELINE_FILE_RE = re.compile(r"^\d+\.(?P<slug>[a-z]{3}\d{2}-c)\.md$")
    HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)\s*$")
    SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
    
    
    class DistributionError(Exception):
        """Raised when input cannot be distributed without ambiguity."""
    
    
    @dataclass(frozen=True)
    class SourceRow:
        code: str
        kind: str
        category: str
        slug: str
        cells: Tuple[str, ...]
    
        def destination_cells(self, distributed_link: str) -> Tuple[str, ...]:
            return (distributed_link, *self.cells[1:])
    
    
    @dataclass(frozen=True)
    class MarkdownTable:
        header_index: int
        separator_index: int
        first_data_index: int
        end_index: int
        header_cells: Tuple[str, ...]
    
    
    @dataclass(frozen=True)
    class PlannedChange:
        path: Path
        original: str
        updated: str
        action: str
    
    
    def parse_markdown_row(line: str) -> Optional[Tuple[str, ...]]:
        """Return trimmed cells from a pipe-delimited Markdown row.
    
        Pipes escaped with a backslash remain part of the cell content.
        """
    
        stripped = line.rstrip("\r\n").strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            return None
    
        body = stripped[1:-1]
        cells: List[str] = []
        current: List[str] = []
        backslash_run = 0
    
        for character in body:
            if character == "|" and backslash_run % 2 == 0:
                cells.append("".join(current).strip())
                current = []
            else:
                current.append(character)
    
            if character == "\\":
                backslash_run += 1
            else:
                backslash_run = 0
    
        cells.append("".join(current).strip())
        return tuple(cells)
    
    
    def is_separator_row(cells: Optional[Tuple[str, ...]]) -> bool:
        return bool(cells) and all(SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)
    
    
    def find_markdown_tables(
        lines: Sequence[str], start: int = 0, end: Optional[int] = None
    ) -> List[MarkdownTable]:
        """Find conventional Markdown tables between two line indexes."""
    
        if end is None:
            end = len(lines)
    
        tables: List[MarkdownTable] = []
        index = start
        while index + 1 < end:
            header = parse_markdown_row(lines[index])
            separator = parse_markdown_row(lines[index + 1])
            if header is None or not is_separator_row(separator):
                index += 1
                continue
    
            if len(header) != len(separator):
                index += 1
                continue
    
            table_end = index + 2
            while table_end < end and parse_markdown_row(lines[table_end]) is not None:
                table_end += 1
    
            tables.append(
                MarkdownTable(
                    header_index=index,
                    separator_index=index + 1,
                    first_data_index=index + 2,
                    end_index=table_end,
                    header_cells=header,
                )
            )
            index = table_end
    
        return tables
    
    
    def read_utf8(path: Path) -> str:
        try:
            return path.read_bytes().decode("utf-8")
        except FileNotFoundError as error:
            raise DistributionError(f"File does not exist: {path}") from error
        except UnicodeDecodeError as error:
            raise DistributionError(f"File is not valid UTF-8: {path}") from error
    
    
    def parse_source_rows(source: Path) -> List[SourceRow]:
        text = read_utf8(source)
        lines = text.splitlines(keepends=True)
        matching_tables = [
            table
            for table in find_markdown_tables(lines)
            if table.header_cells[:2] == ("CERT Rule", "Related Guidelines")
        ]
    
        if len(matching_tables) != 1:
            raise DistributionError(
                f"Expected exactly one 'CERT Rule | Related Guidelines' table in "
                f"{source}, found {len(matching_tables)}"
            )
    
        table = matching_tables[0]
        rows: List[SourceRow] = []
        seen_codes: Dict[str, int] = {}
    
        for line_index in range(table.first_data_index, table.end_index):
            cells = parse_markdown_row(lines[line_index])
            if cells is None or len(cells) < 2:
                raise DistributionError(
                    f"Malformed source row at {source}:{line_index + 1}"
                )
    
            match = GUIDELINE_LINK_RE.fullmatch(cells[0])
            if match is None:
                raise DistributionError(
                    f"The first cell at {source}:{line_index + 1} is not a supported "
                    "CERT C rule or recommendation link"
                )
    
            code = match.group("code")
            slug = match.group("slug")
            if code.lower() != slug:
                raise DistributionError(
                    f"Link text and destination disagree at {source}:{line_index + 1}: "
                    f"{code} versus {slug}"
                )
            if code in seen_codes:
                raise DistributionError(
                    f"Duplicate {code} rows at {source}:{seen_codes[code]} and "
                    f"{source}:{line_index + 1}"
                )
    
            seen_codes[code] = line_index + 1
            rows.append(
                SourceRow(
                    code=code,
                    kind=match.group("kind"),
                    category=match.group("category"),
                    slug=slug,
                    cells=cells,
                )
            )
    
        if not rows:
            raise DistributionError(f"The source table in {source} has no data rows")
    
        return rows
    
    
    def unnumbered_name(path: Path) -> str:
        """Remove a leading numeric ordering prefix from a file or directory name."""
    
        return re.sub(r"^\d+\.", "", path.name)
    
    
    def build_guideline_index(standard_root: Path) -> Dict[Tuple[str, str], Path]:
        """Map (rules/recommendations, URL slug) to local Markdown files."""
    
        index: Dict[Tuple[str, str], Path] = {}
        roots = {
            "rules": standard_root / "03.rules",
            "recommendations": standard_root / "08.recommendations",
        }
    
        for kind, root in roots.items():
            if not root.is_dir():
                raise DistributionError(f"Guideline directory does not exist: {root}")
    
            for path in root.rglob("*.md"):
                match = GUIDELINE_FILE_RE.fullmatch(path.name)
                if match is None:
                    continue
    
                key = (kind, match.group("slug"))
                previous = index.get(key)
                if previous is not None:
                    raise DistributionError(
                        f"Multiple files represent {kind}/{key[1]}: {previous} and {path}"
                    )
                index[key] = path
    
        return index
    
    
    def find_section_bounds(lines: Sequence[str], title: str, path: Path) -> Tuple[int, int]:
        matches: List[Tuple[int, int]] = []
    
        for index, line in enumerate(lines):
            match = HEADING_RE.fullmatch(line.rstrip("\r\n"))
            if match is not None and match.group("title").strip() == title:
                matches.append((index, len(match.group("marks"))))
    
        if len(matches) != 1:
            raise DistributionError(
                f"Expected exactly one '{title}' section in {path}, found {len(matches)}"
            )
    
        section_start, heading_level = matches[0]
        section_end = len(lines)
        for index in range(section_start + 1, len(lines)):
            match = HEADING_RE.fullmatch(lines[index].rstrip("\r\n"))
            if match is not None and len(match.group("marks")) <= heading_level:
                section_end = index
                break
    
        return section_start + 1, section_end
    
    
    def format_markdown_row(cells: Sequence[str], newline: str) -> str:
        return "| " + " | ".join(cells) + " |" + newline
    
    
    def newline_for(text: str) -> str:
        if "\r\n" in text:
            return "\r\n"
        return "\n"
    
    
    def plan_destination_update(
        path: Path, row: SourceRow, distributed_link: str
    ) -> Optional[PlannedChange]:
        original = read_utf8(path)
        lines = original.splitlines(keepends=True)
        section_start, section_end = find_section_bounds(
            lines, "Automated Detection", path
        )
        tables = [
            table
            for table in find_markdown_tables(lines, section_start, section_end)
            if table.header_cells and table.header_cells[0] == "Tool"
        ]
    
        if len(tables) != 1:
            raise DistributionError(
                f"Expected exactly one Automated Detection table beginning with 'Tool' "
                f"in {path}, found {len(tables)}"
            )
    
        table = tables[0]
        desired_cells = row.destination_cells(distributed_link)
        matching_indexes: List[int] = []
    
        for line_index, line in enumerate(lines):
            cells = parse_markdown_row(line)
            if cells is not None and cells and cells[0] == distributed_link:
                matching_indexes.append(line_index)
    
        newline = newline_for(original)
        desired_line = format_markdown_row(desired_cells, newline)
        matching_index_set = set(matching_indexes)
    
        if matching_indexes:
            lines = [
                line for line_index, line in enumerate(lines)
                if line_index not in matching_index_set
            ]
    
        removed_before_insertion = sum(
            line_index < table.end_index for line_index in matching_indexes
        )
        insertion_index = table.end_index - removed_before_insertion
        lines.insert(insertion_index, desired_line)
        updated = "".join(lines)
        if updated == original:
            return None
    
        return PlannedChange(
            path=path,
            original=original,
            updated=updated,
            action="updated" if matching_indexes else "inserted",
        )
    
    
    def plan_changes(
        source: Path, standard_root: Path, distributed_link: str
    ) -> Tuple[List[SourceRow], List[PlannedChange]]:
        """Validate every row and destination, then return the complete write plan."""
    
        rows = parse_source_rows(source)
        guideline_index = build_guideline_index(standard_root)
        changes: List[PlannedChange] = []
    
        for row in rows:
            key = (row.kind, row.slug)
            destination = guideline_index.get(key)
            if destination is None:
                raise DistributionError(
                    f"No local file found for {row.code} ({row.kind}/{row.slug})"
                )
    
            actual_category = unnumbered_name(destination.parent)
            if actual_category != row.category:
                raise DistributionError(
                    f"Category mismatch for {row.code}: source link uses {row.category}, "
                    f"but {destination} is in {actual_category}"
                )
    
            change = plan_destination_update(destination, row, distributed_link)
            if change is not None:
                changes.append(change)
    
        return rows, changes
    
    
    def write_atomic(change: PlannedChange) -> None:
        """Atomically replace one file while preserving its permission bits."""
    
        mode = stat.S_IMODE(change.path.stat().st_mode)
        temporary_name: Optional[str] = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="wb", prefix=f".{change.path.name}.", dir=change.path.parent,
                delete=False
            ) as temporary:
                temporary_name = temporary.name
                temporary.write(change.updated.encode("utf-8"))
                temporary.flush()
                os.fsync(temporary.fileno())
    
            os.chmod(temporary_name, mode)
            os.replace(temporary_name, change.path)
            temporary_name = None
        finally:
            if temporary_name is not None:
                try:
                    os.unlink(temporary_name)
                except FileNotFoundError:
                    pass
    
    
    def path_argument(value: str) -> Path:
        return Path(value).expanduser().resolve()
    
    
    def cell_argument(value: str) -> str:
        """Validate a command-line value that will become one Markdown cell."""
    
        cell = value.strip()
        if not cell:
            raise argparse.ArgumentTypeError("must not be empty")
        if "\n" in cell or "\r" in cell:
            raise argparse.ArgumentTypeError("must not contain a newline")
        if len(parse_markdown_row(f"| {cell} |") or ()) != 1:
            raise argparse.ArgumentTypeError(
                "must not contain an unescaped pipe character"
            )
        return cell
    
    
    def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description=(
                "Copy rows from a related-guidelines table into "
                "the linked guidelines' Automated Detection tables."
            )
        )
        parser.add_argument(
            "--misra-link",
            required=True,
            type=cell_argument,
            help="Markdown cell to place first in every distributed row",
        )
        parser.add_argument(
            "--source",
            required=True,
            type=path_argument,
            help="Markdown file containing the source related-guidelines table",
        )
        parser.add_argument(
            "--standard-root",
            type=path_argument,
            default=DEFAULT_STANDARD_ROOT,
            help=f"CERT C content root (default: {DEFAULT_STANDARD_ROOT})",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="validate and report changes without writing files",
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="list every file that would be or was changed",
        )
        return parser.parse_args(argv)
    
    
    def main(argv: Optional[Sequence[str]] = None) -> int:
        arguments = parse_arguments(argv)
    
        try:
            rows, changes = plan_changes(
                arguments.source, arguments.standard_root, arguments.misra_link
            )
        except (DistributionError, OSError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 1
    
        inserted = sum(change.action == "inserted" for change in changes)
        updated = sum(change.action == "updated" for change in changes)
        unchanged = len(rows) - len(changes)
    
        if arguments.verbose:
            for change in changes:
                try:
                    display_path = change.path.relative_to(REPOSITORY_ROOT)
                except ValueError:
                    display_path = change.path
                print(f"{change.action}: {display_path}")
    
        if arguments.dry_run:
            print(
                f"Dry run: {len(changes)} file(s) would change "
                f"({inserted} inserted, {updated} updated); {unchanged} already current."
            )
            return 0
    
        try:
            for change in changes:
                write_atomic(change)
        except OSError as error:
            print(f"error while writing {change.path}: {error}", file=sys.stderr)
            return 1
    
        print(
            f"Processed {len(rows)} guideline row(s): {inserted} inserted, "
            f"{updated} updated, {unchanged} already current."
        )
        return 0
    
    
    if __name__ == "__main__":
        raise SystemExit(main())
    ✓ • 41ms

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /host/scripts/distribute_guideline_table.py
    @@ -1,8 +1,8 @@
     #!/usr/bin/env python3
    -"""Distribute a related-guidelines table to guideline pages.
    +"""Distribute rows from one Markdown table to linked pages.
     
    -For each row in a related-guidelines table, this script finds the linked CERT C
    -rule or recommendation and adds a row to its Automated Detection table.  The
    -new row replaces the source row's first cell with a caller-supplied link and
    -preserves all remaining source cells.
    +For each source row, this script follows the internal Markdown link in the
    +first cell and adds a row to a table on that page. The new row replaces the
    +source row's first cell with a caller-supplied cell and preserves all remaining
    +source cells.
     
    @@ -11,4 +11,5 @@
         python3 scripts/distribute_guideline_table.py \
    -        --misra-link '[MISRA C:2025](...)' \
    +        --link '[External standard](...)' \
             --source path/to/table.md \
    +        --content-root path/to/content \
             --dry-run
    @@ -31,2 +32,3 @@
     from typing import Dict, List, Optional, Sequence, Tuple
    +from urllib.parse import unquote, urlsplit
     
    @@ -34,13 +36,6 @@
     REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
    -DEFAULT_STANDARD_ROOT = (
    -    REPOSITORY_ROOT / "content/4.sei-cert-c-coding-standard"
    -)
    -
    -GUIDELINE_LINK_RE = re.compile(
    -    r"^\[(?P<code>[A-Z]{3}\d{2}-C)\]"
    -    r"\((?P<url>/sei-cert-c-coding-standard/"
    -    r"(?P<kind>rules|recommendations)/"
    -    r"(?P<category>[a-z0-9-]+)/(?P<slug>[a-z]{3}\d{2}-c))\)$"
    +MARKDOWN_LINK_RE = re.compile(
    +    r"^\[(?P<label>(?:\\.|[^\]])+)\]"
    +    r"\(\s*<?(?P<url>[^\s>)]+)>?(?:\s+['\"][^'\"]*['\"])?\s*\)$"
     )
    -GUIDELINE_FILE_RE = re.compile(r"^\d+\.(?P<slug>[a-z]{3}\d{2}-c)\.md$")
     HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)\s*$")
    @@ -55,6 +50,5 @@
     class SourceRow:
    -    code: str
    -    kind: str
    -    category: str
    -    slug: str
    +    label: str
    +    destination_url: str
    +    line_number: int
         cells: Tuple[str, ...]

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /host/scripts/distribute_guideline_table.py
    @@ -159,20 +159,17 @@
     
    -def parse_source_rows(source: Path) -> List[SourceRow]:
    +def parse_source_rows(source: Path, table_index: int) -> List[SourceRow]:
         text = read_utf8(source)
         lines = text.splitlines(keepends=True)
    -    matching_tables = [
    -        table
    -        for table in find_markdown_tables(lines)
    -        if table.header_cells[:2] == ("CERT Rule", "Related Guidelines")
    -    ]
    +    tables = find_markdown_tables(lines)
     
    -    if len(matching_tables) != 1:
    +    if not tables:
    +        raise DistributionError(f"No Markdown tables found in {source}")
    +    if table_index > len(tables):
             raise DistributionError(
    -            f"Expected exactly one 'CERT Rule | Related Guidelines' table in "
    -            f"{source}, found {len(matching_tables)}"
    +            f"Requested source table {table_index} in {source}, but only "
    +            f"{len(tables)} table(s) were found"
             )
     
    -    table = matching_tables[0]
    +    table = tables[table_index - 1]
         rows: List[SourceRow] = []
    -    seen_codes: Dict[str, int] = {}
     
    @@ -180,3 +177,3 @@
             cells = parse_markdown_row(lines[line_index])
    -        if cells is None or len(cells) < 2:
    +        if cells is None or not cells:
                 raise DistributionError(
    @@ -185,29 +182,14 @@
     
    -        match = GUIDELINE_LINK_RE.fullmatch(cells[0])
    +        match = MARKDOWN_LINK_RE.fullmatch(cells[0])
             if match is None:
                 raise DistributionError(
    -                f"The first cell at {source}:{line_index + 1} is not a supported "
    -                "CERT C rule or recommendation link"
    -            )
    -
    -        code = match.group("code")
    -        slug = match.group("slug")
    -        if code.lower() != slug:
    -            raise DistributionError(
    -                f"Link text and destination disagree at {source}:{line_index + 1}: "
    -                f"{code} versus {slug}"
    -            )
    -        if code in seen_codes:
    -            raise DistributionError(
    -                f"Duplicate {code} rows at {source}:{seen_codes[code]} and "
    -                f"{source}:{line_index + 1}"
    +                f"The first cell at {source}:{line_index + 1} is not a "
    +                "supported Markdown link"
                 )
     
    -        seen_codes[code] = line_index + 1
             rows.append(
                 SourceRow(
    -                code=code,
    -                kind=match.group("kind"),
    -                category=match.group("category"),
    -                slug=slug,
    +                label=match.group("label"),
    +                destination_url=match.group("url"),
    +                line_number=line_index + 1,
                     cells=cells,

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /host/scripts/distribute_guideline_table.py
    @@ -204,34 +204,52 @@
     
    -def unnumbered_name(path: Path) -> str:
    -    """Remove a leading numeric ordering prefix from a file or directory name."""
    +def unnumbered_name(name: str) -> str:
    +    """Remove a leading numeric ordering prefix from a path component."""
     
    -    return re.sub(r"^\d+\.", "", path.name)
    +    return re.sub(r"^\d+\.", "", name)
     
     
    -def build_guideline_index(standard_root: Path) -> Dict[Tuple[str, str], Path]:
    -    """Map (rules/recommendations, URL slug) to local Markdown files."""
    +def normalize_url_path(url: str, context: str) -> str:
    +    """Return a normalized site-relative path without query or fragment."""
     
    -    index: Dict[Tuple[str, str], Path] = {}
    -    roots = {
    -        "rules": standard_root / "03.rules",
    -        "recommendations": standard_root / "08.recommendations",
    -    }
    +    parsed = urlsplit(url)
    +    if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
    +        raise DistributionError(
    +            f"Expected a site-relative destination URL in {context}, got {url!r}"
    +        )
    +    path = unquote(parsed.path)
    +    return path.rstrip("/") or "/"
     
    -    for kind, root in roots.items():
    -        if not root.is_dir():
    -            raise DistributionError(f"Guideline directory does not exist: {root}")
     
    -        for path in root.rglob("*.md"):
    -            match = GUIDELINE_FILE_RE.fullmatch(path.name)
    -            if match is None:
    -                continue
    +def normalize_url_prefix(value: str) -> str:
    +    path = normalize_url_path(value, "--url-prefix")
    +    if path == "/":
    +        return ""
    +    return path
     
    -            key = (kind, match.group("slug"))
    -            previous = index.get(key)
    -            if previous is not None:
    -                raise DistributionError(
    -                    f"Multiple files represent {kind}/{key[1]}: {previous} and {path}"
    -                )
    -            index[key] = path
     
    +def route_for_page(content_root: Path, path: Path, url_prefix: str) -> str:
    +    relative = path.relative_to(content_root)
    +    components = [unnumbered_name(part) for part in relative.parts[:-1]]
    +    page_name = unnumbered_name(path.stem)
    +    if page_name != "index":
    +        components.append(page_name)
    +
    +    suffix = "/".join(components)
    +    if not suffix:
    +        return url_prefix or "/"
    +    return f"{url_prefix}/{suffix}" if url_prefix else f"/{suffix}"
    +
    +
    +def build_page_index(
    +    content_root: Path, url_prefix: str
    +) -> Dict[str, List[Path]]:
    +    """Map site-relative page routes to local Markdown files."""
    +
    +    if not content_root.is_dir():
    +        raise DistributionError(f"Content root does not exist: {content_root}")
    +
    +    index: Dict[str, List[Path]] = {}
    +    for path in content_root.rglob("*.md"):
    +        route = route_for_page(content_root, path, url_prefix)
    +        index.setdefault(route, []).append(path)
         return index
    @@ -239,2 +257,21 @@
     
    +def resolve_destination(
    +    row: SourceRow, source: Path, page_index: Dict[str, List[Path]]
    +) -> Path:
    +    context = f"{source}:{row.line_number}"
    +    route = normalize_url_path(row.destination_url, context)
    +    matches = page_index.get(route, [])
    +    if not matches:
    +        raise DistributionError(
    +            f"No local Markdown file found for {row.label!r} at {route} "
    +            f"({context})"
    +        )
    +    if len(matches) > 1:
    +        formatted_matches = ", ".join(str(path) for path in matches)
    +        raise DistributionError(
    +            f"Multiple local files map to {route} ({context}): {formatted_matches}"
    +        )
    +    return matches[0]
    +
    +
     def find_section_bounds(lines: Sequence[str], title: str, path: Path) -> Tuple[int, int]:

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /host/scripts/distribute_guideline_table.py
    @@ -311,3 +311,7 @@
     def plan_destination_update(
    -    path: Path, row: SourceRow, distributed_link: str
    +    path: Path,
    +    rows: Sequence[SourceRow],
    +    distributed_cell: str,
    +    target_section: str,
    +    target_table_header: str,
     ) -> Optional[PlannedChange]:
    @@ -316,3 +320,3 @@
         section_start, section_end = find_section_bounds(
    -        lines, "Automated Detection", path
    +        lines, target_section, path
         )
    @@ -321,3 +325,3 @@
             for table in find_markdown_tables(lines, section_start, section_end)
    -        if table.header_cells and table.header_cells[0] == "Tool"
    +        if table.header_cells and table.header_cells[0] == target_table_header
         ]
    @@ -326,4 +330,4 @@
             raise DistributionError(
    -            f"Expected exactly one Automated Detection table beginning with 'Tool' "
    -            f"in {path}, found {len(tables)}"
    +            f"Expected exactly one table beginning with {target_table_header!r} "
    +            f"in the {target_section!r} section of {path}, found {len(tables)}"
             )
    @@ -331,3 +335,2 @@
         table = tables[0]
    -    desired_cells = row.destination_cells(distributed_link)
         matching_indexes: List[int] = []
    @@ -336,3 +339,3 @@
             cells = parse_markdown_row(line)
    -        if cells is not None and cells and cells[0] == distributed_link:
    +        if cells is not None and cells and cells[0] == distributed_cell:
                 matching_indexes.append(line_index)
    @@ -340,3 +343,6 @@
         newline = newline_for(original)
    -    desired_line = format_markdown_row(desired_cells, newline)
    +    desired_lines = [
    +        format_markdown_row(row.destination_cells(distributed_cell), newline)
    +        for row in rows
    +    ]
         matching_index_set = set(matching_indexes)
    @@ -353,3 +359,3 @@
         insertion_index = table.end_index - removed_before_insertion
    -    lines.insert(insertion_index, desired_line)
    +    lines[insertion_index:insertion_index] = desired_lines
         updated = "".join(lines)
    @@ -367,26 +373,29 @@
     def plan_changes(
    -    source: Path, standard_root: Path, distributed_link: str
    -) -> Tuple[List[SourceRow], List[PlannedChange]]:
    +    source: Path,
    +    content_root: Path,
    +    url_prefix: str,
    +    distributed_cell: str,
    +    source_table_index: int,
    +    target_section: str,
    +    target_table_header: str,
    +) -> Tuple[List[SourceRow], int, List[PlannedChange]]:
         """Validate every row and destination, then return the complete write plan."""
     
    -    rows = parse_source_rows(source)
    -    guideline_index = build_guideline_index(standard_root)
    -    changes: List[PlannedChange] = []
    +    rows = parse_source_rows(source, source_table_index)
    +    page_index = build_page_index(content_root, url_prefix)
    +    rows_by_destination: Dict[Path, List[SourceRow]] = {}
     
         for row in rows:
    -        key = (row.kind, row.slug)
    -        destination = guideline_index.get(key)
    -        if destination is None:
    -            raise DistributionError(
    -                f"No local file found for {row.code} ({row.kind}/{row.slug})"
    -            )
    -
    -        actual_category = unnumbered_name(destination.parent)
    -        if actual_category != row.category:
    -            raise DistributionError(
    -                f"Category mismatch for {row.code}: source link uses {row.category}, "
    -                f"but {destination} is in {actual_category}"
    -            )
    +        destination = resolve_destination(row, source, page_index)
    +        rows_by_destination.setdefault(destination, []).append(row)
     
    -        change = plan_destination_update(destination, row, distributed_link)
    +    changes: List[PlannedChange] = []
    +    for destination, destination_rows in rows_by_destination.items():
    +        change = plan_destination_update(
    +            destination,
    +            destination_rows,
    +            distributed_cell,
    +            target_section,
    +            target_table_header,
    +        )
             if change is not None:
    @@ -394,3 +403,3 @@
     
    -    return rows, changes
    +    return rows, len(rows_by_destination), changes
     

## Activity

    file changes: Completed · 1 changes
    Update { move_path: None }: /host/scripts/distribute_guideline_table.py
    @@ -451,2 +451,12 @@
     
    +def positive_integer(value: str) -> int:
    +    try:
    +        number = int(value)
    +    except ValueError as error:
    +        raise argparse.ArgumentTypeError("must be an integer") from error
    +    if number < 1:
    +        raise argparse.ArgumentTypeError("must be at least 1")
    +    return number
    +
    +
     def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    @@ -454,4 +464,4 @@
             description=(
    -            "Copy rows from a related-guidelines table into "
    -            "the linked guidelines' Automated Detection tables."
    +            "Copy rows from one Markdown table into tables on the pages linked "
    +            "by each source row."
             )
    @@ -459,3 +469,3 @@
         parser.add_argument(
    -        "--misra-link",
    +        "--link",
             required=True,
    @@ -468,11 +478,35 @@
             type=path_argument,
    -        help="Markdown file containing the source related-guidelines table",
    +        help="Markdown file containing the source table",
         )
         parser.add_argument(
    -        "--standard-root",
    +        "--content-root",
    +        required=True,
             type=path_argument,
    -        default=DEFAULT_STANDARD_ROOT,
    -        help=f"CERT C content root (default: {DEFAULT_STANDARD_ROOT})",
    +        help="root directory containing destination Markdown pages",
    +    )
    +    parser.add_argument(
    +        "--url-prefix",
    +        type=normalize_url_prefix,
    +        help=(
    +            "site-relative URL prefix for the content root; defaults to the "
    +            "content root directory name without a numeric ordering prefix"
    +        ),
    +    )
    +    parser.add_argument(
    +        "--source-table-index",
    +        type=positive_integer,
    +        default=1,
    +        help="1-based index of the Markdown table to distribute (default: 1)",
    +    )
    +    parser.add_argument(
    +        "--target-section",
    +        default="Automated Detection",
    +        help="destination section heading (default: Automated Detection)",
         )
         parser.add_argument(
    +        "--target-table-header",
    +        default="Tool",
    +        help="first header cell of the destination table (default: Tool)",
    +    )
    +    parser.add_argument(
             "--dry-run",
    @@ -491,6 +525,15 @@
         arguments = parse_arguments(argv)
    +    url_prefix = arguments.url_prefix
    +    if url_prefix is None:
    +        url_prefix = "/" + unnumbered_name(arguments.content_root.name)
     
         try:
    -        rows, changes = plan_changes(
    -            arguments.source, arguments.standard_root, arguments.misra_link
    +        rows, destination_count, changes = plan_changes(
    +            source=arguments.source,
    +            content_root=arguments.content_root,
    +            url_prefix=url_prefix,
    +            distributed_cell=arguments.link,
    +            source_table_index=arguments.source_table_index,
    +            target_section=arguments.target_section,
    +            target_table_header=arguments.target_table_header,
             )
    @@ -502,3 +545,3 @@
         updated = sum(change.action == "updated" for change in changes)
    -    unchanged = len(rows) - len(changes)
    +    unchanged = destination_count - len(changes)
     
    @@ -527,4 +570,5 @@
         print(
    -        f"Processed {len(rows)} guideline row(s): {inserted} inserted, "
    -        f"{updated} updated, {unchanged} already current."
    +        f"Processed {len(rows)} source row(s) across {destination_count} "
    +        f"destination file(s): {inserted} inserted, {updated} updated, "
    +        f"{unchanged} already current."
         )

## Activity

    $ rg -n -i 'misra|cert|standard-root|guideline|rules|recommendations|standard' scripts/distribute_guideline_table.py || true
        python3 -B scripts/distribute_guideline_table.py --help
        python3 -B scripts/distribute_guideline_table.py --link '[External standard](/references/example)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --content-root content/4.sei-cert-c-coding-standard --dry-run
    Dry run: 121 file(s) would change (121 inserted, 0 updated); 0 already current.
    ✓ • 342ms

## Assistant

The hard-coded domain model is gone: source rows may now contain any internal Markdown links, destination pages are resolved from a required content root, and the source table can be selected by index. I’m validating the generalized URL-to-file mapping and rerun behavior against a temporary copy.

## Activity

    $ test_root=$(mktemp -d /tmp/distribute-table.XXXXXX)
        cp -a content/4.sei-cert-c-coding-standard "$test_root/content-root"
        python3 -B scripts/distribute_guideline_table.py --link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --content-root "$test_root/content-root" --url-prefix /sei-cert-c-coding-standard
        python3 -B scripts/distribute_guideline_table.py --link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --content-root "$test_root/content-root" --url-prefix /sei-cert-c-coding-standard --dry-run
        rg -l '^\| \[MISRA C:2025\]' "$test_root/content-root/03.rules" "$test_root/content-root/08.recommendations" | wc -l
        printf '%s\n' "$test_root"
    Processed 121 source row(s) across 121 destination file(s): 121 inserted, 0 updated, 0 already current.
    Dry run: 0 file(s) would change (0 inserted, 0 updated); 121 already current.
    121
    /tmp/distribute-table.sIFH8t
    ✓ • 766ms

## Activity

    $ rg -n 'distributed_link|misra_link|standard_root|DEFAULT_|GUIDELINE|CERT|MISRA' scripts/distribute_guideline_table.py || true
        sed -n '1,560p' scripts/distribute_guideline_table.py
    56:    def destination_cells(self, distributed_link: str) -> Tuple[str, ...]:
    57:        return (distributed_link, *self.cells[1:])
    #!/usr/bin/env python3
    """Distribute rows from one Markdown table to linked pages.
    
    For each source row, this script follows the internal Markdown link in the
    first cell and adds a row to a table on that page. The new row replaces the
    source row's first cell with a caller-supplied cell and preserves all remaining
    source cells.
    
    Run from anywhere in the repository:
    
        python3 scripts/distribute_guideline_table.py \
            --link '[External standard](...)' \
            --source path/to/table.md \
            --content-root path/to/content \
            --dry-run
    
    The script preflights every source row and destination before writing any
    files.  It is safe to rerun: existing rows beginning with the supplied link
    are removed before one fresh row is appended.
    """
    
    from __future__ import annotations
    
    import argparse
    import os
    import re
    import stat
    import sys
    import tempfile
    from dataclasses import dataclass
    from pathlib import Path
    from typing import Dict, List, Optional, Sequence, Tuple
    from urllib.parse import unquote, urlsplit
    
    
    REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
    MARKDOWN_LINK_RE = re.compile(
        r"^\[(?P<label>(?:\\.|[^\]])+)\]"
        r"\(\s*<?(?P<url>[^\s>)]+)>?(?:\s+['\"][^'\"]*['\"])?\s*\)$"
    )
    HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)\s*$")
    SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
    
    
    class DistributionError(Exception):
        """Raised when input cannot be distributed without ambiguity."""
    
    
    @dataclass(frozen=True)
    class SourceRow:
        label: str
        destination_url: str
        line_number: int
        cells: Tuple[str, ...]
    
        def destination_cells(self, distributed_link: str) -> Tuple[str, ...]:
            return (distributed_link, *self.cells[1:])
    
    
    @dataclass(frozen=True)
    class MarkdownTable:
        header_index: int
        separator_index: int
        first_data_index: int
        end_index: int
        header_cells: Tuple[str, ...]
    
    
    @dataclass(frozen=True)
    class PlannedChange:
        path: Path
        original: str
        updated: str
        action: str
    
    
    def parse_markdown_row(line: str) -> Optional[Tuple[str, ...]]:
        """Return trimmed cells from a pipe-delimited Markdown row.
    
        Pipes escaped with a backslash remain part of the cell content.
        """
    
        stripped = line.rstrip("\r\n").strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            return None
    
        body = stripped[1:-1]
        cells: List[str] = []
        current: List[str] = []
        backslash_run = 0
    
        for character in body:
            if character == "|" and backslash_run % 2 == 0:
                cells.append("".join(current).strip())
                current = []
            else:
                current.append(character)
    
            if character == "\\":
                backslash_run += 1
            else:
                backslash_run = 0
    
        cells.append("".join(current).strip())
        return tuple(cells)
    
    
    def is_separator_row(cells: Optional[Tuple[str, ...]]) -> bool:
        return bool(cells) and all(SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)
    
    
    def find_markdown_tables(
        lines: Sequence[str], start: int = 0, end: Optional[int] = None
    ) -> List[MarkdownTable]:
        """Find conventional Markdown tables between two line indexes."""
    
        if end is None:
            end = len(lines)
    
        tables: List[MarkdownTable] = []
        index = start
        while index + 1 < end:
            header = parse_markdown_row(lines[index])
            separator = parse_markdown_row(lines[index + 1])
            if header is None or not is_separator_row(separator):
                index += 1
                continue
    
            if len(header) != len(separator):
                index += 1
                continue
    
            table_end = index + 2
            while table_end < end and parse_markdown_row(lines[table_end]) is not None:
                table_end += 1
    
            tables.append(
                MarkdownTable(
                    header_index=index,
                    separator_index=index + 1,
                    first_data_index=index + 2,
                    end_index=table_end,
                    header_cells=header,
                )
            )
            index = table_end
    
        return tables
    
    
    def read_utf8(path: Path) -> str:
        try:
            return path.read_bytes().decode("utf-8")
        except FileNotFoundError as error:
            raise DistributionError(f"File does not exist: {path}") from error
        except UnicodeDecodeError as error:
            raise DistributionError(f"File is not valid UTF-8: {path}") from error
    
    
    def parse_source_rows(source: Path, table_index: int) -> List[SourceRow]:
        text = read_utf8(source)
        lines = text.splitlines(keepends=True)
        tables = find_markdown_tables(lines)
    
        if not tables:
            raise DistributionError(f"No Markdown tables found in {source}")
        if table_index > len(tables):
            raise DistributionError(
                f"Requested source table {table_index} in {source}, but only "
                f"{len(tables)} table(s) were found"
            )
    
        table = tables[table_index - 1]
        rows: List[SourceRow] = []
    
        for line_index in range(table.first_data_index, table.end_index):
            cells = parse_markdown_row(lines[line_index])
            if cells is None or not cells:
                raise DistributionError(
                    f"Malformed source row at {source}:{line_index + 1}"
                )
    
            match = MARKDOWN_LINK_RE.fullmatch(cells[0])
            if match is None:
                raise DistributionError(
                    f"The first cell at {source}:{line_index + 1} is not a "
                    "supported Markdown link"
                )
    
            rows.append(
                SourceRow(
                    label=match.group("label"),
                    destination_url=match.group("url"),
                    line_number=line_index + 1,
                    cells=cells,
                )
            )
    
        if not rows:
            raise DistributionError(f"The source table in {source} has no data rows")
    
        return rows
    
    
    def unnumbered_name(name: str) -> str:
        """Remove a leading numeric ordering prefix from a path component."""
    
        return re.sub(r"^\d+\.", "", name)
    
    
    def normalize_url_path(url: str, context: str) -> str:
        """Return a normalized site-relative path without query or fragment."""
    
        parsed = urlsplit(url)
        if parsed.scheme or parsed.netloc or not parsed.path.startswith("/"):
            raise DistributionError(
                f"Expected a site-relative destination URL in {context}, got {url!r}"
            )
        path = unquote(parsed.path)
        return path.rstrip("/") or "/"
    
    
    def normalize_url_prefix(value: str) -> str:
        path = normalize_url_path(value, "--url-prefix")
        if path == "/":
            return ""
        return path
    
    
    def route_for_page(content_root: Path, path: Path, url_prefix: str) -> str:
        relative = path.relative_to(content_root)
        components = [unnumbered_name(part) for part in relative.parts[:-1]]
        page_name = unnumbered_name(path.stem)
        if page_name != "index":
            components.append(page_name)
    
        suffix = "/".join(components)
        if not suffix:
            return url_prefix or "/"
        return f"{url_prefix}/{suffix}" if url_prefix else f"/{suffix}"
    
    
    def build_page_index(
        content_root: Path, url_prefix: str
    ) -> Dict[str, List[Path]]:
        """Map site-relative page routes to local Markdown files."""
    
        if not content_root.is_dir():
            raise DistributionError(f"Content root does not exist: {content_root}")
    
        index: Dict[str, List[Path]] = {}
        for path in content_root.rglob("*.md"):
            route = route_for_page(content_root, path, url_prefix)
            index.setdefault(route, []).append(path)
        return index
    
    
    def resolve_destination(
        row: SourceRow, source: Path, page_index: Dict[str, List[Path]]
    ) -> Path:
        context = f"{source}:{row.line_number}"
        route = normalize_url_path(row.destination_url, context)
        matches = page_index.get(route, [])
        if not matches:
            raise DistributionError(
                f"No local Markdown file found for {row.label!r} at {route} "
                f"({context})"
            )
        if len(matches) > 1:
            formatted_matches = ", ".join(str(path) for path in matches)
            raise DistributionError(
                f"Multiple local files map to {route} ({context}): {formatted_matches}"
            )
        return matches[0]
    
    
    def find_section_bounds(lines: Sequence[str], title: str, path: Path) -> Tuple[int, int]:
        matches: List[Tuple[int, int]] = []
    
        for index, line in enumerate(lines):
            match = HEADING_RE.fullmatch(line.rstrip("\r\n"))
            if match is not None and match.group("title").strip() == title:
                matches.append((index, len(match.group("marks"))))
    
        if len(matches) != 1:
            raise DistributionError(
                f"Expected exactly one '{title}' section in {path}, found {len(matches)}"
            )
    
        section_start, heading_level = matches[0]
        section_end = len(lines)
        for index in range(section_start + 1, len(lines)):
            match = HEADING_RE.fullmatch(lines[index].rstrip("\r\n"))
            if match is not None and len(match.group("marks")) <= heading_level:
                section_end = index
                break
    
        return section_start + 1, section_end
    
    
    def format_markdown_row(cells: Sequence[str], newline: str) -> str:
        return "| " + " | ".join(cells) + " |" + newline
    
    
    def newline_for(text: str) -> str:
        if "\r\n" in text:
            return "\r\n"
        return "\n"
    
    
    def plan_destination_update(
        path: Path,
        rows: Sequence[SourceRow],
        distributed_cell: str,
        target_section: str,
        target_table_header: str,
    ) -> Optional[PlannedChange]:
        original = read_utf8(path)
        lines = original.splitlines(keepends=True)
        section_start, section_end = find_section_bounds(
            lines, target_section, path
        )
        tables = [
            table
            for table in find_markdown_tables(lines, section_start, section_end)
            if table.header_cells and table.header_cells[0] == target_table_header
        ]
    
        if len(tables) != 1:
            raise DistributionError(
                f"Expected exactly one table beginning with {target_table_header!r} "
                f"in the {target_section!r} section of {path}, found {len(tables)}"
            )
    
        table = tables[0]
        matching_indexes: List[int] = []
    
        for line_index, line in enumerate(lines):
            cells = parse_markdown_row(line)
            if cells is not None and cells and cells[0] == distributed_cell:
                matching_indexes.append(line_index)
    
        newline = newline_for(original)
        desired_lines = [
            format_markdown_row(row.destination_cells(distributed_cell), newline)
            for row in rows
        ]
        matching_index_set = set(matching_indexes)
    
        if matching_indexes:
            lines = [
                line for line_index, line in enumerate(lines)
                if line_index not in matching_index_set
            ]
    
        removed_before_insertion = sum(
            line_index < table.end_index for line_index in matching_indexes
        )
        insertion_index = table.end_index - removed_before_insertion
        lines[insertion_index:insertion_index] = desired_lines
        updated = "".join(lines)
        if updated == original:
            return None
    
        return PlannedChange(
            path=path,
            original=original,
            updated=updated,
            action="updated" if matching_indexes else "inserted",
        )
    
    
    def plan_changes(
        source: Path,
        content_root: Path,
        url_prefix: str,
        distributed_cell: str,
        source_table_index: int,
        target_section: str,
        target_table_header: str,
    ) -> Tuple[List[SourceRow], int, List[PlannedChange]]:
        """Validate every row and destination, then return the complete write plan."""
    
        rows = parse_source_rows(source, source_table_index)
        page_index = build_page_index(content_root, url_prefix)
        rows_by_destination: Dict[Path, List[SourceRow]] = {}
    
        for row in rows:
            destination = resolve_destination(row, source, page_index)
            rows_by_destination.setdefault(destination, []).append(row)
    
        changes: List[PlannedChange] = []
        for destination, destination_rows in rows_by_destination.items():
            change = plan_destination_update(
                destination,
                destination_rows,
                distributed_cell,
                target_section,
                target_table_header,
            )
            if change is not None:
                changes.append(change)
    
        return rows, len(rows_by_destination), changes
    
    
    def write_atomic(change: PlannedChange) -> None:
        """Atomically replace one file while preserving its permission bits."""
    
        mode = stat.S_IMODE(change.path.stat().st_mode)
        temporary_name: Optional[str] = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="wb", prefix=f".{change.path.name}.", dir=change.path.parent,
                delete=False
            ) as temporary:
                temporary_name = temporary.name
                temporary.write(change.updated.encode("utf-8"))
                temporary.flush()
                os.fsync(temporary.fileno())
    
            os.chmod(temporary_name, mode)
            os.replace(temporary_name, change.path)
            temporary_name = None
        finally:
            if temporary_name is not None:
                try:
                    os.unlink(temporary_name)
                except FileNotFoundError:
                    pass
    
    
    def path_argument(value: str) -> Path:
        return Path(value).expanduser().resolve()
    
    
    def cell_argument(value: str) -> str:
        """Validate a command-line value that will become one Markdown cell."""
    
        cell = value.strip()
        if not cell:
            raise argparse.ArgumentTypeError("must not be empty")
        if "\n" in cell or "\r" in cell:
            raise argparse.ArgumentTypeError("must not contain a newline")
        if len(parse_markdown_row(f"| {cell} |") or ()) != 1:
            raise argparse.ArgumentTypeError(
                "must not contain an unescaped pipe character"
            )
        return cell
    
    
    def positive_integer(value: str) -> int:
        try:
            number = int(value)
        except ValueError as error:
            raise argparse.ArgumentTypeError("must be an integer") from error
        if number < 1:
            raise argparse.ArgumentTypeError("must be at least 1")
        return number
    
    
    def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description=(
                "Copy rows from one Markdown table into tables on the pages linked "
                "by each source row."
            )
        )
        parser.add_argument(
            "--link",
            required=True,
            type=cell_argument,
            help="Markdown cell to place first in every distributed row",
        )
        parser.add_argument(
            "--source",
            required=True,
            type=path_argument,
            help="Markdown file containing the source table",
        )
        parser.add_argument(
            "--content-root",
            required=True,
            type=path_argument,
            help="root directory containing destination Markdown pages",
        )
        parser.add_argument(
            "--url-prefix",
            type=normalize_url_prefix,
            help=(
                "site-relative URL prefix for the content root; defaults to the "
                "content root directory name without a numeric ordering prefix"
            ),
        )
        parser.add_argument(
            "--source-table-index",
            type=positive_integer,
            default=1,
            help="1-based index of the Markdown table to distribute (default: 1)",
        )
        parser.add_argument(
            "--target-section",
            default="Automated Detection",
            help="destination section heading (default: Automated Detection)",
        )
        parser.add_argument(
            "--target-table-header",
            default="Tool",
            help="first header cell of the destination table (default: Tool)",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="validate and report changes without writing files",
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="list every file that would be or was changed",
        )
        return parser.parse_args(argv)
    
    
    def main(argv: Optional[Sequence[str]] = None) -> int:
        arguments = parse_arguments(argv)
        url_prefix = arguments.url_prefix
        if url_prefix is None:
            url_prefix = "/" + unnumbered_name(arguments.content_root.name)
    
        try:
            rows, destination_count, changes = plan_changes(
                source=arguments.source,
                content_root=arguments.content_root,
                url_prefix=url_prefix,
                distributed_cell=arguments.link,
                source_table_index=arguments.source_table_index,
                target_section=arguments.target_section,
                target_table_header=arguments.target_table_header,
            )
        except (DistributionError, OSError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 1
    
        inserted = sum(change.action == "inserted" for change in changes)
        updated = sum(change.action == "updated" for change in changes)
        unchanged = destination_count - len(changes)
    
        if arguments.verbose:
            for change in changes:
                try:
                    display_path = change.path.relative_to(REPOSITORY_ROOT)
                except ValueError:
                    display_path = change.path
                print(f"{change.action}: {display_path}")
    
        if arguments.dry_run:
            print(
                f"Dry run: {len(changes)} file(s) would change "
                f"({inserted} inserted, {updated} updated); {unchanged} already current."
            )
    ✓ • 0ms

## Activity

    $ python3 -B scripts/distribute_guideline_table.py --link '[External mapping](/references/example)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/12.mitre-cwe-211.md --content-root content/4.sei-cert-c-coding-standard --dry-run
        python3 -B scripts/distribute_guideline_table.py --link '[External standard](/references/example)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --content-root content/4.sei-cert-c-coding-standard --source-table-index 2 --dry-run 2>&1 | sed -n '1,5p'
    Dry run: 61 file(s) would change (61 inserted, 0 updated); 0 already current.
    error: Requested source table 2 in /host/content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md, but only 1 table(s) were found
    ✓ • 192ms

## Activity

    $ python3 -B scripts/distribute_guideline_table.py --link '[External mapping](/references/example)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/12.mitre-cwe-211.md --content-root /tmp/distribute-table.sIFH8t/content-root --url-prefix /sei-cert-c-coding-standard
        python3 -B scripts/distribute_guideline_table.py --link '[External mapping](/references/example)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/12.mitre-cwe-211.md --content-root /tmp/distribute-table.sIFH8t/content-root --url-prefix /sei-cert-c-coding-standard --dry-run
        rg -n '^\| \[External mapping\]' /tmp/distribute-table.sIFH8t/content-root/03.rules/03.arrays-arr/6.arr38-c.md | head -20
    Processed 124 source row(s) across 61 destination file(s): 61 inserted, 0 updated, 0 already current.
    Dry run: 0 file(s) would change (0 inserted, 0 updated); 61 already current.
    457:| [External mapping](/references/example) | [CWE-119](https://cwe.mitre.org/data/definitions/119.html) [,](https://cwe.mitre.org/data/definitions/121.html) Improper Restriction of Operations within the Bounds of a Memory Buffer |
    458:| [External mapping](/references/example) | [CWE-121](https://cwe.mitre.org/data/definitions/121.html) , Stack-based Buffer Overflow |
    459:| [External mapping](/references/example) | [CWE-123](https://cwe.mitre.org/data/definitions/123.html) , Write-what-where Condition |
    460:| [External mapping](/references/example) | [CWE-125](https://cwe.mitre.org/data/definitions/125.html) , Out-of-bounds Read |
    461:| [External mapping](/references/example) | [CWE-805](https://cwe.mitre.org/data/definitions/805.html) , Buffer Access with Incorrect Length Value |
    ✓ • 279ms

## Activity

    $ rm -r /tmp/distribute-table.sIFH8t
        python3 -B scripts/distribute_guideline_table.py --link '[External standard](/references/example)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --content-root content/4.sei-cert-c-coding-standard --dry-run
        rg -n -i 'misra|cert' scripts/distribute_guideline_table.py || true
        rg -n '[[:blank:]]+$' scripts/distribute_guideline_table.py || true
        git diff --check -- scripts/distribute_guideline_table.py
        git status --short -- scripts/distribute_guideline_table.py content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations
    Dry run: 121 file(s) would change (121 inserted, 0 updated); 0 already current.
    AM scripts/distribute_guideline_table.py
    ✓ • 504ms

## Assistant

Generalized [distribute_guideline_table.py](/host/scripts/distribute_guideline_table.py).

Changes include:

- Renamed `--misra-link` to generic `--link`.
- Added required `--content-root`.
- Removed all MISRA and CERT-specific parsing and text.
- Resolves arbitrary internal Markdown links to numbered content files.
- Supports `--source-table-index` for files containing multiple tables.
- Supports configurable `--target-section` and `--target-table-header`.
- Supports multiple source rows targeting the same page.
- Preserves duplicate-removal and idempotent rerun behavior.

Validated successfully against two different source tables, including one with 124 rows mapping to 61 destination files. No content files were modified.

## User

What is the --content-root directory supposed to be?

## Assistant

`--content-root` is the local directory corresponding to the root of the website section containing the destination pages.

For this task, use:

```bash
--content-root content/4.sei-cert-c-coding-standard
```

The script recursively indexes Markdown files beneath that directory and maps URLs such as:

```text
/sei-cert-c-coding-standard/rules/arrays-arr/arr30-c
```

to numbered source files such as:

```text
content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/2.arr30-c.md
```

The complete invocation is:

```bash
python3 scripts/distribute_guideline_table.py \
  --link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' \
  --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md \
  --content-root content/4.sei-cert-c-coding-standard \
  --dry-run
```

For this directory, `--url-prefix` is inferred automatically as `/sei-cert-c-coding-standard`.

## User

There are many files with a table entry that looks like this:

|                                                   |                                                                                                                                                                      |                                                     |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| Taxonomy                                          | Taxonomy item                                                                                                                                                        | Relationship                                        |

I need them to look like this:

| Taxonomy | Taxonomy item | Relationship |
|----------+---------------+--------------|


Can you generate a script (python or perl) to do this?)

## Assistant

I’ll inspect the actual variants first, then add a narrowly scoped script that rewrites only this three-line taxonomy-table header pattern and supports a dry run. I’ll preserve all following table rows unchanged.

## Activity

    $ rg -n -U '^\|[[:blank:]]*\|[[:blank:]]*\|[[:blank:]]*\|\r?\n\|[-:|[:blank:]]+\|\r?\n\|[[:blank:]]*Taxonomy[[:blank:]]*\|[[:blank:]]*Taxonomy item[[:blank:]]*\|[[:blank:]]*Relationship[[:blank:]]*\|' content scripts | head -120
        rg -l '^\|[[:blank:]]*Taxonomy[[:blank:]]*\|[[:blank:]]*Taxonomy item[[:blank:]]*\|[[:blank:]]*Relationship[[:blank:]]*\|' content | wc -l
        rg -n '^\|[[:blank:]]*Taxonomy[[:blank:]]*\|[[:blank:]]*Taxonomy item[[:blank:]]*\|[[:blank:]]*Relationship[[:blank:]]*\|' content | head -40
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/4.arr02-c.md:114:|                                                                                                 |                                                                                                                                                                                                                                              |                                                     |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/4.arr02-c.md:115:|-------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/4.arr02-c.md:116:| Taxonomy                                                                                        | Taxonomy item                                                                                                                                                                                                                                | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/2.arr00-c.md:115:|                                                   |                                                                                                                                                                            |                                                     |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/2.arr00-c.md:116:|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/2.arr00-c.md:117:| Taxonomy                                          | Taxonomy item                                                                                                                                                              | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/3.arr01-c.md:142:|                                                                                                            |                                                                                                                                                                                                                                              |                                                     |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/3.arr01-c.md:143:|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/3.arr01-c.md:144:| Taxonomy                                                                                                   | Taxonomy item                                                                                                                                                                                                                                | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/05.concurrency-con/06.con05-c.md:132:|                                                                                           |                                                                                                                                               |                                                     |
    content/4.sei-cert-c-coding-standard/08.recommendations/05.concurrency-con/06.con05-c.md:133:|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/08.recommendations/05.concurrency-con/06.con05-c.md:134:| Taxonomy                                                                                  | Taxonomy item                                                                                                                                 | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/05.concurrency-con/07.con06-c.md:126:|                                                   |                                                                              |                            |
    content/4.sei-cert-c-coding-standard/08.recommendations/05.concurrency-con/07.con06-c.md:127:|---------------------------------------------------|------------------------------------------------------------------------------|----------------------------|
    content/4.sei-cert-c-coding-standard/08.recommendations/05.concurrency-con/07.con06-c.md:128:| Taxonomy                                          | Taxonomy item                                                                | Relationship               |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md:111:|                                                   |                                                                                                                                                                      |                                                     |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md:112:|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md:113:| Taxonomy                                          | Taxonomy item                                                                                                                                                        | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/08.api07-c.md:78:|                                                                                                                      |                                                          |                                                     |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/08.api07-c.md:79:|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/08.api07-c.md:80:| Taxonomy                                                                                                             | Taxonomy item                                            | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/3.mem31-c.md:134:|                                                                                                                      |                                                                                                                                       |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/3.mem31-c.md:135:|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/3.mem31-c.md:136:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                         | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/5.mem34-c.md:189:|                                                                                                            |                                                                                                                                       |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/5.mem34-c.md:190:|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/5.mem34-c.md:191:| Taxonomy                                                                                                   | Taxonomy item                                                                                                                         | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/05.fio37-c.md:110:|                                                               |                                                                                                                                                                |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/05.fio37-c.md:111:|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/05.fio37-c.md:112:| Taxonomy                                                      | Taxonomy item                                                                                                                                                  | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/4.flp34-c.md:177:|                                                                                                                      |                                                                                                                                                                                                         |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/4.flp34-c.md:178:|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/4.flp34-c.md:179:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                                           | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/4.mem33-c.md:258:|                                                               |                                                                                                                                                         |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/4.mem33-c.md:259:|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/4.mem33-c.md:260:| Taxonomy                                                      | Taxonomy item                                                                                                                                           | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/06.fio38-c.md:96:|                                                                                                                 |                                                |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/06.fio38-c.md:97:|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/06.fio38-c.md:98:| Taxonomy                                                                                                        | Taxonomy item                                  | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/3.flp32-c.md:389:|                                                               |                                                                                                                            |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/3.flp32-c.md:390:|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/3.flp32-c.md:391:| Taxonomy                                                      | Taxonomy item                                                                                                              | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/2.flp30-c.md:127:|                                                                                                                      |                                                                                                                                                                               |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/2.flp30-c.md:128:|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/2.flp30-c.md:129:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                 | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/02.fio30-c.md:195:|                                                                                                                      |                                                                                                                                                                   |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/02.fio30-c.md:196:|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/02.fio30-c.md:197:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                     | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/5.flp36-c.md:103:|                                                                                           |                                                                                                                                                                                   |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/5.flp36-c.md:104:|-------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/5.flp36-c.md:105:| Taxonomy                                                                                  | Taxonomy item                                                                                                                                                                     | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/10.exp40-c.md:100:|                                                               |                                                                                                                           |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/10.exp40-c.md:101:|---------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/10.exp40-c.md:102:| Taxonomy                                                      | Taxonomy item                                                                                                             | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/5.msc37-c.md:234:|                                                               |                                                                                                                   |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/5.msc37-c.md:235:|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/5.msc37-c.md:236:| Taxonomy                                                      | Taxonomy item                                                                                                     | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/14.fio47-c.md:151:|                                                                                                                 |                                                                                                                                                              |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/14.fio47-c.md:152:|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/14.fio47-c.md:153:| Taxonomy                                                                                                        | Taxonomy item                                                                                                                                                | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/2.mem30-c.md:264:|                                                                                                                      |                                                                                                                                              |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/2.mem30-c.md:265:|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/2.mem30-c.md:266:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/14.exp45-c.md:270:|                                                                                                                      |                                                                                                                                                                                            |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/14.exp45-c.md:271:|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/14.exp45-c.md:272:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                              | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/5.err34-c.md:158:|                                                   |                                                                                                                                                                                                                                          |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/5.err34-c.md:159:|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/5.err34-c.md:160:| Taxonomy                                          | Taxonomy item                                                                                                                                                                                                                            | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/03.fio32-c.md:270:|                                                                                           |                                                                                                                                                  |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/03.fio32-c.md:271:|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/03.fio32-c.md:272:| Taxonomy                                                                                  | Taxonomy item                                                                                                                                    | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/02.dcl30-c.md:204:|                                                                                                                      |                                                                                                                             |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/02.dcl30-c.md:205:|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/02.dcl30-c.md:206:| Taxonomy                                                                                                             | Taxonomy item                                                                                                               | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/6.msc38-c.md:116:|                                        |                                                                                                                                          |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/6.msc38-c.md:117:|----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/6.msc38-c.md:118:| Taxonomy                               | Taxonomy item                                                                                                                            | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/15.exp46-c.md:69:|                                                                                                                      |                                                                                       |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/15.exp46-c.md:70:|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/15.exp46-c.md:71:| Taxonomy                                                                                                             | Taxonomy item                                                                         | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/07.environment-env/5.env33-c.md:297:|                                                                                                                      |                                                                                                                                                                                                            |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/07.environment-env/5.env33-c.md:298:|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/07.environment-env/5.env33-c.md:299:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                                              | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/4.err33-c.md:610:|                                                                                                                 |                                                                                                                                                                                                                                                                     |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/4.err33-c.md:611:|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/4.err33-c.md:612:| Taxonomy                                                                                                        | Taxonomy item                                                                                                                                                                                                                                                       | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/3.msc32-c.md:162:|                                                               |                                                                                                                                            |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/3.msc32-c.md:163:|---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/3.msc32-c.md:164:| Taxonomy                                                      | Taxonomy item                                                                                                                              | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/04.fio34-c.md:210:|                                                                                                                 |                                                                                                                                                                      |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/04.fio34-c.md:211:|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/04.fio34-c.md:212:| Taxonomy                                                                                                        | Taxonomy item                                                                                                                                                        | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/4.msc33-c.md:117:|                                                               |                                                                                                                                  |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/4.msc33-c.md:118:|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/4.msc33-c.md:119:| Taxonomy                                                      | Taxonomy item                                                                                                                    | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/2.msc30-c.md:162:|                                                                                           |                                                                                                                                                                                                              |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/2.msc30-c.md:163:|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/2.msc30-c.md:164:| Taxonomy                                                                                  | Taxonomy item                                                                                                                                                                                                | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/08.dcl40-c.md:255:|                                                                                                            |                                                                         |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/08.dcl40-c.md:256:|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/08.dcl40-c.md:257:| Taxonomy                                                                                                   | Taxonomy item                                                           | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/05.exp34-c.md:245:|                                                                                                                      |                                                                                                                                             |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/05.exp34-c.md:246:|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/05.exp34-c.md:247:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                               | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/07.environment-env/2.env30-c.md:235:|                                                                                                                 |                                                                                                                                                |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/07.environment-env/2.env30-c.md:236:|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/07.environment-env/2.env30-c.md:237:| Taxonomy                                                                                                        | Taxonomy item                                                                                                                                  | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/07.environment-env/4.env32-c.md:181:|                                                                                                                      |                                                                                                                                |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/07.environment-env/4.env32-c.md:182:|----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/07.environment-env/4.env32-c.md:183:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                  | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/3.err32-c.md:221:|                                                                                               |                                                                                                                                |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/3.err32-c.md:222:|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/3.err32-c.md:223:| Taxonomy                                                                                      | Taxonomy item                                                                                                                  | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/2.err30-c.md:284:|                                                                                                                 |                                                                                                                            |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/2.err30-c.md:285:|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/2.err30-c.md:286:| Taxonomy                                                                                                        | Taxonomy item                                                                                                              | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/11.exp42-c.md:143:|                                                                                                            |                                                                                                                                                                                       |                                                     |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/11.exp42-c.md:144:|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/11.exp42-c.md:145:| Taxonomy                                                                                                   | Taxonomy item                                                                                                                                                                         | Relationship                                        |
    98
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/05.fio37-c.md:112:| Taxonomy                                                      | Taxonomy item                                                                                                                                                  | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/06.fio38-c.md:98:| Taxonomy                                                                                                        | Taxonomy item                                  | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/02.fio30-c.md:197:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                     | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/14.fio47-c.md:153:| Taxonomy                                                                                                        | Taxonomy item                                                                                                                                                | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/03.fio32-c.md:272:| Taxonomy                                                                                  | Taxonomy item                                                                                                                                    | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/04.fio34-c.md:212:| Taxonomy                                                                                                        | Taxonomy item                                                                                                                                                        | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/4.arr02-c.md:116:| Taxonomy                                                                                        | Taxonomy item                                                                                                                                                                                                                                | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/10.fio42-c.md:229:| Taxonomy | Taxonomy item | Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/2.arr00-c.md:117:| Taxonomy                                          | Taxonomy item                                                                                                                                                              | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/3.arr01-c.md:144:| Taxonomy                                                                                                   | Taxonomy item                                                                                                                                                                                                                                | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/11.fio44-c.md:120:| Taxonomy                                                                                                        | Taxonomy item                                                                   | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/07.fio39-c.md:144:| Taxonomy                                                                                                        | Taxonomy item                                                                                                                                                               | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/05.api03-c.md:89:| Taxonomy | Taxonomy item | Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/09.fio41-c.md:165:| Taxonomy                                                      | Taxonomy item                                                                                                                   | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/3.mem31-c.md:136:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                         | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/5.mem34-c.md:191:| Taxonomy                                                                                                   | Taxonomy item                                                                                                                         | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/4.flp34-c.md:179:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                                           | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/04.characters-and-strings-str/3.str31-c.md:539:| Taxonomy | Taxonomy item | Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/4.mem33-c.md:260:| Taxonomy                                                      | Taxonomy item                                                                                                                                           | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/3.flp32-c.md:391:| Taxonomy                                                      | Taxonomy item                                                                                                              | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/06.api04-c.md:79:| Taxonomy | Taxonomy item | Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/05.concurrency-con/06.con05-c.md:134:| Taxonomy                                                                                  | Taxonomy item                                                                                                                                 | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/2.flp30-c.md:129:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                 | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/6.mem35-c.md:181:| Taxonomy | Taxonomy item | Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/08.api07-c.md:80:| Taxonomy                                                                                                             | Taxonomy item                                            | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/04.characters-and-strings-str/6.str37-c.md:116:| Taxonomy                                                                                                   | Taxonomy item                                                                                                                                               | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/5.flp36-c.md:105:| Taxonomy                                                                                  | Taxonomy item                                                                                                                                                                     | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md:113:| Taxonomy                                          | Taxonomy item                                                                                                                                                        | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/04.characters-and-strings-str/4.str32-c.md:245:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                       | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/2.mem30-c.md:266:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/04.characters-and-strings-str/2.str30-c.md:180:| Taxonomy                                                                                                        | Taxonomy item                                                                                                                                                              | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/05.concurrency-con/07.con06-c.md:128:| Taxonomy                                          | Taxonomy item                                                                | Relationship               |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/3.arr32-c.md:189:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                     | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/6.arr38-c.md:468:| Taxonomy | Taxonomy item | Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/3.msc32-c.md:164:| Taxonomy                                                      | Taxonomy item                                                                                                                              | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/2.msc30-c.md:164:| Taxonomy                                                                                  | Taxonomy item                                                                                                                                                                                                | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/2.arr30-c.md:428:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                       | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/15.miscellaneous-msc/5.msc37-c.md:236:| Taxonomy                                                      | Taxonomy item                                                                                                     | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/06.declarations-and-initialization-dcl/02.dcl30-c.md:206:| Taxonomy                                                                                                             | Taxonomy item                                                                                                               | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/4.arr36-c.md:105:| Taxonomy                                                                                                   | Taxonomy item                                                                                                                                | Relationship                                        |
    ✓ • 11.01s

## Activity

    $ printf 'taxonomy_header_files='; rg -l '^\|[[:blank:]]*Taxonomy[[:blank:]]*\|[[:blank:]]*Taxonomy item[[:blank:]]*\|[[:blank:]]*Relationship[[:blank:]]*\|' content | wc -l
        printf 'exact_three_line_patterns='; rg -l -U '^\|[[:blank:]]*\|[[:blank:]]*\|[[:blank:]]*\|\r?\n\|[[:blank:]]*:?-{3,}:?[[:blank:]]*\|[[:blank:]]*:?-{3,}:?[[:blank:]]*\|[[:blank:]]*:?-{3,}:?[[:blank:]]*\|\r?\n\|[[:blank:]]*Taxonomy[[:blank:]]*\|[[:blank:]]*Taxonomy item[[:blank:]]*\|[[:blank:]]*Relationship[[:blank:]]*\|' content | wc -l
        printf 'already_target='; rg -l -U '^\| Taxonomy \| Taxonomy item \| Relationship \|\r?\n\|----------\+---------------\+--------------\|' content | wc -l
        rg -n '^\|[[:blank:]]*Taxonomy[[:blank:]]*\|[[:blank:]]*Taxonomy item[[:blank:]]*\|[[:blank:]]*Relationship[[:blank:]]*\|' content | tail -20
    98
    exact_three_line_patterns=89
    already_target=0
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/07.exp36-c.md:255:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                                        | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/13.exp44-c.md:232:| Taxonomy                                 | Taxonomy item                                                                                                                   | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/6.int34-c.md:227:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                          | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/5.int33-c.md:155:| Taxonomy                                                                                                   | Taxonomy item                                                                                                                                                                             | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/03.exp32-c.md:117:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                 | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/16.posix-pos/05.pos36-c.md:175:| Taxonomy                                                                                                        | Taxonomy item                                               | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/4.int32-c.md:512:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                                          | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/09.exp39-c.md:287:| Taxonomy                                                                                                   | Taxonomy item                                                                                                                       | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/08.exp37-c.md:255:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                        | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/8.int36-c.md:221:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                                                                  | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/16.posix-pos/15.pos52-c.md:173:| Taxonomy                                             | Taxonomy item                                                                                                                                 | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/09.expressions-exp/02.exp30-c.md:266:| Taxonomy                                                                                                             | Taxonomy item                                                                                                                                                                   | Relationship                                                                                                                   |
    content/4.sei-cert-c-coding-standard/03.rules/16.posix-pos/17.pos54-c.md:136:| Taxonomy | Taxonomy item | Relationship |
    content/4.sei-cert-c-coding-standard/03.rules/16.posix-pos/06.pos37-c.md:255:| Taxonomy                                                                                                        | Taxonomy item                                                                                                             | Relationship                                        |
    content/4.sei-cert-c-coding-standard/03.rules/16.posix-pos/02.pos30-c.md:113:| Taxonomy                                          | Taxonomy item                                                                         | Relationship                         |
    content/4.sei-cert-c-coding-standard/03.rules/16.posix-pos/11.pos48-c.md:106:| Taxonomy                                          | Taxonomy item                                                                    | Relationship                         |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/05.api03-c.md:89:| Taxonomy | Taxonomy item | Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/06.api04-c.md:79:| Taxonomy | Taxonomy item | Relationship |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/08.api07-c.md:80:| Taxonomy                                                                                                             | Taxonomy item                                            | Relationship                                        |
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md:113:| Taxonomy                                          | Taxonomy item                                                                                                                                                        | Relationship                                        |
    ✓ • 2.56s

## Activity

    $ comm -23 <(rg -l '^\|[[:blank:]]*Taxonomy[[:blank:]]*\|[[:blank:]]*Taxonomy item[[:blank:]]*\|[[:blank:]]*Relationship[[:blank:]]*\|' content | sort) <(rg -l -U '^\|[[:blank:]]*\|[[:blank:]]*\|[[:blank:]]*\|\r?\n\|[[:blank:]]*:?-{3,}:?[[:blank:]]*\|[[:blank:]]*:?-{3,}:?[[:blank:]]*\|[[:blank:]]*:?-{3,}:?[[:blank:]]*\|\r?\n\|[[:blank:]]*Taxonomy[[:blank:]]*\|[[:blank:]]*Taxonomy item[[:blank:]]*\|[[:blank:]]*Relationship[[:blank:]]*\|' content | sort)
    content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/6.arr38-c.md
    content/4.sei-cert-c-coding-standard/03.rules/04.characters-and-strings-str/3.str31-c.md
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/10.fio42-c.md
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/7.int35-c.md
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/6.mem35-c.md
    content/4.sei-cert-c-coding-standard/03.rules/16.posix-pos/17.pos54-c.md
    content/4.sei-cert-c-coding-standard/03.rules/18.signals-sig/3.sig31-c.md
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/05.api03-c.md
    content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/06.api04-c.md
    ✓ • 1.00s

## Activity

    $ for f in content/4.sei-cert-c-coding-standard/03.rules/03.arrays-arr/6.arr38-c.md content/4.sei-cert-c-coding-standard/03.rules/04.characters-and-strings-str/3.str31-c.md content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/10.fio42-c.md content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/7.int35-c.md content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/6.mem35-c.md content/4.sei-cert-c-coding-standard/03.rules/16.posix-pos/17.pos54-c.md content/4.sei-cert-c-coding-standard/03.rules/18.signals-sig/3.sig31-c.md content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/05.api03-c.md content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/06.api04-c.md; do rg -n -B3 -A3 '^\|[[:blank:]]*Taxonomy[[:blank:]]*\|' "$f"; done
    86-
    87-[Key here](/sei-cert-c-coding-standard/front-matter/introduction/how-this-coding-standard-is-organized#HowthisCodingStandardisOrganized-RelatedGuidelines) (explains table format and definitions)
    88-
    89:| Taxonomy | Taxonomy item | Relationship |
    90-| --- | --- | --- |
    91-| [ISO/IEC 9945:2003](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO-IEC9945-2003) | <br> | Prior to 2018-01-12: CERT: Unspecified Relationship |
    92-| [ISO/IEC 23360-1:2006](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO-IEC23360-1-2006) | <br> | Prior to 2018-01-12: CERT: Unspecified Relationship |
    76-
    77-[Key here](/sei-cert-c-coding-standard/front-matter/introduction/how-this-coding-standard-is-organized#HowthisCodingStandardisOrganized-RelatedGuidelines) (explains table format and definitions)
    78-
    79:| Taxonomy | Taxonomy item | Relationship |
    80-| --- | --- | --- |
    81-| [ISO/IEC 9945:2003](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO-IEC9945-2003) | <br> | Prior to 2018-01-12: CERT: Unspecified Relationship |
    82-| [ISO/IEC 23360-1:2006](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-ISO-IEC23360-1-2006) | <br> | Prior to 2018-01-12: CERT: Unspecified Relationship |
    ✓ • 27ms

## User

There are many files with a table entry that looks like this:

|                                                   |                                                                                                                                                                      |                                                     |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| Taxonomy                                          | Taxonomy item                                                                                                                                                        | Relationship                                        |

I need them to look like this:

| Taxonomy | Taxonomy item | Relationship |
|----------|---------------|--------------|

## Assistant

I’ll generate a narrowly scoped script that replaces only the three-line padded taxonomy header with the two compact Markdown header lines shown here, while leaving all table data rows untouched. It will support recursive paths and a dry-run mode.

## Activity

    file changes: Completed · 1 changes
    Add: /host/scripts/normalize_taxonomy_table_headers.py
    #!/usr/bin/env python3
    """Replace padded taxonomy table headers with compact Markdown headers.
    
    The script recognizes this three-line shape, regardless of column widths:
    
        |       |               |              |
        |-------|---------------|--------------|
        | Taxonomy | Taxonomy item | Relationship |
    
    It replaces those lines with:
    
        | Taxonomy | Taxonomy item | Relationship |
        |----------|---------------|--------------|
    
    All subsequent table rows are left unchanged.
    """
    
    from __future__ import annotations
    
    import argparse
    import os
    import re
    import stat
    import sys
    import tempfile
    from dataclasses import dataclass
    from pathlib import Path
    from typing import Iterable, List, Optional, Sequence
    
    
    REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
    DEFAULT_PATH = REPOSITORY_ROOT / "content"
    
    TAXONOMY_HEADER_PATTERN = re.compile(
        r"^\|[ \t]*\|[ \t]*\|[ \t]*\|[ \t]*(?P<newline>\r?\n)"
        r"\|[ \t]*:?-{3,}:?[ \t]*"
        r"\|[ \t]*:?-{3,}:?[ \t]*"
        r"\|[ \t]*:?-{3,}:?[ \t]*\|[ \t]*(?P=newline)"
        r"\|[ \t]*Taxonomy[ \t]*"
        r"\|[ \t]*Taxonomy item[ \t]*"
        r"\|[ \t]*Relationship[ \t]*\|[ \t]*(?P<ending>\r?\n|$)",
        re.MULTILINE,
    )
    
    COMPACT_HEADER = "| Taxonomy | Taxonomy item | Relationship |"
    COMPACT_SEPARATOR = "|----------|---------------|--------------|"
    
    
    class NormalizationError(Exception):
        """Raised when an input path cannot be processed safely."""
    
    
    @dataclass(frozen=True)
    class PlannedChange:
        path: Path
        updated: str
        replacements: int
    
    
    def read_utf8(path: Path) -> str:
        try:
            return path.read_bytes().decode("utf-8")
        except FileNotFoundError as error:
            raise NormalizationError(f"File does not exist: {path}") from error
        except UnicodeDecodeError as error:
            raise NormalizationError(f"File is not valid UTF-8: {path}") from error
    
    
    def replacement(match: re.Match[str]) -> str:
        newline = match.group("newline")
        ending = match.group("ending")
        return COMPACT_HEADER + newline + COMPACT_SEPARATOR + ending
    
    
    def normalize(text: str) -> tuple[str, int]:
        return TAXONOMY_HEADER_PATTERN.subn(replacement, text)
    
    
    def markdown_files(paths: Iterable[Path]) -> List[Path]:
        files = set()
    
        for path in paths:
            if not path.exists():
                raise NormalizationError(f"Path does not exist: {path}")
            if path.is_dir():
                files.update(candidate for candidate in path.rglob("*.md") if candidate.is_file())
            elif path.is_file() and path.suffix.lower() == ".md":
                files.add(path)
            else:
                raise NormalizationError(f"Expected a Markdown file or directory: {path}")
    
        return sorted(files)
    
    
    def plan_changes(paths: Iterable[Path]) -> List[PlannedChange]:
        changes: List[PlannedChange] = []
    
        for path in markdown_files(paths):
            original = read_utf8(path)
            updated, replacements = normalize(original)
            if replacements:
                changes.append(
                    PlannedChange(
                        path=path,
                        updated=updated,
                        replacements=replacements,
                    )
                )
    
        return changes
    
    
    def write_atomic(change: PlannedChange) -> None:
        mode = stat.S_IMODE(change.path.stat().st_mode)
        temporary_name: Optional[str] = None
    
        try:
            with tempfile.NamedTemporaryFile(
                mode="wb",
                prefix=f".{change.path.name}.",
                dir=change.path.parent,
                delete=False,
            ) as temporary:
                temporary_name = temporary.name
                temporary.write(change.updated.encode("utf-8"))
                temporary.flush()
                os.fsync(temporary.fileno())
    
            os.chmod(temporary_name, mode)
            os.replace(temporary_name, change.path)
            temporary_name = None
        finally:
            if temporary_name is not None:
                try:
                    os.unlink(temporary_name)
                except FileNotFoundError:
                    pass
    
    
    def path_argument(value: str) -> Path:
        return Path(value).expanduser().resolve()
    
    
    def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description=(
                "Replace padded three-line taxonomy table headers with compact "
                "two-line Markdown headers."
            )
        )
        parser.add_argument(
            "paths",
            nargs="*",
            type=path_argument,
            help=f"Markdown files or directories (default: {DEFAULT_PATH})",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="report matching files without modifying them",
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="list every matching file",
        )
        return parser.parse_args(argv)
    
    
    def display_path(path: Path) -> Path:
        try:
            return path.relative_to(REPOSITORY_ROOT)
        except ValueError:
            return path
    
    
    def main(argv: Optional[Sequence[str]] = None) -> int:
        arguments = parse_arguments(argv)
        paths = arguments.paths or [DEFAULT_PATH]
    
        try:
            changes = plan_changes(paths)
        except (NormalizationError, OSError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 1
    
        if arguments.verbose:
            for change in changes:
                print(f"{change.replacements}: {display_path(change.path)}")
    
        replacement_count = sum(change.replacements for change in changes)
        if arguments.dry_run:
            print(
                f"Dry run: {replacement_count} header(s) in "
                f"{len(changes)} file(s) would change."
            )
            return 0
    
        try:
            for change in changes:
                write_atomic(change)
        except OSError as error:
            print(f"error while writing {change.path}: {error}", file=sys.stderr)
            return 1
    
        print(
            f"Replaced {replacement_count} header(s) in {len(changes)} file(s)."
        )
        return 0
    
    
    if __name__ == "__main__":
        raise SystemExit(main())

## Activity

    $ chmod 755 scripts/normalize_taxonomy_table_headers.py
        python3 -B scripts/normalize_taxonomy_table_headers.py --dry-run
        python3 -B scripts/normalize_taxonomy_table_headers.py --help
        rg -n '[[:blank:]]+$' scripts/normalize_taxonomy_table_headers.py || true
        git diff --check -- scripts/normalize_taxonomy_table_headers.py
        git status --short -- scripts/normalize_taxonomy_table_headers.py content
    Dry run: 89 header(s) in 89 file(s) would change.
    usage: normalize_taxonomy_table_headers.py [-h] [--dry-run] [--verbose]
                                               [paths ...]
    
    Replace padded three-line taxonomy table headers with compact two-line
    Markdown headers.
    
    positional arguments:
      paths       Markdown files or directories (default: /host/content)
    
    options:
      -h, --help  show this help message and exit
      --dry-run   report matching files without modifying them
      --verbose   list every matching file
    ?? scripts/normalize_taxonomy_table_headers.py
    ✓ • 3.56s

## Assistant

The dry run found 89 matching headers across 89 files. I’m testing one real file in a temporary copy to confirm the replacement is exactly the two requested lines and that the first data row remains unchanged.

## Activity

    $ test_root=$(mktemp -d /tmp/taxonomy-header.XXXXXX)
        cp content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md "$test_root/api00-c.md"
        python3 -B scripts/normalize_taxonomy_table_headers.py "$test_root/api00-c.md"
        rg -n -A3 -B1 '^\| Taxonomy \| Taxonomy item \| Relationship \|$' "$test_root/api00-c.md"
        python3 -B scripts/normalize_taxonomy_table_headers.py "$test_root/api00-c.md" --dry-run
        printf '%s\n' "$test_root"
    Replaced 1 header(s) in 1 file(s).
    110-
    111:| Taxonomy | Taxonomy item | Relationship |
    112-|----------|---------------|--------------|
    113-| [CWE 2.11](https://cwe.mitre.org/data/index.html) | [CWE-20](https://cwe.mitre.org/data/definitions/20.html) , Insufficient input validation                                                                              | Prior to 2018-01-12: CERT:                          |
    114-| [MITRE CWE](https://cwe.mitre.org/)                | [CWE-476](https://cwe.mitre.org/data/definitions/476.html)                                                                                                             | Prior to 2018-01-12:                                |
    Dry run: 0 header(s) in 0 file(s) would change.
    /tmp/taxonomy-header.lc3j5S
    ✓ • 0ms

## Activity

    $ rm -r /tmp/taxonomy-header.lc3j5S
        python3 -B scripts/normalize_taxonomy_table_headers.py --dry-run
        git status --short -- scripts/normalize_taxonomy_table_headers.py content
    Dry run: 89 header(s) in 89 file(s) would change.
    ?? scripts/normalize_taxonomy_table_headers.py
    ✓ • 2.13s

## Assistant

Created [normalize_taxonomy_table_headers.py](/host/scripts/normalize_taxonomy_table_headers.py).

It found 89 matching headers in 89 files. No content files were modified.

Preview changes:

```bash
python3 scripts/normalize_taxonomy_table_headers.py --dry-run
```

Apply changes:

```bash
python3 scripts/normalize_taxonomy_table_headers.py
```

Use `--verbose` to list matching files. You can also pass specific files or directories as positional arguments.

## User

The script worked great, thanks!

My last task is for you to produce the inverse Python script. It should take a bunch of guidelines (perhaps passed as a glob expression of files), and a table header and cell name, and produce one single table of all the guidelines and their corresponding cell.

For example, if given suitable arguments, the script should reproduce the table in content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md.  (It doesn't have to modify any files...the table can go to standard output).  Please give me the command invocation to reproduce the misra-c-2025 table.

## Assistant

I’ll make the inverse generic: it will accept file paths or quoted glob patterns, locate a column by its table-header cell, find rows by a cell’s visible name (or exact Markdown), and emit one consolidated Markdown table. It will derive each guideline’s link from a required content root, with optional section and output-header controls.

## Activity

    file changes: Completed · 1 changes
    Add: /host/scripts/collect_guideline_table.py
    #!/usr/bin/env python3
    """Collect matching cells from Markdown pages into one table on stdout.
    
    Each input page is searched for a table containing ``--table-header``. Rows
    containing ``--cell-name`` are collected, and the cell under the requested
    header is paired with a link back to the input page.
    
    Input arguments may be files, directories, or quoted glob expressions. Glob
    expressions support ``**`` recursion.
    """
    
    from __future__ import annotations
    
    import argparse
    import glob
    import re
    import sys
    from dataclasses import dataclass
    from pathlib import Path
    from typing import Iterable, List, Optional, Sequence, Tuple
    from urllib.parse import quote
    
    
    REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
    HEADING_RE = re.compile(r"^(?P<marks>#{1,6})\s+(?P<title>.*?)\s*$")
    MARKDOWN_LINK_RE = re.compile(
        r"^\[(?P<label>(?:\\.|[^\]])+)\]"
        r"\(\s*<?(?P<url>[^\s>)]+)>?(?:\s+['\"][^'\"]*['\"])?\s*\)$"
    )
    SEPARATOR_CELL_RE = re.compile(r"^:?-{3,}:?$")
    
    
    class CollectionError(Exception):
        """Raised when inputs cannot be collected without ambiguity."""
    
    
    @dataclass(frozen=True)
    class MarkdownTable:
        first_data_index: int
        end_index: int
        header_cells: Tuple[str, ...]
    
    
    @dataclass(frozen=True)
    class CollectedRow:
        guideline_label: str
        guideline_url: str
        value: str
        source_line: int
    
    
    def parse_markdown_row(line: str) -> Optional[Tuple[str, ...]]:
        """Return trimmed cells from a pipe-delimited Markdown row."""
    
        stripped = line.rstrip("\r\n").strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            return None
    
        body = stripped[1:-1]
        cells: List[str] = []
        current: List[str] = []
        backslash_run = 0
    
        for character in body:
            if character == "|" and backslash_run % 2 == 0:
                cells.append("".join(current).strip())
                current = []
            else:
                current.append(character)
    
            if character == "\\":
                backslash_run += 1
            else:
                backslash_run = 0
    
        cells.append("".join(current).strip())
        return tuple(cells)
    
    
    def is_separator_row(cells: Optional[Tuple[str, ...]]) -> bool:
        return bool(cells) and all(SEPARATOR_CELL_RE.fullmatch(cell) for cell in cells)
    
    
    def find_markdown_tables(
        lines: Sequence[str], start: int = 0, end: Optional[int] = None
    ) -> List[MarkdownTable]:
        if end is None:
            end = len(lines)
    
        tables: List[MarkdownTable] = []
        index = start
        while index + 1 < end:
            header = parse_markdown_row(lines[index])
            separator = parse_markdown_row(lines[index + 1])
            if (
                header is None
                or not is_separator_row(separator)
                or len(header) != len(separator)
            ):
                index += 1
                continue
    
            table_end = index + 2
            while table_end < end and parse_markdown_row(lines[table_end]) is not None:
                table_end += 1
    
            tables.append(
                MarkdownTable(
                    first_data_index=index + 2,
                    end_index=table_end,
                    header_cells=header,
                )
            )
            index = table_end
    
        return tables
    
    
    def read_utf8(path: Path) -> str:
        try:
            return path.read_bytes().decode("utf-8")
        except FileNotFoundError as error:
            raise CollectionError(f"File does not exist: {path}") from error
        except UnicodeDecodeError as error:
            raise CollectionError(f"File is not valid UTF-8: {path}") from error
    
    
    def unnumbered_name(name: str) -> str:
        return re.sub(r"^\d+\.", "", name)
    
    
    def normalize_url_prefix(value: str) -> str:
        value = value.strip()
        if not value.startswith("/"):
            raise argparse.ArgumentTypeError("must begin with '/'")
        return value.rstrip("/")
    
    
    def route_for_page(content_root: Path, path: Path, url_prefix: str) -> str:
        try:
            relative = path.relative_to(content_root)
        except ValueError as error:
            raise CollectionError(
                f"Input file is outside --content-root: {path}"
            ) from error
    
        components = [unnumbered_name(part) for part in relative.parts[:-1]]
        page_name = unnumbered_name(path.stem)
        if page_name != "index":
            components.append(page_name)
    
        encoded_suffix = "/".join(quote(component) for component in components)
        if not encoded_suffix:
            return url_prefix or "/"
        return f"{url_prefix}/{encoded_suffix}" if url_prefix else f"/{encoded_suffix}"
    
    
    def page_label(lines: Sequence[str], path: Path) -> str:
        """Use the leading identifier from the first H1, then fall back to the filename."""
    
        for line in lines:
            match = HEADING_RE.fullmatch(line.rstrip("\r\n"))
            if match is None or len(match.group("marks")) != 1:
                continue
            title = match.group("title").strip()
            if ". " in title:
                return title.split(". ", 1)[0].strip()
            if title:
                return title
    
        return unnumbered_name(path.stem)
    
    
    def find_section_bounds(
        lines: Sequence[str], title: Optional[str]
    ) -> Optional[Tuple[int, int]]:
        if title is None:
            return 0, len(lines)
    
        matches: List[Tuple[int, int]] = []
        for index, line in enumerate(lines):
            match = HEADING_RE.fullmatch(line.rstrip("\r\n"))
            if match is not None and match.group("title").strip() == title:
                matches.append((index, len(match.group("marks"))))
    
        if not matches:
            return None
        if len(matches) > 1:
            raise CollectionError(
                f"Found more than one section named {title!r} in one input file"
            )
    
        section_start, heading_level = matches[0]
        section_end = len(lines)
        for index in range(section_start + 1, len(lines)):
            match = HEADING_RE.fullmatch(lines[index].rstrip("\r\n"))
            if match is not None and len(match.group("marks")) <= heading_level:
                section_end = index
                break
        return section_start + 1, section_end
    
    
    def visible_cell_name(cell: str) -> str:
        match = MARKDOWN_LINK_RE.fullmatch(cell)
        return match.group("label") if match is not None else cell
    
    
    def cell_matches(cell: str, requested_name: str) -> bool:
        return cell == requested_name or visible_cell_name(cell) == requested_name
    
    
    def collect_from_file(
        path: Path,
        content_root: Path,
        url_prefix: str,
        section: Optional[str],
        table_header: str,
        cell_name: str,
    ) -> List[CollectedRow]:
        text = read_utf8(path)
        lines = text.splitlines(keepends=True)
        bounds = find_section_bounds(lines, section)
        if bounds is None:
            return []
    
        label = page_label(lines, path)
        url = route_for_page(content_root, path, url_prefix)
        collected: List[CollectedRow] = []
    
        for table in find_markdown_tables(lines, *bounds):
            matching_columns = [
                index
                for index, header in enumerate(table.header_cells)
                if header == table_header
            ]
            if not matching_columns:
                continue
            if len(matching_columns) > 1:
                raise CollectionError(
                    f"Header {table_header!r} occurs more than once in a table in {path}"
                )
    
            value_column = matching_columns[0]
            for line_index in range(table.first_data_index, table.end_index):
                cells = parse_markdown_row(lines[line_index])
                if cells is None or not any(
                    cell_matches(cell, cell_name) for cell in cells
                ):
                    continue
                if value_column >= len(cells):
                    raise CollectionError(
                        f"Matching row at {path}:{line_index + 1} has no cell under "
                        f"header {table_header!r}"
                    )
                collected.append(
                    CollectedRow(
                        guideline_label=label,
                        guideline_url=url,
                        value=cells[value_column],
                        source_line=line_index + 1,
                    )
                )
    
        return collected
    
    
    def expand_inputs(expressions: Iterable[str]) -> List[Path]:
        files = set()
    
        for expression in expressions:
            path = Path(expression).expanduser()
            if path.is_dir():
                files.update(candidate.resolve() for candidate in path.rglob("*.md"))
                continue
            if path.is_file():
                if path.suffix.lower() != ".md":
                    raise CollectionError(f"Expected a Markdown file: {path}")
                files.add(path.resolve())
                continue
    
            matches = [Path(match) for match in glob.glob(expression, recursive=True)]
            markdown_matches = [
                match.resolve()
                for match in matches
                if match.is_file() and match.suffix.lower() == ".md"
            ]
            if not markdown_matches:
                raise CollectionError(f"Input expression matched no Markdown files: {expression}")
            files.update(markdown_matches)
    
        return sorted(files)
    
    
    def escape_table_cell(value: str) -> str:
        """Preserve existing escapes while protecting unescaped table delimiters."""
    
        return re.sub(r"(?<!\\)\|", r"\\|", value)
    
    
    def render_table(
        rows: Sequence[CollectedRow], guideline_header: str, value_header: str
    ) -> str:
        guideline_header = escape_table_cell(guideline_header)
        value_header = escape_table_cell(value_header)
        first_width = max(3, len(guideline_header) + 2)
        second_width = max(3, len(value_header) + 2)
        lines = [
            f"| {guideline_header} | {value_header} |",
            f"|{'-' * first_width}|{'-' * second_width}|",
        ]
    
        for row in rows:
            guideline = f"[{row.guideline_label}]({row.guideline_url})"
            lines.append(
                f"| {escape_table_cell(guideline)} | {escape_table_cell(row.value)} |"
            )
        return "\n".join(lines) + "\n"
    
    
    def path_argument(value: str) -> Path:
        return Path(value).expanduser().resolve()
    
    
    def parse_arguments(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            description=(
                "Collect a named cell from Markdown tables across many linked pages "
                "and print one consolidated table."
            )
        )
        parser.add_argument(
            "inputs",
            nargs="+",
            help="Markdown files, directories, or quoted glob expressions",
        )
        parser.add_argument(
            "--content-root",
            required=True,
            type=path_argument,
            help="root directory used to derive links to input pages",
        )
        parser.add_argument(
            "--url-prefix",
            type=normalize_url_prefix,
            help=(
                "site-relative URL prefix for the content root; defaults to the "
                "content root directory name without a numeric ordering prefix"
            ),
        )
        parser.add_argument(
            "--section",
            help="only search tables within this Markdown section",
        )
        parser.add_argument(
            "--table-header",
            required=True,
            help="header of the column whose value should be collected",
        )
        parser.add_argument(
            "--cell-name",
            required=True,
            help="exact cell content or visible Markdown-link text identifying rows",
        )
        parser.add_argument(
            "--guideline-header",
            default="Guideline",
            help="first header in the generated table (default: Guideline)",
        )
        parser.add_argument(
            "--value-header",
            help="second generated header (default: value of --table-header)",
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="report collection counts to standard error",
        )
        return parser.parse_args(argv)
    
    
    def main(argv: Optional[Sequence[str]] = None) -> int:
        arguments = parse_arguments(argv)
        url_prefix = arguments.url_prefix
        if url_prefix is None:
            url_prefix = "/" + unnumbered_name(arguments.content_root.name)
    
        try:
            input_files = expand_inputs(arguments.inputs)
            rows: List[CollectedRow] = []
            for path in input_files:
                rows.extend(
                    collect_from_file(
                        path=path,
                        content_root=arguments.content_root,
                        url_prefix=url_prefix,
                        section=arguments.section,
                        table_header=arguments.table_header,
                        cell_name=arguments.cell_name,
                    )
                )
        except (CollectionError, OSError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 1
    
        if not rows:
            print("error: no matching rows found", file=sys.stderr)
            return 1
    
        rows.sort(
            key=lambda row: (
                row.guideline_label.casefold(),
                row.source_line,
                row.value.casefold(),
            )
        )
        value_header = arguments.value_header or arguments.table_header
        sys.stdout.write(render_table(rows, arguments.guideline_header, value_header))
    
        if arguments.verbose:
            print(
                f"Collected {len(rows)} row(s) from {len(input_files)} input file(s).",
                file=sys.stderr,
            )
        return 0
    
    
    if __name__ == "__main__":
        raise SystemExit(main())

## Activity

    $ chmod 755 scripts/collect_guideline_table.py
        python3 -B scripts/collect_guideline_table.py --help
        rg -n '[[:blank:]]+$' scripts/collect_guideline_table.py || true
        git diff --check -- scripts/collect_guideline_table.py
        git status --short -- scripts/collect_guideline_table.py content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations
    ?? scripts/collect_guideline_table.py
    ✓ • 232ms

## Assistant

The collector is in place. I’m now doing an end-to-end test in a temporary content copy: distribute the source table, collect it back using the `Version` column and `MISRA C:2025` row name, then verify the reconstructed table has all 121 entries in the expected order.

## Activity

    $ test_root=$(mktemp -d /tmp/collect-guideline-table.XXXXXX)
        cp -a content/4.sei-cert-c-coding-standard "$test_root/content-root"
        python3 -B scripts/distribute_guideline_table.py --link '[MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25)' --source content/4.sei-cert-c-coding-standard/04.back-matter/7.ff-related-guidelines/10.misra-c-2025.md --content-root "$test_root/content-root" --url-prefix /sei-cert-c-coding-standard
        python3 -B scripts/collect_guideline_table.py --content-root "$test_root/content-root" --url-prefix /sei-cert-c-coding-standard --section 'Automated Detection' --table-header 'Version' --cell-name 'MISRA C:2025' --guideline-header 'CERT Rule' --value-header 'Related Guidelines' "$test_root/content-root/03.rules/**/*.md" "$test_root/content-root/08.recommendations/**/*.md" | awk 'NR <= 5 { print } { last = $0 } END { print "..."; print last; print "line_count=" NR; print "data_rows=" NR - 2 }'
        printf '%s\n' "$test_root"
    Processed 121 source row(s) across 121 destination file(s): 0 inserted, 121 updated, 0 already current.
    | CERT Rule | Related Guidelines |
    |-----------|--------------------|
    | [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c) | Dir 4.11 |
    | [ARR01-C](/sei-cert-c-coding-standard/recommendations/arrays-arr/arr01-c) | Rule 12.5 |
    | [ARR30-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr30-c) | Rule 1.3, 18.1, 21.17, 21.18 |
    ...
    | [STR38-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str38-c) | Rule 1.3, 10.3 |
    line_count=123
    data_rows=121
    /tmp/collect-guideline-table.hxjQ6Y
    ✓ • 789ms

## Activity

    $ rm -r /tmp/collect-guideline-table.hxjQ6Y
        python3 -B scripts/collect_guideline_table.py --content-root content/4.sei-cert-c-coding-standard --section 'Automated Detection' --table-header 'Version' --cell-name 'MISRA C:2025' --guideline-header 'CERT Rule' --value-header 'Related Guidelines' 'content/4.sei-cert-c-coding-standard/03.rules/**/*.md' 'content/4.sei-cert-c-coding-standard/08.recommendations/**/*.md' | awk 'END { print "line_count=" NR; print "data_rows=" NR - 2 }'
        git status --short -- scripts/collect_guideline_table.py content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations | sed -n '1,160p'
    error: no matching rows found
    line_count=0
    data_rows=-2
    ?? scripts/collect_guideline_table.py
    ✓ • 465ms

## Activity

    $ rg -n '^\| \[MISRA C:2025\]' content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations | head -20
        rg -l '^\| \[MISRA C:2025\]' content/4.sei-cert-c-coding-standard/03.rules content/4.sei-cert-c-coding-standard/08.recommendations | wc -l
        rg -n -B3 -A3 '^\| \[MISRA C:2025\]' content/4.sei-cert-c-coding-standard/08.recommendations/02.application-programming-interfaces-api/02.api00-c.md
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/7.int35-c.md:157:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Dir 4.1, Rule 1.3 |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/13.fio46-c.md:88:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 22.6 |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/3.mem31-c.md:143:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 22.1 |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/05.fio37-c.md:115:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 21.6 |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/5.mem34-c.md:195:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 22.2 |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/3.int31-c.md:382:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 10.1, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 21.6, 21.13, 21.18 |
    content/4.sei-cert-c-coding-standard/08.recommendations/04.characters-and-strings-str/07.str05-c.md:122:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 7.4 |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/06.fio38-c.md:99:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 22.5 |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/4.mem33-c.md:261:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 18.7 |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/5.int33-c.md:159:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Dir 4.1, Rule 1.3 |
    content/4.sei-cert-c-coding-standard/08.recommendations/03.arrays-arr/3.arr01-c.md:148:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 12.5 |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/08.fio40-c.md:95:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 21.6 |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/6.mem35-c.md:192:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Dir 4.1, 4.12, Rule 1.3, 21.3 |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/4.int32-c.md:527:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Dir 4.1, Rule 1.3 |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/2.int30-c.md:335:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 12.4 |
    content/4.sei-cert-c-coding-standard/03.rules/08.error-handling-err/5.err34-c.md:162:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Dir 4.7, Rule 21.7 |
    content/4.sei-cert-c-coding-standard/03.rules/10.floating-point-flp/4.flp34-c.md:183:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 10.3, 10.4, 10.5, 10.8 |
    content/4.sei-cert-c-coding-standard/03.rules/11.input-output-fio/14.fio47-c.md:156:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 21.6 |
    content/4.sei-cert-c-coding-standard/03.rules/13.memory-management-mem/2.mem30-c.md:275:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Dir 4.12, Rule 1.3, 21.3, 22.2 |
    content/4.sei-cert-c-coding-standard/03.rules/12.integers-int/6.int34-c.md:233:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Rule 10.1, 12.2 |
    121
    112-|----------|---------------|--------------|
    113-| [CWE 2.11](https://cwe.mitre.org/data/index.html) | [CWE-20](https://cwe.mitre.org/data/definitions/20.html) , Insufficient input validation                                                                              | Prior to 2018-01-12: CERT:                          |
    114-| [MITRE CWE](https://cwe.mitre.org/)                | [CWE-476](https://cwe.mitre.org/data/definitions/476.html)                                                                                                             | Prior to 2018-01-12:                                |
    115:| [MISRA C:2025](/sei-cert-c-coding-standard/back-matter/aa-bibliography#AA.Bibliography-MISRA25) | Dir 4.11 |
    116-
    117-## Bibliography
    118-
    ✓ • 0ms

## Activity

    $ python3 -B scripts/collect_guideline_table.py --content-root content/4.sei-cert-c-coding-standard --section 'Related Guidelines' --table-header 'Taxonomy item' --cell-name 'MISRA C:2025' --guideline-header 'CERT Rule' --value-header 'Related Guidelines' 'content/4.sei-cert-c-coding-standard/03.rules/**/*.md' 'content/4.sei-cert-c-coding-standard/08.recommendations/**/*.md' | awk 'NR <= 5 { print } { last = $0 } END { print "..."; print last; print "line_count=" NR; print "data_rows=" NR - 2 }'
    | CERT Rule | Related Guidelines |
    |-----------|--------------------|
    | [API00-C](/sei-cert-c-coding-standard/recommendations/application-programming-interfaces-api/api00-c) | Dir 4.11 |
    | [ARR01-C](/sei-cert-c-coding-standard/recommendations/arrays-arr/arr01-c) | Rule 12.5 |
    | [ARR30-C](/sei-cert-c-coding-standard/rules/arrays-arr/arr30-c) | Rule 1.3, 18.1, 21.17, 21.18 |
    ...
    | [STR38-C](/sei-cert-c-coding-standard/rules/characters-and-strings-str/str38-c) | Rule 1.3, 10.3 |
    line_count=123
    data_rows=121
    ✓ • 253ms

## Activity

    $ rg -n '[[:blank:]]+$' scripts/collect_guideline_table.py || true
        git diff --check -- scripts/collect_guideline_table.py
        stat -c '%a %n' scripts/collect_guideline_table.py
        git status --short -- scripts/collect_guideline_table.py
    755 scripts/collect_guideline_table.py
    ?? scripts/collect_guideline_table.py
    ✓ • 0ms

## Assistant

Created [collect_guideline_table.py](/host/scripts/collect_guideline_table.py). It writes the consolidated Markdown table to standard output.

To reproduce the MISRA C:2025 table:

```bash
python3 scripts/collect_guideline_table.py \
  --content-root content/4.sei-cert-c-coding-standard \
  --section 'Related Guidelines' \
  --table-header 'Taxonomy item' \
  --cell-name 'MISRA C:2025' \
  --guideline-header 'CERT Rule' \
  --value-header 'Related Guidelines' \
  'content/4.sei-cert-c-coding-standard/03.rules/**/*.md' \
  'content/4.sei-cert-c-coding-standard/08.recommendations/**/*.md'
```

The quoted globs are expanded recursively by the script. I validated the command: it produces all 121 rows in the expected order.
