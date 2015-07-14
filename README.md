Shellcode Generator
---

Here is how one would create the shell code that launches python
```bash
python shellcode_gen.py "/usr/bin/python" > sh.s
source make.sh
./build/sh
```

Or of course bash, because why settle for sh
```bash
python shellcode_gen.py "/bin/bash" > sh.s
source make.sh
./build/sh
```


The build executable and source assembly file can be changed in make.sh

To Do
---
Add arguments to launched programs!
