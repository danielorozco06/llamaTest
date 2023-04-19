Install dependencies:
```
pip install -r requirements.txt
```

Create index files on index/:
```
python3 load_data.py
python3 load_wikipedia.py
python3 load_youtube.py
```

Create a request to indexes:
```
python3 query.py --query "Que es RTC?"
```


Known issues
Error:
```
pkg_resources.extern.packaging.version.InvalidVersion: Invalid version: '1.1build1' (package: distro-info)
```

Solution:
```
pip install --upgrade pip
sudo apt remove python3-distro-info
```