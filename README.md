# MyoMIDI

This will allow you to turn music into miracles.


First download the Myo SDK and set this environmental variable
```
export DYLD_LIBRARY_PATH=[path to myo.framework file]
```

In each of the library directories, run 
```
python install setup.py 
```

If you get an "ImportError “No Module named Setuptools"", run the following and try installing again
```
curl https://bootstrap.pypa.io/ez_setup.py -o - | python
```

Run
````
python main.py
````
