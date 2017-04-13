# Creates 3 playlists, short-term, medium-term, and long-term with top tracks from each.

import sys
import spotipy
import spotipy.util as util

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-top-read'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    ranges = ['short_term', 'medium_term', 'long_term']

    for range in ranges:

        # set array of tracks to blank
        track_ids = []

        # create a playlist with custom name
        playlist = sp.user_playlist_create(username, str("Top Tracks: "+range))

        # prime songs that will go in that playlist
        results = sp.current_user_top_tracks(time_range=range, limit=50)

        # loop through each song in results, return its id
        for i, item in enumerate(results['items']):
            track_ids.append(item['id'])
            print i, item['id']

        # add the array of songs to the playlist
        results = sp.user_playlist_add_tracks(username, playlist['id'], track_ids)

else:
    print("Can't get token for", username)