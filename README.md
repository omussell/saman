# saman

Encrypt large files

At a previous workplace we were taking backups for databases and other things which would create large files. They would be created in a folder and many files would exist with some of them being tens of gigabytes. There's no problem with storing them or transferring them to S3 object storage for persistence. However, we didnt want to store them unencrypted. When using tools like GPG, they try to load the whole file into memory and then again as it encrypts it. The servers did not have two times the largest file size in RAM available. 

We created a Python program which would take the plaintext file and read through it X bytes at a time, encrypt that chunk only and then write it to disk. That meant the memory usage was kept low.

I was never happy with the quality of the code and this repo was/is an attempt at a rewrite.

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install saman
```

## License

`saman` is distributed under the terms of the [Unlicense](https://spdx.org/licenses/Unlicense.html) license.
