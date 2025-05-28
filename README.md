# Spotify Watcher
[![Python][Python]][Python-url] 

## Requirements
- [Python 3.8+](https://www.python.org/downloads/)
- [ffmpeg](https://ffmpeg.org/download.html)

## Usage
1. Create a virtual 
2. Install all requirements with 
`pip install -r requirements.txt`
3. Run the main.py
4. Follow the provided instructions and configure some songs before downloading them

## common mistakes
1. The Program has no access to the path
2. Make sure your Playlist is public!

## features
- [x] Downlaod single Files/Album or Playlists from Spotify
- [x] Adding Songs to the Watchlists
- [x] Manually update the added Album/Playlists
- [x] Display all stored data
- [x] Periodic updating the Album/Playlists (Add a Cronjob which executes the cron.py periodic to keep your Playlists up to date)

## To Do
- edit stored values
- toml file
- relative path support
- add alternative download ressource

## Notes
Please keep in mind that downloading new songs may be a CPU intense task caused by file formatting


[Python]: https://img.shields.io/badge/Language-Python-green
[Python-url]: https://www.python.org/
