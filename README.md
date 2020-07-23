# GCMD Keyword Freeze

>*This README automatically updates with each GCMD Keywords sync.*    
>*Last updated: **2020-07-23 HH:MM:SS***

You can find a consistent path to the keywords lists (which are quite hard to find) by following the first link on this wiki page:

https://wiki.earthdata.nasa.gov/display/CMR/GCMD+Keyword+Access

This folder stores the most recent copy of the keyword listings retrieved from the reference documents located here:

https://gcmd.earthdata.nasa.gov/static/kms/

And you should call this script to download/sync the most recent versions of each gcmd reference to this directory:

[sync.py](sync.py)

```shell
./sync.py
```

You could also use the web service if you needed to hit keywords lists routinely for any reason.
