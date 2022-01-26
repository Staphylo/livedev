livedev
=======

## Purpose

When developing for remote devices, development can sometimes be tedious.
Especially when it involves editing code and configuration and testing them in
realtime.

Here are some of the reasons behind this project:
 - Lack of editor on the remote device (busybox / vi)
 - Lack of editor plugin since the device likely uses the default configuration
 - Multiple files to keep in sync with the remote
 - Work on your local repository, have changes automatically applied to the
   device

## Examples

Mirror single script to a remote device
```
livedev -p my-script:/usr/bin user@remote
```

Mirror entire folder to a remote device
```
livedev -p my-package:/usr/lib/python3/dist-packages/my-package user@remote
```

Mirror a script and a path to 2 remote devices and make sure current content on the
remote device is already current.
```
livedev --init \
    -p my-package:/usr/lib/python3/dist-packages/my-package \
    -p my-script:/usr/bin \
    user@remote1 \
    user@remote2
```
