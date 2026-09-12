| Probe | Canonical workflow | Inherited parser | Canonical execution |
|---|---|---|---|
| basic arithmetic | Accept | Accept | 42 |
| semicolon statements | Accept | Accept | 42 |
| comma-separated record | Accept | Accept | 42 |
| newline-separated record | Accept | Accept | 42 |
| space-separated record | Reject | Accept | Not executed |
| comma-separated array | Accept | Accept | 42 |
| space-separated array | Reject | Accept | Not executed |
| closure | Accept | Accept | 42 |
| canonical recovery | Accept | Accept | 42 |
| legacy recovery | Reject | Accept | Not executed |
| range operator | Reject | Accept | Not executed |
| bounded range helper | Accept | Accept | 3 |
| native array method | Accept | Accept | Rejected: method unavailable |
| bounded array helper | Accept | Accept | 42 |
| Makepad UI | Reject | Accept | Not executed |
| deferred tool syntax | Accept | Accept | Not executed |
| L0 card | Reject | Accept | Not executed |
