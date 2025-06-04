Scripts: Tiny broad-ranging ephemeral macros

License: MIT

---

### Overview

Collection of broad-ranging macros that are used for ephemeral problems, which
occur commonly but do not need a seperate repository for each individual macro.

Ephemeral problems can occur weekly, monthly, yearly. This collection offers a
quick lookup for these scripts.

---

### Eeon

Return current time as a timestamp in selected formats.

```text
$ python eeon.py -h
usage: eeon.py [-h] [-f FORMATS] [-a] [-q] [-l]

options:
  -h, --help            show this help message and exit
  -f FORMATS, --formats FORMATS
                        selected formats
  -a, --all             spit out all timestamps
  -q, --quiet           suppress banner
  -l, --list            list available formats
```

```text
$ python eeon.py -qf unix,hfs+

Unix : 1735761280.0165586
HFS+ : -347083519.98344135
```

Based on [SANS](https://assets.contentstack.io/v3/assets/blt36c2e63521272fdc/bltd8ba96a0fce78883/Free_Faculty_Tools.pdf) epochalypse.py

---

### Permutate logins

Given a file with an initial and last name, permutate to create potential
usernames. Useful for bruteforcing logins using tools like MailSniper.ps1
with Invoke-DomainHarvestOWA.

```text
$ python permutate_logins.py < ./names & head -3 users

j.smith
J.Smith
John.Smith
```

---

### RTSP

Bruteforce list of potential RTSP endpoints and returns a valid full path. Using
Shodan, find IPs of cameras that are operating using RTSP and use this macro to
find the actual endpoint for watching live feed.

---

### Watch run

Interactively watches when a selected python file has a new timestamp and runs
it if it does. Great for allocating a tmux pane with this running, everytime you
save the file it automatically runs in that pane saving a little bit of pain ...
get it? haha.

```text
$ sh watch_run.sh

Usage: watch_run.sh <file-to-watch>
```
